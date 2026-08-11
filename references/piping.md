# Piping Reference

## Components

Core components:

- Pipe
- Elbow
- Tee
- Reducer
- Flange
- Valve
- Instrument
- Equipment
- Nozzle
- Support

## Pipe properties

Recommended properties:

- id
- line_number
- nominal_diameter
- material
- schedule
- pipe_class
- fluid
- pressure
- temperature
- insulation

## Connectivity

Every component should expose connection points.

Example:

Equipment nozzle → flange → valve → flange → pipe → elbow → pipe

Connections must be explicitly represented.

## Line

A pipeline should have:

- unique ID
- line number
- specification
- components
- segments
- start connection
- end connection

## Engineering data

Do not invent pressure, temperature, material, pipe class, wall thickness or design code. When information is missing, mark it as unknown.