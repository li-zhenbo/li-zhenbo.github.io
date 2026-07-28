---
layout: post
title: "Paper Notes — The MGHFP Method: A Symbolic Upgrade to the Generalized Harmonic Function Perturbation Framework"
date: 2024-07-14 10:00:00+0800
description: Introducing composite Simpson integration into the GHFP framework for purely symbolic global dynamic analysis — the foundational paper of the MGHFP series
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **Paper:** Li, Z., Cai, J., & Hou, L. (2024). *A Modified Generalized Harmonic Function Perturbation Method and Its Application in Analyzing Generalized Duffing–Harmonic–Rayleigh–Liénard Oscillator*. International Journal of Non-Linear Mechanics, 166, 104832.
> **Links:** [Essential Summary PDF](/assets/pdf/essential-summary-p3.pdf) · [DOI](https://doi.org/10.1016/j.ijnonlinmec.2024.104832)

## TL;DR

The MGHFP method was first published in Physica Scripta (June 2024). This IJNLM paper is the first application of MGHFP to an oscillator with rational restoring force — a more complex test case that validates the method's versatility. It directly follows the original Physica Scripta 2024 publication and precedes the Padé-enhanced version (IJNLM 2025) and the coupled SD oscillator application (Phys. Scr. 2026).

## Motivation

Classical quantitative methods (perturbation-based, energy balance, homotopy-based) can analyze nonlinear oscillators — but only when the restoring force and damping are simple. Once the oscillator becomes complicated (e.g., mixing polynomial and rational nonlinearities), these methods **cannot execute their procedures symbolically**: all system parameters must be assigned numerical values upfront, yielding only isolated solution snapshots in parameter space, never a continuous analytical picture of how solutions evolve.

This work aims to **propose a modified perturbation method** that operates purely symbolically even for complicated oscillators, enabling the analytical derivation of amplitude–parameter relationships — the key to quantitative global dynamic analysis.

## System Model

The generalized Duffing–Harmonic–Rayleigh–Liénard (DHRL) oscillator:

$$
\ddot{x} + \frac{\lambda x + \mu x^3}{1 + \nu x^2} = \varepsilon(\mu_c + \mu_2 x^2 + \mu_4 x^4 + \mu_6 x^6 + \mu_{22} \dot{x}^2 + \mu_{24} \dot{x}^4)\dot{x}
$$

where $\lambda$, $\mu$, $\nu$ are stiffness parameters, and the right side features a **6-term generalized nonlinear damping** combining Rayleigh terms ($\dot{x}^2$, $\dot{x}^4$) and Liénard terms ($x^2$, $x^4$, $x^6$). The rational restoring force $\frac{\lambda x + \mu x^3}{1+\nu x^2}$ makes this oscillator a maximally challenging test case.

![Potential portrait](/assets/img/publication_preview/p3-fig-p13.png){: width="70%"}

*Figure 6: Potential portrait of the DHRL oscillator. The rich landscape enables homoclinic and heteroclinic bifurcations — an ideal platform to validate the MGHFP method.*

## Methodological Innovation: The Birth of MGHFP

### The Classical GHFP Bottleneck

The classical GHFP method proceeds via: (1) nonlinear time transformation, (2) Fourier expansion of the solution, (3) perturbation expansion, and (4) evaluation of integrals to obtain Fourier coefficients. Step (4) is the critical bottleneck — for complicated oscillators, the integrals involving irrational nonlinear terms **cannot be evaluated analytically**. Parameters must be assigned first, and the results degenerate to semi-analytic form.

### The MGHFP Breakthrough

The MGHFP method introduces the **composite Simpson quadrature formula** into Step (4):

$$
\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f(x_0) + 4\sum_{i\ \mathrm{odd}} f(x_i) + 2\sum_{i\ \mathrm{even}} f(x_i) + f(x_n)\right]
$$

By dividing the integration interval into eight equal subintervals, the Fourier coefficients $p_{2i}$ become **explicit algebraic functions** of $a_0$, $b$, and system parameters. The entire perturbation procedure now runs purely symbolically — no parameter pre-assignment required.

### Nonlinear Time Transformation

The solution is assumed as $x(t) = a\cos^2\varphi(t) + b$, with the nonlinear time transformation $d\varphi/dt = \Phi(\varphi)$:

