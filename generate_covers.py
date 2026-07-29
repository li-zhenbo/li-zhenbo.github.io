#!/usr/bin/env python3
"""
Generate 800x1000 publication cover images for 8 academic papers.
Uses PIL (Pillow) with default font. No external font dependencies.
All 8 covers follow the EXACT same template layout.
"""

from PIL import Image, ImageDraw, ImageFont
import os
import sys

W, H = 800, 1000

# ── Paper data ──────────────────────────────────────────────────────────────
PAPERS = [
    {
        "filename": "physica-scripta-cover.png",
        "brand": (0, 51, 102),         # P1: deep blue
        "journal_short": "Physica Scripta",
        "journal_full": "Physica Scripta",
        "year": 2026,
        "topbar_secondary": "Research Article  •  2026",
        "title": "Quantitative Analysis of Dynamical Bifurcations in a Coupled SD Oscillator",
        "authors": "Zhenbo Li, Linxia Hou, Ruyue Peng",
        "doi": "10.1088/1402-4896/ae5134",
    },
    {
        "filename": "ijNlm-cover.png",
        "brand": (0, 102, 51),         # P2: forest green
        "journal_short": "IJNLM",
        "journal_full": "International Journal of Non-Linear Mechanics",
        "year": 2025,
        "topbar_secondary": "Research Article  •  2025",
        "title": "Global Evolution of Limit Cycles and Homoclinic Bifurcation in SD Oscillator with Quartic Damping",
        "authors": "Zhenbo Li, Linxia Hou, Ruyue Peng",
        "doi": "10.1016/j.ijnonlinmec.2025.105185",
    },
    {
        "filename": "ijNlm-cover-p3.png",
        "brand": (0, 102, 51),         # P3: forest green
        "journal_short": "IJNLM",
        "journal_full": "International Journal of Non-Linear Mechanics",
        "year": 2024,
        "topbar_secondary": "Research Article  •  2024",
        "title": "A Modified Generalized Harmonic Function Perturbation Method for Analyzing Duffing–Harmonic–Rayleigh–Liénard Oscillator",
        "authors": "Zhenbo Li, Jin Cai, Linxia Hou",
        "doi": "10.1016/j.ijnonlinmec.2024.104832",
    },
    {
        "filename": "physica-scripta-cover-p4.png",
        "brand": (0, 51, 102),         # P4: deep blue
        "journal_short": "Physica Scripta",
        "journal_full": "Physica Scripta",
        "year": 2024,
        "topbar_secondary": "Research Article  •  2024",
        "title": "A Modified Perturbation Method for Global Dynamic Analysis of Mixed Rayleigh–Liénard Oscillator",
        "authors": "Zhenbo Li, Linxia Hou, Yiqing Zhang, Feng Xu",
        "doi": "10.1088/1402-4896/ad5066",
    },
    {
        "filename": "jsv-cover.png",
        "brand": (0, 51, 102),         # P5: deep blue
        "journal_short": "JSV",
        "journal_full": "Journal of Sound and Vibration",
        "year": 2013,
        "topbar_secondary": "Research Article  •  2013",
        "title": "A Generalized Harmonic Function Perturbation Method for Limit Cycles and Homoclinic Orbits of Helmholtz–Duffing Oscillator",
        "authors": "Zhenbo Li, Jiashi Tang, Ping Cai",
        "doi": "10.1016/j.jsv.2013.05.007",
    },
    {
        "filename": "qtds-cover.png",
        "brand": (100, 30, 100),       # P6: deep purple
        "journal_short": "QTDS",
        "journal_full": "Qualitative Theory of Dynamical Systems",
        "year": 2016,
        "topbar_secondary": "Research Article  •  2016",
        "title": "Predicting Homoclinic and Heteroclinic Bifurcation of Generalized Duffing–Harmonic–van de Pol Oscillator",
        "authors": "Zhenbo Li, Jiashi Tang, Ping Cai",
        "doi": "10.1007/s12346-015-0138-z",
    },
    {
        "filename": "lxxb-cover.png",
        "brand": (160, 30, 30),        # P7: deep red
        "journal_short": "力学学报",           # 力学学报
        "journal_full": "力学学报 (Chinese Journal of Theoretical and Applied Mechanics)",
        "year": 2013,
        "topbar_secondary": "Research Article  •  2013",
        "title": "Generalized Padé Approximation Method for Homoclinic Orbits of Strongly Nonlinear Autonomous Oscillators",
        "authors": "Zhenbo Li, Jiashi Tang, Ping Cai",
        "doi": "10.6052/0459-1879-12-277",
    },
    {
        "filename": "cpb-cover.png",
        "brand": (0, 70, 130),         # P8: blue
        "journal_short": "Chinese Physics B",
        "journal_full": "Chinese Physics B",
        "year": 2014,
        "topbar_secondary": "Research Article  •  2014",
        "title": "A Generalized Padé Approximation Method of Solving Homoclinic and Heteroclinic Orbits",
        "authors": "Zhenbo Li, Jiashi Tang, Ping Cai",
        "doi": "10.1088/1674-1056/23/12/120501",
    },
]


