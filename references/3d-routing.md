# 3D Routing Reference

Use XYZ coordinates.

Example:

P1 = (0, 0, 3)
P2 = (5, 0, 3)
P3 = (5, 4, 3)
P4 = (5, 4, 6)

This creates P1 → P2 → P3 → P4.

Directions:

P1→P2 = EAST
P2→P3 = NORTH
P3→P4 = UP

## Geometry engine

Python should perform:

- vector operations
- distance calculations
- intersections
- transformations
- rotations
- bounding boxes
- collision tests

## Routing rules

A valid route must:

1. contain connected segments;
2. have valid coordinates;
3. have positive segment lengths;
4. preserve pipe diameter;
5. use compatible components;
6. avoid prohibited collisions.

## Data flow

User request → AI interpretation → structured routing instruction → Python geometry engine → updated 3D model → validation.