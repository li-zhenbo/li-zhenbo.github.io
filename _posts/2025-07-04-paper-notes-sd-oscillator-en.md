---
layout: post
title: Paper Notes — Global Evolution of Limit Cycles and Homoclinic Bifurcation in SD Oscillator with Quartic Nonlinear Damping
date: 2025-07-04 10:00:00+0000
description: Padé-enhanced MGHFP method for global limit cycle evolution and homoclinic bifurcation in SD oscillators with quartic damping — first multi-parameter analysis
tags: [paper-notes]
categories: [notes]
featured: false
toc:
  sidebar: left
---

> **Paper:** Li, Z., Hou, L., & Peng, R. (2025). *Global Evolution of Limit Cycles and Homoclinic Bifurcation of Smooth and Discontinuous Oscillator with Quartic Nonlinear Damping*. International Journal of Non-Linear Mechanics, 178, 105185.
> **Links:** [Essential Summary PDF](/assets/pdf/essential-summary-p2.pdf) · [DOI](https://doi.org/10.1016/j.ijnonlinmec.2025.105185)

## TL;DR

Introducing Padé approximation into the MGHFP framework simplifies previously complicated analytical expressions into rational functions — lowering the barrier to practical use and, critically, enabling **multi-parameter** analysis for the first time. This represents a major methodological upgrade for the MGHFP series.

## Motivation

The SD oscillator (Smooth and Discontinuous Oscillator) is a prototypical irrational nonlinear oscillator, but research on its **nonlinearly damped** variant is scarce. Prior work has focused on the SD–van der Pol oscillator (quadratic damping only); the case of **quartic nonlinear damping** ($\mu_4 x^4\dot{x}$), which arises naturally in MEMS micro-beam resonators and high-damping vibration isolators, has remained unaddressed.

Moreover, the authors' previously developed MGHFP method, while effective, produced expressions that were prohibitively complicated — the coefficient functions involved nested Simpson integrals, requiring system parameters to be assigned upfront and degenerating the results to semi-analytic, single-parameter analysis. Padé approximation was introduced precisely to break this bottleneck.

## System Model

The SD oscillator with quartic nonlinear damping:

$$
\ddot{x} + \omega_0^2 x\left(1 - \frac{1}{\sqrt{x^2+\alpha^2}}\right) = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2 + \mu_3 x^3 + \mu_4 x^4)\dot{x}
$$

where $\alpha$ is the smoothing parameter ($\alpha\to 0$ recovers the non-smooth limit), $\omega_0$ is the natural frequency, $\varepsilon$ is a small perturbation parameter, and $\mu_c$ serves as the control parameter.

![Potential portrait](/assets/img/publication_preview/p2-fig2-potential.png){: width="70%"}

*Figure 2: Double-well potential portrait of the SD oscillator. As $\alpha$ decreases from 1 to 0, the system transitions from single-well to double-well dynamics, forming a homoclinic orbit that plays a central role in the bifurcation analysis.*

## Methodological Innovation: MGHFP + Padé Approximation

### The MGHFP Pipeline

1. **Nonlinear time transformation** $d\varphi/dt = \Phi(\varphi)$, assuming a solution of the form $x = a\cos^2\Phi + b$
2. **Perturbation expansion** $a = a_0 + \varepsilon a_1 + \cdots$
3. **Composite Simpson integration** to discretize the integrals of irrational nonlinear terms that cannot be handled analytically

### Padé Approximation — The Key Upgrade

The coefficient functions $f_{2i}(\alpha, A)$ output by MGHFP are formally complex, with nested integrals that hinder direct analysis. This paper introduces Padé approximation to fit these functions as **rational functions**:

$$
f(\alpha, A) \approx \frac{P_n(\alpha, A)}{Q_m(\alpha, A)}
$$

In contrast to the least-squares polynomial approach previously attempted by the authors (which required parameter pre-assignment, degenerating results to semi-analytic form), Padé yields **fully analytical** expressions that support simultaneous multi-parameter discussion.

## Key Equations

### Amplitude–Parameter Relationship

$$
\boxed{\mu_c = -\frac{4}{a_0^2(2p_0 - p_4)}\Big(\tilde{E}_1\mu_1 + \tilde{E}_2\mu_2 + \tilde{E}_3\mu_3 + \tilde{E}_4\mu_4\Big)}
$$

where $\tilde{E}_i$ are now **Padé-approximated rational functions** of $\alpha$ and $A$ — substantially simpler than the raw MGHFP expressions and fully amenable to multi-parameter analysis. The Fourier coefficients $p_{2i}$ are still computed via the composite Simpson formula.