$$
\Phi_0(\varphi) = \frac{\sqrt{2[V(a_0+b) - V(a_0\cos^2\varphi + b)]}}{x'_0(\varphi)}
$$

where $V(x) = \int g(x)dx$ is the potential energy. For complicated $g(x)$, this expression is analytically intractable — precisely why the Simpson discretization is needed. After discretization, $\Phi_0$ is expanded as a Fourier series with $M=4$.

## Key Equations

### Amplitude–Parameter Relation (Central Result)

The analytical relationship between limit cycle amplitude $A$ and control parameter $\mu_c$:

$$
\boxed{\mu_c = -\frac{4}{a_0^2(2p_0 - p_4)}\Big(E_2\mu_2 + E_4\mu_4 + E_6\mu_6 + E_{22}\mu_{22} + E_{24}\mu_{24}\Big)}
$$

where $p_{2i}$ are computed via the composite Simpson formula, and $E_i$ are functions of $a_0$, $b$, and $p_{2i}$. Given system parameters, the limit cycle amplitude is obtained **analytically** — no numerical integration needed.

### Stability Criterion

$$
\boxed{h_0 = \frac{1}{\pi}\int_0^\pi \Big[\mu_c + \sum\mu_i(a_0\cos^2\varphi + b)^i + \sum\mu_{ij}(a_0\cos^2\varphi + b)^i(\dot{x}_0)^2\Big]d\varphi}
$$

$h_0 > 0$: unstable; $h_0 = 0$: semi-stable (bifurcation point); $h_0 < 0$: stable.

## Key Results

### Example 1: Limit Cycle Evolution (Section 4.2)

Parameters: $\lambda=2$, $\mu=1$, $\nu=5$, $\mu_2=-0.88$, $\mu_4=0.39$, $\mu_6=-0.1$, $\mu_{22}=0.17$, $\mu_{24}=0.18$.

![Parametric plane evolution](/assets/img/publication_preview/p3-fig2.png){: width="70%"}

*Figure 2: Evolution of limit cycles in the parametric ($\mu_c$–$A$) plane. Four regions (I–IV) are clearly identified.*

![Phase plane](/assets/img/publication_preview/p3-fig3.png){: width="70%"}

*Figure 3: Phase portraits corresponding to the four regions in Figure 2.*

Figure 2 reveals the complete limit cycle lifecycle:

- **Region I** ($\mu_c < \mu_c^A$): no limit cycle exists
- **Point A**: a semi-stable limit cycle emerges (outer-stable, inner-unstable)
- **Region II**: stable + unstable coexistence
- **Point B**: a second semi-stable bifurcation occurs
- **Region III**: one stable + one unstable limit cycle coexist
- **Region IV** ($\mu_c > 0$): only a single stable limit cycle persists

### Example 2: Heteroclinic Bifurcation (Section 4.3)

![Heteroclinic bifurcation parameters](/assets/img/publication_preview/p3-fig8.png){: width="70%"}

*Figure 8: Variation of the heteroclinic bifurcation parameter $\mu_c^{\mathrm{hetero}}$ with system parameters.*

![Heteroclinic phase portraits](/assets/img/publication_preview/p3-fig9.png){: width="70%"}

*Figure 9: Heteroclinic phase portraits — analytical MGHFP solutions vs. Runge–Kutta numerical reference.*

## Five Key Findings

1. **First purely symbolic GHFP variant:** The introduction of composite Simpson quadrature makes this the first GHFP variant capable of **purely symbolic execution** for complicated oscillators — the foundational innovation enabling all subsequent MGHFP work.

2. **Complete lifecycle from parametric plane:** The $\mu_c$–$A$ curve reveals the entire lifecycle of each limit cycle, with four distinct regions separated by semi-stable bifurcation points. Phase portraits visually confirm the analysis.

3. **Homoclinic and heteroclinic bifurcations predicted:** Both types of global bifurcation are quantitatively analyzed. The analytical expression for $\mu_c^{\mathrm{hetero}}$ enables systematic multi-damping-coefficient study — a capability unique to MGHFP.

4. **Validated on maximally challenging test case:** The DHRL oscillator combines rational restoring force with six-term generalized Rayleigh–Liénard damping. All analytical predictions agree with Runge–Kutta results.

5. **Foundation for the MGHFP series:** This framework was subsequently extended to SD oscillators with quartic damping (IJNLM 2025, with Padé enhancement) and coupled SD oscillators with two irrational terms (Phys. Scr. 2026).

## Limitations

- Large perturbation ($\varepsilon > 0.5$): accuracy degrades
- Limit cycles crossing saddle points: Fourier truncation ($m=4$) may be insufficient
- Non-smooth potential wells ($\alpha = 0$): accuracy affected

## Position in the MGHFP Series

This paper occupies the **foundational position** in the MGHFP series. The composite Simpson integration strategy is the unifying thread: IJNLM 2025 introduces Padé approximation for further simplification and multi-parameter extension, and Phys. Scr. 2026 generalizes the method to coupled SD oscillators with two irrational terms — the most complex application in the series.

For researchers in nonlinear perturbation methods, the methodological contribution — the Simpson discretization + perturbation expansion strategy for systems with irrational/rational nonlinearities — has broad transferability.
