---
name: en-lv-thesis-summary
description: Translate academic dissertation material from English into Latvian at submission quality for the Latvian Academy of Sciences, universities, and promotion councils. Use this skill whenever the user mentions translating a PhD/doctoral summary, promocijas darba kopsavilkums, thesis abstract, defence materials, research summary, or any academic text into Latvian, or asks for Latvian academic proofreading, Latvian terminology checks, or Latvianization of figures, tables, captions and references. Also use it when the user pastes English academic prose and asks for a Latvian version, even if they do not say "thesis" or "Academy of Sciences". Covers business, economics and management topics (digitalization, SMEs, entrepreneurship, innovation) with particular support for texts about Poland. Output is plain translated Latvian text only, no tables, no glossary, no report, unless the user explicitly asks for the supporting material.
---

# EN → LV dissertation summary translation

**Scope: this skill is only for business, digital economy and similar studies (economics, management, entrepreneurship, innovation); do not use it for other fields.**

Produce a Latvian text that a promotion council reviewer would accept as originally written in Latvian: correct grammar, correct orthography with full diacritics, standardized terminology, zero drift in meaning or numbers, and consistent use of every term and claim across the whole document.

The user gives plain English. Return plain Latvian. All the rigor below happens internally and produces exactly one visible output: the translated text.

## What you receive and what you return

Input: plain English text, any length, from a sentence to a full summary.

Output: the Latvian translation, and nothing else. No glossary table, no QA report, no figure/table breakout block, no commentary, no "here is the translation" preamble. The reply is the translation.

Exceptions, stated because silent exceptions are worse than none:

- If something in the source is genuinely ambiguous and the two readings would produce different Latvian, translate the more defensible reading and add a single short bracketed note directly after the affected sentence: `[PIEZĪME: ...]`. Do not do this for ordinary translation choices, only where meaning could fork.
- If a number, name, or figure element cannot be resolved from the text (for example, a cross-reference to something not included in what was pasted), mark it inline the same way rather than inventing it.
- If the user asks for the glossary, the QA report, or the query list, give it. Until asked, none of that surfaces.

Internally, still build and retain the term decisions and the consistency map described below. They are not deleted, they are simply not printed unless requested.

## Workflow

Run these phases for every translation. Phases 1, 3 and 5 run even on short inputs; phases 2 and 4 run when the input contains their subject matter (structure only matters for a full summary, figures only matter when figures are present).

### Phase 1 . Read and inventory

Before translating, read the whole input and note internally:

1. Every domain term, method name, construct name, variable name, institution name, legal act, and proper noun.
2. Every place where the English is genuinely ambiguous or where meaning could fork in translation.
3. Every claim, number, and named concept, so it can be checked for consistency in Phase 5.

Check each extracted term against `references/terminology.md` first.

**If a term is not in the glossary file: research it before translating it.** Do not guess and do not silently pick whichever Latvian word comes to mind. Established terminology in Latvian academic and economic writing is checked against the national term bank (`termini.gov.lv` / AkadTerm) and against how the term is actually used in Latvian-language scholarship in the field, using the web_search tool if available in this environment. When you resolve a new term this way, add it to `references/terminology.md` in the same format as the existing entries, so it is standardized for the rest of this document and for any future document in this project. If a live lookup is not possible, apply the resolution method in `references/terminology.md` § When a term is absent, pick the best-supported option, and flag it inline with `[PIEZĪME: term to confirm]` rather than presenting an unverified term as settled.

This means the glossary file grows over the life of the project. Treat that growth as the point: term drift across a 40-page summary is one of the two failure modes this skill exists to prevent.

### Phase 2 . Structural alignment (full summaries only)

If the input is a complete or near-complete dissertation summary rather than a passage or section, its shape should match the Latvian convention rather than a literal heading-by-heading translation. Read `references/structure.md` for the canonical section list and standard headings, and remap silently . this is a translation decision, not something to report back, unless the remapping changes what content goes where, in which case use an inline `[PIEZĪME: ...]`.

Skip this phase for excerpts, abstracts pasted alone, or non-summary academic text.

### Phase 3 . Translation

Translate section by section, not sentence by sentence, so cohesion, tense and referential chains survive.

Core rules, in priority order:

1. **Meaning before fluency.** Never resolve an ambiguity by picking the prettier option.
2. **Numbers are frozen.** Every figure, percentage, sample size, p-value, coefficient, year, and count is transferred exactly. Formatting changes (decimal comma, thousands separator) are allowed; values are not.
3. **Claims are frozen.** No hedging added, no hedging removed. "suggests" is not "proves". "correlates with" is not "causes".
4. **Latvian syntax, not English syntax in Latvian words.** Break long English participial chains into finite clauses. Avoid stacked genitives beyond three links.
5. **No unmarked Anglicisms.** Use the standardized Latvian term. Where the English term is unavoidable in the field, give the Latvian term with the English in parentheses at first mention only.
6. **Full diacritics, always.** ā č ē ģ ī ķ ļ ņ š ū ž.
7. **One term, one rendering, for the whole document.** Once a term is resolved in Phase 1, every later occurrence uses that exact rendering, including inside headings, captions and footnotes.