![Amplitude–parameter curves](/assets/img/publication_preview/p2-fig3-amplitude.png){: width="70%"}

*Figure 3: (Upper) $\mu_c$–$A$ curves. (Lower) $H_0$–$A$ curves. (Bottom row) Phase portraits at different $\mu_c$ values. Solid/dotted lines: MGHFP. Dots: Runge–Kutta. The complete limit cycle lifecycle — emergence, bifurcation, and convergence — is quantitatively visualized.*

### Stability Criterion

$$
\boxed{H_0 = \frac{1}{\pi}\int_0^\pi \left[\mu_c + \sum_{i=1}^{4}\mu_i(a_0\cos^2\varphi + b)^i\right]d\varphi}
$$

$H_0 > 0$: unstable; $H_0 = 0$: semi-stable; $H_0 < 0$: stable.

### Homoclinic Bifurcation Threshold

Setting $b = h$ (saddle point ordinate) in the amplitude–parameter relation yields the critical $\mu_c^{\mathrm{hom}}$ — the parameter value at which the limit cycle collides with the saddle point and is annihilated.

## Key Results

### Example 1: Single-Well ($\alpha = 2$)

With $\mu_1=-1, \mu_2=1.5, \mu_3=1, \mu_4=-1$, Figure 3 reveals the complete limit cycle lifecycle:

- Below critical $\mu_c$: **no limit cycle exists**
- At critical point: a **semi-stable** limit cycle emerges
- Further increase of $\mu_c$: splits into one **stable** ($H_0 < 0$) and one **unstable** ($H_0 > 0$) limit cycle
- The unstable cycle eventually **collapses** to the equilibrium point; the stable cycle persists and grows

### Example 2: Different Parameter Set ($\alpha = 0.65$)

With $\mu_1=-0.5, \mu_2=1, \mu_3=1, \mu_4=-0.1$, analytical and numerical results are in good agreement.

![Another parameter set](/assets/img/publication_preview/p2-fig8-amplitude2.png){: width="70%"}

*Figure 8: $\mu_c$–$A$ and $H_0$–$A$ curves for a different parameter set. The method accurately captures limit cycle evolution and stability transitions across parameter space.*

### Analytical Solution Verification

![Analytical vs. numerical](/assets/img/publication_preview/p2-fig7-solutions.png){: width="70%"}

*Figure 7: Analytical limit cycle solutions at different $\mu_c$ compared with Runge–Kutta numerical integration, validating the accuracy and reliability of the MGHFP+Padé approach.*

## Five Key Findings

1. **Padé-enhanced MGHFP:** Introducing Padé approximation yields concise, fully analytical amplitude–parameter relationships. Unlike prior semi-analytic results, the present version supports **multi-parameter** analysis.

2. **Complete lifecycle prediction:** The method quantitatively answers: when does a limit cycle emerge? How does it bifurcate? Where does it converge? Is it stable? — including precise prediction of **unstable limit cycles**, notoriously difficult for numerical methods.

3. **Analytical homoclinic bifurcation threshold:** The critical parameter at which the limit cycle collides with the saddle point is obtained analytically.

4. **Multi-parameter classification (Theorems 2 & 3):** The simplified expressions enable deriving **parametric regions** where the oscillator has exactly two limit cycles — a generalization unattainable with prior MGHFP results.

5. **Engineering relevance:** The framework supports both **amplitude regulation** (energy harvesting, predator–prey models) and **oscillation suppression** (vibration isolation, vehicle suspension, aeroelastic flutter). Through bifurcation parameter tuning, limit cycles can be created, modulated, or annihilated.

## Limitations

- Large perturbation ($\varepsilon > 0.5$): accuracy degrades; higher-order expansions can mitigate this
- Limit cycles crossing saddle points: the drop in velocity demands higher Fourier truncation orders
- Non-smooth potential wells ($\alpha = 0$): non-smoothness affects accuracy

## Position in the MGHFP Series

This paper occupies a pivotal position in the MGHFP series — through Padé approximation, it elevates the method from semi-analytic to fully analytic and from single-parameter to multi-parameter. This upgrade directly enabled the subsequent Physica Scripta 2026 work (MGHFP applied to coupled SD oscillators with two irrational nonlinear terms), which is the most complex application in the series to date.

For researchers in nonlinear perturbation methods, the methodological contribution — the Padé + perturbation expansion strategy for systems with irrational nonlinearities — may hold broader value than the specific results.
