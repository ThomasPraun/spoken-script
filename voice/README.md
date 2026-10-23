# Voice profiles

A voice profile captures how one speaker talks, so scripts sound like them and not like a generic creator. The skill works without one, but calibrated scripts are noticeably better.

## Where to find a profile

Use the first one available:

1. Samples or a profile pasted in the conversation.
2. A file the user points to.
3. A saved profile in `voice/profiles/<speaker>.md` (several speakers can coexist; ask which one if it's unclear).
4. None: infer a natural register and say the voice is not calibrated.

## What counts as a sample

Real speech beats writing. In order of usefulness:

1. Transcripts or auto-captions of the speaker's own videos, podcasts or voice notes (unedited, fillers included).
2. Scripts the speaker already recorded and liked.
3. Casual writing (messages, posts). Use it only for vocabulary and humor, not rhythm: people write differently than they speak.

3 or 4 samples of 1 to 3 minutes each are enough. Samples of creators the user wants to sound like also work, but say so in the profile: it's a target style, not their voice.

## Building a profile

1. Read all samples before writing anything.
2. Record manner, never content: how they say things, not what they said. Don't upgrade casual words or "fix" deliberate quirks.
3. Fill `_template.md` with what you actually observe, quoting short real examples for each trait. Don't infer traits the samples don't show.
4. Measure instead of guessing where possible: average words per sentence, fillers per minute, how often they ask the viewer questions.
5. Show the profile to the user and ask what's wrong or missing. They know their voice better than any transcript.
6. Save it as `voice/profiles/<speaker>.md` if the skill folder is writable, or give the user the file to keep and paste next time.

One profile per speaker, with one section per language they record in: a person's voice changes across languages.
