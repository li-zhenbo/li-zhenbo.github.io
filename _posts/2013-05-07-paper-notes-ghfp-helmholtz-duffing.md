---
layout: post
title: "论文笔记：GHFP 方法的提出——Helmholtz–Duffing 振子极限环与同宿轨道的确定"
date: 2013-05-07 10:00:00+0800
description: GHFP 方法的首篇论文：引入二次广义谐波函数与非线性时间变换，统一处理极限环与同宿轨道，首次解析预测同宿分岔参数
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **论文 Paper**: Li, Z., Tang, J., & Cai, P. (2013). *A Generalized Harmonic Function Perturbation Method for Determining Limit Cycles and Homoclinic orbits of Helmholtz–Duffing Oscillator*. Journal of Sound and Vibration, 332(21), 5508–5522.
> **链接 Links**: [精华汇总 PDF](/assets/pdf/essential-summary-p5.pdf) · [DOI](https://doi.org/10.1016/j.jsv.2013.05.007)

## TL;DR 一句话总结

这是 **GHFP 方法（广义谐波函数摄动法）的起点**——提出了一种全新的摄动理论框架：引入二次广义谐波函数 $x = a\cos^2\varphi + b$ 和非线性时间变换，统一处理 Helmholtz–Duffing 振子的极限环确定与同宿轨道预测。核心突破在于——首次用解析方法预测了强非线性振子中同宿分岔的临界参数值。后续所有 GHFP/MGHFP 家族的方法论（2013–2026）都根植于此。

This is the **founding paper** of the GHFP framework: introducing the quadratic generalized harmonic function and nonlinear time transformation for unified treatment of limit cycles and homoclinic orbits — with the first-ever analytical prediction of homoclinic bifurcation parameters.

## 研究动机

Helmholtz–Duffing 振子 $$\ddot{x} + c_1 x + c_2 x^2 + c_3 x^3 = 0$$ 广泛存在于船舶动力学、耳膜振动、单维曲面结构和对称陀螺仪中。不对称二次项 $c_2 x^2$ 打破了经典 Duffing 振子的对称性，引入了质上不同的动力学行为。然而当加入非线性阻尼后，这个振子的极限环和同宿分岔问题**缺乏一个统一的解析处理方法**——经典的摄动法对不对称振子束手无策，而数值打靶法只能提供孤立的参数点，无法给出完整的全局图像。

本文的出发点是：能否从数学上构造一种**天然的适合不对称振子的解形式**，使得摄动程序可以在对称区间上统一执行，从而同时处理极限环和同宿轨道？

## 系统模型

含广义非线性阻尼的 Helmholtz–Duffing 振子：

$$
\ddot{x} + c_1 x + c_2 x^2 + c_3 x^3 = \varepsilon f(\mu, x, \dot{x})
$$

右侧非线性阻尼可为多种形式（位移依赖型、速度依赖型或其组合），$\varepsilon$ 为小参数，$\mu$ 为控制参数。不对称势能面为极限环产生和同宿分岔提供了丰富的结构背景。

## 方法创新：二次广义谐波函数

### 非线性时间变换

核心创新是将时间域的方程转换为角度域的形式：

$$
\frac{d\varphi}{dt} = \Phi(\varphi), \qquad \Phi(\varphi + \pi) = \Phi(\varphi)
$$

这一变换将不对称振子的解问题映射到对称区间 $[0, \pi]$ 上。

### 解的形式构造

GHFP 方法最关键的一步：用**二次广义谐波函数**表示周期运动：

$$
\boxed{x(t) = a \cos^2\varphi(t) + b}
$$

对于同宿轨道，则采用另一种形式：

$$
x(t) = a \sin^2\varphi(t) + b
$$

在经典 GHF 方法中，解的形式是 $x = a\cos\varphi + b$——只能处理对称系统。而 $\cos^2\varphi$ 形式天然包含了二次项 $c_2 x^2$ 引起的不对称性。参数 $a$、$b$ 由保守系统的积分条件 $$\int_{a+b}^b g(u)du = 0$$ 确定（其中 $g(x) = c_1 x + c_2 x^2 + c_3 x^3$）。

### 摄动程序与中心公式

将解参数作摄动展开 $a = a_0 + \varepsilon a_1 + \cdots$、$\Phi = \Phi_0 + \varepsilon \Phi_1 + \cdots$，代入原始微分方程，按 $\varepsilon$ 的幂次等号。关键假设：**$n$ 次近似解保持与生成解相同的函数形式**——这避免了对经典摄动法中冗长积分的依赖。

一阶一致性条件（对 $\varepsilon^1$ 方程在 $[0, \pi]$ 上积分）直接给出了同宿分岔临界参数：

$$
\boxed{\mu_c = -\frac{\int_0^\pi \Phi_0 f_0(\mu, x_0, \Phi_0 x_0') x_0' d\varphi}{\int_0^\pi \Phi_0 \frac{\partial f_0}{\partial \mu} x_0' d\varphi}}
$$

这是 GHFP 方法的中心结果——此前，强非线性振子中的同宿分岔参数只能靠数值打靶法获得。

## 核心结论

### 算例 1：极限环全局演化（$c_1=1$, $c_2=0.5$, $c_3=1$）

$$\ddot{x} + x + 0.5x^2 + x^3 = \varepsilon(\mu + \mu_1 x + \mu_2 x^2)\dot{x}$$

![极限环相图](/assets/img/publication_preview/p5-fig1-limitcycle.png){: width="70%"}

*Figure 1: (原图 Fig. 1) 不同摄动参数下振子的极限环。实线：Runge–Kutta 数值法。虚线：GHFP 方法。$\varepsilon=0.1, 0.3, 0.5, 1$ 四种情况下均能准确匹配。*

即便在 $\varepsilon=1$（并非小参数）时，GHFP 方法的解析解仍与数值结果高度吻合——说明该方法具有超出预期的适用范围。

### 算例 2：同宿轨道与分岔预测（$c_1=1$, $c_2=-1$, $c_3=2$）

$$\ddot{x} + x - x^2 + 2x^3 = \varepsilon(\mu + \mu_2 x^2)\dot{x}$$

该振子在 $x=0$ 处有一个鞍点，势能面支撑同宿分岔。

![同宿轨道](/assets/img/publication_preview/p5-fig5-homoclinic.png){: width="70%"}

*Figure 2: (原图 Fig. 5) $\varepsilon=1, 2$ 时的同宿轨道。实线：Runge–Kutta。虚线：GHFP 方法。即使在 $\varepsilon=2$ 的大扰动下，方法仍能准确捕捉同宿轨道的几何形态。*

GHFP 方法预测的同宿分岔参数与数值结果之间的误差极小，这是首次用解析方法实现这一预测。

## 5 条核心发现

1. **二次广义谐波函数的首次提出**：$x = a\cos^2\varphi + b$（而非经典的一阶 $a\cos\varphi + b$）是不对称振子正确的基函数选择——这一洞见是整个 GHFP 家族的数学根基。

2. **非线性时间变换的统一框架**：同一个方法框架同时处理局部（极限环）和全局（同宿/异宿）动力学现象，无需切换分析工具。

3. **首次解析同宿分岔预测**：GHFP 方法的中心公式让强非线性振子中同宿分岔参数的解析预测成为可能——此前只能用数值打靶法。

4. **远超预期的精度范围**：方法给出的精度范围远超小参数的常规限制（$\varepsilon$ 可达 $1$–$2$）。

5. **GHFP 家族的方法论源头**：本文建立的框架是后续所有 GHFP/MGHFP 工作的摇篮——从 2016 年的有理恢复力拓展到 2024–2026 年的符号化改进。

## 方法的局限

- 摄动精度限制在一阶（$\varepsilon^1$），对更大扰动振幅或特殊参数区域精度不够
- 假设非线性阻尼较小（$\varepsilon \ll 1$），强阻尼系统需要另寻他法
- 仅限单自由度振子，多自由度推广仍是开放问题

## 与系列工作的关系

本文是整个 GHFP/MGHFP 系列的**理论基石**。从方法论角度看，这篇论文确立了三个核心要素：二次广义谐波函数解形式、非线性时间变换、一阶一致性条件。这三者在此后的所有工作中一以贯之——2016 年的 QTDS 论文将框架推广到有理恢复力，2024–2026 年的 MGHFP 系列通过引入复合 Simpson 积分实现了纯符号化执行。对于做非线性摄动方法的同行，这篇论文中的**基函数选择策略**和**非对称系统对称化处理**的思想，值得细读。