# ── Text helpers ────────────────────────────────────────────────────────────

def get_font():
    """Return the default PIL bitmap font."""
    return ImageFont.load_default()


def text_width(draw, text, font):
    """Measure text width. Compatible with PIL < 9 and >= 9."""
    try:
        return int(draw.textlength(text, font=font))
    except AttributeError:
        return draw.textsize(text, font=font)[0]


def font_height(font):
    """Approximate line height for default font."""
    try:
        return font.getsize("Ag")[1] + 4
    except Exception:
        return 16  # safe fallback


def wrap_text(draw, text, font, max_width):
    """Break text into lines that each fit within *max_width* pixels."""
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        test = cur + (" " if cur else "") + w
        if text_width(draw, test, font) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines if lines else [text]


def cx(tw):
    """Return centered x for a text block of width *tw*."""
    return (W - tw) // 2


# ── Drawing helpers ─────────────────────────────────────────────────────────

def draw_bold(draw, x, y, text, font, fill):
    """Faux-bold by stamping twice with 1 px horizontal offset."""
    draw.text((x + 1, y), text, font=font, fill=fill)
    draw.text((x, y), text, font=font, fill=fill)


def centered_text(draw, text, y, font, fill, bold=False):
    """Draw *text* horizontally centred at *y*."""
    tw = text_width(draw, text, font)
    x = cx(tw)
    if bold:
        draw_bold(draw, x, y, text, font, fill)
    else:
        draw.text((x, y), text, font=font, fill=fill)


def centered_lines(draw, lines, start_y, font, fill, line_spacing, bold=False):
    """Draw multiple centred lines, return y after last line."""
    y = start_y
    for line in lines:
        centered_text(draw, line, y, font, fill, bold=bold)
        y += line_spacing
    return y


# ── Single cover builder ────────────────────────────────────────────────────

