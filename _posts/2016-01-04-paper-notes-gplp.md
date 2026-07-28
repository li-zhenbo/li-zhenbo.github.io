---
layout: post
title: "论文笔记：广义Padé–Lindstedt–Poincaré方法——用逼近替代积分的摄动新技术"
date: 2016-01-04 10:00:00+0800
description: 将广义Padé逼近引入Lindstedt–Poincaré流程，用系数匹配替代所有积分运算，实现了无需积分的高阶同异宿分岔预测
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **论文 Paper**: Li, Z., & Tang, J. (2016). *A Generalized Padé–Lindstedt–Poincaré Method for Predicting Homoclinic and Heteroclinic Bifurcations of Strongly Nonlinear Autonomous Oscillators*. Nonlinear Dynamics, 84(3), 1201–1223.
> **链接 Links**: [精华汇总 PDF](/assets/pdf/essential-summary-p10.pdf) · [DOI](https://doi.org/10.1007/s11071-015-2563-6)

## TL;DR 一句话总结

传统摄动法每算一阶解就要推一次导、积一次分——对复杂振子是灾难。本文把广义Padé逼近塞进Lindstedt–Poincaré框架，用"构造逼近式→匹配系数→求解代数方程"替换了全部积分步骤，在无需任何积分的条件下做到了三阶精度，连ε=50的同宿轨都算得准。

The GPLP method replaces every integration step in the Lindstedt–Poincaré procedure with generalized Padé coefficient matching — achieving third-order accuracy on homoclinic/heteroclinic bifurcations without any integration, accurate even at ε = 50.

## 问题：为什么传统摄动法吃不消复杂振子

考虑最一般的非线性振子：

$$
\ddot{x} + g(x) = \varepsilon f(x, \dot{x})
$$

要预测它的同宿/异宿（H/H）分岔，有两类方法：

- **摄动法家族**（HP、HLP、椭圆L–P、GHFP）：体系完整，精度可靠。但每升高一阶就要对前面所有阶的结果求导、积分——$g(x)$ 是高阶多项式或有理函数时，这些积分很快就不可计算。
- **Padé逼近家族**：不需要积分，直接构造有理函数逼近。但只适用于保守系统（$\varepsilon = 0$），不能处理阻尼。

有没有一种方法，既保留摄动法的系统框架，又避开积分的灾难？这就是GPLP方法的出发点。

## 方法核心：三种逼近式，四种解法，零积分

### 广义Padé逼近

首先把经典Padé的定义做了推广：分子分母从多项式函数 $P(z) = \sum a_i z^i$ 推广到**任意连续函数构成的级数**：

$$
P(z) = \sum_{i=0}^m a_i \, g_i(z), \qquad g_i: \mathbb{C} \to \mathbb{C}
$$

$g_i$ 可以是 Sech$^i$、Tanh$^i$、多项式……想用什么用什么。这个推广让经典Padé和所有已知的quasi-Padé变体都变成特例。

![势能与同宿轨](/assets/img/publication_preview/p10-fig1.png){: width="70%"}

*Figure 1: Helmholtz–Duffing振子的势能曲线与同宿轨。三次不对称势能产生两个同宿轨，关于x轴对称但关于\(\dot{x}\)轴不对称。*

### 四步GPLP流程

与经典L–P一样，把解和分岔参数按ε展开：

$$
x = \sum_{n=0}^{\infty} \varepsilon^n x_n, \qquad \mu_c = \sum_{n=0}^{\infty} \varepsilon^n \mu_{cn}
$$

得到一组摄动方程（21）–（24）。关键差异在于每一步怎么解：

**Step I（零阶 $x_0$）**：从保守方程 $\ddot{x}_0 + g(x_0) = 0$ 出发，推导 $x_0$ 的幂级数 $\sum a_i t^i$。然后构造Sech基的广义Padé逼近式：

$$
\text{GPA}[4/4]x_0(t) = \frac{\sum_{i=0}^4 \alpha_i \, \text{Sech}^i t}{1 + \sum_{i=1}^4 \beta_i \, \text{Sech}^i t}
$$

为什么用Sech？因为同宿轨的边界条件 $x(\pm\infty) = h_i$ 天然对应双曲正割的渐近行为。把逼近式Taylor展开后与幂级数逐项匹配，解出 $\alpha_i$、$\beta_i$——不需要任何积分。

**Step II（一阶 $x_1$ 和 $\mu_{c0}$）**：对 $x_1$ 构造带Tanh前缀的逼近式：

$$
\text{GPA}[L_1/M_1]x_1(t) = \text{Tanh}(t) \, \frac{\sum \eta_i t^i}{1 + \sum \xi_i t^i}
$$

Tanh前缀天然保证 $x_1(\pm\infty) = 0$。令 $\eta_{L_1}(\mu_{c0}) = 0$ 即得零阶分岔参数 $\mu_{c0}$。

**Step III–IV**：二阶和三阶用多项式基的逼近式，构造相似但不冗余。最终结果：

$$
\boxed{x(t) = \sum_{i=0}^{3} \varepsilon^i \, \text{GPA}[L_i/M_i]x_i(t) + O(\varepsilon^4)}, \qquad
\boxed{\mu_c = \mu_{c0} + \varepsilon^2 \mu_{c2} + O(\varepsilon^3)}
$$

整个过程没有一次积分——全部是"构造逼近式→Taylor展开→匹配系数→解代数方程组"。

### 为什么用三种不同的逼近式？

这不是拍脑袋的。$x_0$ 用Sech/Tanh基是因为它们精确满足H/H轨道的渐近边界条件。$x_1$ 需要自带 $x_1(\pm\infty)=0$ 的约束——Tanh前缀天然满足。$x_2$、$x_3$ 用多项式基则是因为低阶解已经把渐近条件嵌进去了，多项式在系数匹配上更简洁。论文中的Example 5专门比较了"全用同一种逼近式"和"混合策略"，结论是混合策略精度显著更高。

![同宿轨](/assets/img/publication_preview/p10-fig2.png){: width="70%"}

*Figure 2: Helmholtz–Duffing–Van der Pol振子的同宿轨。(a) ε=2，(b) ε=3。实线：Runge–Kutta。虚线：GPLP（三阶）。*

## 四类振子的验证

### Helmholtz–Duffing–Van der Pol（三次不对称）

方程：$\ddot{x} - 2x + 5x^2 + 5x^3 = \varepsilon(\mu_c + x + x^2)\dot{x}$

鞍点 $H_2(0,0)$，两个不对称同宿轨。GPA[4/4]零阶解：

$$
x_0(t) = \frac{0.0814\,S + 3.2534\,S^2 + 16.0572\,S^3 + 16.8002\,S^4}{1 + 14.2944\,S + 39.3405\,S^2 + 22.9087\,S^3 + 566.4437\,S^4}, \quad S = \text{Sech}\,t
$$

分岔参数 $\mu_{c0} \approx -6.3941$。精度：$\varepsilon=2$、3时仍低于1%，甚至$\varepsilon=50$、60的SD振子变体也准确。

### Duffing-harmonic（有理恢复力）

$\ddot{x} + \frac{-5x + 5x^3}{1 + 5x^2} = \varepsilon(\mu_c + x + x^2)\dot{x}$，$\mu_{c0} = -1.9026$。GPLP对有理恢复力无需任何方法修改——变的只是摄动方程里的系数。

### SD振子（无理恢复力）

即使 $\varepsilon=50$、60，三阶GPLP解仍然与Runge–Kutta高度吻合。这是因为零阶GPA解已经非常接近精确保守轨，高阶修正只需"微调"。

![SD振子同宿轨](/assets/img/publication_preview/p10-fig3.png){: width="70%"}

*Figure 4: SD振子的同宿轨。(a,b) ε=50，(c,d) ε=60。实线：Runge–Kutta。虚线：GPLP。注意扰动参数之大——两个数量级超过典型的"弱非线性"区间。*

### Φ⁶-Van der Pol（五次多项式，同异宿共存）

$\ddot{x} + c_1 x + c_3 x^3 + c_5 x^5 = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2)\dot{x}$。五次势能在同一鞍点同时支持同宿和异宿轨道，GPLP一次性预测两个分岔参数。这个能力以前没有分析工具做到过。

