# Projectile Motion Simulator with Drag

## Key Features
- Shows the path of the projectile
- Graphs for kinetic and potential energy
- Simulates air resistance
- Uses numerical steps to calculate motion (Euler Method)

## Libraries Used
- matplotlib
- math

## Concepts Used
- Newtonian Mechanics
- Vector Math
- Air Resistance
- Euler Integration

## Formulas Used
- Time of Flight
  - T = 2 * vy / g
- Resultant Velocity
  - v = sqrt(vx² + vy²)
- Kinetic Energy
  - KE = 0.5 * m * v²
- Potential Energy
  - PE = m * g * h
- Drag Force
  - Fd = 0.5 * Cd * ρ * A * v²
- Cross Sectional Area
  - A = pi * r²
- Drag Force Components
  - Fx = -Fd * (vx / v)
  - Fy = -Fd * (vy / v)
- Newton's Second Law
  - a = F / m
- Position Update (Euler Method)
  - xnew = xold + vx * dt
  - ynew = yold + vy * dt
- Velocity Update (Euler Method)
  - vnew = vold + a * dt

## How to Run
- Make sure the needed libraries are installed:
  1. pip install matplotlib
- Run the main file:
  1. python Projectile_sim.py
  2. If Windows has issues with python, use this command instead: py Projectile_sim.py
  Make sure you are in the correct folder before running the file.

## Screenshots
- ![Graph 1](Screenshots/Graph_1.png)

