---
layout: post
title: "Review: The Evolution of the MGHFP Method — From Proposal to Completion Across Four Papers"
date: 2026-07-28 10:00:00+0800
description: Tracing the development of the MGHFP method from its first proposal through multi-parameter extension to irrational nonlinearity and coupled multi-well systems
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

## TL;DR

This article traces the complete development trajectory of the MGHFP (Modified Generalized Harmonic Function Perturbation) method across four papers published from 2024 to 2026. The core problem remains consistent: how to **purely symbolically** derive the analytical relationship between limit cycle amplitude and system parameters for complicated nonlinear oscillators. The solution evolved through four stages: first symbolic implementation → simplified multi-parameter extension → generalization to irrational nonlinearity → conquering dual-irrational coupled multi-well systems.

## Method Overview

The unified core framework of the MGHFP method consists of four steps:

1. **Nonlinear time transformation**: $d\varphi/dt = \Phi(\varphi)$ converts the time-domain equation into an angular-domain one
2. **Fourier expansion of the solution**: assuming $x = a\cos^2\varphi + b$, expand $\Phi(\varphi) = \sum (p_{2i}\cos 2i\varphi + q_{2i}\sin 2i\varphi)$
3. **Perturbation expansion**: $a = a_0 + \varepsilon a_1 + \cdots$, treating damping as a small perturbation order by order
4. **Composite Simpson integration**: $\int_a^b f(x)dx \approx \frac{h}{3}[f(x_0) + 4\sum f_{odd} + 2\sum f_{even} + f(x_n)]$, discretizing analytically intractable integrals into explicit algebraic expressions

The application of this framework produces two core formulas: the **amplitude–parameter relation** $\mu(A)$ and the **stability criterion** $h_0(A)$. From these two formulas, all quantitative questions about the complete lifecycle of limit cycles can be answered.

## Global Comparison of Four Papers

| Paper (Year) | Journal | Core System | Damping Complexity | Well Structure | Methodological Innovation |
|---|---|---|---|---|---|
| P1: Phys. Scr. (2024.06) | Physica Scripta 99, 075213 | Mixed Rayleigh–Liénard $(c_1x + c_3x^3 + c_5x^5)$ | 6-term (mixed Rayleigh + Liénard) | Single / Triple | **First MGHFP proposal**: first introduction of composite Simpson integration for purely symbolic GHFP execution |
| P2: IJNLM (2024.07) | Int. J. Non-Linear Mech. 166, 104832 | Generalized DHRL $\frac{\lambda x + \mu x^3}{1+\nu x^2}$ | 6-term (Rayleigh + Liénard) | Single / Double | **First rational restoring force application**: extending MGHFP to rational nonlinearity |
| P3: IJNLM (2025) | Int. J. Non-Linear Mech. 178, 105185 | SD oscillator $\omega_0^2 x(1-1/\sqrt{x^2+\alpha^2})$ | 5-term (quartic damping) | Single / Double | **Padé enhancement**: introducing Padé approximation to simplify expressions and enable multi-parameter analysis |
| P4: Phys. Scr. (2026) | Physica Scripta 101, 125205 | Coupled SD oscillator (dual irrational) | 5-term (quartic damping) | Single / Triple | **Dual-irrational + multi-well coupling**: conquering systems with two simultaneous irrational nonlinear terms |

## Four-Stage Development Path

### Stage 1: Method Proposal (P1, 2024.06)

**Core problem**: The classical GHFP breaks down when facing complicated damping and restoring forces — the integrals involved in Fourier coefficient computation cannot be evaluated analytically, forcing parameter pre-assignment and degenerating results to semi-analytic form.

**Solution**: Introduce the **composite Simpson quadrature formula** ($n=18$ subintervals, $M=4$ harmonic terms) at the Fourier coefficient computation stage, discretizing all analytically intractable integrals into explicit algebraic functions of system parameters. The **mixed Rayleigh–Liénard oscillator with cubic and quintic nonlinearities** served as the first application case:

$$
\ddot{x} + c_1 x + c_3 x^3 + c_5 x^5 = \varepsilon(\mu + \mu_1 x + \mu_2 x^2 + \mu_3 x^3 + \mu_4 x^4 + \mu_{22} \dot{x}^2)\dot{x}
$$

**Milestones**: First purely symbolic derivation of the amplitude–parameter relation $\mu(A)$ (Eq. 35) and stability criterion $h_0(A)$ (Eq. 50). Achieved complete quantitative analysis of up to **three coexisting limit cycles** under single-well conditions, and prediction of homoclinic and heteroclinic bifurcations under triple-well conditions.

