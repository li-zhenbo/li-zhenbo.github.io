---
layout: post
title: 论文笔记：余弦广义Padé逼近法——用周期性的逼近式直接求解周期解
date: 2019-11-18 10:00:00+0800
description: 构造余弦型广义Padé逼近式，通过双重改进求解流程，直接求得强非线性振子的解析周期解
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **论文 Paper**: Li, Z., & Tang, J. (2019). *A Cosine Generalized Padé Approximation Method and Its Application in Solving Periodic Solutions of Strongly Nonlinear Oscillators*. Journal of Vibration and Shock, 38(22), 159–167.
> **链接 Links**: [精华汇总 PDF](/assets/pdf/essential-summary-p9.pdf) · [DOI](https://doi.org/10.13465/j.cnki.jvs.2019.22.023)

## TL;DR 一句话总结

将经典Padé逼近的分子分母从多项式推广为余弦函数级数，使得逼近式本身具有周期性——从而让Padé逼近方法首次能够直接用于求解强非线性振子的周期解，并在Duffing、Duffing-harmonic和SD振子上全部验证通过。

A cosine-function-series generalized Padé approximant with built-in periodicity enables, for the first time, the direct Padé approximation of periodic solutions for strongly nonlinear oscillators — validated on Duffing, Duffing-harmonic, and SD oscillators.

## 背景：为什么Padé逼近不能直接求周期解

经典Padé逼近用有理函数（多项式之比）去逼近一个幂级数，得到的逼近式通常在无穷远处有极限——是有理函数的固有性质。而周期解是周而复始的，不存在极限。所以，经典Padé逼近和一众"类Padé"改进方案，天然不适配周期轨道的求解。此前没有任何文献直接用Padé逼近来求周期解。

作者在前期工作中提出了**广义Padé逼近（GPA）方法**，将分子和分母从多项式推广到任意连续函数构成的函数级数。本文在此基础上更进一步：构造了一类**分子和分母均由余弦函数级数组成**的广义Padé逼近式。余弦函数天生是周期的，因此整个逼近式也是周期的——这就从根本上解决了"用Padé逼近求周期解"的矛盾。

## 广义逼近式的构造

余弦型广义Padé逼近式形如：

$$
x(t) = \frac{\sum_{i=0}^{m} \alpha_i \cos(i\omega t)}{\sum_{j=0}^{n} \beta_j \cos(j\omega t)}
$$

其中 $\omega$ 为广义Padé角频率（待定），$\alpha_i$、$\beta_j$ 由逼近条件确定。

## 两次关键改进

直接把这个逼近式套进经典Padé流程会出问题——因为角频率 $\omega$ 未知，待求量变成非线性耦合的，求解困难。于是本文提出了两种改进方案。

### 改进一：频率主动迭代

把 $\omega$ 从"待求未知数"升级为**主动变量**，以增量 $\Delta\omega$ 步进迭代。从初值 $\omega_0$ 开始，每步求解一套 $\alpha_i$、$\beta_j$。用一个目标函数 $\Gamma = x(\pi/\omega) - x_1$（$x_1$ 是轨道与 $x$ 轴的另一交点）判定是否终止。当 $\vert\Gamma\vert < 10^{-(p+4)}$ 时迭代结束，此时的 $\alpha_i$、$\beta_j$ 和 $\omega$ 就是所求的逼近参数。该方案对多项式势能（Duffing）的振子效果很好。

### 改进二：导数型目标函数 + 分段描述

对于有理函数恢复力（如Duffing-harmonic振子的 $\frac{x+x^3}{1+x^2}$），某些较大周期的轨道用改进一的精度不够。改进二的核心变化：把目标函数换成**半周期处的导数值**——即轨道与坐标轴交点处的速度分量：

$$
\Gamma_2 = \left.\frac{dx}{dt}\right|_{t=\pi/\omega} - y_1
$$

其中 $y_1$ 是轨道在负半轴交点的纵坐标。此外，对解做分段描述，在半周期处进行衔接，进一步提升了逼近精度。

## 三类系统的结果

![Duffing振子的相图和时间历程](/assets/img/publication_preview/p9-fig1.png){: width="70%"}

*图1–3: Duffing振子（多项式恢复力），$A=2$。相图（左）、时间历程（中）、绝对误差（右），误差低于 $10^{-3}$。*

---

![Duffing-harmonic振子](/assets/img/publication_preview/p9-fig7.png){: width="70%"}

*图7–9: Duffing-harmonic振子（有理恢复力），$A=3$。改进二方案处理有理恢复力同样有效。*

---

![SD振子](/assets/img/publication_preview/p9-fig13.png){: width="70%"}

*图13: SD振子（无理恢复力），$\alpha=1$，$A=2.5$。对含几何约束的无理非线性项保持高精度。*

---

![SD振子大振幅轨道](/assets/img/publication_preview/p9-fig16.png){: width="70%"}

*图16: SD振子大振幅轨道，$\alpha=0.5$，$A=3$，$\beta=2$。方法精度不受初始振幅和非线性系数大小影响。*

## 方法特点

- **继承了Padé逼近的简洁性**：从幂级数解出发，构造逼近式、比较系数、解方程组——整个流程简单直接，适合编程实现
- **精度不受非线性强弱影响**：Duffing（弱非线性）和SD振子（强非线性+无理项）的误差同级
- **适用范围广**：不限于某个特定系统，多项式、有理函数、无理函数三种恢复力类型全覆盖
- **能预测周期**：逼近式同时给出了 $\omega$，由此可得解析周期 $T = 2\pi/\omega$

## 与前序工作的关系

这篇论文是作者团队在广义Padé逼近方向的第三篇工作。前两篇——广义Padé逼近提出（力学学报, 2013）和推广到同异宿轨（Chin. Phys. B, 2014）——处理的都是非周期解（同宿/异宿轨，本质上仍是"有极限"的逼近对象）。本文把GPA的能力范围从"有极限"拓展到"周期性"，完成了该方法在振动领域应用的重要拼图。

## 个人思考

这篇文章的思路很有启发性——它没有去"改公式"来适配问题，而是去"改问题的数学结构"来适配方法。经典Padé逼近不是不能求周期解吗？那就构造一个本身就是周期的逼近式。这种思路在方法学上值得借鉴。

实际工程中涉及周期轨道的场景远比同异宿轨道多——转子动力学、MEMS谐振器、能量采集器、隔振器等等。余弦GPA为这些系统提供了一种精度可控、流程简洁的解析近似手段，相比纯粹的数值方法，它能给出连续的系统参数—周期—振幅关系，这对参数设计和灵敏度分析很重要。
