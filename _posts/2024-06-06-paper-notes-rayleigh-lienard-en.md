---
layout: post
title: "Paper Notes — The MGHFP Method: First Public Introduction via a Mixed Rayleigh–Liénard Oscillator"
date: 2024-06-06 10:00:00+0800
description: First publication of the MGHFP method — composite Simpson integration enables purely symbolic global dynamic analysis of a mixed Rayleigh–Liénard oscillator with cubic and quintic nonlinearities
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **Paper:** Li, Z., Hou, L., Zhang, Y., & Xu, F. (2024). *A Modified Perturbation Method for Global Dynamic Analysis of Generalized Mixed Rayleigh–Liénard Oscillator with Cubic and Quintic Nonlinearities*. Physica Scripta, 99(7), 075213.
> **Links:** [Essential Summary PDF](/assets/pdf/essential-summary-p4.pdf) · [DOI](https://doi.org/10.1088/1402-4896/ad5066)

## TL;DR

This is the **first-ever publication** of the MGHFP methodology — embedding the composite Simpson quadrature formula into the classical GHFP framework to enable purely symbolic execution for complicated nonlinear oscillators. All subsequent MGHFP work (IJNLM 2024, IJNLM 2025, Phys. Scr. 2026) traces its origin to this paper.

## Motivation

Deriving the analytical relationship between limit cycle amplitude and system parameters is a central task in quantitative nonlinear dynamics. However, when the restoring force or nonlinear damping is complicated (e.g., mixing Rayleigh-type and Liénard-type terms), many existing analytical methods **cannot execute their procedures symbolically** — parameters must be pre-assigned, yielding only semi-analytic snapshots rather than continuous global pictures.

This paper proposes a **modified generalized harmonic function perturbation method** by introducing the composite Simpson quadrature formula. A mixed Rayleigh–Liénard oscillator with cubic and quintic nonlinearities is chosen as the test case — its damping combines Rayleigh ($\dot{x}^2$) and Liénard ($x^2$, $x^4$) terms, making it an ideal platform to demonstrate the method's capabilities.

## System Model

The generalized mixed Rayleigh–Liénard oscillator:

$$
\ddot{x} + c_1 x + c_3 x^3 + c_5 x^5 = \varepsilon(\mu + \mu_1 x + \mu_2 x^2 + \mu_3 x^3 + \mu_4 x^4 + \mu_{22} \dot{x}^2)\dot{x}
$$

where $c_1$, $c_3$, $c_5$ are stiffness parameters (restoring force includes cubic and quintic terms), $\mu$ is the control parameter, $\mu_1\sim\mu_4$ are Liénard-type damping coefficients, and $\mu_{22}$ is the Rayleigh-type damping coefficient.

![Potential portrait](/assets/img/publication_preview/p4-fig1.png){: width="70%"}

*Figure 1: Potential portrait under single-well conditions. The restoring force defines the qualitative structure within which limit cycles evolve.*

## Methodological Innovation: The Birth of MGHFP

### The Classical GHFP Bottleneck

The classical GHFP method: (1) nonlinear time transformation → (2) Fourier expansion of the solution → (3) perturbation expansion → (4) computation of Fourier coefficients. Step (4) is the bottleneck — for complicated oscillators, integrals involving nonlinear terms **cannot be evaluated analytically**.

### The MGHFP Breakthrough

The composite Simpson quadrature formula is introduced into Step (4):

$$
\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f(x_0) + 4\sum_{i\ \mathrm{odd}} f(x_i) + 2\sum_{i\ \mathrm{even}} f(x_i) + f(x_n)\right]
$$

With eight equal subintervals, the Fourier coefficients $p_{2i}$ become **explicit algebraic functions** of system parameters. The entire perturbation procedure now runs purely symbolically.

## Key Equations

### Amplitude–Parameter Relation

$$
\boxed{\mu = \frac{4}{\pi a_0^2(2p_0 - p_4)}\Big(E_1\mu_1 + E_2\mu_2 + E_3\mu_3 + E_4\mu_4 + E_{22}\mu_{22}\Big)}
$$

where $p_{2i}$ are computed via composite Simpson integration. Given parameters, the limit cycle amplitude is obtained analytically.

### Stability Criterion

$$
\boxed{h_0 = \frac{1}{\pi}\int_0^\pi \Phi_0\Big(\mu + \sum_{i=1}^{4}\mu_i(a_0\cos^2\varphi + b)^i + 3\mu_{22}(-2a_0\Phi_0\cos\varphi\sin\varphi)^2\Big)d\varphi}
$$

where $h_0 = H_0/arepsilon$. $h_0 > 0$: unstable; $h_0 = 0$: semi-stable; $h_0 < 0$: stable.

## Key Results

### Example 1: Single-Well Potential (Section 4.1)

![Phase portraits](/assets/img/publication_preview/p4-fig3.png){: width="70%"}

*Figure 3: Phase portraits of the single-well oscillator with different $\mu$ and $A$ ($\varepsilon = 0.01$). Colorized dots mark initial points.*

![Mu-A curves comparison](/assets/img/publication_preview/p4-fig4.png){: width="70%"}

*Figure 4: Comparison of $\mu$–$A$ curves ($\varepsilon = 0.01$). Solid: present method. Dotted: Runge–Kutta.*

- Below critical $\mu$: **no limit cycle** exists
- At critical point: **semi-stable** limit cycle emerges
- Further increase of $\mu$: splits into stable + unstable
- Unstable cycle eventually collapses; stable cycle persists
- Up to **three coexisting limit cycles** under certain parameters

### Example 2: Triple-Well Potential (Section 4.2)

![Triple-well potential](/assets/img/publication_preview/p4-fig6.png){: width="70%"}

*Figure 6: Triple-well potential portrait. Multiple wells create a rich bifurcation structure.*

![Triple-well mu-A curves](/assets/img/publication_preview/p4-fig7.png){: width="70%"}

*Figure 7: $\mu$–$A$ and $h_0$–$A$ curves for the triple-well oscillator.*

![Mu-A curves comparison](/assets/img/publication_preview/p4-fig9.png){: width="70%"}

*Figure 9: $\mu$–$A$ curves for limit cycles between saddle points ($\varepsilon = 0.1$). The method accurately predicts bifurcation thresholds.*

## Five Key Findings

1. **First MGHFP publication:** This is the first paper to introduce composite Simpson integration into the GHFP framework — the origin of the entire MGHFP series.

2. **Complete lifecycle prediction:** The analytical $\mu$–$A$ relationship reveals the full lifecycle: generation, evolution, and termination.

3. **Up to three coexisting limit cycles:** Parameter regions with three simultaneous limit cycles are identified — a complex scenario that purely numerical methods struggle to fully capture.

4. **Homoclinic/heteroclinic bifurcation prediction:** Both global bifurcation types are quantitatively analyzed, with practical implications for chaos control.

5. **Dual applications:** The framework supports both limit cycle regulation (inertial impact shaker, population dynamics) and chaos prediction via bifurcation thresholds (encryption, equipment protection).

## Position in the MGHFP Series

This paper occupies the **origin position** in the MGHFP series. The composite Simpson integration idea was first published here, then applied to the more complex DHRL oscillator (IJNLM 2024), enhanced with Padé approximation for multi-parameter analysis (IJNLM 2025), and finally extended to coupled SD oscillators with two irrational terms (Phys. Scr. 2026). For researchers in nonlinear perturbation methods, the Simpson discretization + perturbation expansion strategy has foundational reference value.
