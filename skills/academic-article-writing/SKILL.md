---
name: academic-article-writing
description: Plan, draft, audit, revise and submit academic articles for journals and peer-reviewed conferences, tailored to the venue's template and the author's own structure, style and citation format. Use this skill whenever someone is writing or improving a research paper, journal article, conference paper, review article (systematic, scoping, narrative), conceptual paper or short communication; asks where to submit, whether work is novel or publishable, how to structure an introduction, methods, results or discussion, which table or figure to use, how to format citations (APA, IEEE, Vancouver, Harvard, Chicago), how to respond to reviewers or a revise-and-resubmit, or what to check before submission. Use it even when the user only pastes a draft section or abstract and asks for feedback. For master's or PhD theses use academic-thesis-writing instead.
---

# Academic article writing

Help researchers produce articles that survive desk review and peer review, inside the format their venue and they themselves require. Most rejections come from fit, novelty and argument, not prose; so diagnose from the top down and polish last.

## The governing principle: the user's format, best practice inside it

The venue template and the user's stated choices decide the form: section names, order, length, citation style, voice. The skill's job is to make that form work as well as possible, not to replace it with a house model. Concretely:

- **Follow** the given structure, headings, style, terminology, voice, language variety and limits.
- **Guarantee functions, not forms.** Every article must, somewhere, state the problem and why it matters, position it against prior work and name the gap, explain and justify the approach, present evidence or argument, interpret it against the literature, and state contribution, limits and implications. Map each function onto the user's actual sections and report gaps in the user's terms ("Section 3 never justifies the sample size"), never as "papers should have section X".
- **Advise once, then comply.** If a choice raises rejection risk, say so in one or two sentences, propose the smallest fix that fits the user's format, then proceed with the user's decision and remember it. Do not reopen settled decisions.
- **Never silently** restructure, rename sections, convert to IMRaD, or add content the user did not ask for.
- **Refuse only on integrity:** fabricated data or references, plagiarism, duplicate submission, undisclosed AI use where disclosure is required.

Read `references/intake-and-tailoring.md` for the warn-versus-accept threshold and the decision order when no structure is given.

## Session start: build the writing profile

Before substantive advice, establish (ask in one batch, only for what is missing; infer the rest from the user's text and label assumptions):

1. Article type (original quantitative, qualitative, mixed, review type, conceptual, short communication, conference paper, other)
2. Target venue and its author guidelines (limits, required sections, abstract format, statements)
3. Citation style
4. Discipline and audience
5. Stage (idea, outline, draft, revision, rebuttal) and help mode (coach, edit the user's text, draft new text)
6. Venue AI policy
7. Optionally, a sample of the author's prose to match voice

Echo the profile back in a few lines and keep it for the session. Precedence when rules conflict: venue instructions, then the style manual the venue names, then discipline convention, then the author's preference, then this skill's defaults. Name the conflict and the rule followed.

## Route the task

| User need | Read | Core output |
| --- | --- | --- |
| Profile, tailoring, warn thresholds | `references/intake-and-tailoring.md` | Profile and function map |
| Which article type and structure; field variants | `references/article-types.md` | Type, matching structure, reporting guideline |
| Is it novel, is it publishable, where to submit | `references/novelty-and-positioning.md` | Contribution sentence, before/after statement, nearest-neighbour table, venue shortlist |
| Structure and depth of each section | `references/sections.md` | Function map, section audit, ranked fixes |
| Clarity, register, readability, visuals | `references/writing-and-presentation.md` | Reverse outline, jargon list, display plan |
| Reporting guidelines, reproducibility | `references/reporting-standards.md` | Item-by-item compliance table |
| Citations, references, captions, numbering | `references/citation-styles.md` | Mismatch report and corrected samples |
| Submission package, cover letter, venue legitimacy | `references/submission.md` | Pass/fail compliance table, cover letter draft |
| Reviews, rebuttal, rejection | `references/peer-review-response.md` | Comment matrix and response letter |
| Authorship, AI use, citation integrity | `references/ethics-and-ai.md` | Disclosure text, integrity flags |
| Final check before submission | `references/checklist.md` | Checklist with pass, fail or not applicable per item |

Read only the files the task needs. Several may apply to one request. When the user asks what a rule is based on, cite from `references/sources.md`.

## How to work on any draft

1. **Profile and type first.** Without venue, type and stage, advice is generic; get them.
2. **Map functions to the user's sections** before judging anything.
3. **Diagnose top-down:** fit and novelty, then argument (gap stated in the introduction matches the answer in the discussion), then rigour and reporting, then section depth, then prose, then formatting.
4. **Rank findings by rejection risk,** not by position in the manuscript. Give the top five first.
5. **Locate every finding:** quote or point to the passage, name the rule, propose the fix. Feedback like "improve clarity" with no location is not acceptable output.
6. **Edit only what was flagged,** preserving the author's claims, data, terminology and voice. Never strengthen a claim beyond its evidence.
7. **End with decisions only the author can make** (scope, framing, which reviewer request to decline).

Default audit report shape (adapt to what was asked):

```
Profile: <type> for <venue>, <style>, stage <stage>
Function map: <function> -> <user's section> | missing
Top risks (ranked): 1. ... [location] [why it matters] [fix]
Section notes: ...
Decisions for the author: ...
```

## Non-negotiable rules

- **Never invent references, data, results, statistics or quotes.** Large language models fabricate plausible citations at high rates; real journal names paired with nonexistent titles are typical. Mark anything not verified against a database or the user's own files as UNVERIFIED, and ask for DOIs or the source.
- **Never certify novelty from memory.** Novelty is reported as "supported by this comparison" against named prior works, ideally from a documented search. If no search tool is available, say so and ask the user for the closest prior papers.
- **Hedge to the evidence.** Correlational designs do not get causal verbs; samples do not get population claims.
- **Disclose AI assistance** per venue policy; draft the disclosure text if useful (`references/ethics-and-ai.md`).
- **Respect the help mode.** In coach mode ask questions and critique; draft new text only when asked and allowed by the venue's policy.
