# TuringLambdaAI

A personal homepage and project showcase — live at **[jrtx.site](https://jrtx.site)**. It brings together visual learning platforms, developer tools, and a technical book under one roof, all built around a single idea: make complex technology intuitive.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)

**English** · [中文](README.zh-CN.md)

---

## Featured Projects

| Project | What it is |
|---------|------------|
| **[Visual Protocol](https://protocol.jrtx.site)** | Car communication protocols, finally intuitive — CAN, Ethernet, UDS, SOME/IP |
| **[Visual FOC](https://foc.jrtx.site)** | Motor control you can actually see — Clarke/Park, PI tuning, SVPWM |
| **[Taskly](https://taskly.jrtx.site)** | Cross-platform desktop task manager (Windows / macOS / Linux) |
| **[Racket 程序设计](https://racket.jrtx.site)** | An online book on the Racket programming language |

## Features

- **Bilingual** — full Chinese / English toggle with automatic browser-language detection
- **Light & dark themes** — follows the system preference, manually switchable, remembered across visits
- **Localized call-to-action** — WeChat QR for Chinese visitors, GitHub tile for everyone else
- **Shared design system** — an Anthropic-inspired warm palette, reused from Visual Protocol
- **Zero dependencies** — hand-written HTML/CSS with a small vanilla-JS i18n layer; no build step
- **Responsive** — lays out cleanly from desktop down to mobile

## Tech Stack

| Layer | Choice |
|-------|--------|
| Markup | Hand-written HTML5 |
| Styling | Plain CSS with custom properties (light / dark themes) |
| Scripting | Vanilla JS — i18n, theme toggle, localStorage persistence |
| Typography | Inter via Google Fonts |
| Hosting | GitHub Pages + custom domain (`jrtx.site`) |

## Quick Start

### 1. Clone

```bash
git clone https://github.com/turinglambdaai/turinglambdaai.github.io.git
cd turinglambdaai.github.io
```

### 2. Run

There is no build step. Either open `index.html` directly, or serve the directory:

```bash
# Option A: Python
python -m http.server 8000

# Option B: Node
npx serve
```

Then open http://localhost:8000.

## Project Structure

```
turinglambdaai.github.io/
├── index.html              Homepage — markup, inline i18n strings, theme & language logic
├── CNAME                   Custom domain (jrtx.site) for GitHub Pages
├── README.md               English readme (this file)
├── README.zh-CN.md         Chinese readme
└── assets/
    ├── css/
    │   └── main.css        Design system: tokens, layout, components, themes
    └── img/
        └── wechat-qr.jpg   WeChat official-account QR (shown to zh visitors)
```

## Custom Domain

`CNAME` points GitHub Pages at `jrtx.site`. At your DNS provider, add A records pointing to the GitHub Pages IPs:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```
