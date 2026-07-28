---
layout: post
title: "Review: Evolution of the GHFP/MGHFP Method — From Foundation to Completion Across Six Papers"
date: 2026-07-28 10:00:00+0800
description: Tracing the GHFP/MGHFP method from its 2013 foundation through symbolic breakthrough to the most complex dual-irrational coupled application across six sequential papers
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> This is the concise online version. The full academic review — with LaTeX-grade typesetting, complete references, and internal cross-references — is available as a **[[PDF download]](/assets/pdf/mghfp-review.pdf)**.

## Abstract

Quantitative analysis of the global evolution of limit cycles in strongly nonlinear oscillators has long been impeded by the inability of classical perturbation methods to execute their procedures symbolically when the restoring force or damping is complicated. The Generalized Harmonic Function Perturbation (GHFP) method, proposed in 2013, established a unified framework for asymmetric oscillators through the quadratic generalized harmonic function and nonlinear time transformation. Over the subsequent 13 years, this framework evolved — via a crucial symbolic upgrade (MGHFP) introduced in 2024 — into a comprehensive analytical toolkit. This review examines all six papers in the series, tracing the complete development from theoretical foundation through symbolic breakthrough to the most complex dual-irrational coupled system.

## 1. Introduction: Why Symbolic Execution Matters

The global dynamic analysis of limit cycles — their birth, multiplicity, stability, amplitude, and critical bifurcation conditions — lies at the heart of nonlinear oscillator theory. In 2013, Li, Tang, and Cai published the founding paper of the GHFP method in the *Journal of Sound and Vibration*, introducing the quadratic generalized harmonic function $x = a\cos^2\varphi + b$ and a nonlinear time transformation to provide a unified treatment of limit cycles and homoclinic orbits in Helmholtz–Duffing oscillators. A 2016 follow-up in *Qualitative Theory of Dynamical Systems* extended the framework to rational restoring forces.

However, the classical GHFP — powerful as it was — shared a critical limitation with all perturbation-based methods: when the restoring force or damping became complicated, the integrals required for Fourier coefficient computation could not be evaluated analytically. System parameters had to be pre-assigned numerical values, reducing the analysis to semi-analytic snapshots and making a continuous global picture unattainable.

The Modified GHFP (MGHFP) method, introduced between 2024 and 2026, was designed to break precisely this bottleneck. Its defining innovation — embedding the composite Simpson quadrature formula into the GHFP procedure — transforms analytically intractable integrals into explicit algebraic functions of system parameters, enabling purely symbolic execution. Together with the two founding papers, the six papers in this series constitute a complete analytical framework spanning polynomial to dual-irrational nonlinear coupled systems.

## 2. Method Overview and Evolutionary Trajectory

### 2.1 The GHFP Foundation (2013, 2016)

The GHFP framework was established in the 2013 JSV paper through three core elements that remain central to all subsequent work.

**Element 1 — Nonlinear time transformation.** The transformation $d\varphi/dt = \Phi(\varphi)$ with $\Phi(\varphi+\pi) = \Phi(\varphi)$ maps the time-domain oscillator equation onto the symmetric angular interval $[0, \pi]$.

**Element 2 — Quadratic generalized harmonic function.** The solution is expressed as $x(t) = a\cos^2\varphi(t) + b$ for limit cycles (or $x = a\sin^2\varphi + b$ for homoclinic orbits). The critical insight: the $\cos^2\varphi$ form naturally captures the asymmetry induced by quadratic restoring force terms — the correct basis function for asymmetric oscillators, in contrast to the symmetric $a\cos\varphi + b$ used in classical methods.

**Element 3 — First-order consistency condition.** Expanding $a = a_0 + \varepsilon a_1 + \cdots$ and $\Phi = \Phi_0 + \varepsilon\Phi_1 + \cdots$, with the key assumption that the $n$th-order solution retains the generating solution's functional form, the first-order consistency condition (obtained by integrating the $\varepsilon^1$ equation over $[0, \pi]$) yields the critical homoclinic bifurcation parameter — previously obtainable only through numerical shooting.

The 2016 QTDS paper extended this framework from polynomial to rational restoring forces ($\frac{\lambda x + \delta x^3}{1 + \nu x^2}$), simultaneously predicting both homoclinic and heteroclinic bifurcations with a relative error of only 0.14%. This proved that the GHFP framework was not bound to specific restoring force forms — it was a general-purpose analytical instrument.

