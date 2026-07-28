---
layout: post
title: "Paper Notes — Extending the GHFP Method to Rational Restoring Forces: Homoclinic and Heteroclinic Bifurcation Prediction"
date: 2016-02-01 10:00:00+0800
description: First application of GHFP to rational restoring forces — simultaneous prediction of homoclinic and heteroclinic bifurcations in Duffing–Harmonic–van de Pol oscillator
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **Paper:** Li, Z., Tang, J., & Cai, P. (2016). *Predicting Homoclinic and Heteroclinic Bifurcation of Generalized Duffing–Harmonic–van de Pol Oscillator*. Qualitative Theory of Dynamical Systems, 15(1), 19–37.
> **Links:** [Essential Summary PDF](/assets/pdf/essential-summary-p6.pdf) · [DOI](https://doi.org/10.1007/s12346-015-0138-z)

## TL;DR

The GHFP framework's first extension beyond polynomial restoring forces — into the rational regime of $\frac{\lambda x + \delta x^3}{1+\nu x^2}$. This rational restoring force bridges two dynamical regimes: Duffing-like at small amplitudes and linear-harmonic at large amplitudes. The framework simultaneously predicts both homoclinic and heteroclinic bifurcations with a relative error of only **0.14%** for the heteroclinic $\mu_c$. This paper proves the GHFP framework is not a special-purpose tool but a **broadly transferable analytical platform**.

## Motivation

The Duffing–Harmonic oscillator $$\ddot{x} + \frac{\lambda x + \delta x^3}{1 + \nu x^2} = 0$$ is a remarkably useful model: at small $x$, its restoring force is approximately $\delta x^3$ (Duffing); at large $x$, it approaches $(\delta/\nu)x$ (linear harmonic). This amplitude-dependent stiffness transition appears in polymer dynamics, MEMS devices, and vibration isolation systems.

While the conservative Duffing–Harmonic oscillator had been thoroughly studied via harmonic balance, homotopy analysis, and energy balance methods, its **damped** variant — the generalized Duffing–Harmonic–van de Pol oscillator — had received almost no attention from a quantitative global dynamics perspective before 2016. The rational restoring force introduces a fundamentally different computational challenge: Fourier coefficient evaluation involves integrals of rational functions rather than polynomials.

## System Model

The generalized Duffing–Harmonic–van de Pol oscillator:

$$
\ddot{x} + \frac{\lambda x + \delta x^3}{1 + \nu x^2} = \varepsilon(\mu + \mu_1 x + \mu_2 x^2 + \mu_4 x^4)\dot{x}
$$

Left side: rational restoring force with stiffness parameters $\lambda$, $\delta$, $\nu$. Right side: 4-term generalized van de Pol damping.

## Methodological Extension

### Homoclinic Orbits

The saddle point $H(h, 0)$ satisfies $g(h) = \frac{\lambda h + \delta h^3}{1 + \nu h^2} = 0$. The initial condition $c$ is determined by the conservation condition $$\int_h^c \frac{\lambda x + \delta x^3}{1 + \nu x^2} dx = 0$$. The homoclinic solution form is $x(t) = a\sin^2\phi(t) + b$, with $\Phi(0) = \Phi(\pi) = \sqrt{|g(h)/2a|} = 0$ — ensuring infinite period at the saddle point, the defining feature of a homoclinic orbit.

### Heteroclinic Orbits

For two distinct saddle points $h_1$ and $h_2$:

$$
x(0) = h_1, \qquad x(\pi/2) = h_2
$$

The angular velocity satisfies $\Phi(0) = \Phi(\pi/2) = 0$, and the cross-saddle connection must simultaneously satisfy matching conditions at both saddle points — an inherently more stringent test of method accuracy.

### Homoclinic Bifurcation Formula

The first-order consistency condition gives:

$$
\boxed{\mu_c = -\frac{\int_0^\pi \Phi_0 (\mu_1 x_0 + \mu_2 x_0^2 + \mu_4 x_0^4)(\Phi_0 x_0') x_0' d\varphi}{\int_0^\pi \Phi_0^2 (x_0')^2 d\varphi}}
$$

## Key Results

### Example 1: Homoclinic Orbits with $(\mu_1, \mu_2, \mu_4)$ Damping

![Homoclinic orbits 1](/assets/img/publication_preview/p6-fig1-homoclinic.png){: width="70%"}

*Figure 1: (Original Fig. 1) Homoclinic orbits for $\varepsilon=1.2, 2.0$. Solid: Runge–Kutta. Dotted: GHFP method. The quadratic GHF solution form successfully captures homoclinic geometry under rational restoring forces.*

### Example 2: Multiple Coexisting Homoclinic Orbits

![Homoclinic orbits 2](/assets/img/publication_preview/p6-fig2-homoclinic.png){: width="70%"}

*Figure 2: (Original Fig. 2) Homoclinic orbits for $\varepsilon=0.5, 1.0, 1.5, 2.0$. The method tracks orbit morphology across a wide parameter range with consistent accuracy.*

### Example 3: Heteroclinic Bifurcation Prediction

The critical quantitative result — the analytical GHFP prediction vs. numerical Runge–Kutta reference:

$$\mu_c^{\text{(GHFP)}} = -0.1979871606, \qquad \mu_c^{\text{(numerical)}} = -0.1977132821$$

A relative error of approximately **0.14%**.

![Heteroclinic orbits](/assets/img/publication_preview/p6-fig4-heteroclinic.png){: width="70%"}

*Figure 3: (Original Fig. 4) Heteroclinic orbits connecting two distinct saddle points at $\varepsilon=0.5, 0.8, 1.0, 2.0$. The method captures cross-saddle connections with remarkable fidelity across a wide perturbation range.*

## Five Key Findings

1. **First GHFP application to rational restoring forces:** The mathematical leap from polynomial $g(x)$ (JSV 2013) to rational $g(x)$ (here) is non-trivial — every Fourier coefficient integral changes character. The method's success demonstrates the framework's mathematical generality.

2. **Simultaneous homoclinic and heteroclinic prediction:** The same perturbation procedure handles both types of global bifurcation without modification — a capability absent from classical perturbation methods.

3. **~0.14% heteroclinic bifurcation prediction error:** The precision of the analytical $\mu_c$ prediction validates the method's numerical reliability beyond qualitative descriptions.

4. **Flexible $\cos^2\varphi$ / $\sin^2\varphi$ switching:** The choice between basis functions is not arbitrary — homoclinic orbits use $\sin^2\varphi$ while heteroclinic orbits use $\cos^2\varphi$. This flexibility is the mathematical key to the method's success on rational restoring forces.

5. **From specialized tool to general framework:** This paper elevates the GHFP method from a Helmholtz–Duffing-specific tool to a broadly applicable framework for oscillators with diverse restoring force types — providing the methodological confidence that enabled the MGHFP series.

## Limitations

- First-order perturbation only; accuracy degrades for $\varepsilon > 2$
- Requires analytical knowledge of saddle points — limits the admissible restoring force complexity
- Single-degree-of-freedom only

## Position in the GHFP Series

This paper occupies the **crucial methodological extension** position in the GHFP family. If JSV 2013 is "the method is proposed," then QTDS 2016 is "the method survives a significantly harder test." The jump from polynomial to rational restoring forces proves that the GHFP framework is not bound to specific $g(x)$ forms — it is a **general-purpose analytical instrument**. This confidence enabled the subsequent MGHFP series (2024–2026) to tackle even more complex systems: DHRL oscillators with 6-term damping, SD oscillators with Padé-enhanced MGHFP, and coupled SD oscillators with two irrational terms. For researchers in nonlinear dynamics, this paper's demonstration of **basis function flexibility** — choosing $\sin^2$ vs. $\cos^2$ variants depending on the bifurcation type — is a broadly transferable lesson.
