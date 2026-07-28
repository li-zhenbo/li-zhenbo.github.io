---
layout: post
title: 论文笔记：MGHFP 方法的提出——广义谐波函数摄动法的符号化改进
date: 2024-07-14 10:00:00+0800
description: 引入复合 Simpson 积分实现 GHFP 方法的纯符号化执行，MGHFP 系列方法的开篇之作
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **论文 Paper**: Li, Z., Cai, J., & Hou, L. (2024). *A Modified Generalized Harmonic Function Perturbation Method and Its Application in Analyzing Generalized Duffing–Harmonic–Rayleigh–Liénard Oscillator*. International Journal of Non-Linear Mechanics, 166, 104832.
> **链接 Links**: [精华汇总 PDF](/assets/pdf/essential-summary-p3.pdf) · [DOI](https://doi.org/10.1016/j.ijnonlinmec.2024.104832)

## TL;DR 一句话总结

这是 MGHFP 系列方法的**开篇之作**。核心创新是将复合 Simpson 积分公式嵌入经典广义谐波函数摄动法（GHFP），使其首次能够在复杂非线性振子上**纯符号化执行**——不需要预设任何系统参数即可推导出振幅与参数的解析关系。后续 IJNLM 2025（Padé 增强）、Phys. Scr. 2026（耦合 SD 振子）均在此基础上发展而来。

This is the foundational paper of the MGHFP series. Its core innovation — embedding the composite Simpson quadrature formula into the classical GHFP framework — enables purely symbolic execution for the first time, without requiring any system parameter pre-assignment. All subsequent MGHFP work (IJNLM 2025, Phys. Scr. 2026) builds on this foundation.

## 研究动机

经典定量方法（摄动法、能量平衡法、同伦法）可以分析非线性振子，但前提是恢复力和阻尼比较简单。一旦振子变得复杂——比如同时包含多项式和有理非线性——这些方法就**无法纯符号化地执行**，必须先对系统参数赋值，只能得到参数空间中的孤立解快照，无法画出连续的解—参数曲线。

本文的目标就是**提出一种改进的摄动方法**，使其即使在复杂非线性振子上也能纯粹符号化运作，从而能够解析地推导出振幅与系统参数的关系——这正是全球动力学定量分析的关键。

## 系统模型

广义 Duffing–Harmonic–Rayleigh–Liénard（DHRL）振子：

$$
\ddot{x} + \frac{\lambda x + \mu x^3}{1 + \nu x^2} = \varepsilon(\mu_c + \mu_2 x^2 + \mu_4 x^4 + \mu_6 x^6 + \mu_{22} \dot{x}^2 + \mu_{24} \dot{x}^4)\dot{x}
$$

其中 $\lambda$、$\mu$、$\nu$ 为刚度参数，右侧含 **6 项广义非线性阻尼**（Rayleigh 型 $\dot{x}^2$、$\dot{x}^4$ + Liénard 型 $x^2$、$x^4$、$x^6$）。有理恢复力 $\frac{\lambda x + \mu x^3}{1+\nu x^2}$ 使得这个振子成为极具挑战性的测试案例。

![势能图](/assets/img/publication_preview/p3-fig-p13.png){: width="70%"}

*Figure 6: DHRL 振子的势能图。丰富的势能面结构使得同宿和异宿分岔可以发生，是检验 MGHFP 方法的理想平台。*

## 方法创新：MGHFP 的诞生

### 经典 GHFP 的瓶颈

经典 GHFP 方法分四步：非线性时间变换 → Fourier 展开解 → 摄动展开 → 计算 Fourier 系数。第（4）步是关键瓶颈——对于复杂振子，无理非线性项涉及的积分**无法解析计算**，必须先赋参数值再数值积分，结果退化为半解析。

### MGHFP 的突破

MGHFP 方法将**复合 Simpson 积分公式**引入第（4）步：

$$
\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f(x_0) + 4\sum_{i\ \mathrm{odd}} f(x_i) + 2\sum_{i\ \mathrm{even}} f(x_i) + f(x_n)\right]
$$

将积分区间等分为 8 个子区间，Fourier 系数 $p_{2i}$ 被转化为 $a_0$、$b$ 和系统参数的**显式代数函数**——整个摄动流程从此可以纯符号化运行，不再需要参数预赋值。

### 非线性时间变换

解假设为 $x(t) = a\cos^2\varphi(t) + b$，引入 $d\varphi/dt = \Phi(\varphi)$：

