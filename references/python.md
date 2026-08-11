# Python Development Reference

Recommended structure:

geometry/
piping/
routing/
isometric/
pid/
cad/
mto/
qa/
models/

Keep UI, business logic and geometry calculations separated.

Use typed Python models, dataclasses or Pydantic, type hints, unit tests, JSON serialization and clear interfaces.

Geometry calculations must be deterministic.

Never rely on LLM-generated numerical geometry when the application can calculate it.