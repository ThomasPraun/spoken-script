# Script skeletons

Language-independent. Built from vyralcontent (short-form), raroque/boop-agent, mohitagw15856 and sugarforever/video-planner (long-form). Timings are heuristics, not rules; fit them to the target and never pad to reach a length.

## Before the skeleton

Write the **one takeaway** in a sentence: what the viewer walks away with. Every beat must serve it. If you can't write it, the topic needs a sharper angle before it needs a script.

Join beats with **"but"** or **"so"** (a turn or a consequence), never with "and then". "And then" is a list; "but" and "so" are a story.

## Short-form (15 to 90 s: Reels, TikTok, Shorts)

**Hook → Escalation → Payoff → CTA**

| Length | Beats |
| --- | --- |
| 15 to 34 s | 0–3 hook · 3–8 escalation 1 · 8–18 escalation 2 with a re-hook near 12 s · 18–28 payoff · last seconds loop or CTA |
| ~60 s | 0–3 hook · 3–10 promise · 10–25 escalation 1 · 25–28 re-hook · 28–45 escalation 2 · 45–52 payoff · 52–60 loop or CTA |
| 90 s | As 60 s with two re-hooks |

- Put the second-strongest moment near the top and keep the strongest for the payoff.
- Something changes every 2 to 4 s: a new idea, angle, visual or on-screen text.
- Pacing: fast hook, a steadier middle with one peak, fast ending.
- One idea, one CTA per video.

Variants:

- **Talking head**: claim → reason → proof or example → payoff → CTA. Its risk is monotone delivery, so mark pace and emphasis changes.
- **Story**: situation → problem → turn → lesson. The lesson in one line.
- **List**: only with the real count. Strongest item last.
- **Myth-busting**: common belief → why it's wrong → what's true → what to do.
- **Tutorial**: result first (show it), then the steps, each said as one sentence.

## Long-form (3 to 20+ min: YouTube)

**Cold open → Promise → Sections with re-hooks → Payoff → Close**

| Part | Job |
| --- | --- |
| Cold open (0 to 30 s) | Hook. Deliver the title's promise. No greeting, no name, no channel talk |
| Promise (~20 to 30 s) | Two or three sentences: what the viewer gets by staying. Then go; a long promise is where long-form sags first. Credibility, if any, comes from a specific detail woven in ("when I was writing my thesis on this..."), never a self-introduction ("Hi, I'm X, I studied Y") or an agenda ("by the end of this video you'll know...") |
| Sections (2 to 5) | One idea each, with a descriptive title (not "Body 1"). Each ends with a small payoff |
| Re-hooks | Every 30 to 60 s: a new question, a "but...", a tease of what's coming, a story, a pattern break |
| Payoff (~90% of runtime) | The most valuable takeaway, said plainly, closing the loop opened in the cold open |
| Close + CTA | Short. One action. Bridge into the next video instead of "in conclusion" |

Checks: no stretch over ~60 s without a change; every open loop closed; the intro takes under 10% of the runtime.

## Retention mechanics

- **Open loops**: promise something early ("I'll show you the mistake at the end"), close it later. Close every loop you open.
- **Three failure modes**. Diagnose every draft against them:
  - *Weak hook*: viewers gone by second 1. Fix with `hooks.md`.
  - *No escalation*: attention bleeds out in the middle. Fix with a re-hook or a turn ("but").
  - *Buried payoff*: the script stalls before the good part. Move a taste of the payoff earlier.
- **Loops for rewatches** (short-form): the last line flows back into the first; the last frame matches the first; or the hook asks a question and the ending shows its setup.

## CTA

- One ask. Several asks cancel each other ("start today, save it and send it" is three).
- Understood on first hearing. Say it to someone with no context: if they'd ask "who?" or "what?", rewrite it.
- Tie it to the content. Ask for something specific: "send this to whoever always picks the restaurant", "save it for your next move", "tell me yours in the comments". Avoid "like and subscribe" stacks and "tag 3 friends".
- In short-form, a light implicit prompt around 70% plus the explicit close works; a closing line that loops to the hook can be the CTA itself.
- For a Short pointing to a long video: give most of the answer, then send them to the full version.

## Word budget

Budget = target seconds × speaking rate ÷ 60, minus ~5% for pauses (10 to 15% with many long pauses or demos). Split it by the share of time each part takes. Examples at the default rates:

| Target | Spanish (150 wpm) | English (155 wpm) |
| --- | --- | --- |
| 30 s Reel | ~70 words | ~70 words |
| 60 s | ~140 | ~145 |
| 8 min | ~1,140 | ~1,180 |
| 8 min, split | cold open ~70 · promise ~70 · 4 sections ~230 each · close ~80 | same shape |

Measure the result with `scripts/script_stats.py`; don't trust a count by eye.
