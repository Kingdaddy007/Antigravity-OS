---
name: browser-test
description: Use this skill when the user wants to test, inspect, verify, or screenshot a page in the browser (e.g., "/browser-test", "/browser", "test in browser", "take screenshots", "verify in Chrome", "check devtools"). On Windows environments, this skill bypasses browser_subagent and uses Playwright MCP tools to navigate, evaluate JS/scroll, and capture screenshots reliably.
---

# Playwright Browser Testing & DevTools Verification

## PURPOSE
Provides a bulletproof browser verification and screenshot workflow on Windows by leveraging Playwright MCP tools directly (`ServerName: "playwright"`).

## WHEN TO USE THIS
- When the user types `/browser-test`, `/browser`, or requests browser testing on Windows.
- When you need to visually verify UI/UX changes, layout animations, scroll triggers, responsive behavior, or component renders.
- When `browser_subagent` fails or is bypassed due to OS constraints.

## EXECUTION INSTRUCTIONS

When triggered, execute testing using the following step-by-step Playwright MCP workflow:

1. **Navigate**:
   Call `call_mcp_tool` with `ServerName: "playwright"` and `ToolName: "browser_navigate"`:
   ```json
   {
     "ServerName": "playwright",
     "ToolName": "browser_navigate",
     "Arguments": { "url": "http://localhost:3000/path" }
   }
   ```

2. **Evaluate / Interact**:
   Use `browser_evaluate` to execute JS (e.g. scroll to specific element, check offset, verify console errors):
   ```json
   {
     "ServerName": "playwright",
     "ToolName": "browser_evaluate",
     "Arguments": { "function": "() => { window.scrollTo(0, 1000); return window.scrollY; }" }
   }
   ```

3. **Capture Screenshot**:
   Call `browser_take_screenshot` to capture visual evidence:
   ```json
   {
     "ServerName": "playwright",
     "ToolName": "browser_take_screenshot",
     "Arguments": { "type": "png", "scale": "css" }
   }
   ```

4. **Diagnose & Report**:
   Inspect console outputs or errors returned by Playwright. Provide a visual verification summary report to the user with findings and verification state.
