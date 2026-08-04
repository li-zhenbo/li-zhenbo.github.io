---
layout: post
title: "Paper Notes — Generalized Function Projective Synchronization of Two Different Hyperchaotic Systems with Unknown Parameters"
date: 2011-03-15 11:00:00+0800
description: Combining adaptive control with an antisymmetric structure to achieve GFPS of hyperchaotic Chen and Lorenz systems with fully unknown parameters
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **Paper:** Li, Z., & Zhao, X. (2011). *Generalized function projective synchronization of two different hyperchaotic systems with unknown parameters*. Nonlinear Analysis: Real World Applications, 12(5), 2607–2615.
> **Links:** [Essential Summary PDF](/assets/pdf/essential-summary-p13.pdf) · [DOI](https://doi.org/10.1016/j.nonrwa.2011.03.009)

## TL;DR

This paper combines **adaptive control** with an **antisymmetric structure** to design an extended adaptive controller that is more generalized and simpler than existing ones. Under this controller, **generalized function projective synchronization (GFPS)** of hyperchaotic Chen and Lorenz systems is achieved with **completely unknown parameters**, and all unknown parameters are estimated online.

## Background

Projective synchronization is attractive for secure communications due to its proportional feature enabling fast communication. The concept evolved as:

**Projective synchronization** (Mainieri & Rehácek 1999, partially linear systems) → **Modified projective synchronization** (MPS, constant scaling *matrix*) → **Function projective synchronization** (FPS, scaling *function*) → **Modified function projective synchronization** (MFPS, scaling function *matrix*) → **Generalized function projective synchronization** (GFPS, more general scaling function matrix).

This paper addresses the most general scenario: achieving GFPS between two *different* hyperchaotic systems whose parameters are *completely unknown*.

## Method: GFPS with Antisymmetric-Structure Controller

### Problem Formulation

Drive system with unknown parameters $\Theta$:
$$
\dot{x} = f(x) + \Phi(x)\Theta
$$

Response system with unknown parameters $\Omega$:
$$
\dot{y} = g(y) + \Psi(y)\Omega + U
$$

### Error Definition (Key Innovation)

The GFPS error is defined relative to a **scaling function matrix** $h(x) = \mathrm{diag}\{h_1(x), \ldots, h_n(x)\}$:
$$
\boxed{e = y - h(x)x, \qquad \dot{e} = g(y) + \Psi(y)\Omega - J\big(f(x) + \Phi(x)\Theta\big) + U}
$$
where $J = \mathrm{d}(h(x)x)/\mathrm{d}x$. This unifies prior schemes: equal $h_i$ → FPS; constant $h_i$ → MPS; $h \equiv 0$ → chaos control.

### Stability Lemma (Antisymmetric Structure)

**Theorem 1.** For $\dot{x} = B(x)x$ with $B(x) = B_1(x) + B_2$, if $B_1^T = -B_1$ (antisymmetric) and $B_2 = \mathrm{diag}\{b_i\}$ with $b_i < 0$, then the system is asymptotically stable.

**Proof.** With $V = \frac{1}{2}x^Tx$, the antisymmetric part cancels in the derivative:
$$
\dot{V} = x^T B_2 x < 0
$$

The elegance of the antisymmetric structure: **no eigenvalue computation needed** — the Lyapunov function gives global asymptotic stability directly.

### Main Controller (Theorem 2)

$$
\boxed{U = J\big(f(x) + \Phi(x)\hat\Theta\big) - g(y) - \Psi(y)\hat\Omega + Ke}
$$

Parameter update laws:
$$
\dot{\hat\Theta} = -J^T \Phi^T(x) e + \tilde\Theta, \qquad
\dot{\hat\Omega} = \Psi^T(y) e + \tilde\Omega
$$
where $K$ satisfies Theorem 1. The Lyapunov function $V = \frac{1}{2}(e^Te + \tilde\Theta^T\tilde\Theta + \tilde\Omega^T\tilde\Omega)$ has negative-definite derivative, guaranteeing global asymptotic stability of the error system and convergence of parameter estimates.

## Results: Hyperchaotic Chen → Hyperchaotic Lorenz

The drive is a hyperchaotic Chen system and the response a hyperchaotic Lorenz system, with fully unknown parameters ($a=35,b=3,c=12,d=7,r=0.08$; $a_1=10,b_1=28,c_1=8/3,d_1=1.3$).

### Case 1: Periodic Scaling Functions
$$
h_i(x_i) = d_{i1}\sin(d_{i2}x_i + d_{i3}) + d_{i4}
$$

![Parameter estimation (drive system)](/assets/img/publication_preview/nonrwa-fig1.png){: width="70%"}

*Figure 1: Online estimation of the drive system's unknown parameters under periodic scaling functions — all converge to true values.*

![Synchronization errors](/assets/img/publication_preview/nonrwa-fig3.png){: width="70%"}

*Figure 2: Time response of GFPS errors with periodic scaling functions — errors converge to zero.*

### Case 2: Polynomial Scaling Functions
$$
h_i(x) = d_{i1}x_i^2 + d_{i2}x_i + d_{i3}
$$

![Synchronization errors (polynomial)](/assets/img/publication_preview/nonrwa-fig6.png){: width="70%"}

*Figure 3: Time response of GFPS errors with polynomial scaling functions.*

## Key Findings

1. **Unified framework**: GFPS with scaling function matrix $h(x)$ subsumes FPS, MPS, and chaos control as special cases
2. **Simpler and more general**: The antisymmetric-structure design yields a controller simpler than Du et al. (2009) and more general than Yu & Li (2010) — the latter is a special case
3. **Online parameter estimation**: All 8 unknown parameters of both hyperchaotic systems are estimated while synchronization is achieved
4. **Complicated scaling functions**: Periodic (sine) and polynomial scaling functions — not discussed in prior literature — are both demonstrated
5. **Rigorous stability**: The antisymmetric structure guarantees $\dot V < 0$, giving a strict global asymptotic stability proof

## Significance

This is the author's second major work in chaos synchronization, a companion to the 2011 Acta Physica Sinica paper on modified active control for generalized projective synchronization. Together these papers establish the "chaos synchronization" thread in the author's research trajectory. The core methodological idea — designing controllers via an antisymmetric structure validated by Lyapunov theory rather than algebraic eigenvalue criteria — mirrors the Lyapunov-centric philosophy later applied to the analytical perturbation methods (GHFP/MGHFP series).
