---
layout: post
title: "Review: Evolution of the MGHFP Method — From Proposal to Completion Across Four Papers"
date: 2026-07-28 10:00:00+0800
description: Tracing the development of the MGHFP method from its first proposal through multi-parameter extension, irrational nonlinearity, to the most complex dual-irrational coupled application
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> This is the concise online version. The full academic review — with LaTeX-grade typesetting, complete references, and internal cross-references — is available as a **[[PDF download]](/assets/pdf/mghfp-review.pdf)**.

## Abstract

Quantitative analysis of the global evolution of limit cycles in strongly nonlinear oscillators has long been impeded by the inability of classical perturbation methods to execute their procedures symbolically when the restoring force or damping is complicated. Between 2024 and 2026, the Modified Generalized Harmonic Function Perturbation (MGHFP) method evolved across four sequential papers from its initial proposal to a comprehensive analytical framework. This review systematically examines these four papers, tracing the method's development, core framework, and innovation trajectory. It summarizes the contributions at three levels: methodology, theoretical analysis, and engineering applications.

## 1. Introduction: Why Symbolic Execution Matters

The global dynamic analysis of limit cycles — their birth, multiplicity, stability, amplitude, and critical bifurcation conditions — lies at the heart of nonlinear oscillator theory. Most classical perturbation methods encounter a bottleneck at a common stage: when the restoring force or damping is complicated, the integrals involved in Fourier coefficient computation cannot be evaluated analytically. System parameters must be pre-assigned numerical values, reducing the analysis to semi-analytic snapshots and making a continuous global picture unattainable.

The core innovation of the MGHFP method — introducing the composite Simpson quadrature formula into the GHFP procedure — was designed precisely to break this impasse. Four subsequent papers progressively extended the method, ultimately yielding a complete analytical framework capable of covering systems from polynomial restoring forces to dual-irrational nonlinear coupled oscillators.

## 2. Method Overview and Evolutionary Trajectory

The unified MGHFP framework consists of four steps:

**Step 1** Nonlinear time transformation: using $\frac{d\varphi}{dt} = \Phi(\varphi)$ to convert the time-domain oscillator equation into a symmetric, periodic form over the angular domain $[0, \pi]$.

**Step 2** Fourier expansion: assuming $x(\varphi) = a\cos^2\varphi + b$ and expanding $\Phi(\varphi) = \sum_{i=0}^{M}(p_{2i}\cos 2i\varphi + q_{2i}\sin 2i\varphi)$.

**Step 3** Perturbation expansion: treating the damping strength $\varepsilon$ as a small parameter, writing $a = a_0 + \varepsilon a_1 + \cdots$, $\Phi = \Phi_0 + \varepsilon\Phi_1 + \cdots$, and solving order by order.

**Step 4** Composite Simpson integration: for any analytically intractable function $f$, discretizing via $\int_a^b f(x)dx \approx \frac{h}{3}[f(x_0) + 4\sum_{i:odd}f(x_i) + 2\sum_{i:even}f(x_i) + f(x_n)]$. With $n = 18$ subintervals, all Fourier coefficients $p_i$ become **explicit algebraic functions** of the system parameters $\{c_i, \mu_i\}$ — no parameter pre-assignment required.

This framework yields two core formulas: the **amplitude–parameter relation** (control parameter $\mu$ as an explicit function of amplitude $A$ and all system parameters) and the **stability characteristic quantity** $h_0(A)$. Setting $A$ equal to the saddle point coordinate further yields the critical homoclinic or heteroclinic bifurcation parameters.


![MGHFP Method Evolution Overview](/assets/img/publication_preview/mghfp-flowchart.png){: width="85%"}


## 3. Detailed Progression of the Four Papers

### 3.1 Stage I: Method Proposal (P1, 2024.06)

**Reference**: Li, Hou, Zhang, Xu. Phys. Scr. 99, 075213.

