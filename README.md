# ☀️ Solaris – Energy from the Sun to Your Plate

<div align="center">

### A low-cost solar thermal oven developed through theoretical modeling, numerical simulation, and experimental prototyping.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Physics](https://img.shields.io/badge/Computational%20Physics-Modeling-orange)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

## 📖 Overview

**Solaris** is an interdisciplinary engineering project focused on the development of a low-cost solar thermal oven capable of converting solar radiation into usable thermal energy.

The project integrated concepts from:

* Engineering Physics
* Applied Mathematics
* Mechanical Engineering
* Heat Transfer
* Renewable Energy Systems
* Computational Modeling

The development process combined theoretical analysis, numerical simulations, prototype construction, and experimental validation to investigate the feasibility of solar concentration for food-heating applications.

---

## 🎓 Academic Context

Solaris was developed during the undergraduate course:

**EX067 – Development and Prototyping of Social Impact Projects in a Maker Environment**
(*Desenvolvimento e prototipagem de projetos de impacto social em ambiente Maker*)

**University of Campinas (UNICAMP)**
**1st Semester of 2025**

The course focuses on project-development methodologies, maker-space prototyping, and proof-of-concept validation for products and services with potential social impact.

As part of this initiative, the Solaris team proposed, designed, modeled, prototyped, and experimentally evaluated a solar thermal oven built from accessible and low-cost materials.

---

## 🎯 Objectives

* Develop a low-cost solar oven using accessible materials;
* Explore the use of concentrated solar energy for thermal applications;
* Model the thermal behavior of the system;
* Predict temperature evolution through numerical simulations;
* Construct and experimentally test a physical prototype;
* Evaluate the viability of the proposed design.

---

## 🧠 Design Process

The project followed a Design Thinking workflow:

1. Problem identification;
2. Concept development;
3. Theoretical modeling;
4. Computational simulation;
5. Prototype construction;
6. Experimental testing;
7. Performance evaluation.

This iterative process allowed the team to connect theoretical predictions with real-world observations.

---

## 🔬 Theoretical Modeling

The thermal behavior of the oven was described through an energy balance involving:

* Solar radiation absorption;
* Thermal radiation losses;
* Convective heat exchange with the environment.

The resulting nonlinear differential equation governs the temperature evolution of the system and serves as the foundation of the numerical simulations presented in this repository.

---

## 💻 Computational Simulation

To investigate the thermal performance of the oven under different conditions, a numerical model was implemented in Python.

The governing differential equation is solved using the **Fourth-Order Runge-Kutta (RK4)** method.

The simulation allows the study of:

* Heating rates;
* Equilibrium temperatures;
* Solar irradiance effects;
* Convective losses;
* Radiative losses;
* Environmental influences on performance.

### About this Repository

The original Solaris project combined theoretical, experimental, and computational work.

For clarity and reproducibility, this repository presents an **independent implementation** of the thermal model developed during the project. The objective is to reproduce and explore the physical principles, numerical methods, and engineering concepts investigated by the team.

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

The prototype employed a reflective parabolic geometry capable of concentrating incoming solar radiation onto a focal region, increasing the available thermal power.

---

## 📸 Prototype

<p align="center">
<img src="figures/prototype.jpg" width="700">
</p>

*Solaris experimental prototype.*

---

## 📈 Experimental Results

Experimental tests demonstrated the ability of the system to concentrate solar energy and produce measurable heating effects.

Observed outcomes included:

* Heating of dry leaves exposed to the focal region;
* Heating of MDF samples through concentrated solar radiation;
* Validation of the proposed proof of concept.

These results provided qualitative verification of the physical principles employed throughout the project.

---

## 📊 Numerical Results

<p align="center">
<img src="figures/simulation.png" width="700">
</p>

The computational model predicts the temperature evolution of the system and enables comparisons between different operating conditions.

Simulation studies can be used to investigate:

* Solar irradiance effects;
* Thermal equilibrium conditions;
* Convective and radiative heat losses;
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

* Fourth-Order Runge-Kutta (RK4)
* Nonlinear Differential Equations

---

## 📂 Repository Structure

```text
Solaris/
│
├── solar-oven.py
├── README.md
├── LICENSE
│
└── figures/
    ├── prototype.jpg
    ├── simulation.png
    ├── results_1.jpg
    └── results_2.jpg
```

---

## 👥 Team

### Solaris Project Team

Developed for:

**EX067 – Development and Prototyping of Social Impact Projects in a Maker Environment**
**University of Campinas (UNICAMP)**

Instructor:

**Prof. Eder Socrates Najar Lopes**

Team members:

* Gustavo Sobreira Barroso — Engineering Physics
* João Luís Motta Martinez — Applied Mathematics
* Lucas Inoue Kuhl Silva — Applied Mathematics
* Ryan Pereira Pedrozo — Mechanical Engineering

---

## 🌎 Impact

Solaris demonstrates how theoretical modeling, numerical simulation, and experimental engineering can be combined to develop practical renewable-energy solutions using accessible materials and low-cost technologies.

The project highlights the role of computational physics, engineering design, and maker-based prototyping in the development of socially impactful technologies.

---

## 📜 License

This repository is distributed under the MIT License.
