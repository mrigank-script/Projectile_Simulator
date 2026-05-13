# Projectile Motion Simulator with Drag
### Physics-Based Numerical Simulation Using the Euler Integration Method

> A computational physics simulator that models projectile motion under both ideal (vacuum) and realistic (drag) conditions. Implements Newtonian mechanics and numerical integration from scratch using only Python's standard library and Matplotlib — no physics or simulation frameworks used.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Physics & Mathematical Foundation](#physics--mathematical-foundation)
4. [Simulation Architecture](#simulation-architecture)
5. [Default Simulation Parameters](#default-simulation-parameters)
6. [Project Structure](#project-structure)
7. [Installation & Setup](#installation--setup)
8. [How to Run](#how-to-run)
9. [Output & Visualisations](#output--visualisations)
10. [Sample Output](#sample-output)

---

## Project Overview

This simulator computes and visualises the trajectory of a projectile under two conditions simultaneously:

| Simulation Mode | Description |
|---|---|
| **No Drag (Ideal)** | Pure Newtonian mechanics — gravity only |
| **With Drag (Realistic)** | Gravity + velocity-dependent aerodynamic drag force |

Both trajectories are computed using the **Euler Method** — a first-order numerical integration technique — with a time step of `dt = 0.0001 s` for high resolution. The simulator also tracks and plots the **kinetic and potential energy** of the projectile over time for both conditions, allowing direct observation of energy dissipation caused by air resistance.

---

## Key Features

- **Side-by-side trajectory comparison** — ideal vs. drag-affected paths plotted on the same axes
- **Energy analysis** — kinetic energy (KE) and potential energy (PE) graphed against time for both conditions
- **Realistic air resistance model** — drag force computed using the standard aerodynamic drag equation with physically accurate constants (Cd = 0.47 for a sphere, ρ = 1.225 kg/m³ for air at sea level)
- **Velocity decomposition** — initial velocity split into horizontal and vertical components; drag force decomposed back into component form at every time step
- **Analytical vs. numerical comparison** — theoretical time of flight (analytical) printed alongside the numerically computed time of flight for validation
- **Slope calculation** — instantaneous trajectory slope computed at every point along the path (foundation for future extensions such as angle-of-impact analysis)
- **No simulation frameworks** — built entirely with `math` and `matplotlib`; all physics computed manually

---

## Physics & Mathematical Foundation

### Velocity Decomposition

Initial velocity is projected onto horizontal and vertical axes:

$$v_x = v \cos\theta \qquad v_y = v \sin\theta$$

---

### Resultant Speed

At every time step, the resultant speed is computed from the velocity components:

$$v = \sqrt{v_x^2 + v_y^2}$$

---

### Kinetic & Potential Energy

$$KE = \frac{1}{2}mv^2 \qquad PE = mgh$$

where $h$ is the current vertical position of the projectile.

---

### Aerodynamic Drag Force

The drag force magnitude is given by:

$$F_d = \frac{1}{2} C_d \rho A v^2$$

where the cross-sectional area of the spherical projectile is:

$$A = \pi r^2$$

The drag force is then resolved into components opposing the direction of motion:

$$F_x = -F_d \cdot \frac{v_x}{v} \qquad F_y = -F_d \cdot \frac{v_y}{v}$$

---

### Newton's Second Law — Acceleration

$$a_x = \frac{F_x}{m} \qquad a_y = \frac{F_y}{m} - g$$

For the no-drag case: $a_x = 0$, $a_y = -g$

---

### Euler Method — Numerical Integration

Position and velocity are updated at each time step $\Delta t$:

**Position update:**

$$x_{n+1} = x_n + v_x \cdot \Delta t$$

$$y_{n+1} = y_n + v_y \cdot \Delta t$$

**Velocity update:**

$$v_{x,n+1} = v_{x,n} + a_x \cdot \Delta t$$

$$v_{y,n+1} = v_{y,n} + a_y \cdot \Delta t$$

The simulation loop continues until both trajectories return to ground level ($y < 0$).

---

### Analytical Time of Flight (No Drag — Validation Reference)

$$T = \frac{2 v_y}{g}$$

This closed-form result is printed alongside the numerically computed time of flight to validate the accuracy of the Euler integration.

---

### Trajectory Slope

The instantaneous slope of the trajectory is computed at every step:

$$m_i = \frac{y_{i+1} - y_i}{x_{i+1} - x_i}$$

This lays the groundwork for future extensions such as computing the impact angle.

---

## Simulation Architecture

```
Input: Initial Conditions (v, θ, m, r)
        │
        ├── Velocity Decomposition ──────── vx = v·cos(θ),  vy = v·sin(θ)
        │
        └── Euler Integration Loop (dt = 0.0001 s)
                │
                ├── No Drag Path ────────── ay = -g only
                │       └── Position, KE, PE recorded each step
                │
                └── With Drag Path ──────── Fd computed → Fx, Fy resolved
                        └── ax = Fx/m,  ay = Fy/m - g
                        └── Position, KE, PE recorded each step
                │
                Break condition: yi < 0 AND yi_drag < 0
                │
Output:
        ├── Plot 1 — Trajectory: No Drag vs With Drag
        └── Plot 2 — Energy (KE & PE) vs Time for both conditions
```

---

## Default Simulation Parameters

| Parameter | Symbol | Value | Unit |
|---|---|---|---|
| Mass | $m$ | 5 | kg |
| Radius | $r$ | 0.1 | m |
| Initial Speed | $v$ | 50 | m/s |
| Launch Angle | $\theta$ | 60 | degrees |
| Time Step | $\Delta t$ | 0.0001 | s |
| Gravitational Acceleration | $g$ | 9.8 | m/s² |
| Drag Coefficient (sphere) | $C_d$ | 0.47 | — |
| Air Density (sea level) | $\rho$ | 1.225 | kg/m³ |

---

## Project Structure

```
Projectile_Simulator/
│
├── Projectile_sim.py     # Main script — simulation, physics, and plots
└── README.md             # Project documentation
```

---

## Installation & Setup

Ensure Python 3.x is installed, then install the only required external library:

```bash
pip install matplotlib
```

The `math` module is part of Python's standard library — no separate installation needed.

**Dependencies summary:**

| Library | Purpose |
|---|---|
| `matplotlib` | Trajectory and energy visualisation |
| `math` | Trigonometric functions (`sin`, `cos`, `sqrt`, `pi`) |

---

## How to Run

Navigate to the project directory and execute:

```bash
python Projectile_sim.py
```

> Windows alternative: `py Projectile_sim.py`

**What happens at runtime:**

1. Initial velocity is decomposed into horizontal and vertical components
2. The Euler integration loop runs with `dt = 0.0001 s` — simulating both trajectories simultaneously at each time step
3. KE, PE, and position are recorded every step for both conditions
4. The loop terminates when both projectiles return to ground level
5. Analytical and numerical times of flight are printed to the console
6. Two side-by-side plots are displayed

---

## Output & Visualisations

### Plot 1 — Trajectory Comparison

Displays the x–y flight path of both the ideal (no drag) and realistic (with drag) projectiles on the same axes. The drag-affected trajectory reaches a lower maximum height and shorter horizontal range, clearly illustrating the energy-dissipating effect of air resistance.

### Plot 2 — Energy vs Time

Plots KE and PE against time for both conditions. In the no-drag case, total mechanical energy (KE + PE) remains constant — validating conservation of energy. In the drag case, total energy decreases monotonically as work is done against the drag force.

---

## Sample Output

```
Console output:
Analytical time of flight (no drag) : 8.8408 s
Numerical time of flight  (with drag): 7.3120 s
```

The reduction in flight time under drag is a direct consequence of energy loss to air resistance, reducing both peak height and horizontal range compared to the ideal trajectory.

---

> **Note:** Simulation parameters (mass, radius, initial speed, launch angle) can be modified at the top of `Projectile_sim.py` to explore different physical scenarios.
