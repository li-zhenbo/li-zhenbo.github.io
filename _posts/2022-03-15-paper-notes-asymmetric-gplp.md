---
layout: post
title: "论文笔记：非对称GPLP——用新逼近式把同异宿轨精度再推高一个台阶"
date: 2022-03-15 10:00:00+0800
description: 在2016年GPLP方法基础上，引入ω参数化的同宿逼近式和Sech-Tanh混合逼近式，将非对称势振子的同异宿解精度提升40–80%
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **论文 Paper**: Li, Z., & Tang, J. (2022). *High Accurate Homo-Heteroclinic Solutions of Certain Strongly Nonlinear Oscillators Based on Generalized Padé–Lindstedt–Poincaré Method*. Journal of Vibration Engineering & Technologies, 10(4), 1291–1308.
> **链接 Links**: [精华汇总 PDF](/assets/pdf/essential-summary-p11.pdf) · [DOI](https://doi.org/10.1007/s42417-022-00446-7)

## TL;DR 一句话总结

2016年的GPLP方法开了一条"零积分摄动"的路，但只处理了对称势。本文引入三个新东西——ω自由参数的Sech逼近式、改进的Tanh逼近式、以及Sech+Tanh混合逼近式——把GPLP从对称势推广到了全五项Φ⁶非对称势和有理恢复力，同宿轨精度提升40–60%，异宿轨精度从5–8%降到1.5%以下。

Building on the 2016 GPLP method, this paper introduces ω-parameterized and combined Sech-Tanh approximants, extending GPLP to asymmetric quintic potentials and rational restoring forces — reducing heteroclinic error from 5–8% to < 1.5%.

## 2016年版本留下了什么空白

2016年的GPLP方法（Nonlinear Dynamics, 2016）解决了一个核心矛盾——摄动法的积分灾难——但它有三个明确的局限：

- 只处理了**奇次项对称势**（$c_1x + c_3x^3 + c_5x^5$，没有 $x^2$ 和 $x^4$）。很多实际的Φ⁶振子天然包含全五项。
- 异宿轨逼近式比较简单（纯Tanh基），在非对称势下精度不够。
- 没有涉及**有理恢复力**（如Duffing-harmonic振子的 $g(x) = \frac{\lambda x + \delta x^3}{1 + \nu x^2}$）。

这篇2022年的论文就是来填这三个坑的。

## 方法核心：三个新逼近式

### 1. ω自由的同宿逼近式

2016年的Sech基逼近式隐含 $\omega = 1$，不给你调的余地：

$$
x(t) = \frac{\sum \alpha_i \, \text{Sech}^i t}{1 + \sum \beta_i \, \text{Sech}^i t}
$$

2022年版本把时间尺度放开了：

$$
\boxed{x(t) = \frac{\sum_{i=0}^{L} \alpha_i \, \text{Sech}^i(\boldsymbol{\omega} t)}{1 + \sum_{i=1}^{M} \beta_i \, \text{Sech}^i(\boldsymbol{\omega} t)}}
$$

$\omega$ 变成了一个额外的自由参数，和 $\alpha_i$、$\beta_i$ 一起从匹配条件解出。这一改，逼近式就能自适应不同形状的势阱——尤其对非对称势左右两阱曲率不一致的情况，改善非常明显（40–60%的误差降低）。

![Φ⁶-VDP相图](/assets/img/publication_preview/p11-fig1.png){: width="70%"}

*Figure 1: 全五项Φ⁶-Van der Pol振子的相图（ε=0）。$x^2$ 和 $x^4$ 的加入使势能不对称，同宿轨和异宿轨的几何结构明显不同。*

### 2. Type A 改进Tanh异宿逼近式

$$
\text{GPA}[L/M]x(t) = \frac{\sum_{i=0}^{L} \alpha_i \, \text{Tanh}^i(\omega t)}{1 + \sum_{i=1}^{M} \beta_i \, \text{Tanh}^i(\omega t)}
$$

同样加入 $\omega$ 自由参数。对纯异宿轨问题够用。

### 3. Type B Sech+Tanh混合逼近式——这才是杀手锏

$$
\boxed{x(t) = \frac{\sum_{i=0}^{L_1} \alpha_i \, \text{Sech}^i(\omega t) + \sum_{j=0}^{L_2} \gamma_j \, \text{Tanh}^j(\omega t)}{1 + \sum_{i=1}^{M_1} \beta_i \, \text{Sech}^i(\omega t) + \sum_{j=1}^{M_2} \delta_j \, \text{Tanh}^j(\omega t)}}
$$

为什么要混搭？因为非对称势里的几何矛盾：

- 较高鞍点的同宿轨天然是**Sech型的**——从两侧对称趋近同一个鞍点
- 连接两个不等高鞍点的异宿轨天然是**Tanh型的**——不对称趋近两个不同鞍点
- 当两者在同一鞍点共存时，纯Tanh逼近（Type A）难以同时捕捉同宿轨的对称性——误差达5–8%
- Type B用Sech+Tanh两个基同时工作，把这一误差降到1.5%以下

这个几何直觉——"逼近式的函数形式要匹配轨道的渐近行为"——贯穿了两篇GPLP论文，也是它们最值得学习的方法论贡献。

![Φ⁶-VDP同宿轨](/assets/img/publication_preview/p11-fig4.png){: width="70%"}

*Figure 4: Φ⁶-VDP振子（63）在不同参数组下的同宿轨（ε=1）。每个子图对应该文Table 4的一行参数。ω参数化逼近式在非对称势下保持了<1%的误差。*

![Φ⁶-VDP同宿轨多参数](/assets/img/publication_preview/p11-fig6.png){: width="70%"}

*Figure 6: 振子（37）在8组不同参数下的同宿轨（ε=1）。系统性的多参数对比验证了方法的鲁棒性。*

## 两类振子的验证

### Φ⁶-Van der Pol（全五项非对称势）

方程：

$$
\ddot{x} + c_1 x + c_2 x^2 + c_3 x^3 + c_4 x^4 + c_5 x^5 = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2)\dot{x}
$$

