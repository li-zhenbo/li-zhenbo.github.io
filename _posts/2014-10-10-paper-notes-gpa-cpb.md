---
layout: post
title: "论文笔记：广义Padé逼近方法的英文推广——同宿和异宿轨道的统一求解框架"
date: 2014-10-10 10:00:00+0800
description: GPA方法的英文版，首次同时处理同宿和异宿轨道，在三种不同类型振子上验证了方法的精度和广泛适用性
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **论文 Paper**: Li, Z., Tang, J., & Cai, P. (2014). *A Generalized Padé Approximation Method of Solving Homoclinic and Heteroclinic Orbits of Strongly Nonlinear Autonomous Oscillators*. Chinese Physics B, 23(12), 120501.
> **链接 Links**: [精华汇总 PDF](/assets/pdf/essential-summary-p8.pdf) · [DOI](https://doi.org/10.1088/1674-1056/23/12/120501)

## TL;DR 一句话总结

在 2013 年力学学报 GPA 方法的基础上，这篇论文做了两个重要推广：(1) 将方法从同宿轨**拓展到异宿轨**——通过构造基于 $\tanh^i t$ 的新型逼近式；(2) 在 **cubic–quintic Duffing、$\Phi^6$ 势、Duffing-harmonic 三种完全不同类型的振子**上验证了方法的广泛适用性。这是 GPA 方法的英文版正式发表，也是首次建立了同宿/异宿轨道统一求解的计算框架。

This is the English version of the GPA method — extending from homoclinic to heteroclinic orbits via a $\tanh^i t$-based approximant, and validated across three fundamentally different oscillator classes.

## 研究动机

2013 年力学学报的 GPA 方法主要针对同宿轨道，且算例集中在多项式恢复力的振子。本文在三个方向上进行了本质性的拓展：(1) 将方法推广到异宿轨道的求解；(2) 在复杂的 $\Phi^6$ 势振子（五项非对称多项式）上检验方法的性能；(3) 系统论证 GPA 相对于经典 Padé 逼近的精度优势。

## 方法创新：两种新型逼近式

### 同宿轨

基于 $\operatorname{sech}^i t$ 的广义 Padé 逼近式（与 2013 年论文相同）：

$$
\boxed{\text{GPA}_{\text{hom}}[L/M] = \frac{\sum_{i=0}^{L} \alpha_i \operatorname{sech}^i t}{1 + \sum_{i=1}^{M} \beta_i \operatorname{sech}^i t}}
$$

### 异宿轨（新提出）

针对连接两个不同鞍点 $h_1$ 和 $h_2$ 的异宿轨道，构造基于 $\tanh^i t$ 的逼近式：

$$
\boxed{\text{GPA}_{\text{het}}[L/M] = \frac{\sum_{i=0}^{L} \alpha_i \tanh^i t}{1 + \sum_{i=1}^{M} \beta_i \tanh^i t}}
$$

$\tanh^i t$ 自然满足两端不同的边界条件 $x(-\infty)=h_1, x(+\infty)=h_2$（因为 $\tanh(\pm\infty)=\pm1$），无需额外约束。

**求解流程**：(1) 将 $x(t) = \sum a_i t^i$ 代入 $\ddot{x}+g(x)=0$ 求幂级数系数；(2) 由能量积分 $\int_h^a g(x)dx=0$ 确定振幅初值；(3) GPA 在 $t=0$ 处展开为 Taylor 级数，与幂级数匹配系数——得到 $L+M$ 个线性方程加 1 个非线性方程，标准数值求解。

## 核心算例

### 算例 1: Cubic–Quintic Duffing 振子

$$\ddot{x} + c_1 x + c_3 x^3 + c_5 x^5 = 0, \qquad c_1=2, c_3=-10, c_5=9$$

系统有 5 个不动点（3 个中心、2 个鞍点），同时存在两条同宿轨（绕两个外围中心）和一对异宿轨（连接两个鞍点）。GPA[$4/4$] 捕捉同宿轨，GPA[$7/7$] 捕捉异宿轨——这是**首次在同一系统中同时获得同宿和异宿解的 GPA 应用**。

![同宿和异宿轨相图](/assets/img/publication_preview/p8-fig1.png){: width="70%"}

*Figure 1: (Original Fig. 1) Homoclinic and heteroclinic orbits of the cubic–quintic Duffing oscillator. Solid: Runge–Kutta. Dotted: GPA method.*

### 算例 2: $\Phi^6$ 势振子

$$\ddot{x} + c_1 x + c_2 x^2 + c_3 x^3 + c_4 x^4 + c_5 x^5 = 0$$

五项不对称多项式保守系统，参数 $c_1=c_3=c_5=1, c_2=c_4=-1.5$ 时三个鞍点同时支持同宿和异宿轨道。**GPA 在同阶逼近下精度显著高于经典 Padé 逼近**——论文中的 Fig. 3 对比了两种逼近方法与 Runge–Kutta 的吻合程度，GPA 的优势清晰可见。

![Phi-6振子相图](/assets/img/publication_preview/p8-fig3.png){: width="70%"}

*Figure 2: (Original Fig. 3) Homoclinic and heteroclinic orbits of the $\Phi^6$ oscillator. Solid: Runge–Kutta. Dotted: GPA. Dashed: classical Padé approximant.*

### 算例 3: 广义 Duffing–Harmonic 振子

$$\ddot{x} + \frac{\lambda x + \mu x^3}{1 + \nu x^2} = 0$$

这是有理恢复力振子的标准 benchmark。$\lambda=-1, \mu=5, \nu=5$：GPA[$3/3$] 捕捉两条同宿轨。$\lambda=3, \mu=-5, \nu=2$：GPA[$8/8$] 捕捉异宿轨。该振子的精确解不存在于初等函数中——而 GPA 对有理分式恢复力的处理与多项式无本质区别。

![同宿轨相图](/assets/img/publication_preview/p8-fig4.png){: width="70%"}

*Figure 3: (Original Fig. 4) Homoclinic orbits for $\lambda=-1, \mu=5, \nu=5$. Solid: Runge–Kutta. Dotted: GPA[$3/3$].*

![异宿轨相图](/assets/img/publication_preview/p8-fig5.png){: width="70%"}

*Figure 4: (Original Fig. 5) Heteroclinic orbits for $\lambda=3, \mu=-5, \nu=2$. Solid: Runge–Kutta. Dotted: GPA[$8/8$].*

## 5 条核心发现

1. **首次同宿—异宿统一框架**：$\operatorname{sech}^i t$ / $\tanh^i t$ 双逼近式组合在 GPA 框架下实现了同宿和异宿轨道的统一计算架构。

2. **精度碾压经典 Padé**：同阶逼近下，GPA 的精度显著高于多项式基的经典 Padé 逼近——经典 Padé 用多项式拟合指数衰减，天然效率低下。

3. **$\Phi^6$ 势振子的解析求解**：五项不对称多项式振子的同宿/异宿轨道被首次解析获得，证明了 GPA 对高阶多项式恢复力的处理能力。

4. **基函数选择的普适意义**：$\operatorname{sech}^i t$（同宿）和 $\tanh^i t$（异宿）的选择并非特例——任何能够自然满足边界条件的基函数都可纳入 GPA 框架。

5. **与 GHFP/MGHFP 的方法论对比**：GPA 在时域直接构造轨道解，GHFP 在角域通过摄动推导参数关系——两条线共享有理函数逼近的数学内核。

## 方法的局限

- 仅适用于保守系统（$\varepsilon=0$）
- 高逼近阶数时系数匹配的代数方程组可能变为病态
- 单自由度自治振子

## 与系列工作的关系

本文与 2013 年力学学报论文共同构成了 GPA 方法的中英文双篇奠基。在 GHFP/MGHFP 系列之外，GPA 代表了处理强非线性振子全局轨道的另一条解析路线。两种方法的基函数选择策略——GPA 的 $\operatorname{sech}/\tanh$ 和 GHFP 的 $\cos^2\varphi/\sin^2\varphi$——体现了同一批作者在不同数学框架下对非线性振动问题的持续探索。
