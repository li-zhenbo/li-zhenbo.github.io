---
layout: post
title: 论文笔记：SD 振子的极限环全局演化与同宿分岔——Padé 增强的 MGHFP 方法
date: 2025-07-04 10:00:00+0800
description: 引入 Padé 近似改进 MGHFP 方法，对含四次非线性阻尼的 SD 振子进行极限环全局演化与同宿分岔定量分析，首次实现多参数讨论
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **论文 Paper**: Li, Z., Hou, L., & Peng, R. (2025). *Global Evolution of Limit Cycles and Homoclinic Bifurcation of Smooth and Discontinuous Oscillator with Quartic Nonlinear Damping*. International Journal of Non-Linear Mechanics, 178, 105185.
> **链接 Links**: [精华汇总 PDF](/assets/pdf/essential-summary-p2.pdf) · [DOI](https://doi.org/10.1016/j.ijnonlinmec.2025.105185)

## TL;DR 一句话总结

将 Padé 近似引入 MGHFP 方法框架，把原本复杂难用的解析表达式简化为有理函数形式——不仅降低了使用门槛，更重要的是首次实现了**多参数**讨论（此前只能单参数分析）。这是 MGHFP 系列方法论的一次重要升级。

Introducing Padé approximation into the MGHFP framework simplifies the previously complicated analytical expressions into rational functions — lowering the barrier to use and for the first time enabling **multi-parameter** analysis of limit cycle evolution.

## 研究动机

SD 振子（Smooth and Discontinuous Oscillator）是典型的无理非线性振子，但**含非线性阻尼的 SD 振子**研究很少。已有工作主要关注 SD–van der Pol 振子（仅含二次阻尼），对含四次非线性阻尼（\(\mu_4 x^4\dot{x}\)）的情况无人触及。四次阻尼在高阶非线性系统（如 MEMS 微梁谐振器、高阻尼隔振器）中普遍存在，绕不开。

此外，作者此前发展的 MGHFP 方法虽然能解决问题，但输出表达式过于复杂——系数函数包含嵌套的 Simpson 积分，用户必须先给系统参数赋值，表达式退化为半解析，只能单参数分析。引入 Padé 近似就是为了打破这个限制。

## 系统模型

研究含四次非线性阻尼的 SD 振子：

\[
\ddot{x} + \omega_0^2 x\left(1 - \frac{1}{\sqrt{x^2+\alpha^2}}\right) = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2 + \mu_3 x^3 + \mu_4 x^4)\dot{x}
\]

其中 \(\alpha\) 是光滑参数（\(\alpha\to 0\) 退化为非光滑），\(\omega_0\) 是固有频率，\(\varepsilon\) 是小扰动参数，\(\mu_c\) 为控制参数。无理恢复力来自斜弹簧几何构型。

![势能图](/assets/img/publication_preview/p2-fig2-potential.png){: width="70%"}
*Figure 2: SD 振子的双阱势能图。\(\alpha\) 从 1 降至 0，系统从单阱过渡到双阱，形成同宿轨道。*

## 方法创新：MGHFP + Padé 近似

### MGHFP 三步走

1. **非线性时间变换** \(d\varphi/dt = \Phi(\varphi)\)，假设解 \(x = a\cos^2\Phi + b\)
2. **摄动展开** \(a = a_0 + \varepsilon a_1 + \cdots\)
3. **复合 Simpson 积分**离散化无理解析无法处理的无理非线性项积分

### Padé 近似 —— 本次的关键改进

MGHFP 输出的系数函数（如 \(f_{2i}(\alpha, A)\)）形式复杂，包含嵌套积分，不便于直接分析。本文引入 Padé 近似将这些系数函数拟合为**有理函数**：

\[
f(\alpha, A) \approx \frac{P_n(\alpha, A)}{Q_m(\alpha, A)}
\]

相比于作者此前尝试的最小二乘多项式逼近（需先赋参数值 → 退化半解析 → 只能单参数讨论），Padé 的结果是**完全解析的**，可以直接讨论多个参数同时变化时极限环的演化行为。

## 核心公式

### 振幅—参数关系

极限环振幅 \(A\) 与控制参数 \(\mu_c\) 的解析关系：

\[
\boxed{\mu_c = -\frac{4}{a_0^2(2p_0 - p_4)}\Big(\tilde{E}_1\mu_1 + \tilde{E}_2\mu_2 + \tilde{E}_3\mu_3 + \tilde{E}_4\mu_4\Big)}
\]

