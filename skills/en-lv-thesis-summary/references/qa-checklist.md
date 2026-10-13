# Verification checklist

Work through all five passes. Report findings; do not silently correct anything that changes meaning.

## Pass 1 . Automated audit

Run `python scripts/qa_check.py <source.txt> <target.txt>`. It reports:

- numeric tokens present in the source but missing in the target, and vice versa
- suspicious decimal conversions (`3.14` left un-converted, or a value that changed)
- words missing Latvian diacritics where the diacritic form is expected
- residual English words in the Latvian text
- figure and table numbering parity
- straight ASCII quotation marks, which are an orthographic error in formal Latvian

Every flagged item gets resolved or explained. A clean run is not proof of correctness . the script catches mechanical defects only.

## Pass 2 . Meaning integrity

- Every source sentence has a counterpart. Count sentences per section in both versions and account for merges and splits.
- No claim strengthened or weakened. Check every hedge: `may`, `suggests`, `appears`, `tends to`, `is associated with`.
- No causal claim introduced where the source stated correlation.
- Every citation attached to the same claim it was attached to in the source.
- Methodology described with the same constructs, not adjacent ones.
- Limitations preserved in full. Translators habitually compress limitations sections; reviewers read them closely.

## Pass 3 . Language quality

- Diacritics complete throughout, including in headings, captions, and the table of contents.
- Case government correct on every governed verb and preposition, particularly `ietekmēt`, `atbilst`, `sekot`, `veicināt`, `pamatoties`.
- Participial constructions attach to the correct subject . check every `analizējot`, `ņemot vērā`, `balstoties uz`, `izmantojot`.
- No stacked genitive longer than three links.
- No unmarked Anglicisms; every unavoidable English term glossed at first mention only.
- Register consistent: one self-reference convention, one tense convention per section type.
- Comma placement before every subordinate clause.
- Latvian quotation marks `„...”` throughout.

## Pass 4 . Consistency

- Every glossary term rendered identically in body text, headings, captions, legends and appendices.
- Acronyms expanded exactly once, at first occurrence, then used consistently.
- Number formatting uniform: decimal comma everywhere, space thousands separator everywhere, `%` spacing uniform.
- Cross-references resolve: every `sk. N. att.` and `N. tab.` points at an object that exists and carries that number.
- Figure and table numbering sequential with no gaps.
- If the summary is bilingual, the Latvian and English versions carry identical numbering, identical data, and identical section counts.
- Bibliography entries unchanged from the source; only `u.c.` and structural labels Latvianized.

## Pass 5 . Back-translation

Back-translate these sections into English and diff against the original:

1. anotācija / abstract
2. pētījuma mērķis
3. pētījuma uzdevumi
4. aizstāvēšanai izvirzītās tēzes
5. zinātniskā novitāte
6. secinājumi

These are the passages a council quotes and challenges. Report any semantic delta, however small, with the source and target sentences side by side.

## Deliverable: query list

Number every open item and give its location. Categories:

- **Ambiguous source**. the English admits more than one reading.
- **Contested term**. a defensible alternative Latvian term exists.
- **Missing data**. administrative facts, counts, or figure content not present in the source.
- **Unreadable element**. figure text supplied as an image that could not be resolved.
- **Convention conflict**. a place where the source's format conflicts with Latvian academic convention and the author must choose.

State clearly in the handover that the translation is prepared for author review, that terminology choices are open to the author's override, and that where the receiving institution requires it, a native-speaker linguistic review is a separate step this workflow does not replace.
