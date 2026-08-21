# LangFlow workflows

LangFlow is the orchestration layer for PD&I AI workflows. The repository remains the versioned source for skills, rules, schemas, and workflow definitions.

## Planned workflows

1. `sketch-to-isometric`: vision → geometry → topology → validation → human confirmation.
2. `component-search`: user request → catalog/RAG → compatibility checks → proposal.
3. `project-audit`: project graph → engineering validators → warnings/errors.

## Integration boundary

PD&I React communicates with an AI gateway. The gateway submits asynchronous jobs to LangFlow. LangFlow invokes versioned skills from this repository and returns structured results.

LangFlow must not become the source of truth for geometry or engineering rules.
