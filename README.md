# Air Density vs. Altitude Analysis

### Exploring Air Density with Python

I first learned at school that air pressure and other properties of the atmosphere change with altitude. I found this interesting and wanted to understand these changes beyond what I had learned in class.

While studying Python through Harvard's CS50P course, I started looking for a project that could connect programming with my interests in mathematics, physics, and aerospace engineering. I decided to build a program that lets users calculate atmospheric properties at different altitudes and explore the results for themselves.

The program calculates air temperature, pressure, and density at altitudes from 0 to 11,000 meters. It can calculate values for a single altitude, display a table of results, plot air density against altitude, and show how much the modeled density decreases compared with its value at sea level.

The calculations use a simplified atmospheric model published by NASA Glenn Research Center. Building this project has given me a way to put my Python skills into practice while learning more about aerodynamics and flight physics.

## Project Goals

Through this project, I wanted to:

- Connect what I have learned in mathematics and physics with practical Python programming.
- Explore how atmospheric properties change with altitude.
- Create a simple tool that students, curious users, and people interested in scientific computing can use to explore these calculations.

## Features

- **Single-Altitude Calculation:** Calculate temperature, pressure, and air density at a selected altitude between 0 and 11,000 meters.
- **Atmospheric Properties Table:** View the calculated values at 1,000-meter intervals.
- **Air Density Plot:** See how air density changes with altitude, using calculation points spaced 100 meters apart.
- **Density Reduction:** Calculate the percentage decrease in air density compared with the model's sea-level value.
- **Input Validation:** Handle invalid inputs and keep the selected altitude within the supported range.

## Scientific Model

This project uses the simplified metric atmospheric equations published by NASA Glenn Research Center for the troposphere, from sea level to 11,000 meters.

The program uses the following equations, where `h` is altitude in meters.

**Temperature (°C)**

`T = 15.04 - 0.00649 × h`

**Pressure (kPa)**

`p = 101.29 × ((T + 273.1) / 288.08)^5.256`

**Air Density (kg/m³)**

`ρ = p / (0.2869 × (T + 273.1))`

Here, `T` is the temperature in degrees Celsius. The pressure equation converts it to kelvin as part of the calculation. Pressure is expressed in kilopascals, and density in kilograms per cubic meter.

The percentage decrease in density is calculated relative to the value at sea level:

`Reduction (%) = ((ρ₀ - ρₕ) / ρ₀) × 100`

Here, `ρ₀` is the modeled sea-level density and `ρₕ` is the density at the selected altitude.

## Technologies

- **Python** for calculations, input validation, and program logic.
- **Matplotlib** for plotting air density against altitude.

## Installation

Make sure Python is installed, then install the required library:

`python -m pip install -r requirements.txt`

## How to Run

Open a terminal in the project folder and run:

`python main.py`

Follow the menu to calculate atmospheric properties, view the table, display the graph, or compare air density with its sea-level value.

## Assumptions and Limitations

- The results are estimates from a standard-atmosphere model, not real-time weather measurements.
- The program is designed for altitudes between 0 and 11,000 meters.
- Real atmospheric conditions vary with location, time, and weather. This model describes how atmospheric properties vary with altitude under standard conditions.
- Air density affects aerodynamic forces, but this project does not simulate the full performance of an aircraft.
- As a learning project, it can be improved through further testing and development.

## Scientific Reference

NASA Glenn Research Center. [Earth Atmosphere Equation — Metric](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/earth-atmosphere-equation-metric/)
