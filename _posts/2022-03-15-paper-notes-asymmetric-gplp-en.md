---
layout: post
title: "Paper Notes — Asymmetric GPLP: Extending the Integration-Free Perturbation Method to Asymmetric Potentials"
date: 2022-03-15 10:00:00+0800
description: New ω-parameterized and combined Sech-Tanh approximants extend GPLP to full quintic asymmetric potentials, reducing heteroclinic error by 70–80%
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **Paper:** Li, Z., & Tang, J. (2022). *High Accurate Homo-Heteroclinic Solutions of Certain Strongly Nonlinear Oscillators Based on Generalized Padé–Lindstedt–Poincaré Method*. Journal of Vibration Engineering & Technologies, 10(4), 1291–1308.
> **Links:** [Essential Summary PDF](/assets/pdf/essential-summary-p11.pdf) · [DOI](https://doi.org/10.1007/s42417-022-00446-7)

## TL;DR

The 2016 GPLP method opened the door to integration-free perturbation — but only for symmetric potentials. This paper introduces ω-parameterized and combined Sech-Tanh approximants, extending GPLP to the full five-term Φ⁶ asymmetric potential and rational restoring forces, improving heteroclinic accuracy from 5–8% to < 1.5%.

## What the 2016 Version Left on the Table

The 2016 GPLP (Nonlinear Dynamics, 2016) solved the fundamental integration bottleneck — but with three explicit limitations:

- **Symmetric potentials only** ($c_1x + c_3x^3 + c_5x^5$, no $x^2$ or $x^4$ terms). Many real Φ⁶ oscillators have all five terms.
- **Heteroclinic approximant was basic** (pure Tanh basis), with insufficient accuracy under asymmetry.
- **No rational restoring force** coverage (e.g., Duffing-harmonic: $g(x) = \frac{\lambda x + \delta x^3}{1 + \nu x^2}$).

The 2022 paper addresses all three.

## The Method: Three New Approximant Types

### 1. ω-Parameterized Homoclinic Approximant

The 2016 version hard-coded $\omega = 1$:

$$
x(t) = \frac{\sum \alpha_i \, \text{Sech}^i t}{1 + \sum \beta_i \, \text{Sech}^i t}
$$

The 2022 version frees the time scale:

$$
\boxed{x(t) = \frac{\sum_{i=0}^{L} \alpha_i \, \text{Sech}^i(\boldsymbol{\omega} t)}{1 + \sum_{i=1}^{M} \beta_i \, \text{Sech}^i(\boldsymbol{\omega} t)}}
$$

$\omega$ is now a free parameter, solved simultaneously with $\alpha_i$, $\beta_i$. This single change allows the approximant to adapt to different potential well shapes — reducing homoclinic error by 40–60% for asymmetric cases.

![Φ⁶-VDP phase portrait](/assets/img/publication_preview/p11-fig1.png){: width="70%"}

*Figure 1: Phase portraits of the full Φ⁶-Van der Pol oscillator at ε = 0. The $x^2$ and $x^4$ terms create an asymmetric potential where homoclinic and heteroclinic orbits have distinctly different geometries.*

### 2. Type A: Improved Tanh Heteroclinic Approximant

Same ω freedom applied to the heteroclinic form:

$$
\text{GPA}[L/M]x(t) = \frac{\sum_{i=0}^{L} \alpha_i \, \text{Tanh}^i(\omega t)}{1 + \sum_{i=1}^{M} \beta_i \, \text{Tanh}^i(\omega t)}
$$

Sufficient for pure heteroclinic problems.

### 3. Type B: Combined Sech-Tanh — The Game Changer

$$
\boxed{x(t) = \frac{\sum_{i=0}^{L_1} \alpha_i \, \text{Sech}^i(\omega t) + \sum_{j=0}^{L_2} \gamma_j \, \text{Tanh}^j(\omega t)}{1 + \sum_{i=1}^{M_1} \beta_i \, \text{Sech}^i(\omega t) + \sum_{j=1}^{M_2} \delta_j \, \text{Tanh}^j(\omega t)}}
$$

Why both Sech *and* Tanh? The geometric conflict in asymmetric potentials:

- The higher saddle's homoclinic orbit is **Sech-like**: symmetric approach from both sides to the same saddle.
- The heteroclinic orbit connecting unequal saddles is **Tanh-like**: asymmetric approach to two different saddles.
- When both coexist at the same saddle, a pure Tanh (Type A) cannot simultaneously capture the homoclinic orbit's symmetry — 5–8% error at $\varepsilon = 1$.
- Type B resolves this by leveraging **both basis functions simultaneously** — reducing error to < 1.5%.

This geometric intuition — matching the approximant's functional form to the orbit's asymptotic behavior — is the unifying theme across both GPLP papers.

![Φ⁶-VDP homoclinic](/assets/img/publication_preview/p11-fig4.png){: width="70%"}

*Figure 4: Homoclinic orbits of the Φ⁶-VDP oscillator (63) for various parameter sets at ε = 1. The ω-parameterized approximant maintains < 1% error despite asymmetry.*

![Φ⁶-VDP multi-parameter](/assets/img/publication_preview/p11-fig6.png){: width="70%"}

*Figure 6: Homoclinic orbits of oscillator (37) across 8 parameter sets at ε = 1. Systematic multi-parameter comparison validates the method's robustness.*

## Validation on Two Oscillator Classes

### Φ⁶-Van der Pol (Full Five-Term Asymmetric)

$$
\ddot{x} + c_1 x + c_2 x^2 + c_3 x^3 + c_4 x^4 + c_5 x^5 = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2)\dot{x}
$$

