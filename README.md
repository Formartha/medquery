# medquery marketplace

A Claude Code plugin marketplace for biomedical research. Turn authoritative medical sources into a first-class research tool — ask a clinical or scientific question and get a synthesized answer with real citations, never fabricated.

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

## Plugins

| Plugin | Description | Status |
| --- | --- | --- |
| [`medquery`](plugins/medquery) | Search PubMed and synthesize cited answers. | ✔ available |
| `medquery-trials` | ClinicalTrials.gov registry search. | planned |
| `medquery-fda` | openFDA drug labels, adverse events, recalls. | planned |
| `medquery-europepmc` | Europe PMC (includes preprints + full text). | planned |

## Repository layout

```
.
├── .claude-plugin/
│   └── marketplace.json      ← marketplace manifest (lists all plugins)
├── plugins/
│   └── medquery/             ← individual plugin
│       ├── .claude-plugin/plugin.json
│       ├── agents/
│       ├── skills/
│       ├── scripts/
│       └── requirements.txt
├── README.md
└── LICENSE
```

## License

MIT — see [LICENSE](LICENSE).
