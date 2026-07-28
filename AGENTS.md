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

**问题**：用户不能在网站上随意传播论文原文 PDF（IOP/Elsevier 版权协议）。

**解决**：网站上的 PDF 按钮链接的是作者自行整理的**精华汇总 PDF**（含核心公式、关键图片、结论解读），不是论文原文。论文原文 PDF 已从网站目录删除。LaTeX 源码在 `assets/pdf/essential-summary.tex`（第一篇）和 `assets/pdf/essential-summary-p2.tex`（第二篇），修改后用 `xelatex` 编译两遍。每篇论文的精华 PDF 命名规则：`essential-summary.pdf`、`essential-summary-p2.pdf`、`essential-summary-p3.pdf`…

### 11. 引用徽章（Dimensions/Altmetric）不显示

**问题**：al-folio v1.x 的 bib 模板通过 gem 引用，`dimensions = {true}` 和 `altmetric = {true}` 写在 `papers.bib` 里后，页面加载了 `badge.dimensions.ai/badge.js` 和 Altmetric 的 `embed.js`，但论文条目 HTML 里没有渲染出徽章容器（`__dimensions_embed_js__`）。这是 al-folio v1.x 插件层面的模板问题，gem 源码不在本地，无法直接覆盖修复。

**解决**：不依赖客户端 JavaScript 徽章。改为在 `_data/citations.yml` 里手动写入引用数（静态渲染），并通过自动化工作流定期更新（见第 12 条）。Dimensions 和 Altmetric 的 `true` 字段保留在 `papers.bib` 中不影响构建，但不会显示。Google Scholar 徽章需要 `google_scholar_id` 字段，但用户在中国大陆无法创建 Google 账号，此路不通。

### 12. 引用数自动更新工作流

**机制**：`.github/workflows/update-dimensions-citations.yml` 每周一北京时间 8 点自动运行，从 Dimensions 网站抓取每篇论文的引用数，比对 `_data/citations.yml` 旧数据，有变化则自动提交推送，触发网站重新构建。

**添加新论文到自动更新**：在工作流 Python 脚本的 `papers` 字典里加一行：
```python
papers = {
    "li2026quantitative": "10.1088/1402-4896/ae5134",
    "li2025global": "10.1016/j.ijnonlinmec.2025.105185",
    "新论文bib_key": "新论文DOI",  # 加在这里
}
```

**抓取原理**：Dimensions 的 badge 页面 `https://badge.dimensions.ai/details/doi/{DOI}` 内嵌了引用数数据。用 Python `urllib` 请求该页面，正则 `badge\?count=(\d+)` 提取引用数。不需要 API key，不需要注册，GitHub Actions 服务器可正常访问。

**手动触发**：在 GitHub Actions 页面找到 "Update Citations from Dimensions" 工作流，点 "Run workflow" 即可立即执行。

### 13. 添加新论文的标准流程

每篇新论文需完成以下步骤（参考前两篇的实现）：

1. **读论文**：用 `pdftotext -layout` 提取全文，通读摘要、方法、结论。用 PyMuPDF（`fitz`）精确裁剪关键图片（先 `page.get_text("blocks")` 找 Figure 标题 Y 坐标，再 `page.get_pixmap(matrix=Matrix(300/72, 300/72), clip=Rect(...))` 裁剪）。
2. **写 BibTeX 条目**：在 `_bibliography/papers.bib` 中新增条目，字段包括 `abbr`、`bibtex_show`、`title`、`author`、`journal`、`volume`、`pages`、`year`、`doi`、`dimensions`、`altmetric`、`pdf`、`preview`、`abstract`（只放英文原文摘要）、`additional_info`（一句话概括+提示精华PDF）、`selected`。
3. **期刊封面图**：IOP/Elsevier 官网封面图下载不了（返回 HTML），用 Python PIL 生成期刊风格封面图（顶部品牌色横栏+标题+作者+DOI），放到 `assets/img/publication_preview/`，文件名要短。
4. **精华汇总 PDF**：用 XeLaTeX 编写英文精华汇总（含核心公式带方框、关键图片、方法要点、核心结论、局限性、应用前景），编译两遍，放到 `assets/pdf/`。LaTeX 排版注意：图片用 `[htbp]` 浮动+`height=0.38\textheight,keepaspectratio` 限制高度+放宽浮动阈值（`\textfraction=0.07` 等），避免大段空白。
5. **动态**：在 `_news/` 新建 `.md` 文件 announcing 论文发表。
6. **引用数**：在 `update-dimensions-citations.yml` 的 `papers` 字典里加新论文的 DOI。在 `_data/citations.yml` 里加初始引用数。
7. **提交推送**：`git add -A && git commit && git push`。

### 14. LaTeX 公式渲染

**问题**：post 里的公式（`$$...$$` 和 `$...$`）不渲染，显示为原始文本。

**根因**：Jekyll 的 Kramdown Markdown 引擎需要显式配置 `math_engine` 才能将公式块传递给 MathJax。al-folio 默认只加载了 MathJax JS 脚本，但没有在 Kramdown 里声明数学引擎。

**解决**：在 `_config.yml` 的 `kramdown` 配置块中加入 `math_engine: mathjax`：
```yaml
kramdown:
  input: GFM
  math_engine: mathjax
  syntax_highlighter_opts:
    ...
```

**公式分隔符规范**：al-folio 的 MathJax 只认这两种：
- 行内公式：`$...$`（不要用 `\(...\)`）
- 显示公式：`$$...$$`（不要用 `\[...\]`）

### 15. Post 图片排版

**图题位置问题**：图片和斜体图注 `*Figure X: ...*` 必须**在同一行内用空行隔开**，否则 Markdown 渲染器会把图注当成图片的内联 companion 放在右侧。正确格式：
```markdown
![alt](path){: width="70%"}

*Figure X: caption text*
```

**图片尺寸**：用 `{: width="70%"}` 限制宽度为文本宽的 70%，避免撑满页面。

### 16. 首页 latest_posts 和 More 链接

**显示篇数**：在 `_pages/about.md` 的 front matter 中 `latest_posts.limit` 控制，当前设为 5。

**More 链接**：在 `_pages/about.md` 正文末尾添加 `[→ 全部论文笔记 / All Paper Notes](/blog/)` 即可，al-folio 在 latest_posts 模块后会继续渲染 about.md 的正文内容，这个链接会显示在文章列表下方。

### 17. 页面最大宽度

**配置**：`_config.yml` 中 `max_width: 1200px`。小于此宽度时自适应，超过后固定在 1200px 不再增大。CSS 变量 `--max-content-width` 自动引用此值。