### Stage 2: Generalization to Rational Nonlinearity (P2, 2024.07)

**Core problem**: P1's restoring force $g(x) = c_1x + c_3x^3 + c_5x^5$ is purely polynomial — can MGHFP handle restoring forces with denominators containing $x^2$, i.e., rational forms?

**Challenge escalation**: The generalized Duffing–Harmonic–Rayleigh–Liénard oscillator's restoring force is $\frac{\lambda x + \mu x^3}{1 + \nu x^2}$ — a rational function with polynomial numerator and denominator. Compared to P1's pure polynomial, rational nonlinearity significantly increases the complexity of Fourier coefficient computation. Damping was also upgraded to 6 terms (adding $\mu_{24} \dot{x}^4$).

$$
\ddot{x} + \frac{\lambda x + \mu x^3}{1 + \nu x^2} = \varepsilon(\mu_c + \mu_2 x^2 + \mu_4 x^4 + \mu_6 x^6 + \mu_{22} \dot{x}^2 + \mu_{24} \dot{x}^4)\dot{x}
$$

**Milestones**: MGHFP successfully applied to rational nonlinear oscillators, with both the amplitude–parameter relation and the stability criterion maintaining their generalized forms. The analytical approach identified **four regions** in the $\mu_c$–$A$ curve (I: no cycle → II: stable + unstable coexistence → III: stable + unstable → IV: single stable), along with two semi-stable bifurcation point locations.

### Stage 3: Methodological Upgrade — Padé Approximation (P3, 2025)

**Core problem**: While the MGHFP outputs from P1 and P2 are symbolic, they remain excessively complex — coefficient functions involve nested Simpson integrals, raising the barrier to practical use and limiting discussion to single-parameter analysis.

**Solution**: Introduce **Padé approximation** to fit the complex raw expressions into rational function form:

$$
f(\alpha, A) \approx \frac{P_n(\alpha, A)}{Q_m(\alpha, A)}
$$

**Milestones**: Padé approximation brought three breakthrough improvements:

1. **Drastic expression simplification**: nested Simpson integrals replaced by rational functions usable directly by practitioners
2. **First multi-parameter analysis**: the dependence of $\mu_c$ on $\mu_1, \mu_2, \mu_3, \mu_4$ and $\alpha$ can be discussed simultaneously
3. **Multi-parameter classification theorems**: parametric regions where exactly two limit cycles exist were analytically characterized (Theorems 2 & 3)

The system studied at this stage was the SD oscillator — restoring force containing the irrational square-root term $\sqrt{x^2+\alpha^2}$, with quartic nonlinear damping:

$$
\ddot{x} + \omega_0^2 x\left(1 - \frac{1}{\sqrt{x^2+\alpha^2}}\right) = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2 + \mu_3 x^3 + \mu_4 x^4)\dot{x}
$$

This marked MGHFP's first application to **irrational nonlinearity**, laying the groundwork for the coupled system in Stage 4.

### Stage 4: Conquering the Most Complex System — Coupled SD Oscillator (P4, 2026)

**Core problem**: All three previous stages dealt with systems containing only **one** irrational nonlinear term. What if **two** irrational terms are present (arising from two coupled SD oscillators)?

**System complexity**: The coupled SD oscillator's restoring forces are $(x+\beta)/\sqrt{(x+\beta)^2+\alpha^2}$ and $(x-\beta)/\sqrt{(x-\beta)^2+\alpha^2}$. Fourier coefficient computation must simultaneously handle high-dimensional integrals from two independent irrational terms, with exponentially increased complexity.

Furthermore, the well structure expands from single/double-well to **triple-well** — meaning that within the same system, small limit cycles enclosed by homoclinic orbits, large limit cycles enclosing the entire system, and both homoclinic and heteroclinic orbits (connecting different saddle points) can coexist, posing unprecedented demands on the method's bifurcation prediction capability.

**Milestones**: MGHFP successfully applied to dual-irrational-nonlinearity coupled systems, demonstrating sufficient generality and extensibility. This stage marks MGHFP's ability to cover the complete spectrum from simple polynomial restoring forces to complex irrational nonlinear coupled systems.

## Core Framework Summary

