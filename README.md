# medquery

A Claude Code plugin that turns authoritative biomedical sources into a first-class research tool. Ask a clinical or scientific question and get a synthesized answer with real citations — never fabricated.

**Sources today:** PubMed.
**Planned:** Europe PMC, ClinicalTrials.gov, openFDA, bioRxiv/medRxiv, and more.

## What you get

- **`/medquery <question>`** — user-invocable skill that researches a clinical/scientific question end-to-end.
- **`medquery-researcher` subagent** — searches the available sources, reads abstracts, and writes a cited answer (direct answer, key findings, limitations, references).
- **Auto-invocation** — when you ask something like *"what does the evidence say about X?"*, Claude will route to the skill automatically.

## Install

```
/plugin marketplace add Formartha/medquery
/plugin install medquery@medquery
```

Or via the CLI:

```
claude plugin marketplace add Formartha/medquery
claude plugin install medquery@medquery
```

## Use

```
/medquery does metformin reduce all-cause mortality in type 2 diabetes?
/medquery covid vaccine myocarditis risk in adolescents
```

Or just ask naturally — the skill is description-triggered:

> "What's the evidence on clear aligners vs fixed braces for root resorption?"

## Requirements

- **Python 3** on your PATH (`python3`).
- Uses only the Python standard library. `certifi` is optional but recommended on macOS for clean TLS:
  ```
  pip install -r requirements.txt
  ```
- Optional env vars for higher NCBI rate limits (10 req/s vs 3 req/s):
  - `NCBI_API_KEY` — get one at <https://www.ncbi.nlm.nih.gov/account/>
  - `NCBI_EMAIL` — NCBI asks (politely) for a contact address

## How it works

`pubmed_search.py` is a thin wrapper around [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/) (`esearch` + `efetch`). The subagent decides the query (MeSH, boolean, field tags), calls the script, reads abstracts, and refines up to 3 times before answering.

## License

MIT — see [LICENSE](LICENSE).
