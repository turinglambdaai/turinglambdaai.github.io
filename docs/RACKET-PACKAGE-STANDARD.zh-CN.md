# Racket Package 文档与质量规范

[English](RACKET-PACKAGE-STANDARD.md) · **简体中文**

维护规范，2026-10-27。**这不是产品官网模板，也不要求无差别重构全部仓库。** Racket 库专项由 [Issue #7](https://github.com/turlamai/turlamai.github.io/issues/7) 跟踪；用户产品仍采用[公开展示规范](PUBLIC-PRESENTATION.zh-CN.md)及 [Issue #5](https://github.com/turlamai/turlamai.github.io/issues/5)。

## 先分类，后修改

- **自研 Racket Package**（如 `crc`、`ihex`、`srec`、`isotp`、`uds`、`pcap`）：以 README、Scribble API 文档、测试、正确的包元数据为中心，**不必建设独立营销官网**。
- **桌面应用/服务产品**：继续执行产品主页、安装、隐私、更新、支持和截图标准。使用 Racket 编写不等于它只是一个 Package。
- **书籍、归档、社区内容**：侧重来源、链接、无障碍和勘误，不虚构 API。
- **Fork、镜像、归档、上游源码**：先核实来源、许可和维护权属，不把第三方代码强行纳入自研包的改造清单。

## README：让第一次使用简单成功

建议包含以下必要内容，按库的实际情况精简：

1. **用途、适用场景、稳定程度、必要系统依赖**以及中英文互链。
2. **真实安装方式**：仅在核实已上架 Racket Catalog 时使用 `raco pkg install <package>` 的正式包名；否则提供仓库源码安装。不能凭空添加文档网址、版本或徽章。
3. **完整、可直接运行的最小示例**：明确 `#lang`、`require`、输入、预期结果；链接源码中的示例文件或 Scribble 可执行示例，并纳入 CI。
4. **Scribble API 文档**：说明导出模块、契约、错误、资源和兼容性。README 只给导航，不复制维护第二份完整 API。
5. **开发与测试**：本地安装/链接、测试、文档构建和依赖检查命令、问题反馈方式。
6. **许可证及署名**。性能数据应有可复现的基准环境；不写无证据的吞吐量承诺。

双语 README 的安装命令、模块名称、参数语义、限制、测试输出应一致。技术契约以代码和 Scribble 为准，不强制翻译每一页 API 参考。

## 遵循 Racket 原生包结构

单 collection 包可使用顶层 `info.rkt`、`main.rkt`、`scribblings/`、`tests/`。Multi-collection 包在包根 `info.rkt` 定义 `(define collection 'multi)`，各 collection 的 `scribblings` 应注册到对应的 collection 级 `info.rkt`。不要误认为 package 名一定等于 collection 名；应依据代码布局配置 `deps` 与 `build-deps`，避免不必要运行时依赖，但不要为追求模板破坏已发布包。

核实真实包名和 collection 后，通常运行：

```sh
raco pkg install --auto --link .
raco test -p <actual-package-name>
raco setup -l <collection-name> --check-pkg-deps
racket examples/quickstart.rkt   # 文件存在时才运行
```

上面尖括号是占位符，不能原样执行。`raco test -p` 对包执行测试；`raco setup` 构建并注册 Scribble 文档，同时检查依赖。对多 collection 或特殊布局，可选择合适的包级检查。已有跨平台 CI 保留，不要给协议库硬塞 GUI 验收。

## 必须真实验证

- RackUnit 测试需要覆盖正常、边界、错误、契约、回归场景；算法/协议包应有标准向量与必要的往返/性质测试。
- README 示例要在 CI 中直接执行；或通过 `scribble/example` 在文档构建时执行。不保留无法运行的“伪代码式”Racket 示例。
- 检查干净安装、公共模块 `require`、`raco test -p`、Scribble 编译与依赖声明。失败就修复，不能通过跳过验收伪装成功。
- 跨 Racket 版本/系统仅宣称真实验证结果。需要硬件或网络的测试应说明环境门禁。
- 文档只引用已验证的 release/catalog 地址；未核实线上发布状态就链接仓库内的 Scribble 源文件。公共 API 变更要提供兼容性说明和测试。

## 推进策略

先以已有 Scribble 和测试基础的 `crc`、`ihex` 做试点：修正文档示例、将示例和文档构建纳入 CI，补齐 README 导航。然后按缺口逐步处理其他**确认自研维护**的包，不以改动仓库数量为目标，不新增单独官网、营销头图或无关运行时功能。

官方参考：[包创建](https://docs.racket-lang.org/pkg/getting-started.html)、[包元数据](https://docs.racket-lang.org/pkg/metadata.html)、[Scribble](https://docs.racket-lang.org/scribble/how-to-doc.html)、[raco test](https://docs.racket-lang.org/raco/test.html)、[依赖检查](https://docs.racket-lang.org/raco/setup-check-deps.html)。
