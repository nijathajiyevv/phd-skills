# Citation, reference and caption styles

More than 10,000 citation styles exist in the Citation Style Language (CSL) repository, but they reduce to a few families. Model the family plus a small set of parameters; do not memorise styles. Delegate bulk reference formatting to a reference manager (Zotero, Mendeley, EndNote) with the CSL style; the skill checks consistency and completeness.

## Families

| Family | Examples | In-text marker | Reference list order |
| --- | --- | --- | --- |
| Author-date | APA 7, Harvard variants, Chicago author-date | (Smith, 2020); Smith (2020) | Alphabetical by author |
| Numeric | IEEE, Vancouver, ACS, many journal styles | [1] or superscript, numbered by first appearance | Numerical |
| Note | Chicago notes-bibliography, OSCOLA | Footnote or endnote | Bibliography alphabetical, if required |
| Label | Some CS and maths styles | [Smi20] | Alphabetical by label |

"Harvard" is a generic name for author-date formats, not one standard. Always get the exact variant (institution or journal guide).

## Style module template

For every style in the profile, fill these fields from the venue's author guide (or a known style below). Unknown fields are marked "check guide", never guessed.

```
Style: 
Family: 
In-text format (1, 2, 3+ authors; narrative vs parenthetical): 
et al. threshold (in text / in list): 
Multiple citations order and separator: 
Page or locator format: 
Reference list order: 
DOI / URL format: 
Table label: position, numbering, title format, notes position
Figure label: position, numbering, caption format
Heading levels: 
Equation numbering: 
```

## Known styles (summary)

| Element | APA 7 | IEEE | Vancouver | Chicago notes-bibliography |
| --- | --- | --- | --- | --- |
| In-text | (Author, Year); 3+ authors as "et al." from first citation | [n] by first appearance; ranges [4]–[6]; page [4, p. 23] | Numbers by first appearance, brackets or superscript per journal | Superscript note number; full note at first citation, short note after |
| List order | Alphabetical | Numerical | Numerical | Bibliography alphabetical |
| Table label | Bold "Table 1" above; italic title-case title on next line; notes below; horizontal rules only | "TABLE I" (Roman) above; caption centred below the label; notes below | Per journal | Per publisher |
| Figure label | Same as tables: number and title above, notes below | Caption below figure: "Fig. 1." | Per journal | Per publisher |

When the venue's own guide differs from these summaries, the venue wins.

## Rules that hold across nearly all styles

- Number tables and figures in order of first mention, with separate sequences; appendix and supplementary items use their own scheme (A1, S1).
- Call out every display in the text before or where it appears.
- Captions are self-contained: what is shown, sample or source, abbreviations, statistical notation, units.
- Reproduced or adapted displays: "Adapted from [citation]" plus permission where required.
- Every in-text citation has a list entry; every list entry is cited.

## Checks the skill runs

- Cited but missing from the list; listed but never cited
- Mixed formats (two styles in one manuscript)
- Wrong caption position or label format for the style
- Numbering gaps or out-of-order first mentions; displays never called out
- Missing DOIs where the style requires them
- Metadata that cannot be verified: mark UNVERIFIED; never invent missing volume, issue, pages or DOIs

Output: a mismatch table (location, problem, rule, corrected example), not a silently reformatted list.
