---
layout: post
title: Paper Notes — Quantitative Analysis of Dynamical Bifurcations in a Coupled SD Oscillator with High-order Nonlinear Damping
date: 2026-07-16 10:00:00+0000
description: MGHFP method for global limit cycle evolution and homo-heteroclinic bifurcation in coupled SD oscillators with two irrational nonlinearities
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **Paper:** Li, Z., Hou, L., & Peng, R. (2026). *Quantitative Analysis of Dynamical Bifurcations in a Coupled Smooth and Discontinuous Oscillator with High-order Nonlinear Damping*. Physica Scripta, 101(12), 125205.
> **Links:** [Essential Summary PDF](/assets/pdf/essential-summary.pdf) · [DOI](https://doi.org/10.1088/1402-4896/ae5134)

## TL;DR

For the first time, the MGHFP method achieves a complete quantitative framework for analyzing the global evolution of limit cycles in a coupled SD oscillator with two irrational nonlinearities — predicting the birth, evolution, stability, and annihilation of every limit cycle.

## System Model

The coupled SD oscillator with high-order nonlinear damping:

$$
\ddot{x} + (x+\beta)\frac{1}{\sqrt{(x+\beta)^2+\alpha^2}} + (x-\beta)\frac{1}{\sqrt{(x-\beta)^2+\alpha^2}} = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2 + \mu_3 x^3 + \mu_4 x^4)\dot{x}
$$

where $\alpha$ is the smoothing parameter ($\alpha=0$ yields the non-smooth limit), $\beta$ is the coupling parameter, $\mu_c$ is the control parameter, and $\mu_1$–$\mu_4$ are nonlinear damping coefficients. The two irrational nonlinear terms arise from the geometric configuration of oblique springs and form the primary analytical difficulty.

![Potential energy diagram](/assets/img/publication_preview/fig5-potential.png){: width="70%"}

*Figure 5: Triple-well potential energy diagram. Five equilibrium points create a complex landscape where homoclinic and heteroclinic orbits can coexist at the same saddle point.*

## Key Findings

### 1. Analytical Amplitude–Parameter Relationship

The core output of the MGHFP method is the analytical relationship between the limit cycle amplitude $A$ and the control parameter $\mu_c$:

$$
\boxed{\mu_c = -\frac{4}{a_0^2(2p_0 - p_4)}\Big(E_1\mu_1 + E_2\mu_2 + E_3\mu_3 + E_4\mu_4\Big)}
$$

where $p_{2i}$ are computed via the composite Simpson formula and $E_i$ are functions of $a_0$, $b$, and $p_{2i}$. Given system parameters, one can directly compute the number, amplitude, and existence interval of every limit cycle — no numerical search needed.

![Amplitude–parameter relationship](/assets/img/publication_preview/fig1-amplitude.png){: width="70%"}

*Figure 1: (Upper) Relationship between limit cycle amplitude $A$ and control parameter $\mu_c$. (Lower) Characteristic quantity $h_0$ determining stability. Key bifurcation points: $\mu^{(0)}=-0.1249$ (semi-stable cycle emerges), $\mu^{(1)}=-0.05$ (splits into stable + unstable), $\mu^{(2)}=0.02$ (unstable cycle collapses to singular point).*

### 2. Stability Criterion

Limit cycle stability is determined by the characteristic quantity $h_0$:

$$
\boxed{h_0 = \frac{1}{\pi}\int_0^\pi \left[\mu_c + \sum_{i=1}^{4}\mu_i(a_0\cos^2\varphi + b)^i\right]d\varphi}
$$

Based on the qualitative theory of ODEs: $h_0 > 0$ — unstable; $h_0 = 0$ — semi-stable (bifurcation point); $h_0 < 0$ — stable. Notably, unstable and semi-stable limit cycles — exceedingly difficult to capture by purely numerical means — are reliably identified by this method.

![Limit cycle phase portraits](/assets/img/publication_preview/fig2-limitcycles.png){: width="70%"}

*Figure 2: Phase portraits of limit cycles at different $\mu_c$ values ($\varepsilon=0.2$). Solid lines: Runge–Kutta numerical integration. Dotted lines: MGHFP analytical method.*

### 3. Single-Well and Triple-Well Configurations

The single-well case concerns large limit cycles enclosing equilibrium points. The triple-well case is considerably more complex — the system can simultaneously host small limit cycles (enclosed by homoclinic orbits), large limit cycles (enclosing all equilibria), and both homoclinic and heteroclinic orbits. The MGHFP method successfully predicts homo-heteroclinic bifurcation parameters for the triple-well system, with excellent agreement against Runge–Kutta.

![Triple-well limit cycles](/assets/img/publication_preview/fig7-triplewell.png){: width="70%"}

*Figure 7: Limit cycles for the triple-well coupled SD oscillator at different $\mu_c$ ($\varepsilon = 1$). Solid lines: Runge–Kutta. Dotted lines: MGHFP. Even at large perturbation, analytical results closely match the numerical reference.*

### 4. Method Applicability Limits

The paper candidly identifies conditions under which accuracy degrades. When $\lvert\varepsilon\mu_i\rvert > 0.5$, the first-order expansion loses precision; when limit cycles cross saddle points, a higher Fourier truncation order is needed.

## Method Highlights

**Nonlinear time transformation:** $\frac{d\varphi}{dt} = \Phi(\varphi)$ → Fourier expansion $x = a\cos^2\Phi + b$ → perturbation expansion $a = a_0 + \varepsilon a_1 + \cdots$. The core innovation of MGHFP is introducing the **composite Simpson quadrature formula** to discretize integrals involving the two irrational nonlinear terms, making the entire perturbation procedure computationally tractable.

**Homo-heteroclinic bifurcation parameters:** Setting the amplitude equal to the saddle-point energy in the amplitude–parameter relation directly yields the corresponding bifurcation threshold. For triple-well systems, homoclinic and heteroclinic orbits can coexist at the same saddle — a challenge uniquely addressed by MGHFP.

## Relation to Prior Work

This paper is part of the authors' ongoing MGHFP series: first proposed for Rayleigh–Liénard oscillators (Phys. Scr. 2024), extended to Duffing–Harmonic–Rayleigh–Liénard oscillators (IJNLM 2024) and SD oscillators with quartic damping (IJNLM 2025). The present work extends MGHFP to coupled SD oscillators — doubling the irrational terms, raising the damping order to quartic, and expanding the multi-well configuration to triple-well — making it the most complex application in the series.

## Personal Reflections

This paper offers value on two levels for the nonlinear dynamics community. First, the **MGHFP method itself can be transferred** to other systems with irrational or non-smooth nonlinearities (e.g., MEMS micro-beam vibrations, quasi-zero stiffness isolators). Second, the **analytical discrimination of unstable and semi-stable limit cycles** and the **simultaneous prediction of homoclinic and heteroclinic bifurcations** address two long-standing gaps in the analytical treatment of complex engineering oscillators.
