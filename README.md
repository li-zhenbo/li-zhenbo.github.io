# 个人学术主页 · Personal Academic Homepage

基于 [al-folio](https://github.com/alshedivat/al-folio) 主题搭建的中英双语学术主页，展示发表论文与核心结论、配套代码、研究笔记和学术简历。

- 境外访问（GitHub Pages）：`https://你的用户名.github.io`
- 国内访问（Gitee Pages）：`https://你的用户名.gitee.io`

**上手请阅读 → [部署指南.md](部署指南.md)**（占位信息替换、GitHub/Gitee 双端部署、日常更新方法，全部在里面）。

A bilingual (EN/中文) academic homepage built with the al-folio theme: publications with key findings, code, research notes, and CV. Dual-hosted on GitHub Pages (international) and Gitee Pages (mainland China) with automatic sync via GitHub Actions. See 部署指南.md for setup instructions (in Chinese).

## 目录结构 Where things live

| 路径 | 内容 |
| --- | --- |
| `_bibliography/papers.bib` | 论文列表（BibTeX，附核心结论与代码链接） |
| `_projects/` | 代码 / 项目卡片 |
| `_posts/` | 博客 / 研究笔记 |
| `_news/` | 首页动态 |
| `_data/cv.yml` | 学术简历数据 |
| `_data/socials.yml` | 邮箱、Scholar、GitHub/Gitee 等链接 |
| `_pages/about.md` | 首页自我介绍 |
| `assets/img/`、`assets/pdf/` | 照片、论文 PDF、CV PDF 等静态文件 |

所有待替换的占位信息都带 `TODO-HOMEPAGE` 标记，全局搜索即可找到。