**The bottleneck.** In both 2013 and 2016 papers, the Fourier coefficient evaluation — specifically the integral $\Phi_0(\varphi) = \sqrt{2[V(a_0+b) - V(a_0\cos^2\varphi + b)]}/x_0'(\varphi)$ — could not be carried out analytically for general $g(x)$. Parameters had to be pre-assigned, and the analysis remained semi-analytic.

### 2.2 The MGHFP Breakthrough: Symbolic Execution (2024–2026)

MGHFP's core innovation occurs at the fourth step of the GHFP procedure — introducing the composite Simpson quadrature formula to discretize the Fourier coefficient integrals. The unified four-step procedure underlying the four MGHFP papers is:

**Step 1–3** Identical to the GHFP framework.

**Step 4 — Composite Simpson integration.** For any analytically intractable function $f$, discretize via:
$$\int_a^b f(x)dx \approx \frac{h}{3}\left[f(x_0) + 4\sum_{j\ \text{odd}} f(x_j) + 2\sum_{j\ \text{even}} f(x_j) + f(x_n)\right]$$

With $n = 18$ subintervals, all Fourier coefficients $p_i$ become **explicit algebraic functions** of the system parameters — no pre-assignment needed.

This framework yields two universal outputs: the **amplitude–parameter relation** $\mu(A)$, and the **stability criterion** $h_0(A)$. Setting $A$ equal to the saddle coordinate yields the homoclinic or heteroclinic bifurcation threshold.


![GHFP/MGHFP Method Evolution Overview](/assets/img/publication_preview/mghfp-flowchart.png){: width="85%"}


## 3. Detailed Progression of the Six Papers

### 3.1 Stage 0: GHFP Foundation (P5, 2013)

**Reference:** Li, Tang, Cai. *J. Sound Vib.* 332(21), 5508–5522.

**Target system:** Helmholtz–Duffing oscillator $\ddot{x} + c_1 x + c_2 x^2 + c_3 x^3 = \varepsilon f(\mu, x, \dot{x})$. The asymmetric quadratic term $c_2 x^2$ breaks the symmetry of classical Duffing oscillators, rendering classical perturbation methods (based on the symmetric $x = a\cos\varphi + b$) ineffective.

**Milestones:** (i) First proposal of the quadratic generalized harmonic function $x = a\cos^2\varphi + b$, establishing the correct basis for asymmetric oscillators — the single insight that is the mathematical DNA of the entire GHFP/MGHFP family; (ii) The nonlinear time transformation provides a unified treatment of limit cycles and homoclinic orbits within the same framework; (iii) First-ever analytical prediction of homoclinic bifurcation parameters in a strongly nonlinear oscillator; (iv) Accuracy maintained at $\varepsilon = 1$–$2$, far beyond what the small-parameter assumption guarantees. **This is the theoretical cornerstone of the entire series.**

### 3.2 Stage 0+: GHFP Extension to Rational Restoring Forces (P6, 2016)

**Reference:** Li, Tang, Cai. *Qual. Theory Dyn. Syst.* 15(1), 19–37.

**Target system:** Duffing–Harmonic–van de Pol oscillator $\ddot{x} + \frac{\lambda x + \delta x^3}{1 + \nu x^2} = \varepsilon(\mu + \mu_1 x + \mu_2 x^2 + \mu_4 x^4)\dot{x}$. The rational restoring force bridges two regimes — Duffing-like at small amplitudes, linear-harmonic at large amplitudes.

**Milestones:** (i) First GHFP application to rational restoring forces — Fourier coefficient integrals change from explicit polynomials to rational-function integrals, executed manually without Simpson discretization, a computationally demanding achievement; (ii) Simultaneous prediction of both homoclinic and heteroclinic bifurcations, with the heteroclinic $\mu_c$ achieving ~0.14% relative error against Runge–Kutta; (iii) Demonstrated that the GHFP framework is not a special-purpose tool but a broadly transferable analytical platform — this confidence enabled the subsequent MGHFP series.

### 3.3 Stage I: MGHFP Method Proposal (P1, 2024.06)

**Reference:** Li, Hou, Zhang, Xu. *Phys. Scr.* 99, 075213.

