---
layout: post
title: "论文笔记：MGHFP 方法首次提出——混合 Rayleigh–Liénard 振子的全局动力学定量分析"
date: 2024-06-06 10:00:00+0800
description: 复合 Simpson 积分改进 GHFP 方法的首次公开发表，对含三次和五次非线性的混合 Rayleigh–Liénard 振子进行极限环全局演化与同异宿分岔的定量分析
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **论文 Paper**: Li, Z., Hou, L., Zhang, Y., & Xu, F. (2024). *A Modified Perturbation Method for Global Dynamic Analysis of Generalized Mixed Rayleigh–Liénard Oscillator with Cubic and Quintic Nonlinearities*. Physica Scripta, 99(7), 075213.
> **链接 Links**: [精华汇总 PDF](/assets/pdf/essential-summary-p4.pdf) · [DOI](https://doi.org/10.1088/1402-4896/ad5066)

## TL;DR 一句话总结

这是 **MGHFP 方法的第一次公开发表**——在经典广义谐波函数摄动法中引入复合 Simpson 积分公式，使方法能够在复杂非线性振子上纯符号化执行，无需预设任何系统参数即可推导振幅与参数的解析关系。后续 IJNLM 2024（DHRL 振子）、IJNLM 2025（SD 振子四次阻尼）、Phys. Scr. 2026（耦合 SD 振子）均从此处起源。

This is the **first publication** of the MGHFP methodology — introducing composite Simpson integration into the classical GHFP framework to enable purely symbolic execution. All subsequent MGHFP work (IJNLM 2024, IJNLM 2025, Phys. Scr. 2026) originates from this paper.

## 研究动机

推导极限环振幅与系统参数之间的解析关系，是非线性动力学定量分析的核心任务。但当恢复力或非线性阻尼比较复杂时（例如同时包含 Rayleigh 型和 Liénard 型阻尼项），许多现有的分析方法**无法纯符号化地执行其流程**——必须预先对系统参数赋值，结果退化为半解析，只能获得参数空间中的孤立解快照。

本文的目标是**提出一种改进的广义谐波函数摄动法**，通过引入复合 Simpson 积分公式来解决上述符号化执行的问题。为验证方法的有效性，本文选择了一个**含三次和五次非线性的混合 Rayleigh–Liénard 振子**作为测试案例——这个振子的阻尼项同时包含 Rayleigh 型（$\dot{x}^2$ 项）和 Liénard 型（$x^2$、$x^4$ 项），是检验方法能力的理想平台。

## 系统模型

广义混合 Rayleigh–Liénard 振子含三次和五次非线性：

$$
\ddot{x} + g(x) = \varepsilon(\mu + \mu_2 x^2 + \mu_4 x^4 + \mu_{1r} \dot{x}^2 + \mu_{2r} x\dot{x}^2 + \mu_{3r} x^3\dot{x}^2)\dot{x}
$$

其中 $g(x)$ 为恢复力，$\mu$ 为控制参数，$\mu_2$、$\mu_4$ 为 Liénard 型阻尼系数，$\mu_{1r}$、$\mu_{2r}$、$\mu_{3r}$ 为 Rayleigh 型阻尼系数。阻尼项的混合特性使得经典方法难以处理。

![势能图](/assets/img/publication_preview/p4-fig1.png){: width="70%"}

*Figure 1: 单阱条件下的势能图。恢复力决定极限环演化的定性结构背景。*

## 方法创新：MGHFP 的诞生

### 经典 GHFP 的瓶颈

经典 GHFP 方法的核心步骤：(1) 非线性时间变换 → (2) Fourier 展开解 → (3) 摄动展开 → (4) 计算 Fourier 系数。第 (4) 步在复杂振子上遇到瓶颈——无理非线性项涉及的积分**无法解析计算**，必须先赋参数值再数值积分。

### MGHFP 的突破

MGHFP 方法将**复合 Simpson 积分公式**引入第 (4) 步：

$$
\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f(x_0) + 4\sum_{i\ \mathrm{odd}} f(x_i) + 2\sum_{i\ \mathrm{even}} f(x_i) + f(x_n)\right]
$$

将积分区间等分为 8 个子区间后，Fourier 系数 $p_{2i}$ 被转化为系统参数的**显式代数函数**——整个摄动流程从此可以纯符号化运行。

## 核心公式

### 振幅—参数关系

