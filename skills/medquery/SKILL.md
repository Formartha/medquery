---
name: medquery
description: Research a clinical or scientific question against authoritative biomedical sources (PubMed today; Europe PMC, ClinicalTrials.gov, openFDA, and more planned) and return a synthesized, cited answer. Use whenever the user asks about medical evidence, treatment comparisons, drug effects, clinical outcomes, diagnostic accuracy, or anything requiring citations from the biomedical literature. Also invoke when the user types /medquery.
---

# medquery — biomedical research

Delegate the user's question to the `medquery-researcher` subagent, which searches authoritative biomedical sources and synthesizes findings with inline citations (e.g. `[PMID:...]`).

## When to use

- The user asks a clinical or biomedical question ("does X help with Y?", "what's the evidence on Z?", "is drug A safer than drug B?").
- The user explicitly invokes `/medquery <question>`.
- The user asks for citations, references, or "what does the literature say".

## How to invoke

Launch the `medquery-researcher` subagent (via the Agent tool) with the user's question as the prompt. Pass the question verbatim — do not pre-summarize or pre-filter it; the subagent is responsible for translating it into source-specific queries.

If the user invoked `/medquery` with no question, ask them what they want researched before launching the subagent.

## What to return

Relay the subagent's answer to the user as-is. Do not strip citations, references, or caveats — the citations are the point.
