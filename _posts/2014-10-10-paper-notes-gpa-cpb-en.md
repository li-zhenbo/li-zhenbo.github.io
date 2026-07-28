---
layout: post
title: "Paper Notes — The GPA Method Extended: A Unified Framework for Homoclinic and Heteroclinic Orbits"
date: 2014-10-10 10:00:00+0800
description: The English version of the GPA method — first simultaneous homoclinic and heteroclinic orbit solving via sech/tanh dual approximants
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **Paper:** Li, Z., Tang, J., & Cai, P. (2014). *A Generalized Padé Approximation Method of Solving Homoclinic and Heteroclinic Orbits of Strongly Nonlinear Autonomous Oscillators*. Chinese Physics B, 23(12), 120501.
> **Links:** [Essential Summary PDF](/assets/pdf/essential-summary-p8.pdf) · [DOI](https://doi.org/10.1088/1674-1056/23/12/120501)

## TL;DR

Building on the 2013 Chinese paper, this English version introduces two major advances: (1) extending the GPA method from homoclinic to **heteroclinic orbits** via a novel $\tanh^i t$-based approximant; (2) validating the method across **three fundamentally different oscillator classes** — cubic–quintic Duffing, $\Phi^6$ potential, and Duffing-harmonic. This establishes the first unified computational framework for both homoclinic and heteroclinic orbit determination.

## Motivation

The 2013 paper demonstrated GPA for homoclinic orbits of polynomial-restoring-force oscillators. This paper makes three essential advances: (1) extending to heteroclinic orbits with a dual-approximant strategy; (2) testing on the complex $\Phi^6$ oscillator (five-term asymmetric polynomial); (3) systematically demonstrating GPA's accuracy advantage over classical Padé approximants.

## Core Innovation

### The Dual-Approximant Strategy

For $\ddot{x} + g(x) = 0$ with saddle points $H_i(h_i,0)$:

**Homoclinic** ($x(\pm\infty)=h$):
$$\boxed{\text{GPA}_{\text{hom}}[L/M] = \frac{\sum_{i=0}^{L} \alpha_i \operatorname{sech}^i t}{1 + \sum_{i=1}^{M} \beta_i \operatorname{sech}^i t}}$$

**Heteroclinic** ($x(-\infty)=h_1, x(+\infty)=h_2$):
$$\boxed{\text{GPA}_{\text{het}}[L/M] = \frac{\sum_{i=0}^{L} \alpha_i \tanh^i t}{1 + \sum_{i=1}^{M} \beta_i \tanh^i t}}$$

The $\tanh^i t$ basis satisfies the asymmetric boundary condition $\tanh(\pm\infty)=\pm1$ automatically, requiring no extra constraints. Coefficients are determined by Taylor-expanding at $t=0$ and matching with the power series coefficients $\{a_i\}$ — producing $L+M$ linear equations plus one nonlinear equation from the energy integral.

## Key Results

### Cubic–Quintic Duffing
With $c_1=2, c_3=-10, c_5=9$, the system possesses five fixed points (three centers, two saddles). Two homoclinic orbits (GPA[$4/4$]) and one heteroclinic pair (GPA[$7/7$]) are captured simultaneously — the first demonstration of unified homoclinic–heteroclinic treatment.

![Cubic-quintic orbits](/assets/img/publication_preview/p8-fig1.png){: width="70%"}

*Figure 1: (Original Fig. 1) Homoclinic and heteroclinic orbits of the cubic–quintic Duffing oscillator. Solid: Runge–Kutta. Dotted: GPA method.*

### $\Phi^6$ Potential Oscillator
Five-term asymmetric polynomial. GPA[$5/5$] and GPA[$7/7$] capture both orbit types, with accuracy **demonstrably higher than the classical Padé approximant** at the same order — since polynomial bases struggle with exponential decay asymptotics.

![Phi-6 orbits](/assets/img/publication_preview/p8-fig3.png){: width="70%"}

*Figure 2: (Original Fig. 3) Homoclinic and heteroclinic orbits of the $\Phi^6$ oscillator. Solid: Runge–Kutta. Dotted: GPA. Dashed: classical Padé approximant.*

### Duffing-Harmonic Oscillator
Rational restoring force benchmark. Homoclinic: GPA[$3/3$] with $\lambda=-1, \mu=5, \nu=5$. Heteroclinic: GPA[$8/8$] with $\lambda=3, \mu=-5, \nu=2$. The computational pipeline is unchanged from polynomial cases.

![DH homoclinic](/assets/img/publication_preview/p8-fig4.png){: width="70%"}

*Figure 3: (Original Fig. 4) Homoclinic orbits for $\lambda=-1, \mu=5, \nu=5$. Solid: Runge–Kutta. Dotted: GPA[$3/3$].*

![DH heteroclinic](/assets/img/publication_preview/p8-fig5.png){: width="70%"}

*Figure 4: (Original Fig. 5) Heteroclinic orbits for $\lambda=3, \mu=-5, \nu=2$. Solid: Runge–Kutta. Dotted: GPA[$8/8$].*

## Five Key Findings

1. **First unified homoclinic–heteroclinic framework:** The $\operatorname{sech}^i t$ / $\tanh^i t$ pair provides a single computational architecture for both orbit types.
2. **Superior accuracy to classical Padé:** Hyperbolic-function bases outperform polynomial bases for exponential-decay asymptotics at the same approximation order.
3. **$\Phi^6$ solved analytically:** Five-term asymmetric polynomial oscillator's homoclinic/heteroclinic orbits obtained for the first time.
4. **Rational restoring force is not a barrier:** GPA treats $g(x) = (\lambda x + \mu x^3)/(1+\nu x^2)$ identically to polynomial $g(x)$.
5. **Basis function selection philosophy:** Any function series that naturally satisfies boundary conditions can be used — the choice of basis is the key design decision.

## Limitations
- Conservative systems only ($\varepsilon=0$); damped oscillators need separate methods
- High-order coefficient matching may become ill-conditioned
- Single-degree-of-freedom

## Position in the GPA/GHFP Series

Together with the 2013 Chinese paper, this work forms the foundational GPA duo. Alongside the GHFP/MGHFP series, the GPA method represents a complementary analytical route: direct orbit construction via rational function approximation, as opposed to angular-domain perturbation. The shared mathematical toolkit — rational function approximation for strongly nonlinear systems — connects both methodological families.
