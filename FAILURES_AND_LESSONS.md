# Failures and Lessons

This repository intentionally does not present a perfect build history.

Examples of preserved non-success states:

- early local Brain prototype attempts produced failures before later corrected passes
- campaign delivery could be materially better than engagement; one awareness result recorded 96% delivered, 13.54% opened, 0% clicked, and 4% hard bounced
- a later campaign scheduling attempt produced an operation-not-scheduled error
- knowledge staging could pass governance checks while still remaining blocked from deployment because owner decisions and exceptions were unresolved
- local AI could run successfully and still be practically unusable because generation speed was too slow

The project treats failures as evidence. A later pass does not erase the earlier failure; the purpose is to understand what changed and whether the correction is reproducible.
