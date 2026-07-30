"""
前四篇封面 v1: 2026/2025/2024/2024 四篇论文封面，基于 gen_back4.py 的 make() 函数
"""
from PIL import Image, ImageDraw, ImageFont
import random, os

W, H = 800, 1000; M = 48; WHITE = (255,255,255)
OUT = "/sessions/kind-intelligent-fermat/mnt/outputs/front4-covers"
STRIPE_H = 74

Fn=lambda s,n,**kw:ImageFont.truetype(s,n,**kw)
F_PUB=Fn("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",18)
F_JRN=Fn("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",28)
F_JRN_S=Fn("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",22)
F_TITLE=Fn("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",28)
F_AUTH=Fn("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",20)
F_INFO=Fn("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",17)
F_DOI=Fn("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",16)
F_BOT=Fn("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",18)
F_BOT2=Fn("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",14)

ZC="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FC_PUB=Fn(ZC,18,index=2); FC_JRN=Fn(ZC,28,index=2); FC_JRN_S=Fn(ZC,22,index=2)
FC_TITLE=Fn(ZC,28,index=2); FC_AUTH=Fn(ZC,20,index=2); FC_INFO=Fn(ZC,17,index=2)
FC_DOI=Fn(ZC,16,index=2); FC_BOT=Fn(ZC,18,index=2); FC_BOT2=Fn(ZC,14,index=2)

def tw(d,t,f):
    try: return int(d.textlength(t,font=f))
    except: return d.textsize(t,font=f)[0]
def lt(d,t,x,y,f,c): d.text((x,y),t,font=f,fill=c)
def rt(d,t,xr,y,f,c):
    w=tw(d,t,f); d.text((xr-w,y),t,font=f,fill=c)

def pick_font(d,full,abbr,big,sm,max_w):
    if tw(d,full,big)<=max_w: return full,big
    if tw(d,abbr,big)<=max_w: return abbr,big
    return abbr,sm

def wrap(d,t,f,mw):
    words=t.split(); lines,cur=[],""
    for w in words:
        test=cur+(" " if cur else "")+w
        if tw(d,test,f)<=mw: cur=test
        else:
            if cur: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines or [t]

def auto_crop(img):
    """裁掉图片四周的白边"""
    w,h=img.size
    top,bottom,left,right=0,h-1,0,w-1
    for y in range(h):
        for x in range(0, w, 10):
            p=img.getpixel((x,y))
            if p!=(255,255,255) and (len(p)<4 or p[3]>128):
                top=y; break
        else: continue
        break
    for y in range(h-1,-1,-1):
        for x in range(0, w, 10):
            p=img.getpixel((x,y))
            if p!=(255,255,255) and (len(p)<4 or p[3]>128):
                bottom=y; break
        else: continue
        break
    for x in range(w):
        for yy in range(top, bottom+1, 10):
            p=img.getpixel((x,yy))
            if p!=(255,255,255) and (len(p)<4 or p[3]>128):
                left=x; break
        else: continue
        break
    for x in range(w-1,-1,-1):
        for yy in range(top, bottom+1, 10):
            p=img.getpixel((x,yy))
            if p!=(255,255,255) and (len(p)<4 or p[3]>128):
                right=x; break
        else: continue
        break
    pad=5
    top=max(0,top-pad); bottom=min(h-1,bottom+pad)
    left=max(0,left-pad); right=min(w-1,right+pad)
    return img.crop((left,top,right+1,bottom+1))

