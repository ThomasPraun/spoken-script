# English (`en`)

Language layer for English scripts. Adds to `../ai-patterns.md` and `../orality.md`; doesn't repeat them.

## Metadata

| Field | Value |
| --- | --- |
| Code | `en` |
| Variants | `en-us` (default), `en-uk` |
| Speaking rate | ~155 words per minute (range 140 to 170) |
| Voice files | `voice/samples/en-*` |

## Performance-mark labels

| Use | Label |
| --- | --- |
| Visual / B-roll | `[B-ROLL: ...]` |
| On-screen text | `[TEXT: ...]` |
| Pace change | `[PACE: faster / slower]` |
| Intent of the beat (a verb) | `[INTENT: surprise / warn / confess / challenge...]` |
| Tone | `[TONE: ...]` |
| Sound or music | `[SFX: ...]` |
| Cut or angle change | `[CUT]` |
| Fact to verify | `[FACT: ...]` |
| Anecdote to fill | `[STORY: ...]` |

## English-specific AI tells

On top of the universal catalog.

### AI vocabulary (strong)

delve, crucial, pivotal, showcase, underscore, tapestry, testament, landscape, realm, navigate (a challenge), embark, journey (for a process), unlock, unleash, elevate, empower, foster, leverage, seamless, robust, game-changer, cutting-edge, transformative, "in today's fast-paced world", "ever-evolving", "it's worth noting", "at the end of the day", "the power of".

Fix: the plain word. "Use" for "leverage", "show" for "showcase", "look at" for "delve into".

### Worn-out creator lines (strong)

"Here's the thing", "Let's dive in", "Stop scrolling", "You won't believe...", "Most people don't know this", "Let that sink in", "Read that again", "This changes everything", "And that's the real secret", "Stay till the end".

### Essay connectors (strong when spoken)

"Moreover", "Furthermore", "Additionally", "In conclusion", "Firstly... Secondly...", "That being said", "With that in mind".

Fix: "and", "but", "so", "also", "the other thing is", or nothing.

### Too formal for speech (medium)

No contractions ("do not", "it is"), "one should", "individuals" for "people", "utilize" for "use", "purchase" for "buy", "assist" for "help".

### Stock images (strong)

"a journey", "a rollercoaster", "the tip of the iceberg", "a double-edged sword", "get out of your comfort zone", "a wake-up call", "the key to", "move the needle", "at the end of the day". Fix: an image from the topic's own world (see `../craft.md` §6).

### Hyphenated-pair overuse (weak)

data-driven, real-time, end-to-end, high-quality, next-level stacked in one script.

### What not to flag in English

- "So," "Look," "Okay," "Honestly," as openers when the speaker uses them in their samples. They're spoken English; the tell is the same one opening every beat.
- "you guys", "like", "kind of", "literally" in a casual voice at the frequency the samples show.
- A single "here's the thing" in a voice that really says it.

## Orality in English

- **Contractions** by default: it's, you're, don't, I've. Uncontracted only for emphasis ("I did **not** say that").
- **Phrasal verbs** sound spoken: "figure out", "set up", "find out" over "determine", "configure", "discover".
- **Sibilant and consonant pileups**: "she sells", "sixth sense", "statistics", "specifically" in a fast line. Swap or reorder.
- **Numbers**: write as said when it helps: "a third", "about two thousand", "30 percent". Say years naturally ("twenty twenty-six").
- **Acronyms**: mark whether letters or a word the first time (U-R-L vs. NASA).
- **Homographs**: watch "read", "live", "lead", "record" in ambiguous spots.

## Punctuation in English

Commas and periods are the speaker's sheet music. Keep them complete and correct.

- **Period** at the end of every thought. When in doubt, end the sentence.
- **Comma required** after introductory words and clauses ("So, here's what happened." / "If you do this every day, it shows."), around direct address ("Look, Sam, it's simple."), around non-essential clauses, and between items in a list (use the Oxford comma consistently; it helps the speaker pace lists).
- **No comma** between subject and verb, however long the subject. If it needs a breath, split the sentence.
- **Question marks** on every real question, so the speaker lifts the intonation. Tag questions get a comma before them ("It works, right?").
- **Exclamation marks** only where the voice really rises. One per line reads like an ad.
- **Quotation marks** for a change of voice: quoting or imitating someone (`And she goes, "no way."`), a word mentioned as a word, or irony. US style uses "double" quotes outside and 'single' inside; UK usually the reverse. Be consistent.
- **Colon** to introduce a quote or a short list; avoid it as a reveal ("The best part: it's free."). **Em dashes, semicolons, parentheses**: avoid in the script; use a period or a comma.
- **Ellipsis**: only for real suspense, once per script at most.

## Craft in English

How `../craft.md` applies with English's own resources.

- **Short, old words hit hardest.** English has a plain Germanic layer (help, start, buy, fear, work) and a formal Latin one (assist, commence, purchase, apprehension, employment). Spoken eloquence lives in the first.
- **End-weight through structure.** English word order is rigid, so move the stress word to the end with structure: "What costs you is waiting", "The one thing I'd never skip is sleep."
- **Phrasal verbs as strong verbs.** "It wiped out my savings", "she shut it down", "I blew it" carry more than "eliminated", "terminated", "failed".
- **Present tense for the key moment.** "So I walk in, and he looks at me..." is how live storytellers talk.
- **Direct speech** with "says" or "goes": `And she goes, "You're sure about this?"`
- **Lessons from the greats:** King's extended image (a check marked "insufficient funds"), Churchill's short words and anaphora, Kennedy's reversal ("ask not..."). Learn the shapes; never reuse the lines.

## Variants

### `en-us` (default)

US spelling and vocabulary (apartment, fall, cell phone, check). Casual "you guys" only if the voice uses it.

### `en-uk`

UK spelling and vocabulary (flat, autumn, mobile, cheers, quid). Understatement reads more natural than US-style hype; dial the hook's intensity to the speaker.

## Before and after

Three levels of the same opening. The second no longer sounds like AI, but it's flat. The third is the goal.

> **1. AI:** In today's fast-paced world, productivity is crucial. It's not just about working harder, it's about working smarter. Let's dive into three game-changing tools that will elevate your routine.
>
> **2. Correct but flat:** You work ten hours and feel like you did nothing. Same here. I changed one thing and got an hour back every day.
>
> **3. Eloquent:**
> [INTENT: portray]
> It's 7 p.m. You've got twenty-three tabs open, / a cold coffee, // and the feeling you did nothing today.
> [INTENT: confess]
> That was me. Until a friend looked at my screen and said, "Do you work, or do you collect tabs?"
> [INTENT: challenge]
> I didn't need more time. I needed fewer **windows**.
> [TEXT: 23 tabs]

Why the third works: scene before concept, details you can see, a rising list that ends on the strongest item, direct speech, and a contrast the viewer really believes ("I need more time") closed with the stress word last. In a real script the friend's line must come from the speaker; otherwise use `[STORY: ...]`.
