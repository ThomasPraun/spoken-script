# Universal AI tells

Patterns that make a script sound machine-written in any language. Built from blader/humanizer and jooray/humanizer (both based on Wikipedia's "Signs of AI writing"), Hainrixz/humanizalo and macCesar/humaniza, and reweighted for spoken video. Language-specific wording and extra tells live in `languages/<code>.md`.

Strength: **S** strong (fix on sight), **M** medium (fix when two or more cluster), **W** weak alone.

## Spoken override

These catalogs were written for text that is read. Speech is different: a short fragment, a rhetorical question or a "Look," opener can be exactly how a person talks. Judge each hit by two questions: would this speaker say it (check the voice profile), and is it a one-off or a pattern? One punchy fragment is delivery. A fragment closing every section is a tell.

## A. Staging instead of saying

| # | Pattern | Str | What it looks like | Spoken fix |
| --- | --- | --- | --- | --- |
| A1 | Not X but Y | S | Rebuts a claim nobody made: "It's not just X, it's Y", "No fue X. No fue Y. Fue Z." | State Y. Keep a contrast only if the audience really believes X |
| A2 | Manufactured punchline | S | "Let that sink in", "Read that again", "Every. Single. Day.", a closer restating the point | Cut, or replace with a concrete consequence |
| A3 | Aphorism formula | S | "X is the new Y", "The real question is...", "at its core", "X has an expiry date" | Put the concrete fact back, or cut |
| A4 | Announced run-up | S | "Here's the thing", "Let's dive in", "Plot twist:", "what nobody tells you" | Start with the thing |
| A5 | Colon reveal | M | "The best part: it's free." | "And it's free." |
| A6 | Performed candor | M | "To be honest", "I'll be real with you", "no spin" as a frame | Drop the announcement, keep what follows. Fine if it's a habit in the voice samples |
| A7 | Arguing with no one | M | "Some might argue", "Don't get me wrong", rejecting options nobody raised | Delete; answer only objections the viewer really has |
| A8 | Self-answered question chain | M | "The result? Amazing. The cost? Zero." | One real question at most, then answer it plainly |

## B. Rhythm by rule

| # | Pattern | Str | What it looks like | Spoken fix |
| --- | --- | --- | --- | --- |
| B1 | Forced triad | S | Lists of three when the content has two or four, or three items of equal weight | Use the real count. Two is fine. A rising three that escalates is rhetoric, not a tell (`craft.md` §5) |
| B2 | Metronome | M | Every sentence or section the same length | Vary on purpose; a spoken script needs real variation |
| B3 | Same opening | M | Consecutive sentences starting with the same word | Vary, or make the repetition deliberate and short |
| B4 | Connective pile-up | M | More than one connector opener per beat, the same connector twice in a section | Let sentence order carry the logic |
| B5 | Hedged enumeration | M | "There are several factors...", "It depends on many things" | Give the answer first |
| B6 | Stacked hedges | M | "could potentially", "it might be possible that" | One hedge or none |
| B7 | Lazy extremes | M | always, never, everyone, nobody, every single | Say the real proportion |
| B8 | False range | W | "from beginners to experts, from X to Y" | Name who it's actually for |
| B9 | Dash or colon everywhere | M | Long dashes as universal glue | Split with a period, or use a comma |
| B10 | Passive, no subject | W | "It has been shown..." | Who did it? Name them |

## C. Inflation and borrowed authority

| # | Pattern | Str | What it looks like | Spoken fix |
| --- | --- | --- | --- | --- |
| C1 | AI vocabulary | S | See the word list in the language file | The everyday word the speaker would use |
| C2 | Inflated stakes | S | "game-changer", "revolution", "this changes everything" | Say what concretely changes, for whom |
| C3 | Brochure tone | S | "stunning", "seamless", "unlock your potential" | Describe it; let the viewer decide it's great |
| C4 | Unnamed experts | S | "Experts say", "studies show" | Name the source or drop the claim |
| C5 | Generic future closer | S | "The future is bright", "only time will tell" | End on the payoff or the CTA |
| C6 | Vague link | M | "is linked to", "plays a role in" | Say how |
| C7 | Hollow -ing tail | M | "..., highlighting the importance of..." | Cut, or its own sentence with content |
| C8 | Fancy verb for "is/has" | M | "serves as", "stands as", "boasts" | "is", "has" |
| C9 | False agency | M | "The data tells us", "the market rewards" | Who concluded it? Say that |
| C10 | Stock image | S | "a journey", "a rollercoaster", "the tip of the iceberg", "a double-edged sword" | An image from the topic's own world (`craft.md` §6) |
| C11 | Synonym cycling | M | The same thing called three names in three sentences | Repeat the right word. Out loud, repetition helps |

## D. Chat and drafting residue

| # | Pattern | Str | What it looks like | Spoken fix |
| --- | --- | --- | --- | --- |
| D1 | Assistant voice | S | "Great question!", "I hope this helps" | Delete |
| D2 | Meta opener or agenda | S | "In this video we'll explore...", "By the end of this video...", "Hi, I'm X and today...", "See you next time" | Open with the hook; let the content show the plan; end on the last real line |
| D3 | Reasoning residue | S | "Let's break this down", "Step 1:" in a script that isn't a tutorial | Delete; just say the step |
| D4 | Recap of everything | M | "In summary, we've seen that..." | One-line takeaway or none |
| D5 | Over-explaining | M | Rebuilding background the audience already has | Cut to what's new |
| D6 | Template leftovers | S | Unfilled `[Your name]`, citation markers, tracking URLs, invisible characters | Remove before delivering |

## E. Written, not spoken

| # | Pattern | Str | What it looks like | Spoken fix |
| --- | --- | --- | --- | --- |
| E1 | Visual-only structure | S | Bullets, headings, parentheses, "see below" | Spoken signposts ("first...", "and the second thing...") |
| E2 | Breathless sentence | S | Needs a breath before it ends, or runs on without commas | Split, or punctuate where the breath goes |
| E3 | Front-loaded clause | M | Long subordinate before the main verb | Main idea first, detail after |
| E4 | Symbols and abbreviations | M | %, &, vs., e.g., 1.5k | Write as spoken (see language file) |
| E5 | Too clean | M | No contraction, aside, reaction or self-correction ever | Add what the speaker naturally adds, per the voice profile |

## Not tells

Don't flag these alone; look for clusters, and count a cluster once.

- One dash, one "however", one short emphatic sentence, one rhetorical question.
- Plain, bland sentences. Simple is not AI.
- Fillers and openers the speaker really uses in their samples.

Signs of a human that the rewrite must keep: odd specific details, unresolved or mixed feelings, self-corrections, era-bound slang, uneven sentence lengths, an opinion.

## How to audit

1. Read the whole script once and mark every hit, strongest first, quoting the fragment.
2. **Reshuffle test**: if you could swap two middle sections and nothing breaks, the script is a stack of interchangeable blocks. Give it a real progression (each beat needs the previous one).
3. Rewrite each marked point the way the speaker would say it. Restate the idea; don't patch words one at a time.
4. **Fabrication check**: does the rewrite state any fact, name, number, date, quote or ranking that wasn't in the source, the brief or the verified research? Did it drop one? Superlatives (only, first, most) must survive or be removed on purpose. An unsupported addition is an error.
5. Hunt the survivors: A1, A2, B1, C5 and E2 come back most often after edits.
