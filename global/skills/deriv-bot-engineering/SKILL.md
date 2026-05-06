---
name: deriv-bot-engineering
description: >
  Use this skill when designing, writing, or troubleshooting Deriv Bot (DBot) XML strategies, 
  Blockly configurations, or trading algorithms for the Deriv platform. Activated when the user 
  mentions "Deriv bot", "DBot", "XML5 format", "Accumulator strategy", "trade_definition", 
  or asks to build/fix a trading bot file. Do NOT use for standard web or backend development 
  (use coding skill) or generic Python/JS trading algorithms outside the DBot ecosystem.
---

# Deriv Bot (DBot) Engineering

## WHEN TO USE THIS

- Generating new `.xml` bot strategies for the Deriv Bot platform.
- Debugging "Unsupported elements" or "XML5 Format" import errors on Deriv.
- Designing block logic for DBot options like Accumulators, Rise/Fall, or Martingale.

## NEVER DO

- Never generate flat `<block type="trade">` structures. They are deprecated and will crash the V10 parser.
- Never use generic XML namespaces (e.g., W3 XHTML) in the root tag.
- Never define duplicate variables with different casing (e.g., `Stake` vs `STAKE`).
- Never guess custom block names. Only use verified Deriv Blockly structural tags.
- Never write raw Javascript inside the XML; DBot XML is pure serialized Blockly logic.

## V10 ARCHITECTURE REQUIREMENTS

Every bot file MUST wrap its setup inside a deeply nested `trade_definition` chain.

The root tags MUST be: 
`<xml xmlns="https://developers.google.com/blockly/xml" is_dbot="true" collection="false">`

Inside the `TRADE_OPTIONS` statement, you MUST chain blocks sequentially using the `<next>` tag in this exact order:
1. `trade_definition_market`
2. `trade_definition_tradetype`
3. `trade_definition_contracttype`
4. `trade_definition_candleinterval`
5. `trade_definition_restartbuysell`
6. `trade_definition_restartonerror`

## ACCUMULATOR CONFIGURATION

Accumulator logic MUST reside inside the `SUBMARKET` statement of the main definition block.
Use the `<block type="trade_definition_tradeoptions">` tag.
Set the Barrier value via the `BARRIER` value block. Barrier values directly map to growth rates: `<field name="NUM">1</field>` = 1% growth rate.

## ANTI-PATTERNS

| Anti-Pattern | What It Is | Fix |
| --- | --- | --- |
| The HTML Trap | Using `xmlns="http://www.w3.org/1999/xhtml"` in the root XML tag. | Use `xmlns="https://developers.google.com/blockly/xml"`. |
| The Flat Trade Block | Using `<block type="trade">` to define the strategy setup. | Use the deeply nested `trade_definition` chain. |
| Case Conflicts | Defining `Win` and `win` as separate variables. | Blockly V10 is case-insensitive. Consolidate to one casing. |

## OUTPUT SHAPE

**When generating a bot:** Explanation of the strategy logic (1-2 sentences) → The V10-compliant XML code block → Instructions to import via the Deriv folder icon.
**When fixing a bot:** Identification of the broken block or namespace (1 sentence) → Corrected XML code → Brief explanation of why the V10 parser rejected the old structure.

## NON-NEGOTIABLE CHECKLIST

- [ ] Root tag contains the exact Google developers Blockly XML namespace.
- [ ] Root tag contains `is_dbot="true"`.
- [ ] Setup logic is properly nested inside the `trade_definition` chain using `<next>` tags.
- [ ] Accumulator specific logic is correctly mapped to `SUBMARKET` -> `trade_definition_tradeoptions`.
- [ ] Variable casing is strictly uniform throughout the entire file.
- [ ] No generic/legacy `<block type="trade">` blocks exist in the output.