这是本文的主战场。$c_2$、$c_4$ 非零时势能不对称——左阱和右阱深度不同，左右同宿轨的曲率也不同，异宿轨连接的两个鞍点不等高。GPLP用Type B混合逼近式，对所有情况保持了<1.5%的误差。原文Table 4–8共24组参数的对比数据证实了鲁棒性。

### Duffing-Harmonic-Van der Pol（有理恢复力）

这是GPLP首次进入有理恢复力领域。方程：

$$
\ddot{x} + \frac{\lambda x + \delta x^3}{1 + \nu x^2} = \varepsilon(\mu_c + \mu_1 x + \mu_2 x^2)\dot{x}
$$

测试范围从ε=0.5一直拉到ε=2（这已经不是"弱非线性"了）。GPLP的方法流程无需任何修改——有理恢复力只改变摄动方程里的系数。

![DH-VDP同异宿轨](/assets/img/publication_preview/p11-fig2.png){: width="70%"}

*Figure 2: Duffing-Harmonic-Van der Pol振子的同异宿轨。(a) ε=0.8，(b) ε=1。虚线：GPLP（Type B）。实线：Runge–Kutta。*

![DH-VDP异宿轨](/assets/img/publication_preview/p11-fig8.png){: width="70%"}

*Figure 8: DH-VDP振子在不同参数组合下的异宿轨。系统性的多参数研究验证了GPLP在有理恢复力场景的广泛适用性。*

## 精度对比：2022 vs. 2016

| 场景 | 2016 GPLP 误差 | 2022 GPLP 误差 | 改善 |
|------|:---:|:---:|:---:|
| 对称势 + 小ε | ~1% | ~1% | 持平 |
| 非对称势同宿轨（ε=1） | ~2.5% | <1% | 40–60% |
| 非对称势异宿轨（ε=1） | 5–8% | <1.5% | 70–80% |
| 有理恢复力 | 未涉及 | <2% | — |

## 个人思考

这篇论文是"在一个好框架上做精细改进"的典型案例。2016年的GPLP已经把"零积分摄动"这条路走通了，2022年没有去开辟新路，而是做了三件实实在在的事：让逼近式更灵活（ω参数化）、让异宿轨更精确（Type A/B）、让使用范围更宽（加有理恢复力）。这些改进单独看都"不大"，但合在一起就是一轮实质性的方法升级。

还有一个容易被忽略的贡献：原文系统性地给出了8×3=24组参数的对比数据（Tables 4–8），每组都跟Runge–Kutta对过。这种"工程验收式"的验证在方法论文里不多见，但它恰恰是让读者放心把方法用到自己系统上的关键。

从应用角度，如果你研究的振子涉及**非对称势**（如偏置MEMS梁、非对称吸能器、倾斜弹簧系统），2022版GPLP是更合适的选择——Type B的Sech+Tanh混合逼近式本身就是为非对称设计的。如果你的系统是对称的且非线性不强，2016版已经够用。