**Target system:** $\ddot{x} + c_1 x + c_3 x^3 + c_5 x^5 = \varepsilon(\mu + \mu_1 x + \mu_2 x^2 + \mu_3 x^3 + \mu_4 x^4 + \mu_{22} \dot{x}^2)\dot{x}$. A mixed Rayleigh–Liénard oscillator with 6-term damping — already beyond classical GHFP's symbolic capability.

**Milestones:** (i) First public proposal of the MGHFP method with the "composite Simpson + GHFP" formulation — marking the GHFP family's transition from manual numerical integration to automated symbolic execution; (ii) First purely symbolic derivation of $\mu(A)$ and $h_0(A)$; (iii) Complete quantitative analysis of up to three coexisting limit cycles; (iv) Simultaneous homoclinic and heteroclinic bifurcation prediction under triple-well conditions.

### 3.4 Stage II: Generalization to Rational Restoring Force (P2, 2024.07)

**Reference:** Li, Cai, Hou. *Int. J. Non-Linear Mech.* 166, 104832.

**Target system:** DHRL oscillator $\ddot{x} + \frac{\lambda x + \mu x^3}{1 + \nu x^2} = \varepsilon(\mu_c + \mu_2 x^2 + \mu_4 x^4 + \mu_6 x^6 + \mu_{22} \dot{x}^2 + \mu_{24} \dot{x}^4)\dot{x}$. Compared to P6's manual GHFP treatment of a similar rational restoring force, MGHFP's Simpson discretization shifts the complexity from algebraic derivation to automated discretization — an order-of-magnitude reduction in practical barrier to use.

**Milestones:** (i) Demonstrated MGHFP's symbolic capability on rational restoring forces — a direct comparison point with P6 (QTDS 2016), where GHFP required manual integration; (ii) Four-region structure identified in the $\mu_c$–$A$ curve; (iii) Successful bifurcation prediction under triple-well conditions.

### 3.5 Stage III: Padé Enhancement and Multi-Parameter Extension (P3, 2025)

**Reference:** Li, Hou, Peng. *Int. J. Non-Linear Mech.* 178, 105185.

**Target system:** SD oscillator $\ddot{x} + \omega_0^2 x(1 - 1/\sqrt{x^2+\alpha^2}) = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2 + \mu_3 x^3 + \mu_4 x^4)\dot{x}$. First MGHFP application to irrational nonlinearity — the restoring force contains a square root whose Taylor expansion is an infinite series.

**Milestones:** (i) Introduction of **Padé approximation** $f(\alpha, A) \approx P_n(\alpha, A)/Q_m(\alpha, A)$, compressing multi-page coefficient expressions into simple rational functions; (ii) **First multi-parameter limit cycle analysis** — $\mu_c$'s joint dependence on $(\mu_1,\mu_2,\mu_3,\mu_4,\alpha)$ can be discussed simultaneously; (iii) Derivation of Theorems 2 and 3 characterizing the exact parametric regions with two limit cycles.

### 3.6 Stage IV: Dual-Irrational Coupled Multi-Well System (P4, 2026)

**Reference:** Li, Hou, Peng. *Phys. Scr.* 101, 125205.

**Target system:** Coupled SD oscillator $\ddot{x} + \frac{x+\beta}{\sqrt{(x+\beta)^2+\alpha^2}} + \frac{x-\beta}{\sqrt{(x-\beta)^2+\alpha^2}} = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2 + \mu_3 x^3 + \mu_4 x^4)\dot{x}$. **Dual irrational terms** represent the highest complexity in the series.

**Milestones:** (i) MGHFP successfully applied to a coupled system with two irrational nonlinear terms; (ii) Simultaneous coexistence of small limit cycles, large limit cycles, and heteroclinic orbits in the triple-well + dual-irrational configuration; (iii) Marks the completion of the series' coverage from polynomial to dual-irrational coupled systems.

## 4. Comparative Summary

