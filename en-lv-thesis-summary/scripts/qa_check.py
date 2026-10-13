#!/usr/bin/env python3
"""
qa_check.py - mechanical audit of an EN -> LV academic translation.

Usage:
    python qa_check.py source_en.txt target_lv.txt
    python qa_check.py source_en.txt target_lv.txt --json report.json

Checks performed:
  1. numeric parity        - every number in the source appears in the target
  2. decimal formatting    - dot decimals left unconverted in the Latvian text
  3. diacritics            - Latvian text with implausibly low diacritic density,
                             plus known diacritic-stripped word forms
  4. residual English      - English function words surviving in the Latvian text
  5. figure/table parity   - counts of Figure/Table vs att./tab. references
  6. quotation marks       - ASCII quotes instead of Latvian low-high quotes
  7. acronym coverage      - acronyms in the source absent from the target

The script flags candidates for human review. It does not judge meaning.
"""

import argparse
import json
import re
import sys
from collections import Counter

LV_DIACRITICS = set("āčēģīķļņšūžĀČĒĢĪĶĻŅŠŪŽ")

# High-frequency English function words that should not survive in Latvian prose.
ENGLISH_MARKERS = {
    "the", "and", "with", "from", "that", "this", "these", "those", "which",
    "have", "has", "been", "were", "was", "are", "for", "their", "there",
    "between", "among", "through", "however", "therefore", "moreover",
    "research", "study", "results", "analysis", "enterprises", "companies",
    "development", "management", "digital", "small", "medium", "table",
    "figure", "chapter", "conclusion", "conclusions", "objectives", "aim",
}

# Words that are wrong without diacritics; left side is the stripped form.
STRIPPED_FORMS = {
    "petijums": "pētījums", "petijuma": "pētījuma", "petijumi": "pētījumi",
    "merkis": "mērķis", "merka": "mērķa", "uzdevums": "uzdevums",
    "secinajumi": "secinājumi", "priekslikumi": "priekšlikumi",
    "uznemums": "uzņēmums", "uznemumi": "uzņēmumi", "uznemumu": "uzņēmumu",
    "uznemejdarbiba": "uzņēmējdarbība", "digitalizacija": "digitalizācija",
    "konkuretspeja": "konkurētspēja", "attistiba": "attīstība",
    "ieviesana": "ieviešana", "istenosana": "īstenošana",
    "novertejums": "novērtējums", "novertesana": "novērtēšana",
    "metodologija": "metodoloģija", "metodes": "metodes",
    "hipoteze": "hipotēze", "hipotezes": "hipotēzes", "tezes": "tēzes",
    "aktualitate": "aktualitāte", "rezultati": "rezultāti",
    "literatura": "literatūra", "literaturas": "literatūras",
    "attels": "attēls", "atteli": "attēli",
    "zinatniska": "zinātniskā", "zinatniskais": "zinātniskais",
    "novitate": "novitāte", "nozime": "nozīme",
    "produktivitate": "produktivitāte", "inovacijas": "inovācijas",
    "tehnologijas": "tehnoloģijas", "digitalais": "digitālais",
    "digitala": "digitālā", "vidējie": "vidējie", "videjie": "vidējie",
    "mazie": "mazie", "izlases": "izlases", "aptauja": "aptauja",
    "anketa": "anketa", "respondenti": "respondenti",
    "gadijuma": "gadījuma", "izpete": "izpēte", "analize": "analīze",
    "korelacija": "korelācija", "regresija": "regresija",
    "ticamiba": "ticamība", "validitate": "validitāte",
    "vadibas": "vadības", "parvaldiba": "pārvaldība",
    "efektivitate": "efektivitāte", "ietekmes": "ietekmes",
}
# Entries whose key already equals the correct form are inert by design:
# they document a checked word without producing a false positive.
STRIPPED_FORMS = {k: v for k, v in STRIPPED_FORMS.items() if k != v}

