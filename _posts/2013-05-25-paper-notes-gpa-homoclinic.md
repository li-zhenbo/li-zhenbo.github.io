---
layout: post
title: "论文笔记：广义Padé逼近方法的提出——双曲函数构造逼近式求解强非线性振子同宿轨"
date: 2013-05-25 10:00:00+0800
description: 在经典Padé逼近理论基础上提出广义Padé逼近（GPA）方法，利用双曲函数构造新逼近式求解同宿轨道
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **论文 Paper**: 李震波, 唐驾时, 蔡萍. (2013). *求强非线性自治振子同宿轨的广义Padé逼近方法*. 力学学报, 45(3), 461–464.
> **链接 Links**: [精华汇总 PDF](/assets/pdf/essential-summary-p7.pdf) · [DOI](https://doi.org/10.6052/0459-1879-12-277)

## TL;DR 一句话总结

在经典Padé逼近理论的基础上进行了**理论推广**——将逼近式的分子分母从多项式函数推广到任意函数的级数形式，并利用双曲函数构造了一种新的广义Padé逼近式，在求解强非线性自治振子同宿解时具有计算简便、精度高、适用范围广的优点。这是广义Padé逼近（GPA）方法的首次公开发表，其英文推广版随后发表于 Chinese Physics B (2014)。

This is the **first publication** of the Generalized Padé Approximation (GPA) method, extending the classical Padé framework from polynomial to arbitrary-function bases. A hyperbolic-function approximant is constructed for solving homoclinic orbits of strongly nonlinear autonomous oscillators.

## 研究动机

求解非线性振子的同宿轨在全局分岔、混沌和孤立波研究中至关重要。经典Padé逼近方法已被用于构造同宿解，但其分子分母被限制为多项式函数——这一约束限制了逼近式对同宿轨指数衰减行为的拟合灵活度。现有改进（类Padé逼近、指数函数Padé等）都是个案式的，缺乏一个统一的理论框架。

本文的出发点是：**将Padé逼近的定义从数学上进行推广**，使逼近式的分子分母可以是任意函数的级数，从而可以针对同宿轨的特性灵活选择基函数。

## 方法创新：广义Padé逼近

### 经典Padé逼近

对形式幂级数 $f(z) = \sum_{i=0}^{\infty} a_i z^i$，其 $[L/M]$ 阶Padé逼近式为有理分式 $P_L(z)/Q_M(z)$（$P_L$、$Q_M$ 为多项式），满足：

$$
f(z) - \frac{P_L(z)}{Q_M(z)} = \mathcal{O}(z^{L+M+1}), \qquad Q_M(0)=1
$$

### 广义Padé逼近的定义

将分子分母的空间从多项式 $H_m$ 推广到**任意函数的级数**构成的 $\widehat{H}_m$：

$$
\boxed{\widehat{H}_m = \left\{P : P(z) = \sum_{i=0}^m a_i g_i(z)^i, \; g_i: \mathbb{C}\to\mathbb{C}, \; a_i \in \mathbb{C}\right\}}
$$

$G(m,n) = \{R = P/Q : P \in \widehat{H}_m, Q \in \widehat{H}_n\setminus\{0\}\}$。若存在 $P_L/Q_M \in G(L,M)$ 满足相同的 $\mathcal{O}(z^{L+M+1})$ 条件，则称其为**广义Padé逼近式**，记为 GPA[$L/M$]$_f$。

当 $g_i(z)=z^i$（经典多项式基），GPA 退化为经典Padé逼近。所有已有的类Padé逼近改进都可以归为GPA的特例。

### 同宿轨的构造

对自治振子 $\ddot{x} + g(x) = 0$，首先将解展开为幂级数 $x(t) = \sum a_i t^i$。对于通过鞍点 $H(h,0)$ 的同宿轨，由能量积分 $\int_h^a g(x)dx = 0$ 确定初值。关键创新：用**双曲函数**构造GPA逼近式：

$$
\boxed{\text{GPA}[L/M] = \frac{\sum_{i=0}^{L} \alpha_i \operatorname{sech}^i t}{1 + \sum_{i=1}^{M} \beta_i \operatorname{sech}^i t}}
$$

$\operatorname{sech}^i t$ 的选择有三重优势：(1) 其 Taylor 展开比指数函数简单，减少匹配计算量；(2) 自动满足边界条件 $x(\pm\infty) = h$；(3) $g(x)$ 为任意多项式或有理函数时均可适用。

## 核心算例

### 算例 1: Helmholtz–Duffing 振子 ($c_1 = -3, c_2 = 100$)

$$\ddot{x} + c_1 x + c_2 x^2 = 0$$

在 $c_2 = 100 \gg 1$ 的强不对称非线性下，取 $L=M=2$：

$$\text{GPA}[2/2] = \frac{0.005\operatorname{sech} t + 0.07\operatorname{sech}^2 t}{1 + 0.611111\operatorname{sech} t + 0.055555\operatorname{sech}^2 t}$$

解析解与 Runge–Kutta 数值解吻合极好。

![同宿轨相图](/assets/img/publication_preview/p7-fig1.png){: width="70%"}

*Figure 1: (Original Fig. 1) Homoclinic orbit of the Helmholtz–Duffing oscillator with $c_1=-3, c_2=100$. Solid: Runge–Kutta. Dotted: GPA[$2/2$].*

### 算例 2: Helmholtz–Duffing 振子 ($c_1 = -2, c_2 = 5, c_3 = 15$)

$$\ddot{x} + c_1 x + c_2 x^2 + c_3 x^3 = 0$$

$L=M=2$ 同时获得鞍点左右两侧的同宿轨，展示了方法对不对称三次—二次非线性的处理能力。

![同宿轨相图](/assets/img/publication_preview/p7-fig2.png){: width="70%"}

*Figure 2: (Original Fig. 2) Homoclinic orbits for $c_1=-2, c_2=5, c_3=15$. Solid: Runge–Kutta. Dotted: GPA[$2/2$].*

### 算例 3: Duffing–Harmonic 振子

$$\ddot{x} + \frac{\lambda x + \mu x^3}{1 + \nu x^2} = 0, \quad \lambda=-1, \mu=1, \nu=1$$

$L=M=3$ 的 GPA 成功捕捉了有理恢复力振子的同宿轨——该系统的精确解无法用初等函数或经典椭圆函数表示。

![同宿轨相图](/assets/img/publication_preview/p7-fig3.png){: width="70%"}

*Figure 3: (Original Fig. 3) Homoclinic orbits of the Duffing-harmonic oscillator. Solid: Runge–Kutta. Dotted: GPA[$3/3$].*

## 5 条核心发现

1. **GPA 的定义统一了所有 Padé 类方法**：经典 Padé、类 Padé（Mikhlin 1995）、指数函数型逼近（Manucharyan & Mikhlin 2005）、改进 Padé（张琪昌等 2011）均可归为 GPA 的特例。

2. **基函数的灵活选择是关键**：针对同宿轨的指数衰减特性选择 $\operatorname{sech}^i t$ 基，同时兼顾了边界条件自动满足和泰勒展开简洁性。

3. **有理恢复力振子无障碍**：GPA 对有理分式 $g(x) = (\lambda x + \mu x^3)/(1+\nu x^2)$ 的处理与多项式 $g(x)$ 无本质区别。

4. **与 GHFP 方法的关系**：GPA 和 GHFP 代表了处理强非线性振子的两条互补路线。$\operatorname{sech}^i t$ 基函数的思想后来也出现在 GHFP 的同宿轨构造 $x = a\sin^2\varphi + b$ 中。

5. **方法简洁性**：仅需求解 $L+M+1$ 个代数方程，相比于经典摄动方法更直接。

## 方法的局限

- 仅适用于保守系统（$\varepsilon = 0$）
- 逼近阶数 $L=M$ 需经验选择，无先验误差界
- 单自由度自治振子

## 与后续工作的关系

本文的英文扩展版发表于 Chinese Physics B (2014)，将方法推广到异宿轨道并增加了更多算例系统。该系列是 GHFP/MGHFP 方法体系的平行发展路线，共同构成了强非线性振子解析方法的工具集。
