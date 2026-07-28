---
layout: post
title: "论文笔记：二次广义谐波函数摄动法——Duffing–Harmonic–van de Pol 振子的同宿与异宿分岔预测"
date: 2016-02-01 10:00:00+0800
description: GHFP 方法首次拓展至有理恢复力振子——同时预测同宿和异宿分岔的临界参数，方法适用面大幅拓宽
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **论文 Paper**: Li, Z., Tang, J., & Cai, P. (2016). *Predicting Homoclinic and Heteroclinic Bifurcation of Generalized Duffing–Harmonic–van de Pol Oscillator*. Qualitative Theory of Dynamical Systems, 15(1), 19–37.
> **链接 Links**: [精华汇总 PDF](/assets/pdf/essential-summary-p6.pdf) · [DOI](https://doi.org/10.1007/s12346-015-0138-z)

## TL;DR 一句话总结

GHFP 方法从 2013 年 JSV 论文的多项式恢复力，首次**拓展到有理恢复力 $\frac{\lambda x + \delta x^3}{1+\nu x^2}$**——这种恢复力在小振幅下近似为 Duffing 振子、大振幅下退化为线性振子，是振幅相关刚度转变的经典模型。方法在此新问题上成功同时预测了同宿和异宿两种全局分岔，证明了 GHFP 框架的广泛适用性。这是二次广义谐波函数摄动法从"方法提出"走向"方法拓展"的关键一步。

This paper extends the GHFP framework from polynomial restoring forces (JSV 2013) to rational restoring forces for the first time — simultaneously predicting both homoclinic and heteroclinic bifurcations, validating the framework's versatility.

## 研究动机

Duffing–Harmonic 振子 $$\ddot{x} + \frac{\lambda x + \delta x^3}{1 + \nu x^2} = 0$$ 是一个十分特殊但又常见于工程实际的系统：小振幅下近似于 Duffing 振子（$\ddot{x} + \delta x^3 \approx 0$），大振幅下退化为线性谐振子（$\ddot{x} + (\delta/\nu)x \approx 0$）。这种振幅依赖的刚度过渡在高分子材料、微机电系统和隔振装置中具有重要应用。

保守情况下的 Duffing–Harmonic 振子已有大量研究，但其**受迫耗散版本**——广义 Duffing–Harmonic–van de Pol 振子——在 2016 年之前几乎没有非线性动力学的定量研究成果。有理恢复力的引入为解析处理带来了全新的挑战：Fourier 系数的计算从多项式积分变成了含分式的复杂积分。

## 系统模型

广义 Duffing–Harmonic–van de Pol 振子：

$$
\ddot{x} + \frac{\lambda x + \delta x^3}{1 + \nu x^2} = \varepsilon(\mu + \mu_1 x + \mu_2 x^2 + \mu_4 x^4)\dot{x}
$$

其中左侧为有理恢复力（$\lambda$、$\delta$、$\nu$ 为刚度参数），右侧为含 4 项广义 van de Pol 阻尼（位移依赖型），$\mu$ 为控制参数。

## 方法拓展：GHFP 在有理恢复力下的应用

### 同宿轨道

鞍点 $H(h, 0)$ 满足 $g(h) = \frac{\lambda h + \delta h^3}{1 + \nu h^2} = 0$，初始条件 $c$ 由守恒条件 $$\int_h^c \frac{\lambda x + \delta x^3}{1 + \nu x^2} dx = 0$$ 确定。同宿解形式为 $x(t) = a\sin^2\phi(t) + b$，且需满足 $x(\phi_{0, \pi}) = h$。角速度 $\Phi(\phi)$ 在鞍点处满足 $\Phi(0) = \Phi(\pi) = \sqrt{|g(h)/2a|} = 0$——保证无穷周期。

### 异宿轨道

当系统存在两个不同的鞍点时，异宿轨道连接 $h_1$ 和 $h_2$：

$$
x(0) = h_1, \qquad x(\pi/2) = h_2
$$

角速度满足 $\Phi(0) = \Phi(\pi/2) = 0$。异宿解的跨鞍连接需要同时满足两端鞍点的匹配条件——这对方法精度提出了更高的要求。

### 同宿分岔预测公式

一阶一致性条件给出临界参数：

$$
\boxed{\mu_c = -\frac{\int_0^\pi \Phi_0 (\mu_1 x_0 + \mu_2 x_0^2 + \mu_4 x_0^4)(\Phi_0 x_0') x_0' d\varphi}{\int_0^\pi \Phi_0^2 (x_0')^2 d\varphi}}
$$

## 核心结论

### 算例 1：含 $(\mu_1, \mu_2, \mu_4)$ 阻尼的同宿轨道

![同宿轨道 1](/assets/img/publication_preview/p6-fig1-homoclinic.png){: width="70%"}

*Figure 1: (原图 Fig. 1) $\varepsilon=1.2, 2.0$ 时的同宿轨道。实线：Runge–Kutta。虚线：GHFP 方法。有理恢复力下，二次广义谐波函数仍能准确捕捉同宿轨道的鞍点连接形态。*

### 算例 2：多类型同宿轨道共存

![同宿轨道 2](/assets/img/publication_preview/p6-fig2-homoclinic.png){: width="70%"}

*Figure 2: (原图 Fig. 2) $\varepsilon=0.5, 1.0, 1.5, 2.0$ 时的同宿轨道。方法在广泛的参数范围内成功跟踪轨道形态——直至 $\varepsilon=2.0$ 仍保持精度。*

### 算例 3：异宿分岔的预测精度

![异宿轨道](/assets/img/publication_preview/p6-fig4-heteroclinic.png){: width="70%"}

*Figure 3: (原图 Fig. 4) $\varepsilon=0.5, 0.8, 1.0, 2.0$ 时连接两个不同鞍点的异宿轨道。方法以极高的精度捕捉了跨鞍连接的几何形态。*

最关键的定量指标：异宿分岔临界参数 $\mu_c = -0.1979871606$（GHFP 预测）与 $\mu_c^{\text{(numerical)}} = -0.1977132821$（Runge–Kutta 数值结果）之间的相对误差约为 **0.14%**——即使在 2016 年的标准下也是极高的精度水平。

## 5 条核心发现

1. **GHFP 方法首次应用于有理恢复力**：多项式恢复力（JSV 2013）和有理恢复力在数学结构上有本质区别——Fourier 系数的积分从显式多项式变为含分式的积分。方法的成功证明了 GHFP 框架的数学通用性。

2. **同一框架同时预测同宿和异宿分岔**：无需修改方法体系，GHFP 就能同时处理两种类型的全局分岔——这是经典摄动法不具备的能力。

3. **异宿分岔预测精度极高**：$\mu_c$ 的解析预测与数值参考之间的相对误差仅 0.14%，充分体现了方法的数值可靠性。

4. **$\cos^2\varphi$ 和 $\sin^2\varphi$ 的灵活切换**：同宿解用 $\sin^2\varphi$ 形式、异宿解用 $\cos^2\varphi$ 形式——这种基函数的灵活选择是 GHFP 方法在有理恢复力问题上成功的数学关键。

5. **从提出到拓展的关键一步**：这篇论文将 GHFP 方法从一个针对特例（Helmholtz–Duffing）的专门工具，提升为面向**更多类型的恢复力函数和分岔模式**的通用框架——为 MGHFP 系列提供方法论信心。

## 方法的局限

- 一阶摄动限制：在 $\varepsilon > 2$ 时精度可能下降
- 需要预先知道鞍点的解析表达式——这限制了恢复力形式不能过于复杂
- 仅限单自由度分析

## 与系列工作的关系

本文在 GHFP 系列中占据**方法论拓展的关键位置**。如果说 JSV 2013 是"提出了方法"，那么 QTDS 2016 就是"方法通过了更大难度的检验"。从多项式到有理恢复力的跨越，证明了 GHFP 的数学框架并非依赖于特定的 $g(x)$ 形式，而是一个具有**普适性的分析工具**。这一信心的建立是后续 MGHFP 系列（2024–2026）在更复杂系统上持续推进的前提——从 6 项阻尼的 DHRL 振子到含两个无理非线性项的耦合 SD 振子。
