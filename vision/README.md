# Vision pipeline

This directory defines the provider-neutral contract for photo/sketch recognition.

## Contract

```text
image
  -> detector / VLM / segmentation / OCR adapters
  -> observation.json
  -> topology / reconstruction
```

The vision layer must not emit engineering geometry as fact. Image-derived values remain observations with confidence and evidence.

## Provider neutrality

A future implementation may use a VLM, SAM, YOLO, OCR engine, or a combination. The downstream skills consume only `schemas/observation.json`.

## Minimum output

- source metadata
- detected objects
- text observations
- visual relations
- confidence
- evidence references

See `agents/vision/SKILL.md` and `schemas/observation.json`.