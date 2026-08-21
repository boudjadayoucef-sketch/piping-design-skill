# PD&I AI agents

This directory defines the agent layer for PD&I. Agents orchestrate skills; they do not replace deterministic engineering validation.

## Planned agents

- `piping-auditor`: validates project graphs and reports engineering issues.
- `component-selector`: searches component knowledge and proposes compatible components.
- `sketch-to-isometric`: coordinates vision, geometry, topology, and validation skills.
- `engineering-assistant`: user-facing assistant that decomposes engineering requests into skills.

## Design rule

**AI proposes → deterministic skills verify → user validates.**

Heavy operations must run asynchronously in queues/workers so they do not block the PD&I UI.

The roadmap source explicitly requires heavy future tasks to use queues/workers and defines human validation for the vision workflow.