| | P5 (JSV '13) | P6 (QTDS '16) | P1 (Phys. Scr.'24) | P2 (IJNLM '24) | P3 (IJNLM '25) | P4 (Phys. Scr.'26) |
|---|---|---|---|---|---|---|
| **Published** | 2013 | 2016 | 2024.06 | 2024.07 | 2025 | 2026 |
| **Restoring Force** | $c_1x+c_2x^2+c_3x^3$ | $\frac{\lambda x+\delta x^3}{1+\nu x^2}$ | $c_1x+c_3x^3+c_5x^5$ | $\frac{\lambda x+\mu x^3}{1+\nu x^2}$ | $\omega_0^2x(1-\frac{1}{\sqrt{x^2+\alpha^2}})$ | Dual-irrational coupled |
| **Force Class** | Polynomial (asymmetric) | Rational | Polynomial | Rational | Irrational | Dual Irrational |
| **Damping Terms** | 2–3 | 4 | 5 | 6 | 5 | 5 |
| **Potential Wells** | Single | Single | Single/Triple | Single/Double | Single/Double | Single/Triple |
| **Core Innovation** | **GHFP first proposal** | **GHFP rational extension** | MGHFP first proposal | Rational restoring force | Padé + multi-param | Dual-irrational + multi-well |
| **Method Family** | GHFP | GHFP | MGHFP | MGHFP | MGHFP | MGHFP |
| **Homo-hetero Pred.** | ✓ (homoclinic) | ✓ (both) | ✓ | ✓ | ✓ (homoclinic) | ✓ (all types) |

## 5. Discussion and Contributions

### 5.1 Methodological

The six papers trace two interleaved evolutionary threads.

The first thread is **basis function and framework establishment** (P5 → P6). The 2013 JSV paper introduced three core elements — the quadratic GHF, nonlinear time transformation, and first-order consistency condition — that remain central to every subsequent paper. The 2016 QTDS paper proved the generality of these elements by extending them to rational restoring forces. The $\cos^2\varphi$ basis function choice, made in 2013, is still the mathematical bedrock of the entire family.

The second thread is **symbolic execution** (P1 → P4). MGHFP addressed the critical deficiency left by the first thread: inability to execute purely symbolically on complicated oscillators. Composite Simpson integration transforms analytically intractable integrals into explicit algebraic operations. Padé approximation compresses unwieldy outputs into compact closed forms and enables multi-parameter analysis. An instructive contrast runs through the series: P6 (2016, GHFP manually handling rational forces) versus P2 (2024, MGHFP automatically handling an even more complex rational system) — between them lies a fundamental gap in automation and practical accessibility.

### 5.2 Theoretical Analysis

Across the six papers, the same framework delivers: (i) **complete lifecycle quantitative prediction** — from semi-stable emergence through stability bifurcation to termination; (ii) a **global evolutionary portrait** on any designated parameter plane; (iii) analytical determination of **homoclinic and heteroclinic bifurcation thresholds** as precursors to chaos.

### 5.3 Engineering Applications

From $\mu(A)$ one can directly design amplitude control strategies; from $h_0(A)$ and bifurcation thresholds one can determine chaotic boundaries. The framework has demonstrated transferability to MEMS, quasi-zero stiffness vibration isolation, and energy harvesting.

## 6. Conclusion and Outlook

The GHFP/MGHFP series — spanning six papers across 13 years (2013–2026) — progressed from theoretical foundation to full coverage of dual-irrational nonlinear coupled systems. The 2013 JSV paper established the quadratic GHF framework; the 2016 QTDS paper proved its generality; the four MGHFP papers (2024–2026) automated it for symbolic execution and extended its reach to increasingly complex systems. Together they form a complete analytical toolkit filling the longstanding gap where perturbation-based methods could not be executed symbolically on complicated oscillators.

Promising future directions include: (i) extension to multi-degree-of-freedom coupled systems; (ii) higher-order perturbation expansions for improved accuracy under large damping; (iii) machine learning integration for automatic Simpson subinterval optimization and Padé coefficient generation.

----

*This review is based on the following six papers (full PDF review with **[[PDF download]](/assets/pdf/mghfp-review.pdf)** ):*
1. Li et al. (2013) JSV 332, 5508–5522 — GHFP foundation (Helmholtz–Duffing oscillator)
2. Li et al. (2016) QTDS 15, 19–37 — GHFP rational extension (Duffing–Harmonic–van de Pol oscillator)
3. Li et al. (2024) Phys. Scr. 99, 075213 — MGHFP first proposal
4. Li et al. (2024) IJNLM 166, 104832 — MGHFP rational nonlinearity extension
5. Li et al. (2025) IJNLM 178, 105185 — Padé enhancement & multi-parameter analysis
6. Li et al. (2026) Phys. Scr. 101, 125205 — Dual-irrational coupled multi-well system