With $c_2, c_4 \neq 0$, the left and right wells differ in depth, the homoclinic orbits around each saddle have different curvatures, and heteroclinic orbits connect unequal saddles. GPLP with Type B handles all these complications, with errors < 1.5% across 24 parameter sets (Tables 4–8).

### Generalized Duffing-Harmonic-Van der Pol (Rational)

GPLP's first foray into rational restoring forces:

$$
\ddot{x} + \frac{\lambda x + \delta x^3}{1 + \nu x^2} = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2)\dot{x}
$$

Tested from $\varepsilon = 0.5$ to $\varepsilon = 2$ (well beyond "weak nonlinearity"). No modification to the GPLP procedure is needed — only the coefficients change. The method captures both homoclinic and heteroclinic orbits accurately, with heteroclinic orbits at $\varepsilon = 2$ still within 2% of Runge–Kutta.

![DH-VDP homo-heteroclinic](/assets/img/publication_preview/p11-fig2.png){: width="70%"}

*Figure 2: Homo-heteroclinic orbits of the DH-VDP oscillator. (a) ε = 0.8, (b) ε = 1. Dashed: GPLP Type B. Solid: Runge–Kutta.*

![DH-VDP heteroclinic](/assets/img/publication_preview/p11-fig8.png){: width="70%"}

*Figure 8: Heteroclinic orbits of the DH-VDP oscillator at various parameter sets. The systematic study validates GPLP's broad applicability to rational restoring force configurations.*

## Accuracy: 2022 vs. 2016

| Scenario | 2016 Error | 2022 Error | Improvement |
|----------|:---:|:---:|:---:|
| Symmetric + small ε | ~1% | ~1% | Similar |
| Asymmetric homoclinic, ε = 1 | ~2.5% | < 1% | 40–60% |
| Asymmetric heteroclinic, ε = 1 | 5–8% | < 1.5% | 70–80% |
| Rational restoring force | N/A | < 2% | — |

## Why This Paper Matters

This is "refinement on a solid framework" done right. The 2016 paper proved the concept — integration-free perturbation works. The 2022 paper doesn't try to reinvent the wheel; it makes three concrete, well-motivated improvements: more flexible approximants (ω parameterization), better heteroclinic accuracy (Type A/B), and broader scope (rational restoring forces). Each seems small in isolation; together they constitute a substantial methodological upgrade.

An often-overlooked contribution: the paper systematically reports 24 parameter-set comparisons against Runge–Kutta (Tables 4–8). This "engineering validation" approach is rare in methods papers, but it's exactly what gives readers confidence to apply the method to their own systems.

For practitioners: if your oscillator involves **asymmetric potentials** (biased MEMS beams, asymmetric energy absorbers, tilted-spring systems), the 2022 GPLP with Type B approximant is the appropriate choice. If your system is symmetric and weakly nonlinear, the 2016 version suffices.
