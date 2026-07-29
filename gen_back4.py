"""
后四篇封面 v6: 标准期刊缩写 + 图片自动裁白边 + 中文 SC(index=2)
"""
from PIL import Image, ImageDraw, ImageFont
import random, os

W, H = 800, 1000; M = 48; WHITE = (255,255,255)
OUT = "/sessions/beautiful-inspiring-keller/mnt/个人主页/assets/img/publication_preview"
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
    # 从四边向内收缩直到碰到非白色像素
    top,bottom,left,right=0,h-1,0,w-1
    # top
    for y in range(h):
        for x in range(0, w, 10):
            p=img.getpixel((x,y))
            if p!=(255,255,255) and (len(p)<4 or p[3]>128):
                top=y; break
        else: continue
        break
    # bottom
    for y in range(h-1,-1,-1):
        for x in range(0, w, 10):
            p=img.getpixel((x,y))
            if p!=(255,255,255) and (len(p)<4 or p[3]>128):
                bottom=y; break
        else: continue
        break
    # left
    for x in range(w):
        for yy in range(top, bottom+1, 10):
            p=img.getpixel((x,yy))
            if p!=(255,255,255) and (len(p)<4 or p[3]>128):
                left=x; break
        else: continue
        break
    # right
    for x in range(w-1,-1,-1):
        for yy in range(top, bottom+1, 10):
            p=img.getpixel((x,yy))
            if p!=(255,255,255) and (len(p)<4 or p[3]>128):
                right=x; break
        else: continue
        break
    # 留一点边距
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
         brand, accent, seed, img_path=None, zh=False):
    img=Image.new("RGB",(W,H),WHITE)
    d=ImageDraw.Draw(img)

    fp,fj,fjs,ft,fa,fi,fdoi,fb,fb2 = \
        (FC_PUB,FC_JRN,FC_JRN_S,FC_TITLE,FC_AUTH,FC_INFO,FC_DOI,FC_BOT,FC_BOT2) if zh else \
        (F_PUB,F_JRN,F_JRN_S,F_TITLE,F_AUTH,F_INFO,F_DOI,F_BOT,F_BOT2)

    d.rectangle([(0,0),(W,121)],fill=brand)
    g=(255,210,210) if zh else (210,210,210)
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
    g2=(255,200,200) if zh else (200,200,200)
    lt(d,"南华大学" if zh else "University of South China",x0,940,fb,WHITE)
    lt(d,"数理学院" if zh else "School of Mathematics and Physics",x0,968,fb2,g2)

    img.save(os.path.join(OUT,fn),"PNG")
    print(f"  {fn}")

ESS="/sessions/beautiful-inspiring-keller/mnt/个人主页/assets"

make("qtds-cover.png",
    "Springer","Qualitative Theory of Dynamical Systems","Qual. Theory Dyn. Syst.",
    "Vol.15 · No.1","2016",
    "Predicting Homoclinic and Heteroclinic Bifurcation of Generalized Duffing–Harmonic–van de Pol Oscillator",
    "Zhenbo Li, Jiashi Tang, Ping Cai",
    "Qual. Theory Dyn. Syst., Vol.15, pp.19–37 (2016)",
    "DOI: 10.1007/s12346-015-0138-z",
    (100,30,100),lambda s:(s,int(s*0.7),30),42,
    f"{ESS}/essential-summary-p6/p6-fig1-homoclinic.png")

make("jsv-cover.png",
    "Elsevier","Journal of Sound and Vibration","J. Sound Vib.",
    "Vol.332 · No.21","2013",
    "A Generalized Harmonic Function Perturbation Method for Limit Cycles and Homoclinic Orbits",
    "Zhenbo Li, Jiashi Tang, Ping Cai",
    "J. Sound Vib., Vol.332, pp.5508–5522 (2013)",
    "DOI: 10.1016/j.jsv.2013.05.007",
    (0,51,102),lambda s:(s,int(s*0.5),int(s*0.3)),77,
    f"{ESS}/essential-summary-p5/p5-fig1-limitcycle.png")

make("cpb-cover.png",
    "IOP Publishing","Chinese Physics B","Chin. Phys. B",
    "Vol.23 · No.12","2014",
    "A Generalized Padé Approximation Method for Homoclinic and Heteroclinic Orbits",
    "Zhenbo Li, Jiashi Tang, Ping Cai",
    "Chin. Phys. B, Vol.23, 120501 (2014)",
    "DOI: 10.1088/1674-1056/23/12/120501",
    (0,70,130),lambda s:(s,int(s*0.65),int(s*0.5)),123,
    f"{ESS}/essential-summary-p8/p8-fig1.png")

make("lxxb-cover.png",
    "中国力学学会 · 中国科学院","力学学报","力学学报",
    "第45卷 · 第3期","2013",
    "Generalized Padé Approximation Method for Homoclinic Orbits of Strongly Nonlinear Oscillators",
    "Zhenbo Li, Jiashi Tang, Ping Cai",
    "力学学报 (Chin. J. Theor. Appl. Mech.), Vol.45, pp.461–464 (2013)",
    "DOI: 10.6052/0459-1879-12-277",
    (160,30,30),lambda s:(s,int(s*0.35),int(s*0.35)),456,
    f"{ESS}/essential-summary-p7/p7-fig1.png",zh=True)

print("Done!")