NUM_RE = re.compile(
    r"(?<![\w])("
    r"\d{1,3}(?:[ \u00a0,.]\d{3})+(?:[.,]\d+)?"   # grouped: 1,250,000 / 1 250 000
    r"|\d+(?:[.,]\d+)?"                            # plain: 384 / 3.42 / 0,05
    r")(?![\w])"
)
WORD_RE = re.compile(r"[A-Za-zĀČĒĢĪĶĻŅŠŪŽāčēģīķļņšūž]+")
ACRONYM_RE = re.compile(r"\b[A-ZĀČĒĢĪĶĻŅŠŪŽ]{2,6}\b")


def normalize_number(tok: str) -> str:
    """Reduce a numeric token to a canonical value string comparable across
    English and Latvian formatting conventions.

    Handles: 1,250,000 / 1 250 000 / 1.250.000 as grouped integers, and
    3.42 / 3,42 / 0,05 as decimals. A two-part token whose tail is exactly
    three digits is read as thousands grouping, so a genuine decimal written
    as 1,500 (= one and a half) is canonicalized as 1500; such values are rare
    in this domain, and the same rule is applied to both texts, so parity
    checking stays symmetric.
    """
    t = tok.replace("\u00a0", "").replace(" ", "")

    if "," in t and "." in t:
        dec = max(t.rfind(","), t.rfind("."))
        whole = re.sub(r"[.,]", "", t[:dec])
        frac = t[dec + 1:]
    else:
        sep = "," if "," in t else ("." if "." in t else None)
        if sep is None:
            whole, frac = t, ""
        else:
            parts = t.split(sep)
            grouped = len(parts) > 2 or (len(parts) == 2
                                         and len(parts[1]) == 3
                                         and 1 <= len(parts[0]) <= 3)
            if grouped:
                whole, frac = "".join(parts), ""
            else:
                whole, frac = parts[0], parts[1]

    frac = frac.rstrip("0")
    whole = whole.lstrip("0") or "0"
    return f"{whole}.{frac}" if frac else whole


def numeric_parity(src: str, tgt: str):
    s = Counter(normalize_number(m.group(0)) for m in NUM_RE.finditer(src))
    t = Counter(normalize_number(m.group(0)) for m in NUM_RE.finditer(tgt))
    missing = [(v, s[v] - t.get(v, 0)) for v in s if s[v] > t.get(v, 0)]
    added = [(v, t[v] - s.get(v, 0)) for v in t if t[v] > s.get(v, 0)]
    return sorted(missing), sorted(added)


def decimal_dots(tgt: str):
    return [m.group(0) for m in re.finditer(r"(?<!\d\.)\b\d+\.\d+\b", tgt)]


def diacritic_report(tgt: str):
    letters = [c for c in tgt if c.isalpha()]
    density = sum(1 for c in letters if c in LV_DIACRITICS) / len(letters) if letters else 0.0
    words = [w.lower() for w in WORD_RE.findall(tgt)]
    hits = sorted({w for w in words if STRIPPED_FORMS.get(w)})
    return density, [(w, STRIPPED_FORMS[w]) for w in hits]


def residual_english(tgt: str):
    words = [w.lower() for w in WORD_RE.findall(tgt)]
    found = Counter(w for w in words if w in ENGLISH_MARKERS)
    return found.most_common()


def figure_table_parity(src: str, tgt: str):
    src_fig = len(re.findall(r"\bfig(?:ure)?\.?\s*\d+", src, re.I))
    src_tab = len(re.findall(r"\btable\s*\d+", src, re.I))
    tgt_fig = len(re.findall(r"\d+\.\s*att\.", tgt))
    tgt_tab = len(re.findall(r"\d+\.\s*tab(?:ula)?\.?", tgt))
    tgt_fig += len(re.findall(r"\d+\.\s*attēls", tgt))
    return {
        "source_figures": src_fig, "target_figures": tgt_fig,
        "source_tables": src_tab, "target_tables": tgt_tab,
    }