```
            ┌─────────────────────────────────────┐
            │      GHFP Framework                  │
            │  (Nonlinear time transformation)     │
            │   + Fourier solution expansion       │
            │   + Perturbation expansion           │
            └──────────────┬──────────────────────┘
                           │
              ┌────────────▼──────────────┐
              │  Composite Simpson         │  ← P1 (2024): First introduced
              │  Integration (n=18, M=4)   │     Enables pure symbolics
              └────────────┬──────────────┘
                           │
              ┌────────────▼──────────────┐
              │  Derive μ(A) relation      │
              │  Derive h₀(A) criterion    │
              └────────────┬──────────────┘
                           │
         ┌─────────────────┼──────────────────┐
         │                 │                  │
    ┌────▼────┐    ┌───────▼──────┐    ┌─────▼──────┐
    │ P1 Out   │    │ P2 Out       │    │P3+P4 Out   │
    │Poly rest │    │Rational rest │    │Irrational  │
    │Mixed damp│    │General damp  │    │Multi-well  │
    └─────────┘    └──────────────┘    └────────────┘
                           │
              ┌────────────▼──────────────┐
              │  Padé Approximation       │
              │  (P3, 2025)               │
              │  Simplification +         │
              │  Multi-parameter ability  │
              └────────────┬──────────────┘
                           │
              ┌────────────▼──────────────┐
              │  Dual-irrational Coupled  │
              │  Multi-well (P4, 2026)    │
              │  Most complex application │
              └──────────────────────────┘
```

## System Complexity Evolution

```
Restoring force:   Polynomial ──→ Rational ──→ Irrational ──→ Dual-Irr Coupled
                   (P1)         (P2)         (P3)           (P4)

Damping order:     5-term       6-term       5-term         5-term
                   (+μ₂₂)       (+μ₂₄)       (quartic)      (quartic)

Well structure:    Single/Triple  Single/Double  Single/Double  Single/Triple

Method:            First symbolic   Rational ext    Padé-enhanced   Full-system ext

Key capability:    Symbolic execution  Rational NL    Multi-param     Dual-irrational
                   Homo-hetero pred   4-region ID     2-cycle theorem  Multi-well coupling
```

## Logical Relationships Among the Four Papers

These four papers form a clear methodological evolution chain:

- **P1 → P2**: From polynomial to rational — validating the method's extensibility in restoring force forms
- **P2 → P3**: "Subtraction" after producing results — introducing Padé approximation to simplify while enabling multi-parameter analysis
- **P2 + P3 → P4**: After being validated on rational nonlinearity and simplified by Padé, simultaneously conquering "doubled irrational terms" + "triple-well structure"

Notably, P1 and P2 were published only about one month apart — P2's work started earlier but took longer due to the more complex DHRL oscillator, allowing P1 to be published first. The transition from P3 (SD oscillator + Padé) to P4 (coupled SD oscillator) represents a substantial leap in the spiral of progress, requiring method validation preparation from single to dual irrational terms.

## Core Contributions

From the perspective of nonlinear perturbation methodology, the MGHFP series' contributions can be summarized at three levels:

1. **Methodological**: Solved the long-standing challenge of symbolic execution on complicated oscillators. Composite Simpson integration is the key; Padé approximation is the lubricant after unlocking.

2. **Theoretical analysis**: Advanced global limit cycle analysis from qualitative description to quantitative prediction. Previously, this capability barely existed for complicated oscillators — analysis could only answer "how many" and "are they stable," not "when do they emerge, what amplitudes do they have, when do they vanish."

3. **Engineering applications**: Provided directly computable analytical tools for limit cycle amplitude regulation and chaos threshold prediction, with direct applicability to MEMS, quasi-zero stiffness vibration isolation, and energy harvesting.

## Outlook

The MGHFP series' development trajectory suggests three promising directions: (1) extension to multi-degree-of-freedom coupled systems (e.g., Coupled van der Pol–Duffing oscillators); (2) introduction of higher-order perturbation expansions for improved accuracy under large perturbation parameters; (3) integration with machine learning to accelerate Fourier coefficient computation or automate Padé coefficient generation. These directions will further expand the application boundaries of MGHFP.

*This review is based on the following four papers:*
1. Li et al. (2024) Phys. Scr. 99, 075213 — MGHFP first proposal
2. Li et al. (2024) IJNLM 166, 104832 — Rational nonlinearity extension
3. Li et al. (2025) IJNLM 178, 105185 — Padé enhancement & multi-parameter analysis
4. Li et al. (2026) Phys. Scr. 101, 125205 — Dual-irrational coupled multi-well system
