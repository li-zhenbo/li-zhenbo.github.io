#!/usr/bin/env python3
"""GPA技术路线图 方案A — 大字号版"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'
C_TITLE = '#003C78'; C_BG = '#FAFBFC'

PALETTE       = ['#1a5276', '#e67e22', '#27ae60', '#c0392b', '#8e44ad']
PALETTE_LIGHT = ['#d6eaf8', '#fdebd0', '#d5f5e3', '#fadbd8', '#e8daef']

PAPERS = [
    ('2013', 'I. GPA\nDefinition',
     'P(z) = Σ aᵢ gᵢ(z)\ngᵢ: any continuous function\nSech basis → homoclinic',
     'Chin. J. Theor. Appl. Mech., 45, 461'),
    ('2014', 'II. Extension to\nHeteroclinic',
     'Tanh basis → heteroclinic\nPolynomial + Irrational (SD)\nSech↔Hom | Tanh↔Het',
     'Chin. Phys. B, 23, 120501'),
    ('2016', 'III. GPLP Method\n(+ L-P Integration)',
     'GPA + Lindstedt-Poincaré\nε³ accurate at ε = 50\nSimultaneous H/H prediction',
     'Nonlinear Dyn., 84, 1201'),
    ('2019', 'IV. Periodic\nSolutions',
     'Cosine basis: cos(iωt)\nApproximant itself periodic\nTwo iterative schemes',
     'J. Vib. Shock, 38, 159'),
    ('2022', 'V. Asymmetric\nRefinement',
     'Full Φ⁶ with x² + x⁴ terms\nω-Sech + Type A/B Tanh\nRational restoring force',
     'J. Vib. Eng. Technol., 10, 1291'),
]

fig, ax = plt.subplots(1, 1, figsize=(20, 7))
ax.set_xlim(0, 20); ax.set_ylim(0, 7); ax.axis('off')
fig.patch.set_facecolor(C_BG)

ax.text(10, 6.6, 'Generalized Padé Approximation Methods — Technical Roadmap (2013–2022)',
        ha='center', fontsize=20, fontweight='bold', color=C_TITLE)

for i, (yr, title, desc, ref) in enumerate(PAPERS):
    x = 0.4 + i * 3.95; w = 3.75; h_top = 0.9; h_mid = 2.9; h_bot = 0.65
    c = PALETTE[i]; cl = PALETTE_LIGHT[i]

    # 顶部色块：年份
    b = FancyBboxPatch((x, 4.55), w, h_top, boxstyle="round,pad=0.1",
                        facecolor=c, edgecolor='none', linewidth=0, zorder=3)
    ax.add_patch(b)
    ax.text(x+w/2, 4.55 + h_top/2, yr, ha='center', va='center',
            fontsize=26, fontweight='bold', color='white')

    # 中间：标题+描述
    b2 = FancyBboxPatch((x, 1.6), w, h_mid, boxstyle="round,pad=0.1",
                         facecolor=cl, edgecolor='#ccc', linewidth=0.8, zorder=3)
    ax.add_patch(b2)
    ax.text(x+w/2, 4.2, title, ha='center', va='center',
            fontsize=12.5, fontweight='bold', color=c, linespacing=1.2)
    ax.text(x+w/2, 2.9, desc, ha='center', va='center',
            fontsize=10, color='#333', linespacing=1.4)

    # 底部：期刊
    ax.text(x+w/2, 1.25, ref, ha='center', va='center',
            fontsize=8, color='#888', fontstyle='italic')

    # 箭头
    if i < 4:
        ax.annotate('', xy=(x+w+0.12, 5.0), xytext=(x+w, 5.0),
                    arrowprops=dict(arrowstyle='->', color='#555', lw=2.5))

# 底部核心原则条
b3 = FancyBboxPatch((0.4, 0.1), 19.1, 0.7, boxstyle="round,pad=0.15",
                     facecolor='#f0f5ff', edgecolor=C_TITLE, linewidth=1.2, zorder=3)
ax.add_patch(b3)
ax.text(10, 0.45, 'Core Principle: Match basis functions to solution geometry     |     Sech (homoclinic)  →  Tanh (heteroclinic)  →  Sech+Tanh (mixed)  →  Cosine (periodic)',
        ha='center', va='center', fontsize=10.5, fontweight='bold', color=C_TITLE)

plt.tight_layout(pad=0.3)
plt.savefig('/sessions/beautiful-inspiring-keller/mnt/个人主页/assets/mghfp-review/gpa-review/gpa-roadmap-A.png',
            dpi=200, facecolor=C_BG, edgecolor='none')
print('saved roadmap-A (large font)')
plt.close()
