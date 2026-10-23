# Changelog

All notable changes to this skill are documented here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning: [SemVer](https://semver.org/).

## [0.1.0] - 2026-10-23

### Added

- `SKILL.md` with four modes: write, rewrite, detect and voice profile.
- Language layer in `references/languages/` with Spanish (Rioplatense, neutral, Spain), English (US, UK) and a template for new languages.
- References for AI tells, craft (eloquence), orality and punctuation, hooks and structures.
- Voice profile workflow in `voice/`.
- `scripts/script_stats.py` to measure spoken words, duration, breath, punctuation and possible lists of three.
- Eval cases in `evals/`. In blind comparisons against the same model without the skill, the skill won all three cases (pass rate 90% vs 57%).
