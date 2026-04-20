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

## Commands

One plugin, one slash namespace. Each biomedical source gets its own command under `/medquery:*`.

| Command | Source | Status |
| --- | --- | --- |
| `/medquery:pubmed <question>` | PubMed (NCBI E-utilities) | ✔ available |
| `/medquery:trials <question>` | ClinicalTrials.gov | planned |
| `/medquery:fda <question>` | openFDA drug labels, adverse events, recalls | planned |
| `/medquery:europepmc <question>` | Europe PMC (preprints + full text) | planned |

## Disclaimer

medquery is an AI-assisted research tool. **Every AI tool — including this one — can make mistakes.** Answers can misread abstracts, miss important studies, misstate effect sizes, or cite studies out of context. Treat every response as a starting point, not a conclusion:

- **Not medical advice.** Nothing produced by this plugin is a substitute for professional clinical judgment. Consult a licensed healthcare provider for anything affecting real patients.
- **Verify the citations.** Open the PMIDs the plugin returns and read the actual abstracts / full text before acting on any claim.
- **Evidence evolves.** PubMed indexing lags; preprints and ongoing trials may change the picture.

Take everything with a grain of salt.

## License

MIT — see [LICENSE](LICENSE).