## 个人思考

这篇文章的方法学价值大于任何单个算例。它的核心洞察是：**摄动法最痛苦的部分（积分）是可以被替换的**——只要你能针对每一步的数学结构，构造一个合适的逼近式。

这个思想对做方法研究的人有两个启发：

第一，Padé逼近的"泛化"潜力远超经典定义。把分子分母从多项式推广到任意连续函数——这扇门一打开，Sech/Tanh基用于H/H轨道只是第一个应用场景。周期解（余弦基）、准周期解（混合基）、衰减振荡（指数+三角基）理论上都可以用同样的框架构造。

第二，"零积分摄动"可以在很多传统摄动法上复现。椭圆L–P方法的积分步骤能不能也用GPA替代？多尺度方法的长期项消除能不能转化为逼近问题？这篇论文开启了一类新思路。

工程上，GPLP相比纯数值方法的优势是解析性：分岔参数 $\mu_c$ 是以代数表达式给出的，可以系统地研究它如何随系统参数变化——而纯数值方法需要为每一组参数跑一次数值延拓。这个差异在参数空间维度高的时候是数量级的差距。

需要注意的是，GPLP不适用于"追踪连续参数依赖"的场景——系统参数必须在计算前设好，不像代数类方法（如MGHFP）那样能导出参数空间里的完整解析关系。它和MGHFP是互补的，一个适合高精度单点求解，一个适合全局参数分析。
