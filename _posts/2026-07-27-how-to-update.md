---
layout: post
title: 如何更新这个主页（写作指南）
date: 2026-07-27 09:00:00+0800
description: 添加论文、项目、动态和博客文章的速查说明 / A cheat sheet for updating this site
tags: [research-notes]
categories: [notes]
featured: false
---

这篇笔记汇总了更新本站各个板块的方法，建议保留（也可以随时删除）。
This post is a cheat sheet for updating every section of this site. Keep it around, or delete it anytime.

## 添加一篇论文 Adding a publication

打开 `_bibliography/papers.bib`，仿照示例添加一个 BibTeX 条目即可，论文页会自动按年份倒序展示。

- 标记 `selected = {true}` 的论文会出现在首页「Selected Publications」
- 用 `abstract` 字段写摘要（可中英对照），用 `additional_info` 字段写**核心结论**（支持 Markdown）
- 用 `pdf`、`code`、`video`、`slides` 等字段挂对应材料，按钮会自动出现在论文条目下方
- 文件头部注释里有全部可用字段的说明

## 写一篇笔记 Writing a post

在 `_posts/` 目录新建 `YYYY-MM-DD-标题.md`，复制《论文笔记模板》的 front matter 后写作即可。支持数学公式、代码块、图片。

## 添加一个项目 Adding a project

在 `_projects/` 目录新建 `.md` 文件。想写详细介绍就写正文；想让卡片直接跳转到 GitHub 仓库，在 front matter 里加一行 `redirect: 仓库地址` 即可。`importance` 数字越小排序越靠前。

## 添加一条动态 Adding news

在 `_news/` 目录新建 `.md` 文件，参考已有示例。首页最多显示 5 条（在 `_pages/about.md` 里调整）。

## 发布 Publishing

改完之后：

```bash
git add -A
git commit -m "更新内容"
git push
```

push 后 GitHub Actions 会自动构建，GitHub Pages（境外）和 Gitee Pages（国内）两边都会更新（首次部署配置见仓库根目录的《部署指南.md》）。

> 提示：正文中所有 `TODO-HOMEPAGE` 标记的地方都是需要替换的个人信息，全局搜索这个关键词即可找到它们。
