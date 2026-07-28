# AGENTS.md — 个人主页项目维护指南

> 本文件供 AI agent（Claude）在维护本项目时先行读取，避免重复踩坑。

## 项目概况

- **技术栈**：al-folio（Jekyll 学术主题，v1.x 架构，含 al_folio_core 系列插件）
- **部署**：GitHub Pages（境外）+ Gitee Pages（国内）双部署
- **GitHub 账号**：`li-zhenbo`，仓库 `li-zhenbo.github.io`
- **网站地址**：`https://li-zhenbo.github.io`
- **语言**：中英双语（同页行内对照，非双语言站点树）
- **内容板块**：发表论文与核心结论、代码/项目、博客/研究笔记、CV 与简介
- **构建方式**：push 到 main 分支后，GitHub Actions（`.github/workflows/deploy.yml`）自动用 Ruby 3.3.5 + Jekyll 构建并部署到 gh-pages 分支。**不需要本地构建。**

## 关键文件速查

| 用途 | 文件路径 |
|------|----------|
| 站点配置（姓名、网址、开关） | `_config.yml` |
| 首页自我介绍 | `_pages/about.md` |
| 论文列表（BibTeX） | `_bibliography/papers.bib` |
| 论文 PDF | `assets/pdf/` |
| 论文预览图 | `assets/img/publication_preview/` |
| 头像 | `assets/img/prof_pic.jpg`（同名覆盖） |
| 邮箱、GitHub、Scholar 链接 | `_data/socials.yml` |
| 简历数据 | `_data/cv.yml` |
| 动态 | `_news/` 目录下 `.md` 文件 |
| 博客笔记 | `_posts/` 目录下 `YYYY-MM-DD-标题.md` |
| 项目卡片 | `_projects/` 目录下 `.md` 文件 |
| 精华汇总 LaTeX 源码 | `assets/pdf/essential-summary.tex` |

## 推送方式

用户已提供 GitHub Fine-grained Personal Access Token（权限：Contents read+write、Workflows read+write，仅限本仓库）。推送命令：

```bash
git push https://x-access-token:<TOKEN>@github.com/li-zhenbo/li-zhenbo.github.io.git main
```

推送后在日志中打码：`sed -E "s/github_pat_[A-Za-z0-9_]+/github_pat_***/g"`。

用户可能随时撤销令牌，届时需请用户重新生成。日常小改也可直接在 GitHub 网页编辑 Commit。

## 已踩过的坑（务必避免）

### 1. YAML 冒号问题

**问题**：`_data/cv.yml` 中字段值含有 `Research on: nonlinear` 这样的英文冒号+空格，YAML 解析器会误认为嵌套键值对，导致 Jekyll 构建崩溃。

**解决**：含冒号+空格的值必须用双引号包裹：
```yaml
summary: "主要研究方向：... / Research on: nonlinear dynamics ..."
```

中文全角冒号「：」不会触发此问题，只有英文冒号+空格 `": "` 会。

### 2. RenderCV 工作流

**问题**：al-folio 自带 `.github/workflows/render-cv.yml`，每次 `_data/cv.yml` 变化就自动跑 Python RenderCV 工具生成 CV PDF。但 RenderCV 有严格的字段格式规范，自定义 section 名（如中文标题）会导致它报错退出，显示红叉。**不影响网站本身**（网站由 deploy.yml 构建）。

**解决**：已删除 `render-cv.yml`。不要恢复它。CV PDF 由用户手动放置。

### 3. 论文预览图文件名长度

**问题**：al-folio 的 bib 模板对 `preview` 字段的文件名有长度限制。过长的文件名（如 `li2026-fig19-preview.png`）会在渲染时被截断，导致路径无效、图片加载不出来。

**解决**：预览图文件名要短，如 `fig19-preview.png`、`physica-scripta-cover.png`。`preview` 字段只写文件名，不写路径前缀（al-folio 自动在 `assets/img/publication_preview/` 下查找）：
```bibtex
preview = {physica-scripta-cover.png},
```

### 4. 论文摘要（abstract）字段不要塞太长内容