def build_cover(paper):
    """Create one 800x1000 cover image from *paper* dict."""
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    font = get_font()
    lh = font_height(font)
    brand = paper["brand"]

    # Pre-defined palette
    WHITE           = (255, 255, 255)
    LIGHT_GRAY_TOP  = (200, 200, 200)   # top-bar secondary text
    GRAY_AUTHORS    = (100, 100, 110)   # author line
    GRAY_JOURNAL    = (140, 140, 150)   # journal reference line
    GRAY_DOI        = (150, 150, 160)   # DOI line
    GRAY_LABEL      = (130, 130, 130)   # "Essential Summary" heading
    GRAY_NOTE       = (160, 160, 160)   # disclaimer lines

    # ── Top bar  (y = 0 .. 120) ─────────────────────────────────────────
    draw.rectangle([(0, 0), (W, 120)], fill=brand)

    # Journal name - bold white
    centered_text(draw, paper["journal_short"], 40, font, WHITE, bold=True)

    # Secondary info (volume / research article)
    centered_text(draw, paper["topbar_secondary"], 70, font, LIGHT_GRAY_TOP, bold=False)

    # ── White body  (y = 121 .. 919) ────────────────────────────────────

    # Title (wrapped, up to 3 lines)
    TITLE_Y = 180
    TITLE_MAX_W = W - 80
    title_lines = wrap_text(draw, paper["title"], font, TITLE_MAX_W)
    title_spacing = lh + 6
    after_title = centered_lines(draw, title_lines, TITLE_Y, font, brand,
                                 title_spacing, bold=True)

    # Authors
    AUTHORS_Y = 340
    centered_text(draw, paper["authors"], AUTHORS_Y, font, GRAY_AUTHORS, bold=False)

    # Journal reference line
    JOURNAL_Y = 440
    journal_text = f"{paper['journal_full']} ({paper['year']})"
    centered_text(draw, journal_text, JOURNAL_Y, font, GRAY_JOURNAL, bold=False)

    # DOI
    DOI_Y = 510
    doi_text = f"DOI: {paper['doi']}"
    centered_text(draw, doi_text, DOI_Y, font, GRAY_DOI, bold=False)

    # Decorative horizontal rule
    LINE_Y = 580
    draw.line([(40, LINE_Y), (W - 40, LINE_Y)], fill=brand, width=2)

    # "Essential Summary" heading
    SUMMARY_Y = 680
    centered_text(draw, "■  Essential Summary  ■", SUMMARY_Y, font, GRAY_LABEL, bold=False)

    # Disclaimer lines
    NOTE1_Y = 750
    NOTE2_Y = 790
    centered_text(draw, "This is an author-prepared essential summary.", NOTE1_Y, font, GRAY_NOTE, bold=False)
    centered_text(draw, "Please cite the published version.", NOTE2_Y, font, GRAY_NOTE, bold=False)

    # Icon / flourish
    ICON_Y = 870
    icon = "◆"   # ◆ – safe geometric glyph in bitmap fonts
    centered_text(draw, icon, ICON_Y, font, brand, bold=False)

    # ── Bottom bar  (y = 920 .. 999) ────────────────────────────────────
    draw.rectangle([(0, 920), (W, H - 1)], fill=brand)

    return img


# ── Verification ────────────────────────────────────────────────────────────

def verify(filepath, expected_brand):
    img = Image.open(filepath)
    w, h = img.size
    ok = True
    if (w, h) != (800, 1000):
        print(f"  FAIL  size {w}x{h} (expected 800x1000)")
        ok = False

    c_top = img.getpixel((400, 20))
    if c_top != expected_brand:
        print(f"  FAIL  top-bar colour at (400,20) = {c_top}, expected {expected_brand}")
        ok = False

    c_bot = img.getpixel((400, 960))
    if c_bot != expected_brand:
        print(f"  FAIL  bottom-bar colour at (400,960) = {c_bot}, expected {expected_brand}")
        ok = False

    c_body = img.getpixel((400, 500))
    if c_body != (255, 255, 255):
        print(f"  WARN  body at (400,500) = {c_body} (expected pure white)")
        # not fatal

    if ok:
        print(f"  OK    {os.path.basename(filepath)}")
    return ok


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    parts = sys.argv[0].split("/mnt/")
    if len(parts) == 2:
        # Running inside Cowork sandbox — resolve via mount
        output_dir = "/sessions/nice-hopeful-allen/mnt/个人主页/assets/img/publication_preview"
    else:
        # Running on host
        output_dir = "/Users/lizhenbo/Claude Code Project/个人主页/assets/img/publication_preview"
    os.makedirs(output_dir, exist_ok=True)

    print(f"Generating {len(PAPERS)} cover images …")
    print(f"Output: {output_dir}\n")

    generated = []
    for p in PAPERS:
        img = build_cover(p)
        path = os.path.join(output_dir, p["filename"])
        img.save(path, "PNG")
        generated.append((path, p["brand"]))
        print(f"  saved  {p['filename']}")

    print("\nVerification …\n")
    all_pass = True
    for path, brand in generated:
        if not verify(path, brand):
            all_pass = False

    print()
    if all_pass:
        print("SUCCESS  All 8 covers generated and verified.")
    else:
        print("FAILED   Some covers did not pass verification. See log above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