**Target system**: $\ddot{x} + c_1 x + c_3 x^3 + c_5 x^5 = \varepsilon(\mu + \mu_1 x + \mu_2 x^2 + \mu_3 x^3 + \mu_4 x^4 + \mu_{22} \dot{x}^2)\dot{x}$. This mixed Rayleigh–Liénard oscillator features a purely polynomial restoring force and six-term damping combining Rayleigh ($\dot{x}^2$) and Liénard ($x, x^3$) types — making the classical GHFP incapable of symbolic execution.

**Milestones**: (i) First public proposal of the MGHFP method with its "composite Simpson + GHFP" formulation; (ii) First purely symbolic derivation of the complete $\mu(A)$ and $h_0(A)$ expressions; (iii) Complete quantitative analysis of up to three coexisting limit cycles under single-well conditions; (iv) Simultaneous prediction of homoclinic and heteroclinic bifurcation thresholds under triple-well conditions.

### 3.2 Stage II: Generalization to Rational Restoring Force (P2, 2024.07)

**Reference**: Li, Cai, Hou. Int. J. Non-Linear Mech. 166, 104832.

**Target system**: $\ddot{x} + \frac{\lambda x + \mu x^3}{1 + \nu x^2} = \varepsilon(\mu_c + \mu_2 x^2 + \mu_4 x^4 + \mu_6 x^6 + \mu_{22} \dot{x}^2 + \mu_{24} \dot{x}^4)\dot{x}$. The defining challenge is the rational restoring force — a denominator containing $\nu x^2$ significantly complicates the Fourier coefficient computation compared to P1's pure polynomial.

**Milestones**: (i) Demonstrated that MGHFP can handle rational restoring forces with $x^2$-containing denominators; (ii) Identified a four-region structure in the $\mu_c$–$A$ curve (I: no cycle → II: stable + unstable coexistence → III: distinct stable/unstable structure → IV: single stable); (iii) Successful homoclinic and heteroclinic bifurcation prediction under triple-well conditions confirmed the framework's robustness across restoring force forms.

### 3.3 Stage III: Padé Enhancement and Multi-Parameter Extension (P3, 2025)

**Reference**: Li, Hou, Peng. Int. J. Non-Linear Mech. 178, 105185.

**Target system**: SD oscillator, $\ddot{x} + \omega_0^2 x(1 - 1/\sqrt{x^2+\alpha^2}) = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2 + \mu_3 x^3 + \mu_4 x^4)\dot{x}$. This marks MGHFP's **first application to irrational nonlinearity** — the restoring force contains a square-root term whose Taylor expansion is an infinite series. Damping extends to quartic order ($\mu_4 x^4\dot{x}$).

**Milestones**: (i) Introduction of **Padé approximation** $f(\alpha, A) \approx P_n(\alpha, A)/Q_m(\alpha, A)$ to fit previously complex nested Simpson integration outputs into simple rational functions; (ii) **First multi-parameter limit cycle analysis** — the joint dependence of $\mu_c$ on $(\mu_1,\mu_2,\mu_3,\mu_4,\alpha)$ can now be discussed simultaneously, in contrast to earlier single-parameter discussions; (iii) Derivation of "Theorems 2 & 3" characterizing the complete parametric regions where the oscillator has exactly two limit cycles — an impossibility in the P1/P2 framework without Padé.

### 3.4 Stage IV: Dual-Irrational Coupled Multi-Well System (P4, 2026)

**Reference**: Li, Hou, Peng. Phys. Scr. 101, 125205.

**Target system**: Coupled SD oscillator, $\ddot{x} + (x+\beta)/\sqrt{(x+\beta)^2+\alpha^2} + (x-\beta)/\sqrt{(x-\beta)^2+\alpha^2} = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2 + \mu_3 x^3 + \mu_4 x^4)\dot{x}$. The **dual irrational terms** represent the highest complexity in the series — Fourier coefficient computation must simultaneously apply Simpson discretization to two independent square-root terms in a high-dimensional parameter space.

