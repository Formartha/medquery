# medquery-pubmed

PubMed source for the [`medquery`](../../README.md) marketplace. Ask a clinical or scientific question and get a synthesized answer with real `[PMID:...]` citations from the peer-reviewed biomedical literature.

## Install

```
/plugin marketplace add Formartha/medquery
/plugin install medquery-pubmed@medquery
```

## Use

```
/pubmed does metformin reduce all-cause mortality in type 2 diabetes?
```

Or ask naturally — the skill auto-invokes on biomedical questions:

> "What does the evidence say about clear aligners vs fixed braces for root resorption?"

## Layout

```
plugins/medquery-pubmed/
├── .claude-plugin/plugin.json
├── agents/pubmed-researcher.md   ← subagent that runs the searches
├── skills/pubmed/SKILL.md        ← /pubmed entry point
├── scripts/
│   └── pubmed_search.py          ← NCBI E-utilities wrapper
└── requirements.txt
```

## Requirements

- `python3` on PATH. Only stdlib is used; `certifi` is optional (recommended on macOS).
- Optional env vars for higher NCBI rate limits: `NCBI_API_KEY`, `NCBI_EMAIL`.

## Disclaimer

medquery-pubmed is an AI-assisted research tool. **Every AI tool — including this one — can make mistakes.** Answers can misread abstracts, miss important studies, misstate effect sizes, or cite studies out of context. Treat every response as a starting point, not a conclusion.

- **Not medical advice.** Nothing produced by this plugin is a substitute for professional clinical judgment. Consult a licensed healthcare provider for anything affecting real patients.
- **Verify the citations.** Open the PMIDs the plugin returns and read the actual abstracts / full text before acting on any claim.
- **Evidence evolves.** PubMed indexing lags; preprints and ongoing trials may change the picture.

Take every answer with a grain of salt.
