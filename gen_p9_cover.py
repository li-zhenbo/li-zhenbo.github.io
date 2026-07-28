#!/usr/bin/env python3
"""生成第9篇论文封面: 振动与冲击 2019"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_back4 import *

ESS = "/sessions/beautiful-inspiring-keller/mnt/个人主页/assets"

make("jvs-cover-p9.png",
    "Chinese Vibration Engineering Society",
    "Journal of Vibration and Shock",
    "J. Vib. Shock",
    "Vol.38 · No.22", "2019",
    "A Cosine Generalized Padé Approximation Method for Periodic Solutions of Strongly Nonlinear Oscillators",
    "Zhenbo Li, Jiashi Tang",
    "J. Vib. Shock, Vol.38, pp.159–167 (2019)",
    "DOI: 10.13465/j.cnki.jvs.2019.22.023",
    (0, 100, 60),
    lambda s: (s, int(s*0.6), int(s*0.3)),
    99,
    f"{ESS}/essential-summary-p9/p9-fig1.png")