def quotation_marks(tgt: str):
    ascii_q = len(re.findall(r'"', tgt))
    curly_en = len(re.findall(r"[“”]", tgt))
    lv_q = len(re.findall(r"[„”]", tgt))
    return {"ascii_double": ascii_q, "english_curly": curly_en, "latvian_pairs": lv_q}


def acronym_coverage(src: str, tgt: str):
    known_map = {"SME": "MVU", "ICT": "IKT", "GDP": "IKP", "EU": "ES",
                 "R&D": "P&A", "OECD": "ESAO"}
    src_ac = {a for a in ACRONYM_RE.findall(src) if len(a) >= 2}
    missing = []
    for a in sorted(src_ac):
        lv = known_map.get(a, a)
        if lv not in tgt and a not in tgt:
            missing.append((a, lv))
    return missing


def main():
    ap = argparse.ArgumentParser(description="EN->LV translation mechanical audit")
    ap.add_argument("source")
    ap.add_argument("target")
    ap.add_argument("--json", dest="json_out")
    args = ap.parse_args()

    try:
        src = open(args.source, encoding="utf-8").read()
        tgt = open(args.target, encoding="utf-8").read()
    except OSError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    missing_nums, added_nums = numeric_parity(src, tgt)
    dots = decimal_dots(tgt)
    density, stripped = diacritic_report(tgt)
    english = residual_english(tgt)
    figtab = figure_table_parity(src, tgt)
    quotes = quotation_marks(tgt)
    acronyms = acronym_coverage(src, tgt)

    report = {
        "numbers_missing_in_target": missing_nums,
        "numbers_added_in_target": added_nums,
        "unconverted_decimal_dots": dots,
        "diacritic_density": round(density, 4),
        "diacritic_stripped_words": stripped,
        "residual_english_words": english,
        "figure_table_counts": figtab,
        "quotation_marks": quotes,
        "acronyms_missing_in_target": acronyms,
    }

    print("=" * 60)
    print("EN -> LV TRANSLATION AUDIT")
    print("=" * 60)

    def block(title, items, empty="clean"):
        print(f"\n[{title}]")
        if not items:
            print(f"  {empty}")
        else:
            for it in items:
                print(f"  - {it}")

    block("NUMBERS MISSING IN TARGET", [f"{v} (x{n})" for v, n in missing_nums])
    block("NUMBERS PRESENT ONLY IN TARGET", [f"{v} (x{n})" for v, n in added_nums])
    block("DECIMAL DOTS NOT CONVERTED TO COMMAS", dots)

    print("\n[DIACRITIC DENSITY]")
    print(f"  {density:.2%} of letters carry Latvian diacritics")
    if density < 0.05:
        print("  WARNING: below 5% - text is likely missing diacritics")

    block("DIACRITIC-STRIPPED WORDS", [f"{w} -> {c}" for w, c in stripped])
    block("RESIDUAL ENGLISH WORDS", [f"{w} (x{n})" for w, n in english])

    print("\n[FIGURE / TABLE PARITY]")
    for k, v in figtab.items():
        print(f"  {k}: {v}")
    if figtab["source_figures"] != figtab["target_figures"]:
        print("  WARNING: figure reference counts differ")
    if figtab["source_tables"] != figtab["target_tables"]:
        print("  WARNING: table reference counts differ")

    print("\n[QUOTATION MARKS]")
    for k, v in quotes.items():
        print(f"  {k}: {v}")
    if quotes["ascii_double"] or quotes["english_curly"]:
        print("  WARNING: use Latvian low-high quotes")

    block("ACRONYMS NOT FOUND IN TARGET", [f"{a} (expected {lv})" for a, lv in acronyms])

    print("\n" + "=" * 60)
    print("Mechanical checks only. Meaning, register and terminology")
    print("require the manual passes in references/qa-checklist.md.")
    print("=" * 60)

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"\nJSON written to {args.json_out}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
