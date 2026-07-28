#!/usr/bin/env python3
"""更新P10/P11封面配图为精确裁剪版"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_back4 import *

ESS = "/sessions/beautiful-inspiring-keller/mnt/个人主页/assets"

# P10: 用精确裁剪的 p10-fig1, p10-fig2, p10-fig3
make("nody-cover.png",
    "Springer", "Nonlinear Dynamics", "Nonlinear Dyn.",
    "Vol.84 · No.3", "2016",
    "A Generalized Padé–Lindstedt–Poincaré Method for Predicting Homoclinic and Heteroclinic Bifurcations",
    "Zhenbo Li, Jiashi Tang",
    "Nonlinear Dyn., Vol.84, pp.1201–1223 (2016)",
    "DOI: 10.1007/s11071-015-2563-6",
    (0, 70, 140),
    lambda s: (s, int(s*0.55), int(s*0.4)),
    555,
    f"{ESS}/essential-summary-p10/p10-fig2.png")

# P11
make("jvet-cover.png",
    "Springer", "J. Vib. Eng. Technol.", "J. Vib. Eng. Technol.",
    "Vol.10 · No.4", "2022",
    "High Accurate Homo-Heteroclinic Solutions Based on Generalized Padé–Lindstedt–Poincaré Method",
    "Zhenbo Li, Jiashi Tang",
    "J. Vib. Eng. Technol., Vol.10, pp.1291–1308 (2022)",
    "DOI: 10.1007/s42417-022-00446-7",
    (0, 90, 60),
    lambda s: (s, int(s*0.6), int(s*0.35)),
    777,
    f"{ESS}/essential-summary-p11/p11-fig1.png")