Read `references/latvian-conventions.md` before drafting. It covers case government traps, proper-noun Latvianization (including Polish names), number and date formatting, quotation marks, abbreviations, and the specific interference errors English speakers produce in Latvian.

### Phase 4 . Figures and tables (when present)

Translate every visible element: caption, axis labels, category and series names, legend entries, units, in-chart annotations, footnotes, and the source line. This happens inline, in place, as part of the returned text . not as a separate breakout block. Latvian convention places table captions above the table and figure captions below the figure, using `att.` and `tab.`.

If a figure is supplied as an image with text that cannot be read, mark the specific unreadable element inline with `[PIEZĪME: ...]` rather than guessing at its content.

### Phase 5 . Consistency and logical-flow check

Run this on every input, and run it with particular weight whenever a full thesis summary is given, because a full document is where the same idea gets restated in the introduction, the methodology, the results and the conclusions . and where drift between those restatements is easiest to introduce during translation and hardest for the author to catch afterward.

Check, across the whole translated text:

1. **Same concept, same words.** Every time the source restates the same finding, definition, or claim in different sections, confirm the Latvian restates it with the same terms and the same strength, not just a paraphrase that happens to sound similar. A concept defined one way in the introduction and rendered with different Latvian vocabulary in the conclusions is a document that contradicts itself in translation even though the English never did.
2. **Same number, same value, everywhere it recurs.** Sample sizes, percentages, and dates that appear more than once in the source must match every time they recur in the Latvian.
3. **Logical chain intact.** Where the source's argument depends on a claim made in one section being picked up again later (a hypothesis stated early and confirmed or rejected later, a gap identified early and closed later), confirm the Latvian preserves that dependency in wording strong enough that a reader tracking the argument across sections can still follow it. Weakening a claim in one place and not in its later restatement breaks the argument even if each sentence in isolation reads fine.
4. **No silent reconciliation.** If two mentions of the same thing genuinely differ in the source itself, do not quietly pick one and translate both the same way. Preserve the discrepancy and flag it with `[PIEZĪME: ...]`, since resolving an author's own inconsistency is not a translation decision.

Where this check finds a drift introduced during translation, fix it before returning the text rather than flagging it . the fix belongs in Phase 3's job of producing one correct rendering per term. Where the check finds an inconsistency that was already present in the source, flag it inline instead of fixing it, since that is the author's discrepancy to resolve, not the translation's to hide.

Also run the mechanical layer of this check: `scripts/qa_check.py source.txt target.txt` if both texts are available as files, to catch numeric mismatches, missing diacritics, residual English, and figure/table numbering gaps as a backstop to the manual check above.

## Non-negotiables

- Do not invent content absent from the source, including plausible-sounding citations, institution names, or legal references.
- Do not omit content because it is hard to render. Translate it and mark it if uncertain.
- Do not normalize the author's methodology terminology into a related-but-different construct.
- Do not silently fix a genuine inconsistency in the source; flag it instead.
- The output is a translation for the author's own use. Where the receiving institution requires a certified or native-speaker-reviewed version, that is a separate step this skill does not replace, and is worth mentioning once if the user has not indicated they already know that . not repeated on every reply.

## Bundled files

- `references/terminology.md` . domain glossary, method terms, commonly mistranslated words, and the resolution method for terms not yet listed. This file is expected to grow: add newly researched terms here as they are resolved.
- `references/latvian-conventions.md` . register, syntax, case government, proper-noun Latvianization, numbers, punctuation, abbreviations, figures and references, orthography.
- `references/structure.md` . canonical section list and heading wordings for a full Latvian summary, used only in Phase 2.
- `references/qa-checklist.md` . the detailed manual-check version of Phase 5, for when the user asks for the full report instead of plain output.
- `scripts/qa_check.py` . mechanical audit of numbers, diacritics, residual English, figure/table parity, quotation marks, acronyms.

## Domain note: this project

The recurring subject matter is digitalization of small and medium-sized enterprises in Poland: digitalizācija, digitālā transformācija, digitālais briedums, mazie un vidējie uzņēmumi (MVU), mikrouzņēmumi, uzņēmējdarbības vide, inovācijas, informācijas un komunikācijas tehnoloģijas (IKT), konkurētspēja, produktivitāte, digitālās prasmes, e-komercija.

Polish material brings recurring naming problems: institution names (GUS, PARP, ministries), programme names, place names, and personal names. Handle per `references/latvian-conventions.md` § Proper nouns . Latvianized form with the original in parentheses at first mention, original spelling retained in the bibliography.
