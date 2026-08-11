# Isometric Reference

Input: 3D piping model.

Output: isometric drawing data.

## Required information

- line number
- pipe segments
- fittings
- valves
- coordinates
- elevations
- dimensions
- component tags
- flow direction

## Process

3D model → centerline extraction → component extraction → projection → dimensions → annotations → BOM → drawing.

The AI prepares the information. The deterministic drawing engine generates the final geometry.