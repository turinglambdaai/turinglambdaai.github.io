# AGENTS.md

turinglambdaai 家族主站（jrtx.site）——纯静态 HTML/CSS 单页，零依赖零构建，GitHub Pages 直出。

## 结构

- `index.html` — 主页全部内容（产品卡片、i18n 文案都在这一个文件）
- `assets/` — 字体（自托管可变字体）与图片
- `CNAME` — jrtx.site 域名绑定
- `README.md` / `README.zh-CN.md` — 双语说明

## 常用命令

无构建系统：本机直接开 `index.html` 或起任意静态服务器预览（如 `python3 -m http.server`）。

## 验证与发版

- push master（默认分支）即部署 GitHub Pages，**推送即发布**。
- 改 HTML 后必须跑标签配平检查——历史上丢 `</p>` 导致产品卡渲染成空壳的事故发生过，改动大时逐卡预览。
- 产品卡与 GitHub About/产品站是三个检查面：改文案时核对主站卡片、对应产品站、rivet docs 是否同步。

## 仓库特定规矩

- 零依赖：不引外部 JS/CSS 框架；字体只走自托管（禁 Google Fonts，大陆阻塞首屏）。
- 页面含 data-i18n 双语文案，改动须中英同步。
- 头部不放版本号（版本信息只在各产品仓库/About 承载）。

## 产品组合与交付治理

组合归属以 `PORTFOLIO.md` 为准；交付基线见 `docs/PRODUCT-STANDARD.md`，本轮逐产品证据与 issue 入口见 `docs/PRODUCT-REVIEW-2026-10.md`，主页改版执行简报见 `docs/HOME-PAGE-PLAN.md`。库间依赖图仍以 Keel 的 `docs/family-architecture.md` 为准，不在主站另造协议或复制各仓实施队列。