**问题**：al-folio 论文列表的摘要区域是窄栏排版。如果在 `abstract` 字段里塞入核心结论、图片 Markdown、长段中英文，会导致布局挤乱、文本挤到一块。

**解决**：
- `abstract`：只放论文原始英文摘要（或中英简短摘要），不要放图片和长内容
- `additional_info`：放一句话精简概括，提示精华内容可点击 PDF 按钮获取
- 详细图文解读放在 `_posts/` 下的博客笔记里

### 5. 从 PDF 论文中提取图片

**问题**：用 `pdfimages` 直接提取嵌入图片，会得到大量碎片（背景蒙版、透明层等），且矢量图形（matplotlib/Excel 图表）不会被提取。用整页截图 + 按比例猜裁剪位置，会截多或截少。

**解决**：用 **PyMuPDF（fitz）** 精确定位：
1. `page.get_text("blocks")` 找到 Figure 标题的 Y 坐标
2. `page.get_drawings()` 获取矢量图形的包围盒
3. 以 Figure 标题的 Y 位置为下边界，矢量图形顶部为上边界，用 `page.get_pixmap(matrix=Matrix(300/72, 300/72), clip=Rect(...))` 精确裁剪渲染

### 6. LaTeX PDF 编译

**环境**：VM 内有 `xelatex`（支持中文），`pdflatex` 不支持中文（缺中文字体）。

**问题**：`TeX Gyre Termes` 等英文字体不含中文字符，所有中文会丢失（PDF 里只有公式没有文字）。

**解决**：
- 纯英文文档用 `pdflatex` 即可
- 含中文的文档必须用 `xelatex` + `\usepackage{fontspec}` + 中文字体（`Noto Serif CJK SC`）
- 当前精华 PDF 已改为纯英文，用 `xelatex` 编译（因为用了 `fontspec`）

### 7. LaTeX 浮动图片导致大段空白

**问题**：图片高度接近半页时，LaTeX 浮动机制找不到合适的放置位置，推迟到下一页，留下大片空白。

**解决**：
- 图片同时限制宽度和高度：`\includegraphics[width=\textwidth,height=0.38\textheight,keepaspectratio]{...}`
- 放宽浮动阈值：
```latex
\renewcommand{\topfraction}{0.9}
\renewcommand{\bottomfraction}{0.9}
\renewcommand{\textfraction}{0.07}
\renewcommand{\floatpagefraction}{0.7}
\setcounter{topnumber}{3}
\setcounter{bottomnumber}{3}
\setcounter{totalnumber}{5}
```
- 不要用 `\newpage` 手动分页，让 LaTeX 自由排版
- 浮动体用 `[htbp]` 而非 `[ht]`

### 8. GitHub Pages 分支配置

**问题**：`用户名.github.io` 仓库 push 代码后，GitHub 会自动触发内置的 "pages build and deployment" 工作流，用简化版 Jekyll 构建 main 分支。al-folio 的自定义插件它不认识，会报错或产出残缺页面。

**解决**：等 al-folio 的 "Deploy site" 工作流（`.github/workflows/deploy.yml`）完成后，去仓库 Settings → Pages，把 Branch 从 `main` 改为 `gh-pages`，选 `/(root)`。这样 GitHub Pages 用 al-folio 构建好的 `_site` 内容，不触发内置 Jekyll。

### 9. GitHub API 限频

**问题**：通过 `api.github.com` 查询 Actions 构建状态时，未认证请求 IP 限频严格（每小时 60 次），容易 403。

**解决**：用用户的 token 认证请求，或直接让用户在 GitHub 网页查看 Actions 页面。

### 10. 论文版权

**问题**：用户不能在网站上随意传播论文原文 PDF（IOP 版权协议）。

**解决**：网站上的 PDF 按钮链接的是作者自行整理的**精华汇总 PDF**（含核心公式、关键图片、结论解读），不是论文原文。论文原文 PDF 已从网站目录删除。LaTeX 源码在 `assets/pdf/essential-summary.tex`，修改后用 `xelatex` 编译两遍。