$$
\Phi_0(\varphi) = \frac{\sqrt{2[V(a_0+b) - V(a_0\cos^2\varphi + b)]}}{x'_0(\varphi)}
$$

其中 $V(x) = \int g(x)dx$ 为势能。对于复杂的 $g(x)$，此式无法解析——这正是 Simpson 离散化的用武之地。离散化后 $\Phi_0$ 展开为 Fourier 级数（$M=4$）。

## 核心公式

### 振幅—参数关系（中心结果）

极限环振幅 $A$ 与控制参数 $\mu_c$ 的解析关系：

$$
\boxed{\mu_c = -\frac{4}{a_0^2(2p_0 - p_4)}\Big(E_2\mu_2 + E_4\mu_4 + E_6\mu_6 + E_{22}\mu_{22} + E_{24}\mu_{24}\Big)}
$$

其中 $p_{2i}$ 由复合 Simpson 公式计算，$E_i$ 为 $a_0$、$b$、$p_{2i}$ 的函数。给定参数即可直接得到极限环振幅——**无需数值积分**。

### 稳定性判据

$$
\boxed{h_0 = \frac{1}{\pi}\int_0^\pi \Big[\mu_c + \sum\mu_i(a_0\cos^2\varphi + b)^i + \sum\mu_{ij}(a_0\cos^2\varphi + b)^i(\dot{x}_0)^2\Big]d\varphi}
$$

$h_0 > 0$：不稳定；$h_0 = 0$：半稳定（分岔点）；$h_0 < 0$：稳定。

## 核心结论

### 算例 1：极限环全局演化（Section 4.2）

参数 $\lambda=2$、$\mu=1$、$\nu=5$、$\mu_2=-0.88$、$\mu_4=0.39$、$\mu_6=-0.1$、$\mu_{22}=0.17$、$\mu_{24}=0.18$。

![参数平面演化](/assets/img/publication_preview/p3-fig2.png){: width="70%"}

*Figure 2: $\mu_c$–$A$ 参数平面上的极限环演化。四个区域（I–IV）清晰可见。*

![相平面](/assets/img/publication_preview/p3-fig3.png){: width="70%"}

*Figure 3: 与 Figure 2 四个区域对应的相图。*

Figure 2 揭示了完整的极限环生命周期：

- **区域 I**（$\mu_c < \mu_c^A$）：无限环
- **点 A**：半稳定极限环产生（外稳定-内不稳定）
- **区域 II**：稳定 + 不稳定共存
- **点 B**：第二个半稳定分岔
- **区域 III**：一稳定一不稳定共存
- **区域 IV**（$\mu_c > 0$）：仅存单一稳定极限环

### 算例 2：异宿分岔定量分析（Section 4.3）

![异宿分岔参数变化](/assets/img/publication_preview/p3-fig8.png){: width="70%"}

*Figure 8: 异宿分岔参数 $\mu_c^{\mathrm{hetero}}$ 随系统参数的变化。*

![异宿轨道相图](/assets/img/publication_preview/p3-fig9.png){: width="70%"}

*Figure 9: 不同参数下的异宿轨道相图，解析解与 Runge–Kutta 数值解对比。*

## 5 条核心发现

1. **首个纯符号化 GHFP 变体**：复合 Simpson 积分的引入使该方法成为第一个能在复杂振子上**纯符号化执行**的 GHFP 变体——这是后续所有 MGHFP 工作的基石。

2. **参数平面上的完整生命周期**：$\mu_c$–$A$ 曲线揭示了每个极限环从产生到消亡的全过程，四个区域被半稳定分岔点清晰分隔。

3. **同宿和异宿分岔同时预测**：两种全局分岔均可定量分析。$\mu_c^{\mathrm{hetero}}$ 的解析表达式使多阻尼系数的同时研究成为可能。

4. **在最大挑战性案例上验证**：DHRL 振子融合了有理恢复力和 6 项广义 Rayleigh–Liénard 阻尼。所有解析预测与 Runge–Kutta 结果一致。

5. **MGHFP 系列的基石**：本文建立的框架随后被拓展到含四次阻尼的 SD 振子（IJNLM 2025，Padé 增强）和含两个无理非线性项的耦合 SD 振子（Phys. Scr. 2026）。

## 方法的局限

- 大扰动（$\varepsilon > 0.5$）精度下降
- 极限环穿越鞍点时 Fourier 截断（$m=4$）可能不够
- 非光滑势阱（$\alpha = 0$）影响精度

## 与系列工作的关系

本文在 MGHFP 系列中处于**奠基位置**。复合 Simpson 积分的思想在整个系列中一以贯之：IJNLM 2025 引入 Padé 近似将表达式进一步简化并拓展到多参数分析，Phys. Scr. 2026 将方法推广到含两个无理非线性项的耦合 SD 振子——这是系列中最复杂的应用。

对于做非线性摄动方法的同行，本文的方法论价值在于：**Simpson 离散化 + 摄动展开**的组合策略，在无理/有理非线性系统中具有很好的可迁移性。
