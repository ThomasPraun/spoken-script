---
name: spoken-script
description: Writes, humanizes and audits video scripts on any topic, meant to be spoken on camera by a real person in their own voice. Works in Spanish (Rioplatense, neutral, Spain) and English, and supports more languages through pluggable language files. Use it whenever someone wants a script, guion, voiceover, Reel, TikTok, Short, YouTube video, hook or intro to record; asks to make a script "sound human", "less AI" or "more like me"; wants a script reviewed for AI tells or read-aloud problems; wants to build a voice profile from their transcripts; or pastes a draft and asks to tighten it for camera, even if they never say "script".
---

# Spoken Script

Produce scripts, on any topic, that a specific person can say out loud in their own voice and that hold attention from the first second to the last. A script passes only if it does four things at once:

1. **Hooks**: a strong opening in the first seconds and a structure that keeps attention to the close.
2. **Sounds human**: no AI tells (inflated phrasing, forced triads, generic closers, brochure vocabulary).
3. **Sounds like the speaker**: their rhythm, words and register, calibrated from real samples when available.
4. **Works out loud**: short, easy-to-say sentences, punctuated so the speaker can read them at a glance, with emphasis and visuals marked for recording.

On top of those four, aim for **eloquence with plain words**: simple vocabulary, but specific, rhythmic and alive, the way good playwrights, orators and storytellers sound. Removing AI tells only makes a script correct; `references/craft.md` is what makes it worth listening to.

Text that reads well is not the goal. Listeners can't re-read and decide in about two seconds whether to keep watching. And the speaker reads the script from a teleprompter or a phone, so its punctuation is their sheet music: commas and periods tell them where to breathe and where a thought ends. Every rule below follows from that.

## Language layer

The workflow is language-independent. Everything that changes between languages lives in `references/languages/<code>.md`: AI tells specific to that language, pronunciation traps, punctuation conventions, speaking rate, mark labels and regional variants.

1. **Script language**, in this order: what the user asks for; the language of the brief or pasted draft; the language of the voice profile; otherwise ask.
2. **Variant** (e.g. `es` → Rioplatense, neutral or Spain; `en` → US or UK), in this order: what the user names; the voice profile; clear signals in how the user writes (voseo → Rioplatense, vosotros → Spain); otherwise the default in the language file. The user's own message is the strongest signal, stronger than the register of a draft they paste: someone who writes "revisalo" and "decime" records in voseo, so a pasted draft in tuteo is a mismatch to fix, not a reason to switch to neutral. State the variant you chose in the notes so the user can correct it.
3. **Load** `references/languages/<code>.md`. If it doesn't exist, say so, work with the universal references only, and offer to create the file from `references/languages/_template.md`.

Write the script in that language. Talk to the user in the language and variant they write to you in, in plain words: no craft jargon from these references (hook, payoff, CTA, beat) unless the user uses it first. Say "gancho", "remate", "llamado a la acción" or whatever the user would say.

## Files

| File | Read when |
| --- | --- |
| `references/languages/<code>.md` | Always, once the language is known |
| `references/orality.md` | Always: it governs every sentence, including the draft |
| `references/craft.md` | Always, from step 1 (material) to step 4 (eloquence tests) |
| `voice/README.md` | When looking for a voice profile or building one |
| `references/hooks.md` | Step 2 |
| `references/structures.md` | Step 3 |
| `references/ai-patterns.md` | Step 4 and detect mode |
| `assets/script-template.md` | Final output |
| `scripts/script_stats.py` | Step 6: measure spoken words, duration and breath/punctuation issues |

## Modes

Infer the mode from the request; ask only if it's truly unclear.

