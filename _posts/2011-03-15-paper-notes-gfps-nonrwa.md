---
layout: post
title: "论文笔记：参数未知的两类不同超混沌系统广义函数投影同步——基于反对称结构的自适应控制"
date: 2011-03-15 11:00:00+0800
description: 结合自适应控制理论与反对称结构，设计更广义更简洁的控制器，实现参数完全未知的超混沌Chen系统与Lorenz系统广义函数投影同步
tags: [paper-notes]
categories: [notes]
featured: true
toc:
  sidebar: left
---

> **论文 Paper**: 李震波, 赵小山. (2011). *Generalized function projective synchronization of two different hyperchaotic systems with unknown parameters*. Nonlinear Analysis: Real World Applications, 12(5), 2607–2615.
> **链接 Links**: [精华汇总 PDF](/assets/pdf/essential-summary-p13.pdf) · [DOI](https://doi.org/10.1016/j.nonrwa.2011.03.009)

## TL;DR 一句话总结

将**自适应控制**与**反对称结构**相结合，设计了一个比已有控制器更广义、更简洁的扩展自适应控制器，在系统参数**完全未知**的情况下实现了超混沌 Chen 系统与超混沌 Lorenz 系统之间的**广义函数投影同步（GFPS）**，同时在线估计了全部未知参数。

This paper combines **adaptive control** with an **antisymmetric structure** to design an extended adaptive controller that is more generalized and simpler than existing ones, achieving **generalized function projective synchronization (GFPS)** between hyperchaotic Chen and Lorenz systems with **completely unknown parameters**, while simultaneously estimating all unknown parameters.

## 研究背景

投影同步因其比例特性可获得更快的通信速率，一直是混沌同步的研究热点。其演化脉络为：

**投影同步**（Mainieri & Rehácek 1999，部分线性系统）→ **修正投影同步 MPS**（常数比例矩阵）→ **函数投影同步 FPS**（比例函数）→ **修正函数投影同步 MFPS**（比例函数矩阵）→ **广义函数投影同步 GFPS**（更广义的比例函数矩阵）。

本文研究的是：当两个**不同**的超混沌系统参数**完全未知**时，如何实现 GFPS。这是比物理学报 2011 那篇（常数比例因子 + 已知结构）更一般的情形。

## 方法：GFPS 与反对称结构控制器

### 问题建模

带未知参数的驱动系统：
$$
\dot{x} = f(x) + \Phi(x)\Theta
$$

带未知参数的响应系统：
$$
\dot{y} = g(y) + \Psi(y)\Omega + U
$$

### 误差定义（核心创新）

GFPS 的误差相对于**比例函数矩阵** $h(x) = \mathrm{diag}\{h_1(x), \ldots, h_n(x)\}$ 定义：
$$
\boxed{e = y - h(x)x, \qquad \dot{e} = g(y) + \Psi(y)\Omega - J\big(f(x) + \Phi(x)\Theta\big) + U}
$$

其中 $J = \mathrm{d}(h(x)x)/\mathrm{d}x$。这一框架统一了多种已有方案：所有 $h_i$ 相等退化为 FPS；所有 $h_i$ 为常数退化为 MPS；$h \equiv 0$ 退化为混沌控制。

### 稳定性引理（反对称结构）

**定理1**：对 $\dot{x} = B(x)x$，$B(x) = B_1(x) + B_2$，若 $B_1^T = -B_1$（反对称）、$B_2 = \mathrm{diag}\{b_1,\ldots,b_n\}$ 且 $b_i < 0$，则系统渐近稳定。

**证明**：取 $V = \frac{1}{2}x^Tx$，反对称部分在 $\dot V$ 中自动抵消：
$$
\dot{V} = x^T B_2 x < 0
$$

这就是反对称结构的妙处——**无需计算特征值**，Lyapunov 函数直接给出全局渐近稳定性。

### 主控制器（定理2）

$$
\boxed{U = J\big(f(x) + \Phi(x)\hat\Theta\big) - g(y) - \Psi(y)\hat\Omega + Ke}
$$

参数更新律：
$$
\dot{\hat\Theta} = -J^T \Phi^T(x) e + \tilde\Theta, \qquad
\dot{\hat\Omega} = \Psi^T(y) e + \tilde\Omega
$$

其中 $K$ 满足定理1（反对称非对角 + 负对角）。Lyapunov 函数 $V = \frac{1}{2}(e^Te + \tilde\Theta^T\tilde\Theta + \tilde\Omega^T\tilde\Omega)$ 的导数负定，保证误差系统全局渐近稳定且参数估计收敛。

## 数值验证：超混沌 Chen → 超混沌 Lorenz

驱动为超混沌 Chen 系统，响应为超混沌 Lorenz 系统，参数全部未知（$a=35,b=3,c=12,d=7,r=0.08$；$a_1=10,b_1=28,c_1=8/3,d_1=1.3$）。

### 情形一：周期比例函数

$$
h_i(x_i) = d_{i1}\sin(d_{i2}x_i + d_{i3}) + d_{i4}
$$

![参数估计（驱动系统）](/assets/img/publication_preview/nonrwa-fig1.png){: width="70%"}

*图 1: 周期比例函数下，驱动系统（超混沌Chen）8个未知参数的在线估计，最终收敛到真值。*

![同步误差](/assets/img/publication_preview/nonrwa-fig3.png){: width="70%"}

*图 2: 周期比例函数下，两超混沌系统 GFPS 同步误差的时间响应，误差趋于零。*

### 情形二：多项式比例函数

$$
h_i(x) = d_{i1}x_i^2 + d_{i2}x_i + d_{i3}
$$

![同步误差（多项式）](/assets/img/publication_preview/nonrwa-fig6.png){: width="70%"}

*图 3: 多项式比例函数下，GFPS 同步误差的时间响应。*

## 核心结论

1. **统一框架**：GFPS 以比例函数矩阵 $h(x)$ 统一了 FPS、MPS、混沌控制等方案
2. **更简单更广义**：反对称结构设计使控制器比 Du et al. (2009) 更简洁，比 Yu & Li (2010) 更广义（后者是特例）
3. **参数在线估计**：同步过程中同时估计了两个超混沌系统的全部 8 个未知参数
4. **复杂的比例函数**：周期函数和多项式函数两类此前未讨论过的比例函数均验证可行
5. **严格稳定性证明**：反对称结构保证 $\dot V < 0$，全局渐近稳定有严格数学保证

## 研究意义

这是作者混沌同步方向的第二篇代表作（与物理学报 2011 那篇改进主动控制法互为姊妹篇）。两篇论文共同确立了作者研究轨迹中的「混沌同步」线索。其核心方法论——用反对称结构 + Lyapunov 理论替代代数特征值判据来设计控制器——与后来摄动方法（GHFP/MGHFP 系列）中体现的设计哲学一脉相承。
