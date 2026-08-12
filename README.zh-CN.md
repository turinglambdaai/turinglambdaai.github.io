# TuringLambdaAI

个人主页与项目导航 — 上线于 **[jrtx.site](https://jrtx.site)**。把可视化学习平台、开发者工具和技术书籍汇集在一处，围绕同一个理念：把复杂技术做直观。

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)

[English](README.md) · **中文**

---

## 精选项目

| 项目 | 简介 |
|------|------|
| **[Visual Protocol](https://protocol.jrtx.site)** | 汽车通信协议，从未如此直观 — CAN、Ethernet、UDS、SOME/IP |
| **[Visual FOC](https://foc.jrtx.site)** | 电机控制原理，看得见摸得着 — Clarke/Park、PI 调参、SVPWM |
| **[Taskly](https://taskly.jrtx.site)** | 跨平台任务管理桌面应用（Windows / macOS / Linux） |
| **[Racket 程序设计](https://racket.jrtx.site)** | 一本关于 Racket 编程语言的在线技术书 |

## 特性

- **中英双语** — 完整的中 / 英文切换，自动识别浏览器语言
- **明暗主题** — 跟随系统偏好，可手动切换，跨次访问保持记忆
- **本地化引导** — 中文访客展示微信公众号二维码，其他地区展示 GitHub
- **统一设计系统** — Anthropic 风格的暖色调，复用自 Visual Protocol
- **零依赖** — 纯手写 HTML/CSS 加一层极简 vanilla-JS 国际化，无需构建
- **响应式** — 从桌面到移动端布局自适应

## 技术栈

| 层 | 选型 |
|----|------|
| 结构 | 手写 HTML5 |
| 样式 | 原生 CSS，基于 CSS 自定义属性（明 / 暗主题） |
| 脚本 | 原生 JS — 国际化、主题切换、localStorage 持久化 |
| 字体 | Inter（Google Fonts） |
| 托管 | GitHub Pages + 自定义域名（`jrtx.site`） |

## 快速开始

### 1. 克隆

```bash
git clone https://github.com/turinglambdaai/turinglambdaai.github.io.git
cd turinglambdaai.github.io
```

### 2. 运行

无需构建。直接打开 `index.html`，或起一个本地静态服务：

```bash
# 方式一：Python
python -m http.server 8000

# 方式二：Node
npx serve
```

然后访问 http://localhost:8000。

## 项目结构

```
turinglambdaai.github.io/
├── index.html              主页 — 标记、内联 i18n 文案、主题与语言逻辑
├── CNAME                   GitHub Pages 自定义域名（jrtx.site）
├── README.md               英文说明
├── README.zh-CN.md         中文说明（本文件）
└── assets/
    ├── css/
    │   └── main.css        设计系统：变量、布局、组件、主题
    └── img/
        └── wechat-qr.jpg   微信公众号二维码（向中文访客展示）
```

## 自定义域名

`CNAME` 将 GitHub Pages 指向 `jrtx.site`。需在 DNS 服务商添加指向 GitHub Pages IP 的 A 记录：

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```
