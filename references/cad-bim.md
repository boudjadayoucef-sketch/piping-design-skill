# CAD/BIM Reference

The piping model should remain independent from file formats.

Recommended architecture:

Importer → normalized model → geometry engine → exporter

Potential formats:

- DXF
- DWG
- IFC
- Revit
- CSV
- XLSX
- JSON

The CAD/BIM layer must not contain the core piping business logic.