极限环振幅 $A$ 与控制参数 $\mu$ 的解析关系：

$$
\boxed{\mu = -\frac{1}{a_0^2(2p_0 - p_4)}\Big(E_2\mu_2 + E_4\mu_4 + E_{1r}\mu_{1r} + E_{2r}\mu_{2r} + E_{3r}\mu_{3r}\Big)}
$$

其中 $p_{2i}$ 由复合 Simpson 公式计算，$E_i$ 为 $a_0$、$b$、$p_{2i}$ 的函数。给定参数即可直接获得极限环振幅。

### 稳定性判据

$$
\boxed{h_0 = \frac{1}{\pi}\int_0^\pi \Big[\mu + \sum\mu_i(a_0\cos^2\varphi + b)^i + \sum\mu_{jr}(a_0\cos^2\varphi + b)^j(\dot{x}_0)^2\Big]d\varphi}
$$

$h_0 > 0$：不稳定；$h_0 = 0$：半稳定（分岔点）；$h_0 < 0$：稳定。

## 核心结论

### 算例 1：单阱势（Section 4.1）

![相图](/assets/img/publication_preview/p4-fig3.png){: width="70%"}

*Figure 3: 单阱振子在不同 $\mu$ 和 $A$ 值下的相图（$\varepsilon = 0.01$）。彩色点标记每条轨道的初始点。*

![$\mu$–$A$ 曲线对比](/assets/img/publication_preview/p4-fig4.png){: width="70%"}

*Figure 4: 单阱振子 $\mu$–$A$ 曲线的对比（$\varepsilon = 0.01$）。实线：本文方法。虚线：Runge–Kutta 参考结果。*

- 低于临界 $\mu$：**无限环**
- 临界点：**半稳定**极限环产生
- $\mu$ 增大：分裂为稳定 + 不稳定极限环
- 不稳定环最终坍缩至平衡点
- **最多三个极限环共存**是可能的（参考原文 Figure 5）

### 算例 2：三阱势（Section 4.2）

![三阱势能](/assets/img/publication_preview/p4-fig6.png){: width="70%"}

*Figure 6: 三阱振子的势能图。多个势阱形成丰富的分岔结构，同宿与异宿轨道可共存。*

![三阱 $\mu$–$A$ 曲线](/assets/img/publication_preview/p4-fig7.png){: width="70%"}

*Figure 7: 三阱振子的 $\mu$–$A$ 和 $h_0$–$A$ 曲线。整个参数范围内的极限环演化和稳定性被定量捕捉。*

![$\mu$–$A$ 曲线对比](/assets/img/publication_preview/p4-fig9.png){: width="70%"}

*Figure 9: 三阱振子鞍点间极限环的 $\mu$–$A$ 曲线对比（$\varepsilon = 0.1$）。方法准确预测分岔阈值。*

## 5 条核心发现

1. **MGHFP 方法的首次提出**：这是复合 Simpson 积分引入 GHFP 框架的首篇公开发表论文，是后续所有 MGHFP 系列工作的起点。

2. **完整生命周期定量预测**：解析的 $\mu$–$A$ 关系揭示了每个极限环从产生到消亡的全过程，包括稳定、不稳定和半稳定分支。

3. **最多三个极限环共存**：方法识别出了三个极限环同时共存的参数区域——这种复杂动力学场景纯数值方法难以完整捕捉。

4. **同宿和异宿分岔预测**：两种全局分岔均可定量分析。解析表达式可作为混沌出现的先兆指示器，具有混沌控制的实用意义。

5. **双重应用价值**：框架同时支持 (i) 极限环**幅度调控**（惯性冲击摇床设计、种群动力学）和 (ii) 通过同异宿分岔阈值**混沌预测**（加密算法、设备保护）。

## 与系列工作的关系

本文在 MGHFP 系列中处于**起点位置**。复合 Simpson 积分的思想在此首次公开发表，随后在 IJNLM 2024 中被应用于更复杂的 DHRL 振子（有理恢复力 + 六项阻尼），在 IJNLM 2025 中通过 Padé 近似得到简化和多参数拓展，在 Phys. Scr. 2026 中被推广到含两个无理非线性项的耦合 SD 振子。对于做非线性摄动方法的同行，本文的方法论贡献——Simpson 离散化 + 摄动展开的组合策略——具有基础性的参考价值。