- **Write** (default): a topic or idea is given. Run the full workflow.
- **Rewrite**: a draft is given and the user wants it improved. Keep its content and claims. Skip steps 1 to 3 unless the draft lacks a hook or structure, then run steps 4 to 6.
- **Detect**: the user wants a review, not a rewrite ("revisá", "check", "audit", "¿suena a IA?"). Don't rewrite unless asked. Read it once as a viewer would and name the exact line where attention drops. Then list findings, each with the quoted fragment, the pattern, why it hurts spoken delivery, and a concrete fix ("cut lines 1 and 2, open on line 3", not "tighten the intro"). Include punctuation problems (missing commas, periods, question or exclamation marks, run-ons) and generic lines that fail the swap test in `references/craft.md`. Don't give an "AI probability": it's a guess dressed as a measurement. Write findings in plain language for the user: never show the internal pattern codes or test names from the references ("A1", "swap test"); describe the problem instead. Any count you state (words, seconds) must be measured, not guessed. Flag punctuation only where it hurts spoken delivery; correct punctuation is not a finding. End with the three changes that would matter most, in order, and a single line of 1 to 10 scores (hook, human, eloquence, voice, orality). Keep it scannable: group findings that share a cause, and give each one the fragment, the problem and the fix in a few lines. A review longer than the script it reviews is a smell.
- **Voice profile**: the user shares transcripts, captions or past scripts and wants the skill to learn their voice. Follow `voice/README.md` to build a profile and save it where the user can reuse it.

## Workflow

### 1. Brief

Collect: topic, format (short under 90 s or long), target duration, platform, audience, goal (inform, convince, sell, entertain, teach) and call to action. Infer what you can and ask only for what's missing and matters, all in one message. Only a missing topic blocks you. For anything else, assume, mark it *(assumed)* and list the assumptions in the notes so the user can correct them.

Then write the **one takeaway**: the sentence the viewer walks away with. Every beat serves it.

The topic can be anything, so treat accuracy as part of the job. If the script relies on facts, figures, dates, prices, quotes, health, legal or financial claims, research them first and note the sources. If web search is available, using it is not optional when the script cites a study, a researcher or a statistic: check each one before writing. Rank each claim by its source: official or primary source, reputable third party, community report, your own inference. Inference never goes into the script as fact. Never invent a number, study, quote or anecdote: a made-up statistic said on camera damages the speaker's credibility far more than a missing one. If something can't be verified, leave a visible placeholder (`[DATO: ...]`, `[FACT: ...]`) and tell the user. A placeholder is for a claim you believe is true but couldn't confirm. A figure you know is poorly sourced (a viral statistic that traces back to no real study) gets cut, not flagged.

Personal stories belong to the speaker. Ask for them or leave a placeholder; never fabricate experiences.

Then **gather material** yourself, from what you know and what you researched, following `references/craft.md` section 1: cases, scenes, real numbers, a common mistake, a surprising detail, a defensible opinion, an image from the topic's own world. Don't ask the user for this; it's your job. Build the hooks and the draft on the strongest pieces. This step is what keeps the script from being the average take on the topic.

### 2. Hooks

Propose 3 to 5 openings that differ in mechanism (see `references/hooks.md`), not five rewordings of one idea. For each give the mechanism label, the spoken line, what's on screen in the first second, and on-screen text. Run each through the hook checklist before showing it. Let the user pick or mix. If they asked for a one-shot result ("just write it"), pick the strongest and mention the runners-up in one line each.

### 3. Draft

Use the skeleton for the format from `references/structures.md`. Before writing, set the **word budget**: target seconds × speaking rate (language file) ÷ 60, split across the sections as `structures.md` shows. An 8-minute English script needs about 1,240 spoken words; a 30-second Reel in Spanish about 70. Write to that budget, section by section. Models reliably misjudge length by eye, usually short for long-form and long for short-form, so never estimate it: measure it (step 6). Write for the ear from the first draft, following `references/orality.md`: one idea per sentence, concrete nouns, active verbs, correct punctuation. Write with `references/craft.md`: the example before the concept, scenes in present tense with direct speech, the strongest word at the end of the sentence, one intention per beat, and one or two figures where they matter most.

### 4. Humanize and voice

Find the speaker's voice (see `voice/README.md`): samples or a profile in the conversation, a profile file the user points to, or one saved earlier. Then:

