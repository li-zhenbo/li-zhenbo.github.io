---
layout: post
title: 论文笔记：耦合 SD 振子的极限环全局演化与同异宿分岔定量分析
date: 2026-07-16 10:00:00+0800
description: 提出 MGHFP 方法，对含高阶非线性阻尼的耦合 SD 振子进行极限环全局演化与同异宿分岔的定量分析
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **论文 Paper**: Li, Z., Hou, L., & Peng, R. (2026). *Quantitative Analysis of Dynamical Bifurcations in a Coupled Smooth and Discontinuous Oscillator with High-order Nonlinear Damping*. Physica Scripta, 101(12), 125205.
> **链接 Links**: [精华汇总 PDF](/assets/pdf/essential-summary.pdf) · [DOI](https://doi.org/10.1088/1402-4896/ae5134)

## TL;DR 一句话总结

首次用改进广义谐波函数摄动法（MGHFP）打通了耦合 SD 振子全局极限环分析的完整路径，能够定量预测每一个极限环的出生、演化、稳定性与消亡全过程——这在含两个无理非线性项的系统中，此前没有人做出来过。

For the first time, the MGHFP method achieves a complete quantitative framework for analyzing the global evolution of limit cycles in a coupled SD oscillator with two irrational nonlinearities — predicting the birth, evolution, stability, and annihilation of every limit cycle.

## 系统模型

研究的耦合 SD 振子含高阶非线性阻尼：

\[
\ddot{x} + (x+\beta)\frac{1}{\sqrt{(x+\beta)^2+\alpha^2}} + (x-\beta)\frac{1}{\sqrt{(x-\beta)^2+\alpha^2}} = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2 + \mu_3 x^3 + \mu_4 x^4)\dot{x}
\]

其中 \(\alpha\) 为光滑参数（\(\alpha=0\) 退化为非光滑），\(\beta\) 为耦合参数，\(\mu_c\) 为控制参数，\(\mu_1\)–\(\mu_4\) 为非线性阻尼系数。两个无理非线性项来自斜弹簧的几何构型，是分析的主要难点。

![三阱势能](/assets/img/publication_preview/fig5-potential.png)
*Figure 5: 三阱势能图。五个平衡点形成复杂势能面，同宿与异宿轨道可共存于同一鞍点。*

## 核心结论 Key Findings

### 1. 解析的振幅—参数关系

MGHFP 方法的核心输出是极限环振幅 \(A\) 与控制参数 \(\mu_c\) 的解析关系：

\[
\boxed{\mu_c = -\frac{4}{a_0^2(2p_0 - p_4)}\Big(E_1\mu_1 + E_2\mu_2 + E_3\mu_3 + E_4\mu_4\Big)}
\]

其中 \(p_{2i}\) 由复合 Simpson 公式计算，\(E_i\) 为 \(a_0\)、\(b\)、\(p_{2i}\) 的函数。给定系统参数，就可以直接算出有多少个极限环、每个的振幅多大、何时出现何时消失，不需要反复打数值搜索。

![振幅—参数关系图](/assets/img/publication_preview/fig1-amplitude.png)
*Figure 1: (上) 极限环振幅 \(A\) 与控制参数 \(\mu_c\) 的关系。(下) 特征量 \(h_0\)（决定稳定性）。关键分岔点：\(\mu^{(0)}=-0.1249\)（半稳定环产生），\(\mu^{(1)}=-0.05\)（分裂为稳定+不稳定），\(\mu^{(2)}=0.02\)（不稳定环坍缩至奇点）。*

### 2. 稳定性判据首次建立

极限环稳定性由特征量 \(h_0\) 判定：

\[
\boxed{h_0 = \frac{1}{\pi}\int_0^\pi \left[\mu_c + \sum_{i=1}^{4}\mu_i(a_0\cos^2\varphi + b)^i\right]d\varphi}
\]

基于常微分方程定性理论：

- \(h_0 > 0\)：极限环**不稳定**
- \(h_0 = 0\)：极限环**半稳定**（分岔点）
- \(h_0 < 0\)：极限环**稳定**

尤其可以判别不稳定极限环和半稳定极限环——后者纯数值手段几乎捕捉不到，对理解系统的全局动力学结构意义重大。

![极限环相图](/assets/img/publication_preview/fig2-limitcycles.png)
*Figure 2: 不同 \(\mu_c\) 值下的极限环相图（\(\varepsilon=0.2\)）。实线：Runge–Kutta 数值积分。虚线：MGHFP 解析方法。*

### 3. 单阱 + 三阱两种构型全覆盖

单阱条件关心的是包围平衡点的大极限环的振幅—参数依赖；三阱条件更复杂——系统可以同时存在小极限环（被同宿轨道包围）、大极限环（包围所有平衡点），以及同宿轨道和异宿轨道（连接不同鞍点）。

![三阱极限环](/assets/img/publication_preview/fig7-triplewell.png)
*Figure 7: 三阱耦合 SD 振子在不同 \(\mu_c\) 下的极限环（\(\varepsilon = 1\)）。实线：Runge–Kutta。虚线：MGHFP。即使在大扰动参数下，解析结果仍与数值结果高度吻合。*

### 4. 方法适用范围明确

论文坦诚地给出了精度退化条件。当 \(\lvert\varepsilon\mu_i\rvert > 0.5\)（大扰动参数或强非线性阻尼），一阶展开精度下降；当极限环穿越鞍点时，需提高 Fourier 截断阶数（本文默认 m=4）。

## 方法要点 Method Highlights

**非线性时间变换**：引入 \(\frac{d\varphi}{dt} = \Phi(\varphi)\) 转换系统方程 → Fourier 展开解 \(x = a\cos^2\Phi + b\) → 摄动展开 \(a = a_0 + \varepsilon a_1 + \cdots\) ——MGHFP 的改进核心在于**引入复合 Simpson 公式**把两个无理非线性项涉及的积分离散化，使得整个摄动流程可以走通。

**同异宿分岔参数**：在振幅—参数关系式中令振幅趋于鞍点能量对应值，即可预测对应的分岔参数。对于三阱系统，同一鞍点可以同时存在同宿和异宿轨道，这在以前分析方法中是一大难题。

## 与已有文献的关系

本文的 MGHFP 方法是作者团队系列工作的持续推进：2024 年首次提出用于 Rayleigh–Liénard 振子（Phys. Scr. 2024），随后拓展到 Duffing–Harmonic–Rayleigh–Liénard 振子（IJNLM 2024）和含四次非线性阻尼的 SD 振子（IJNLM 2025）。本次是 MGHFP 应用于耦合 SD 振子——无理非线性项从一个变成两个、阻尼阶数提高到四次、系统多阱构型从最多双阱扩展到三阱，属于系列工作中最复杂的一步。

## 个人思考

这篇文章对于非线性动力学领域的同道有两个层面的价值：一是 **MGHFP 方法本身可以作为工具迁移**到其他含无理非线性、或者非光滑非线性项的系统（比如 MEMS 中的微梁振动、准零刚度隔振器等）；二是结论部分对**不稳定极限环和半稳定极限环的解析判别**、以及对**同宿与异宿分岔的并时预测**，这两个点是很多复杂工程振子设计中长期没有好的解析手段的地方。

如果你的工作接触 Van der Pol、Rayleigh 类的非线性阻尼、或者多阱势振子（如 MEMS、吸能结构），这篇的方法思路可能比具体结果更有参考价值。