**Milestones**: (i) MGHFP successfully applied to a coupled system with two irrational nonlinear terms, demonstrating its generality and extensibility; (ii) The triple-well + dual-irrational coupling allows simultaneous coexistence of small limit cycles (within homoclinic orbits), large limit cycles (enclosing the full space), and heteroclinic orbits (cross-saddle connections) — MGHFP provides all bifurcation predictions in this highest-dimensional setting; (iii) Marks the completion of the series' coverage from polynomial restoring forces to dual-irrational coupled systems.

## 4. Comparative Summary

| | P1 (Phys. Scr.'24) | P2 (IJNLM '24) | P3 (IJNLM '25) | P4 (Phys. Scr.'26) |
|---|---|---|---|---|
| **Published** | 2024.06 | 2024.07 | 2025 | 2026 |
| **Restoring Force** | $c_1x + c_3x^3 + c_5x^5$ | $\frac{\lambda x+\mu x^3}{1+\nu x^2}$ | $\omega_0^2x(1-\frac{1}{\sqrt{x^2+\alpha^2}})$ | Dual-irrational coupled |
| **Damping Terms** | 5 | 6 | 5 | 5 |
| **Potential Wells** | Single/Triple | Single/Double | Single/Double | Single/Triple |
| **Core Innovation** | MGHFP first proposal | Rational restoring force | Padé + multi-parameter | Dual-irrational + multi-well |
| **Homo-hetero Prediction** | ✓ | ✓ | ✓ (homoclinic) | ✓ (all types) |

## 5. Discussion and Contributions

### 5.1 Methodological

MGHFP resolved the core deficiency of nonlinear perturbation methodology — the inability to execute purely symbolically on complicated oscillators. Composite Simpson integration is the key that unlocks the door; Padé approximation compresses the factory-produced expressions into simple closed-form rational functions, simultaneously upgrading them from single-parameter numerical byproducts to true multi-parameter analytical tools.

### 5.2 Theoretical Analysis

Across the four papers, the same framework provides: (i) **Complete lifecycle quantitative prediction** — from semi-stable emergence through stability bifurcation to termination; (ii) A **global evolutionary portrait** on any designated parameter plane; (iii) Analytical determination of **homoclinic and heteroclinic bifurcation thresholds** as precursors to chaos, with direct implications for controller design.

### 5.3 Engineering Applications

From $\mu(A)$ one can directly design amplitude control strategies — maintaining limit cycles of specified amplitudes in inertial impact shakers or population dynamics. From $h_0(A)$ and bifurcation thresholds one can determine the boundary of chaotic behavior, applicable to encryption or equipment protection. The framework has demonstrated transferability to MEMS, quasi-zero stiffness vibration isolation, and energy harvesting systems.

## 6. Conclusion and Outlook

The MGHFP series — spanning four papers in less than two years — progressed from method proposal to full coverage of dual-irrational nonlinear coupled systems. From the perspective of analytical methodology, this toolkit fills a longstanding gap in the GHFP family where symbolic execution on complicated oscillators was impossible, and provides a bridge from qualitative description to global quantitative prediction.

Promising future directions include: (i) extension to multi-degree-of-freedom coupled systems (e.g., Coupled van der Pol–Duffing oscillators); (ii) higher-order perturbation to improve accuracy under large damping; (iii) machine learning acceleration of Simpson subinterval optimization or automated Padé coefficient generation, further expanding the method's complexity frontier.

----

*This review is based on the following four papers (full PDF review with **[[PDF download]](/assets/pdf/mghfp-review.pdf)** ):* 
1. Li et al. (2024) Phys. Scr. 99, 075213 — MGHFP first proposal
2. Li et al. (2024) IJNLM 166, 104832 — Rational nonlinearity extension
3. Li et al. (2025) IJNLM 178, 105185 — Padé enhancement & multi-parameter analysis
4. Li et al. (2026) Phys. Scr. 101, 125205 — Dual-irrational coupled multi-well system