其中 \(\tilde{E}_i\) 现在是 Padé-近似的有理函数——**比原始 MGHFP 表达式简洁得多**，且支持多参数分析。\(p_{2i}\) 仍通过复合 Simpson 公式计算。

![振幅—参数关系](/assets/img/publication_preview/p2-fig3-amplitude.png){: width="70%"}
*Figure 3: (上) \(\mu_c\)–\(A\) 曲线。(下) \(H_0\)–\(A\) 曲线。(底行) 不同 \(\mu_c\) 下的相图。实线/虚线：MGHFP。圆点：Runge–Kutta。极限环从产生、分岔到收敛全过程定量可视化。*

### 稳定性判据

\[
\boxed{H_0 = \frac{1}{\pi}\int_0^\pi \left[\mu_c + \sum_{i=1}^{4}\mu_i(a_0\cos^2\varphi + b)^i\right]d\varphi}
\]

\(H_0 > 0\)：不稳定；\(H_0 = 0\)：半稳定（分岔点）；\(H_0 < 0\)：稳定。

### 同宿分岔阈值

令 \(b = h\)（鞍点纵坐标）代入振幅—参数关系，即得同宿分岔的临界参数 \(\mu_c^{\mathrm{hom}}\)——极限环与鞍点碰撞并消失的时刻。

## 核心结论

### 算例 1：单阱（\(\alpha = 2\)）

参数 \(\mu_1=-1, \mu_2=1.5, \mu_3=1, \mu_4=-1\)，Figure 3 揭示了完整的极限环生命周期：

- 低于临界值 \(\mu_c\)：**无极限环**
- 临界点：**半稳定**极限环产生
- \(\mu_c\) 继续增大：分裂为一个**稳定**（\(H_0 < 0\)）和一个**不稳定**（\(H_0 > 0\)）极限环
- 不稳定环最终**坍缩**至平衡点；稳定环持续增大

### 算例 2：不同参数集（\(\alpha = 0.65\)）

参数 \(\mu_1=-0.5, \mu_2=1, \mu_3=1, \mu_4=-0.1\)，解析与数值一致性好。

![另一个参数集](/assets/img/publication_preview/p2-fig8-amplitude2.png){: width="70%"}
*Figure 8: 不同参数集下的 \(\mu_c\)–\(A\) 和 \(H_0\)–\(A\) 曲线。方法在参数空间内准确捕捉极限环演化和稳定性过渡。*

### 极限环解析解

![解析解对比](/assets/img/publication_preview/p2-fig7-solutions.png){: width="70%"}
*Figure 7: 不同 \(\mu_c\) 下极限环的解析解与 Runge–Kutta 数值解对比。验证了 MGHFP+Padé 方法的精度和可靠性。*

## 5 条核心发现

1. **Padé 增强的 MGHFP**：将 Padé 近似引入 MGHFP 得到简洁、全解析的振幅—参数关系式。不同于此前的最小二乘半解析结果，现版本支持**多参数**分析。
2. **完整生命周期定量预测**：回答了极限环何时出现、如何分岔、收敛于何处、是否稳定——包括不稳定极限环的精确预测（数值方法极难做到）。
3. **同宿分岔阈值解析化**：给出了极限环与鞍点碰撞并湮灭的临界参数解析表达式。
4. **多参数分类定理**（Theorem 2 & 3）：利用简化的表达式，首次推导出振荡器恰好存在两个极限环的参数区域——这是此前 MGHFP 结果做不到的。
5. **工程指导意义**：框架同时支持振荡**幅度调控**（能量采集、捕食者-猎物模型）和振荡**抑制**（隔振平台、车辆悬架、气动弹性颤振）。通过分岔参数调节，极限环可被创建、调制或消除。

## 方法的局限

- 大扰动（\(\varepsilon > 0.5\)）精度下降，需提高截断阶数
- 极限环穿越鞍点时速度急剧下降，Fourier 截断（\(m = 4\)）可能不够
- 非光滑势阱（\(\alpha = 0\)）影响精度

## 与系列工作的关系

本文在 MGHFP 系列中处于承上启下的位置——首次通过 Padé 近似将方法从半解析升级为全解析、从单参数扩展到多参数。这一改进直接催生了后续 Physica Scripta 2026 的工作（MGHFP 应用于含两个无理非线性项的耦合 SD 振子），后者是系列中最复杂的一步。

对于做非线性摄动方法的同行，本文的方法论价值可能比具体结果更大——Padé 近似 + 摄动展开的组合策略，在无理非线性系统中具有很好的迁移性。
