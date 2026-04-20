---
name: pubmed
description: Search PubMed and return a synthesized, cited answer to a clinical or scientific question. Use whenever the user asks about medical evidence, treatment comparisons, drug effects, clinical outcomes, diagnostic accuracy, or anything requiring citations from the peer-reviewed biomedical literature. Also invoke when the user types /pubmed.
---

# pubmed — PubMed research

Delegate the user's question to the `pubmed-researcher` subagent, which searches PubMed via NCBI E-utilities and synthesizes findings with inline `[PMID:...]` citations.

## When to use

- The user asks a clinical or biomedical question ("does X help with Y?", "what's the evidence on Z?", "is drug A safer than drug B?").
- The user explicitly invokes `/pubmed <question>`.
- The user asks for citations, references, or "what does the literature say".

Sibling plugins in the `medquery` marketplace (e.g. `/trials`, `/fda`) may be better fits for registry data or regulatory questions — defer to those when the question is clearly about ongoing trials or drug safety signals rather than published literature.

## How to invoke

Launch the `pubmed-researcher` subagent (via the Agent tool) with the user's question as the prompt. Pass the question verbatim — do not pre-summarize or pre-filter it; the subagent is responsible for translating it into PubMed queries.

If the user invoked `/pubmed` with no question, ask them what they want researched before launching the subagent.

## What to return

Relay the subagent's answer to the user as-is. Do not strip citations, references, or the closing disclaimer — they are all part of the answer. The disclaimer (AI tools can make mistakes; not medical advice; verify PMIDs and consult a clinician) MUST appear in every response.