- Go through `references/ai-patterns.md` and the AI-tells section of the language file. Mark every hit, strongest first, and restate each point the way a person would say it instead of swapping words one by one.
- Match the speaker: sentence length, openings, connectors, fillers and how often they use them, humor, how they address the viewer, words they use and words they'd never say. Take their manner, never their content: no facts, names or stories carry over from the samples into a new script. Real samples outrank the style rules: if the speaker really says something a rule forbids, keep it at the frequency they use it. They never outrank the no-fabrication rule.
- Keep what makes it human: odd specific details, opinions, mixed feelings, self-corrections. A script with every rough edge sanded off sounds as artificial as one full of tells.
- No voice available? Don't fall back to a neutral, voiceless register: that's where generic text lives. Use the default voice: someone who knows the topic well and tells it to one smart friend, with opinions, concrete examples, a little humor where it fits, and plain but exact words. Adapt its register to platform, audience and variant, and say in the notes that the voice is not calibrated and how to add samples.
- Run the eloquence tests at the end of `references/craft.md`. The swap test matters most: any line that any creator could say about any topic gets rewritten with something only this topic or this speaker can say.

### 5. Oral pass

Read the whole script as if saying it aloud, at speaking pace, and fix:

- **Punctuation first.** Punctuation is the main pause and intonation system; marks only add what punctuation can't. Every sentence ends with a period, question mark or exclamation mark. Commas go wherever the speaker breathes or the language's norm requires one. Every real question gets its question marks and every raised voice its exclamation marks (opening `¿ ¡` included in Spanish), so the speaker knows the intonation before reaching the end. Quotation marks flag a change of voice: a quote, an imitation, irony. Any sentence that runs on without a comma or period where a breath belongs gets split or punctuated.
- any sentence that needs a breath in the middle;
- tongue twisters, consonant clusters and hard-to-pronounce words;
- numbers, symbols and abbreviations written the way they're said;
- spots where attention would drop (add a re-hook, cut, or change pace).

Then add performance marks with the labels from the language file: the intention of each beat, emphasis, extra pauses, pace changes, visuals, on-screen text.

### 6. Final audit

Save the script and measure it:

```bash
python3 <skill-dir>/scripts/script_stats.py <script.md> --lang <code> --target-seconds <N>
```

It counts only the spoken words (marks, headings and notes excluded), times each section with the language's speaking rate and pauses, and lists sentences that need a breath, dashes, missing `¿ ¡`, numbers written as digits and possible lists of three (`TRIAD`), which you then judge one by one with the Lists check below. If it says "add" or "cut", do it and measure again until it says OK. Report the measured figures in the notes, not an estimate. Without a shell, count the spoken words by hand, section by section.

Then go through this list and fix any failure:

- [ ] Hook: lands on the first word, passes the hook checklist, and the script keeps its promise.
- [ ] Structure: no weak hook, no flat middle, no buried payoff (`references/structures.md`); every open loop closed; one CTA.
- [ ] Human: no survivors of the common tells ("not X but Y", manufactured punchlines, generic closers, greetings or self-introductions anywhere ("Hi, I'm...", "today we're...", "by the end of this video"), "like and subscribe", "see you next time").
- [ ] Lists: find every enumeration of three (items, adjectives, benefits, "why X, why Y, and Z"). Keep it only if the content really has three parts and the third is the strongest; otherwise use two, or four, or one.
- [ ] Eloquence: passes the swap, picture, stake and change tests; at least one image or scene of its own; figures scarce and earned.
- [ ] Voice: sounds like the profile, or the notes say it isn't calibrated.
- [ ] Orality: every sentence passes the breath test; numbers and symbols written as said.
- [ ] Punctuation: periods, commas, question and exclamation marks complete; quotes on voice changes; no dashes, semicolons or parentheses.
- [ ] Facts: nothing added beyond the brief or verified research; every claim sourced or flagged.
- [ ] Length: `script_stats.py` says OK for the target (within 10%).

## Output

Use `assets/script-template.md`. Give the script ready to record, then a short notes block: measured duration and spoken word count, language variant used, assumptions, open placeholders, sources and unverified claims, whether the voice was calibrated, plus one alternative hook and one alternative CTA. Keep the notes brief; the script is the deliverable.

If the user asks for a teleprompter version, also give the script with every bracket mark removed. Keep all punctuation.
