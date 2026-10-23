# spoken-script

Claude skill that writes, humanizes and audits video scripts on any topic, to be spoken on camera in the speaker's own voice. Spanish (Rioplatense, neutral, Spain) and English; other languages plug in through `references/languages/`.

## Install

Copy this folder to `~/.claude/skills/spoken-script/`.

## Layout

| Path | Content |
| --- | --- |
| `SKILL.md` | Workflow and modes (write, rewrite, detect, voice profile) |
| `references/` | Language-independent rules: AI tells, craft (eloquence), orality and punctuation, hooks, structures |
| `references/languages/` | One file per language; `_template.md` to add a new one |
| `voice/` | How to build a speaker's voice profile; profiles go in `voice/profiles/` |
| `assets/script-template.md` | Output format |
| `scripts/script_stats.py` | Measures spoken words, duration and delivery issues |
| `evals/` | Test cases (`claude plugin eval .` runs them) |
| `docs/design.md` | Original design notes |

## Adding a language

Copy `references/languages/_template.md` to `<code>.md`, write it in that language and keep the section order. `es.md` and `en.md` are worked examples.

## Sources

Built after reading these community skills (read only, not installed):

| Source | Taken |
| --- | --- |
| [blader/humanizer](https://github.com/blader/humanizer) | AI-pattern catalog, voice calibration, audit with second pass |
| [jooray/humanizer](https://github.com/jooray/humanizer) | Detect-mode contract, "manner not content", fabrication check, false positives, reshuffle test, per-language appendix |
| [macCesar/aiskills · humaniza](https://github.com/macCesar/aiskills) | Spanish AI lexicon and structures (es-MX seed, extended for spoken and Rioplatense Spanish) |
| [Hainrixz/humanizalo](https://github.com/Hainrixz/humanizalo) | Synonym cycling, false ranges, lazy extremes |
| [vyralcontent/content-skills](https://github.com/vyralcontent/content-skills) | Hook archetypes and three layers, upgrade ladder, timing tiers, failure modes, loops, CTA rules, critique mode |
| [sugarforever/01coder-agent-skills · video-planner](https://github.com/sugarforever/01coder-agent-skills) | Read-aloud rules, one-breath test, fact-source tiers |
| [raroque/boop-agent · youtube-script-writer](https://github.com/raroque/boop-agent) | Research before writing, one takeaway, alt hook and CTA |
| [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | Assumed-input protocol, short-form word budget |
| [minhnv0807/ai-business-skills · 04-script-video-global](https://github.com/minhnv0807/ai-business-skills) | Pre-delivery checklist idea, pre-recording read-through |
| [cdeistopened/content-os · short-form-video](https://github.com/cdeistopened/content-os) | Zero-context test for hooks, keywords spoken early |
| [postplusai/hook-skills · visual-hook](https://github.com/postplusai/hook-skills) | First-frame question test |

The craft layer (`references/craft.md`) draws on what great speakers and storytellers have in common: Aristotle's ethos, pathos and logos; Stanislavski's objectives and playable verbs; the anaphora, antithesis and extended images of King, Churchill and Kennedy; Nancy Duarte's "what is / what could be"; Ira Glass's anecdote and reflection; Matthew Dicks's five-second moment (*Storyworthy*); The Moth's stakes and change; and Spanish oral narration (Galeano, Machado, Rioplatense storytellers).

Read but not used: eddiebe147/script-writer (repo unavailable), lukeslp/skill-humanize (not found), jmsktm/reel-script-writer (placeholder content), ailabs-393/script-writer, gtmagents/scriptwriting, kostja94/video-marketing, Pictory, aaaaqwq/humanize.
