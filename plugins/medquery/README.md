# medquery

Biomedical research plugin for Claude Code. Ask a clinical or scientific question and get a synthesized answer with real `[PMID:...]` citations.

## Install

```
/plugin marketplace add Formartha/medquery
/plugin install medquery@medquery
```

## Use

```
/medquery does metformin reduce all-cause mortality in type 2 diabetes?
```

Or ask naturally — the skill auto-invokes on biomedical questions:

> "What does the evidence say about clear aligners vs fixed braces for root resorption?"

## Layout

```
plugins/medquery/
├── .claude-plugin/plugin.json
├── agents/medquery-researcher.md   ← subagent that runs the searches
├── skills/medquery/SKILL.md        ← /medquery entry point
├── scripts/
│   └── pubmed_search.py            ← NCBI E-utilities wrapper
└── requirements.txt
```

## Requirements

- `python3` on PATH. Only stdlib is used; `certifi` is optional (recommended on macOS).
- Optional env vars for higher NCBI rate limits: `NCBI_API_KEY`, `NCBI_EMAIL`.
