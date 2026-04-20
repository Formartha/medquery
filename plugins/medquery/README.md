# medquery

Biomedical research plugin for Claude Code. Ask a clinical or scientific question and get a synthesized answer with real citations from authoritative medical sources — never fabricated.

One plugin, one skill per source. Install once, get `/medquery-pubmed` today; more sources drop in as new sibling skills.

## Install

```
/plugin marketplace add Formartha/medquery
/plugin install medquery@medquery
```

## Skills

| User invocation | Source | Status |
| --- | --- | --- |
| `/medquery-pubmed <question>` | PubMed (NCBI E-utilities) | ✔ available |
| `/medquery-trials <question>` | ClinicalTrials.gov | planned |
| `/medquery-fda <question>` | openFDA drug labels, adverse events, recalls | planned |
| `/medquery-europepmc <question>` | Europe PMC (preprints + full text) | planned |

Each skill also auto-invokes on natural-language biomedical questions — e.g. *"what does the evidence say about clear aligners vs fixed braces for root resorption?"* routes to `medquery-pubmed` automatically.

## Layout

```
plugins/medquery/
├── .claude-plugin/plugin.json
├── skills/
│   └── medquery-pubmed/SKILL.md    ← /medquery-pubmed (user + auto)
├── agents/
│   └── pubmed-researcher.md        ← subagent that runs the searches
├── scripts/
│   └── pubmed_search.py            ← NCBI E-utilities wrapper
└── requirements.txt
```

As new sources are added, each drops in as a sibling set: `skills/medquery-trials/SKILL.md`, `agents/trials-researcher.md`, `scripts/trials_search.py` — no restructure.

## Requirements

- `python3` on PATH. Only stdlib is used; `certifi` is optional (recommended on macOS).
- Optional env vars for higher NCBI rate limits: `NCBI_API_KEY`, `NCBI_EMAIL`.

## Disclaimer

medquery is an AI-assisted research tool. **Every AI tool — including this one — can make mistakes.** Answers can misread abstracts, miss important studies, misstate effect sizes, or cite studies out of context. Treat every response as a starting point, not a conclusion.

- **Not medical advice.** Nothing produced by this plugin is a substitute for professional clinical judgment. Consult a licensed healthcare provider for anything affecting real patients.
- **Verify the citations.** Open the PMIDs the plugin returns and read the actual abstracts / full text before acting on any claim.
- **Evidence evolves.** PubMed indexing lags; preprints and ongoing trials may change the picture.

Take every answer with a grain of salt.
