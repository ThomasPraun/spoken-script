#!/usr/bin/env python3
"""Measure the spoken part of a script: words, duration per section, breath and punctuation issues.

Usage: python3 script_stats.py <script.md> [--lang es|en] [--wpm N] [--target-seconds N]
"""
import argparse
import re
import sys

# Speaking rates mirror the "Speaking rate" row of references/languages/<code>.md.
DEFAULT_WPM = {"es": 150, "en": 155}
SHORT_PAUSE_S, LONG_PAUSE_S = 0.4, 1.0
BREATH_WORDS = 20  # orality.md: most sentences under ~15 words; flag clear outliers only
NOTES_HEADINGS = ("notes", "notas")
# "a, b and c" / "a, b y c" with short items, the shape of most forced triads.
TRIAD_RE = re.compile(r"(?:^|[\s¿¡])([^,.;?!]{1,40}),\s+([^,.;?!]{1,40}),?\s+(?:and|y|e|or|o|u)\s+([^,.;?!]{1,40})[.,;?!]?", re.I)


def spoken_sections(text):
    """Yield (section title, spoken text). Stops at the notes block; skips marks and headings."""
    sections, title, lines = [], "(start)", []
    for raw in text.splitlines():
        line = raw.strip()
        if line == "---" or line.lower().rstrip(":") in NOTES_HEADINGS or line.lower().startswith(("## notas", "## notes")):
            if line != "---":
                break
            continue
        if line.startswith("# "):
            continue  # document title, not spoken
        if line.startswith("#"):
            if lines:
                sections.append((title, " ".join(lines)))
            title, lines = line.lstrip("# ").strip(), []
            continue
        line = re.sub(r"\[[^\]]*\]", "", line).strip()
        if not line or line.startswith(("|", "- ")) or " · " in line:
            continue  # tables, lists and the "platform · format · duration" meta line
        lines.append(line)
    if lines:
        sections.append((title, " ".join(lines)))
    return sections


def words(s):
    return re.findall(r"[\w\d%$€]+(?:[.,'’][\w\d]+)*", s.replace("**", ""))


def sentences(s):
    return [x.strip() for x in re.split(r"(?<=[.?!…])\s+|//|/(?=\s)", s) if x.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--lang", default="es")
    ap.add_argument("--wpm", type=int)
    ap.add_argument("--target-seconds", type=float)
    a = ap.parse_args()
    wpm = a.wpm or DEFAULT_WPM.get(a.lang, 150)
    text = open(a.path, encoding="utf-8").read()
    secs = spoken_sections(text)
    if not secs:
        sys.exit("No spoken lines found.")

    total_w, total_s, issues, triads = 0, 0.0, [], []
    print(f"{'section':40} {'words':>6} {'sec':>6}")
    for title, body in secs:
        w = len(words(body))
        pauses = body.count("//") * LONG_PAUSE_S + len(re.findall(r"(?<!/)/(?!/)", body)) * SHORT_PAUSE_S
        s = w / wpm * 60 + pauses
        total_w, total_s = total_w + w, total_s + s
        print(f"{title[:40]:40} {w:6d} {s:6.1f}")
        sents = sentences(body)
        for i in range(len(sents) - 2):
            if all(len(words(x)) <= 3 for x in sents[i:i + 3]):
                triads.append("fragments: " + " ".join(sents[i:i + 3])[:90])
        for sent in sents:
            if TRIAD_RE.search(sent):
                triads.append("list: " + sent[:90])
            n = len(words(sent))
            if n > BREATH_WORDS:
                issues.append(f"breath ({n} words): {sent[:90]}")
            if re.search(r"[—–;]", sent):
                issues.append(f"dash/semicolon: {sent[:90]}")
            if a.lang == "es" and "?" in sent and "¿" not in sent:
                issues.append(f"missing ¿: {sent[:90]}")
            if a.lang == "es" and "!" in sent and "¡" not in sent:
                issues.append(f"missing ¡: {sent[:90]}")
            if re.search(r"\d+\s*%|\b\d{4,}\b", sent):
                issues.append(f"number as digits (write as said): {sent[:90]}")
    m, sec = divmod(round(total_s), 60)
    print(f"{'TOTAL':40} {total_w:6d} {total_s:6.1f}  (~{m}:{sec:02d} at {wpm} wpm, pauses included)")
    if a.target_seconds:
        diff = total_s - a.target_seconds
        need = round(abs(diff) * wpm / 60)
        verdict = "OK" if abs(diff) <= a.target_seconds * 0.1 else ("cut ~%d words" % need if diff > 0 else "add ~%d words" % need)
        print(f"target {a.target_seconds:.0f}s → {verdict}")
    for i in issues:
        print("ISSUE", i)
    for t in triads:
        print("TRIAD", t)
    if triads:
        print(f"{len(triads)} possible lists of three: keep only those with three real parts where the third is strongest")


if __name__ == "__main__":
    main()
