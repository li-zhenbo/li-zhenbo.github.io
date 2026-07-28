---
layout: post
title: "Paper Notes — A Cosine Generalized Padé Approximation Method for Periodic Solutions of Strongly Nonlinear Oscillators"
date: 2019-11-18 10:00:00+0800
description: Constructing a cosine-function-series generalized Padé approximant with inherent periodicity for direct periodic solution of strongly nonlinear oscillators
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **Paper:** Li, Z., & Tang, J. (2019). *A Cosine Generalized Padé Approximation Method and Its Application in Solving Periodic Solutions of Strongly Nonlinear Oscillators*. Journal of Vibration and Shock, 38(22), 159–167.
> **Links:** [Essential Summary PDF](/assets/pdf/essential-summary-p9.pdf) · [DOI](https://doi.org/10.13465/j.cnki.jvs.2019.22.023)

## TL;DR

A cosine-function-series generalized Padé approximant with built-in periodicity enables, for the first time, the direct Padé approximation of periodic solutions for strongly nonlinear oscillators — validated on Duffing, Duffing-harmonic, and SD oscillators.

## Background: Why Padé Cannot Directly Solve for Periodic Solutions

Classical Padé approximation constructs rational functions (ratios of polynomials) to approximate a given power series. By their very nature as rational functions, Padé approximants possess limits at infinity — which makes them fundamentally unsuited for approximating periodic functions, which by definition never converge to a limit. No prior study had directly applied Padé approximation to periodic solution problems.

The authors' earlier work introduced the **generalized Padé approximation (GPA)** method, extending the numerator and denominator from polynomials to series composed of arbitrary continuous functions. This paper takes the next step: constructing a generalized Padé approximant whose numerator and denominator are both **series of cosine functions**. Since cosine functions are inherently periodic, the entire approximant carries this periodic character — resolving the fundamental conflict between Padé approximation and periodic solutions.

## The Cosine-Type Generalized Padé Approximant

The constructed approximant takes the form:

$$
x(t) = \frac{\sum_{i=0}^{m} \alpha_i \cos(i\omega t)}{\sum_{j=0}^{n} \beta_j \cos(j\omega t)}
$$

where $\omega$ is the generalized Padé angular frequency (to be determined) and $\alpha_i$, $\beta_j$ are coefficients obtained through Padé matching conditions.

## Two Improvement Schemes

Directly applying this approximant to the classical Padé procedure fails — the unknown frequency $\omega$ renders the coefficient equations nonlinearly coupled. Two improvement schemes were developed to overcome this.

### Scheme I: Active Frequency Iteration

Rather than treating $\omega$ as yet another unknown, it is elevated to the role of an **active variable** with increment $\Delta\omega$, stepping iteratively from an initial guess $\omega_0$. At each step, $\alpha_i$ and $\beta_j$ are solved, and a target function $\Gamma = x(\pi/\omega) - x_1$ (where $x_1$ is the other intersection of the orbit with the $x$-axis) determines when to terminate. Iteration stops when $\vert\Gamma\vert < 10^{-(p+4)}$, where $p$ is the precision index. This scheme works well for polynomial restoring forces (Duffing oscillator).

### Scheme II: Derivative-Based Target + Piecewise Description

For oscillators with rational restoring forces (e.g., Duffing-harmonic, $\frac{x+x^3}{1+x^2}$), certain longer-period orbits require a more refined approach. Scheme II introduces two changes: (1) the target function is switched to the **derivative at half-period** — specifically, the velocity value at the negative $x$-axis intersection:

$$
\Gamma_2 = \left.\frac{dx}{dt}\right|_{t=\pi/\omega} - y_1
$$

where $y_1$ is the velocity of the orbit at the negative intersection; and (2) the solution is described piecewise, with segments matched at the half-period point. These refinements restore the accuracy to the level achieved by Scheme I for polynomial potentials.

## Results Across Three Oscillator Classes

![Duffing oscillator phase portrait](/assets/img/publication_preview/p9-fig1.png){: width="70%"}

*Figures 1–3: Duffing oscillator (polynomial potential), $A=2$. Phase portrait (left), time history (center), and absolute error (right). Error below $10^{-3}$.*

---

![Duffing-harmonic oscillator](/assets/img/publication_preview/p9-fig7.png){: width="70%"}

*Figures 7–9: Duffing-harmonic oscillator (rational potential), $A=3$. Scheme II handles the rational restoring force effectively, with the same error level.*

---

![SD oscillator](/assets/img/publication_preview/p9-fig13.png){: width="70%"}

*Figure 13: SD oscillator (irrational potential), $\alpha=1$, $A=2.5$. High accuracy maintained even with the geometric-constraint-induced irrational nonlinearity.*

---

![SD oscillator large-amplitude](/assets/img/publication_preview/p9-fig16.png){: width="70%"}

*Figure 16: Large-amplitude trajectory of the SD oscillator, $\alpha=0.5$, $A=3$, $\beta=2$. The method's accuracy is independent of both the magnitude of nonlinear coefficients and the initial amplitude.*

## Method Characteristics

- **Simplicity:** Inherits the straightforward workflow of Padé approximation — start from a power series solution, construct the approximant, match coefficients, solve a system of equations. Straightforward to program.
- **Nonlinearity-robust:** Error levels are consistent across weak nonlinearity (Duffing) and strong nonlinearity (SD oscillator with irrational terms).
- **Broad applicability:** Covers all three canonical restoring-force types: polynomial, rational, and irrational.
- **Period prediction:** The approximation yields $\omega$ directly, from which the analytic period $T = 2\pi/\omega$ is obtained.

## Relationship to Prior Work

This paper is the third installment in the authors' GPA series. The first two — the proposal of GPA itself (力学学报, 2013) and its extension to homoclinic/heteroclinic orbits (Chin. Phys. B, 2014) — dealt with non-periodic solutions (homoclinic/heteroclinic orbits, which are fundamentally functions with limits at infinity and thus amenable to rational-type approximation). The present paper extends GPA's range from "with limits" to "periodic," completing an important piece of the method's applicability in nonlinear vibration analysis.

## Reflections

The conceptual approach of this paper is worth noting: rather than modifying the approximation formula to fit the problem, the authors modified the **mathematical structure** of the approximant to match the problem's nature. If classical Padé cannot handle periodic solutions — construct an approximant that is itself periodic. This design philosophy holds lessons beyond the specific context.

In practical engineering, periodic orbit analysis appears far more frequently than homoclinic/heteroclinic problems — rotor dynamics, MEMS resonators, energy harvesters, vibration isolators, and more. The cosine GPA method provides these systems with an analytically-controlled, computationally-light approximation tool that yields continuous parameter-period-amplitude relationships — precisely what is needed for parametric design and sensitivity analysis.
