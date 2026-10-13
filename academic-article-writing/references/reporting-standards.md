# Reporting standards and reproducibility

Reporting checklists are gatekeepers. NeurIPS desk-rejects submissions missing its paper checklist; many health journals require the matching EQUATOR checklist at submission. The EQUATOR Network indexes over 700 guidelines.

| Study type | Guideline |
| --- | --- |
| Randomised trials | CONSORT |
| Observational studies | STROBE |
| Systematic reviews, meta-analyses | PRISMA (and extensions, e.g. for scoping reviews) |
| Protocols | SPIRIT, PRISMA-P |
| Diagnostic or prognostic studies | STARD, TRIPOD |
| Qualitative research | SRQR, COREQ |
| Animal studies | ARRIVE |
| Case reports | CARE |
| Quality improvement | SQUIRE |
| Economic evaluations | CHEERS |
| ML and NLP conference papers | NeurIPS, ICML, ICLR, ACL checklists |

## Do

- Identify the guideline before data collection; it shapes what must be recorded.
- Write a dedicated limitations section. NeurIPS guidance warns that reviewers discovering unacknowledged limitations is worse than disclosing them, and instructs reviewers not to penalise honesty about limitations.
- Share data, code and materials in a persistent repository with a DOI, or state precisely why not.
- Pre-register confirmatory studies; label exploratory analyses as exploratory.
- Report all conditions, exclusions and measures, including null results.

## Don't

- Fill the checklist after writing and answer "yes" without pointing to the section that satisfies the item.
- Present hypotheses formed after seeing results as a priori.
- Report only significant analyses; tune on the test set (ML).

## Output

Ask for study design, map it to the guideline, and produce:

```
| Item | Requirement | Location in draft | Status (met / partial / missing) | Fix |
```

Mark missing, never assume. If the guideline text is not available to the skill, say so and work from the user's copy or the guideline website.