def draw_stripes(d, brand, accent, seed):
    rng=random.Random(seed)
    style=rng.randint(0,3)
    n=rng.randint(18,30)
    if style==0: sp,off=rng.randint(25,60),rng.randint(-300,-50)
    elif style==1: sp,off=rng.randint(45,75),rng.randint(-200,0)
    elif style==2: sp,off=rng.randint(30,55),rng.randint(-200,-50)
    else: sp,off=rng.randint(35,65),rng.randint(-250,-80)

    for i in range(n):
        x0=off+i*sp; x1=x0+950
        if style==2 and i%4==0:
            center=rng.randint(300,500)
            s1=rng.randint(180,230); s2=rng.randint(60,120)
            for dx in (-1,0,1):
                d.line([(x0+dx,121),(center,121+STRIPE_H//2)],fill=accent(s1),width=1)
                d.line([(center,121+STRIPE_H//2),(x1+dx,121+STRIPE_H)],fill=accent(s2),width=1)
            continue
        s=rng.randint(180,230) if i%2==0 else rng.randint(50,110)
        c=accent(s)
        for dx in (-1,0,1): d.line([(x0+dx,121),(x1+dx,121+STRIPE_H)],fill=c,width=1)

    if style==3:
        off2=off+rng.randint(300,500)
        for i in range(n-5):
            x0=off2+i*sp; x1=x0-950
            s=rng.randint(100,170); c=accent(s)
            for dx in (-1,0,1): d.line([(x0+dx,121+STRIPE_H),(x1+dx,121)],fill=c,width=1)

def make(fn, pub, jrn, abbr, vol, yr, title, authors, jline, doi,
         brand, accent, seed, img_path=None):
    img=Image.new("RGB",(W,H),WHITE)
    d=ImageDraw.Draw(img)

    fp,fj,fjs,ft,fa,fi,fdoi,fb,fb2 = \
        (F_PUB,F_JRN,F_JRN_S,F_TITLE,F_AUTH,F_INFO,F_DOI,F_BOT,F_BOT2)

    d.rectangle([(0,0),(W,121)],fill=brand)
    g=(210,210,210)
    lt(d,pub,M,22,fp,g)
    jd,jf=pick_font(d,jrn,abbr,fj,fjs,W-2*M-160)
    lt(d,jd,M,54,jf,WHITE)
    rt(d,vol,W-M,36,fi,g)
    rt(d,yr,W-M,64,fi,g)

    draw_stripes(d,brand,accent,seed)

    bw=640; x0=(W-bw)//2; y=121+STRIPE_H+40
    for line in wrap(d,title,ft,bw):
        lt(d,line,x0,y,ft,brand); y+=ft.size+10
    y+=30
    lt(d,authors,x0,y,fa,(110,110,110))
    y+=42; lt(d,jline,x0,y,fi,(130,130,145))
    y+=34; lt(d,doi,x0,y,fdoi,(150,150,160))
    y+=45
    d.line([(x0,y),(x0+bw,y)],fill=(200,200,205),width=1)

    y+=30
    if img_path and os.path.exists(img_path):
        pimg=Image.open(img_path).convert("RGB")
        pimg=auto_crop(pimg)
        pw,ph=pimg.size
        tw_img=min(500,bw)
        scale=tw_img/pw; th_img=int(ph*scale)
        if th_img>320: th_img=320; scale=th_img/ph; tw_img=int(pw*scale)
        pimg=pimg.resize((tw_img,th_img),Image.LANCZOS)
        px=(W-tw_img)//2
        d.rectangle([(px-1,y-1),(px+tw_img+1,y+th_img+1)],outline=(210,210,215))
        img.paste(pimg,(px,y))

    d.rectangle([(0,920),(W,999)],fill=brand)
    g2=(200,200,200)
    lt(d,"University of South China",x0,940,fb,WHITE)
    lt(d,"School of Mathematics and Physics",x0,968,fb2,g2)

    img.save(os.path.join(OUT,fn),"PNG")
    print(f"  {fn}")

PUB = "/sessions/kind-intelligent-fermat/mnt/个人主页/assets/img/publication_preview"

# ====== P1: li2026quantitative — Physica Scripta 2026 ======
make("physica-scripta-cover.png",
    "IOP Publishing", "Physica Scripta", "Phys. Scr.",
    "Vol.101 · No.12", "2026",
    "Quantitative Analysis of Dynamical Bifurcations in a Coupled Smooth and Discontinuous Oscillator with High-order Nonlinear Damping",
    "Zhenbo Li, Linxia Hou, Ruyue Peng",
    "Phys. Scr., Vol.101, 125205 (2026)",
    "DOI: 10.1088/1402-4896/ae5134",
    (0, 65, 115),
    lambda s: (s, int(s*0.6), int(s*0.45)),
    2026,
    f"{PUB}/fig1-amplitude.png")

# ====== P2: li2025global — IJNLM 2025 ======
make("ijnlm-cover.png",
    "Elsevier", "International Journal of Non-Linear Mechanics", "Int. J. Non-Linear Mech.",
    "Vol.178", "2025",
    "Global Evolution of Limit Cycles and Homoclinic Bifurcation of Smooth and Discontinuous Oscillator with Quartic Nonlinear Damping",
    "Zhenbo Li, Linxia Hou, Ruyue Peng",
    "Int. J. Non-Linear Mech., Vol.178, 105185 (2025)",
    "DOI: 10.1016/j.ijnonlinmec.2025.105185",
    (5, 35, 75),
    lambda s: (s, int(s*0.55), int(s*0.35)),
    2025,
    f"{PUB}/p2-fig3-amplitude.png")

# ====== P3: li2024modified — IJNLM 2024 ======
make("ijnlm-cover-p3.png",
    "Elsevier", "International Journal of Non-Linear Mechanics", "Int. J. Non-Linear Mech.",
    "Vol.166", "2024",
    "A Modified Generalized Harmonic Function Perturbation Method and Its Application in Analyzing Generalized Duffing–Harmonic–Rayleigh–Liénard Oscillator",
    "Zhenbo Li, Jin Cai, Linxia Hou",
    "Int. J. Non-Linear Mech., Vol.166, 104832 (2024)",
    "DOI: 10.1016/j.ijnonlinmec.2024.104832",
    (10, 40, 85),
    lambda s: (s, int(s*0.6), int(s*0.4)),
    424,
    f"{PUB}/p3-fig-p10.png")

# ====== P4: li2024modified2 — Physica Scripta 2024 ======
make("physica-scripta-cover-p4.png",
    "IOP Publishing", "Physica Scripta", "Phys. Scr.",
    "Vol.99 · No.7", "2024",
    "A Modified Perturbation Method for Global Dynamic Analysis of Generalized Mixed Rayleigh–Liénard Oscillator with Cubic and Quintic Nonlinearities",
    "Zhenbo Li, Linxia Hou, Yiqing Zhang, Feng Xu",
    "Phys. Scr., Vol.99, 075213 (2024)",
    "DOI: 10.1088/1402-4896/ad5066",
    (0, 70, 120),
    lambda s: (s, int(s*0.65), int(s*0.5)),
    724,
    f"{PUB}/p4-fig3.png")

print("Done! All four front covers generated.")
