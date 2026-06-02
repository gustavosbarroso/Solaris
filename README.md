# ☀️ Solaris – Energy from the Sun to Your Plate

<div align="center">

### A low-cost solar oven developed through theoretical modeling, numerical simulation, and experimental validation.

</div>

---

## 📖 Overview

**Solaris** was an interdisciplinary project developed by undergraduate students in Engineering Physics, Applied Mathematics, and Mechanical Engineering with the goal of investigating the use of concentrated solar energy for food heating applications.

The project combined:

* Design Thinking methodologies;
* Theoretical thermal modeling;
* Numerical simulations;
* Prototype construction;
* Experimental validation.

By integrating concepts from physics, mathematics, and engineering, Solaris explored how low-cost materials can be used to build a functional solar thermal system.

---

## 🎯 Objectives

* Develop a low-cost solar oven using accessible materials;
* Model the thermal behavior of the system;
* Predict temperature evolution through numerical simulations;
* Construct and test a physical prototype;
* Evaluate the feasibility of solar concentration for thermal applications.

---

## 🧠 Design Process

The project followed a Design Thinking approach that included:

1. Problem identification;
2. Concept generation;
3. Theoretical analysis;
4. Computational modeling;
5. Prototype development;
6. Experimental testing;
7. Performance evaluation.

This process allowed the team to iterate between theory and experimentation throughout the project.

---

## 🔬 Theoretical Modeling

The thermal dynamics of the oven were modeled using an energy balance that accounts for:

* Solar radiation absorption;
* Thermal radiation losses;
* Convective heat exchange with the environment.

The resulting nonlinear differential equation describes the temperature evolution of the system and serves as the basis for the computational simulations.

---

## 💻 Computational Simulation

Numerical simulations were performed to investigate the thermal behavior of the oven under different environmental conditions.

The model was solved using the **Fourth-Order Runge-Kutta (RK4)** method, allowing the study of:

* Heating rates;
* Equilibrium temperatures;
* Effects of irradiance variations;
* Thermal loss mechanisms.

### About this Repository

The original Solaris project combined theoretical, experimental, and computational work.

For clarity and reproducibility, this repository presents an **independent implementation** of the thermal model developed during the project. The objective is to reproduce and explore the physical principles and numerical methods investigated by the team.

---

## 🛠️ Prototype Development

A physical prototype was constructed using commercially available and low-cost components.

### Materials

| Component                       |          Cost |
| ------------------------------- | ------------: |
| Parabolic satellite dish        |      R$ 94.45 |
| Reflective Mylar insulation     |      R$ 38.88 |
| Candles (thermal storage tests) |      R$ 12.29 |
| **Total Cost**                  | **R$ 145.62** |

The prototype used a reflective parabolic geometry to concentrate incoming solar radiation onto a focal region, increasing the available thermal power.

---

## 📸 Prototype

<p align="center">
<img src="figures/prototype.jpg" width="700">
</p>

*Solaris experimental prototype.*

---

## 📈 Experimental Results

Experimental tests demonstrated the ability of the system to concentrate solar energy and generate significant heating effects.

Observed outcomes included:

* Heating of dry leaves exposed to the focal region;
* Heating of MDF samples through solar concentration;
* Experimental verification of the proposed concept.

These tests provided qualitative validation of the physical principles used throughout the project.

---

## 📊 Numerical Results

<p align="center">
<img src="figures/simulation.png" width="700">
</p>

The numerical model predicts the temperature evolution of the system and allows comparisons between different operating conditions.

Simulation studies can be used to investigate:

* Solar irradiance effects;
* Thermal equilibrium conditions;
* Convective and radiative losses;
* Design optimization strategies.

---

## 🚀 Technologies Used

### Engineering & Physics

* Heat Transfer
* Thermal Radiation
* Energy Balance Analysis
* Renewable Energy Systems

### Programming

* Python
* NumPy
* Matplotlib

### Numerical Methods

* Runge-Kutta 4th Order Method
* Nonlinear Differential Equations

---

## 📂 Repository Structure

```text
Solaris/
│
├── Fornosolar.py
├── README.md
│
├── figures/
│   ├── prototype.jpg
│   ├── simulation.png
│   ├── results_1.jpg
│   └── results_2.jpg
│
└── docs/
    └── project_report.pdf
```

---

## 👥 Team

### Solaris Project Team

* Gustavo Sobreira Barroso — Engineering Physics
* João Luís Motta Martinez — Applied Mathematics
* Lucas Inoue Kuhl Silva — Applied Mathematics
* Ryan Pereira Pedrozo — Mechanical Engineering

---

## 🌎 Impact

Solaris demonstrates how theoretical modeling, numerical simulation, and experimental engineering can be combined to create practical renewable-energy solutions using accessible materials and low-cost technologies.

The project highlights the role of computational physics and engineering design in the development of sustainable technologies.

---

## 📜 License

MIT License.
