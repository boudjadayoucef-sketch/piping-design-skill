# Vision providers

Concrete providers belong here and must implement `VisionProvider`.

Expected boundary:

```text
provider SDK -> normalized fields -> Observation -> structural validation
```

A provider must not modify the canonical piping model and must not perform
engineering validation. Keep credentials and provider configuration outside
these modules.

Planned adapters can include Gemini, OpenAI Vision, SAM/YOLO and OCR, but no
provider is mandatory for the core skill.
