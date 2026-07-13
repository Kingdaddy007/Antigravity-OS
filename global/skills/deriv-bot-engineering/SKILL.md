---
name: deriv-bot-engineering
description: Design, inspect, or troubleshoot Deriv Bot XML and block-based trading strategies. Use for DBot imports, exported XML, block logic, demo validation, or migration errors; do not use for unrelated trading software.
---

# Deriv Bot Engineering

## Verified Baseline

Rechecked 2026-07-13:

- Deriv's Help Centre describes Deriv Bot as a block-based strategy builder and confirms that strategies are saved and imported as XML.
- A first-party Deriv administrator notice states that the Blockly V10 update made variable names case-insensitive and can cause unsupported-element errors in older XML.

See [the source verification baseline](../../baselines/source-verification.md).

Exact block IDs, nesting, parser versions, field names, ordering, and contract mappings are not a stable public contract. Never infer them from memory or community examples.

## Workflow

1. Ask whether the request is diagnosis, proposal, implementation, or incident mitigation. Diagnosis remains read-only.
2. Obtain a fresh XML export created by the active Deriv Bot surface for the target trade type.
3. Preserve its root namespace, metadata, block IDs, field names, and structural ordering unless the active surface proves a change is required.
4. Compare the failing strategy with the fresh export and isolate the smallest structural difference.
5. Reject duplicate variable names that differ only by case.
6. Make the smallest authorized local edit; never upload, run, fund, or trade without separate explicit approval.
7. Import into a demo account, inspect the reconstructed blocks, and execute only with virtual funds under explicit limits.
8. Record the export date, active surface, observed parser behavior, and test evidence.

## Safety

- Generated XML is code-like trading logic, not financial advice.
- Never embed credentials, API tokens, account identifiers, or secrets.
- Default to a demo account and bounded virtual stake.
- Stop on unsupported elements, missing blocks, changed contract fields, or unexplained behavior.
- Live-account execution is an `external_or_production` mutation and requires just-in-time approval.

## Output Contract

Return the XML or diagnostic diff together with:

- source export and verification date;
- assumptions and unverified fields;
- risk limits;
- demo import result;
- remaining blockers before any live use.
