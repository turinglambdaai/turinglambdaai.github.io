# PORTFOLIO — 产品组合与授权策略

每个项目走哪条轨道、用什么授权形态、按什么节奏推进。本文是组合层面的唯一权威；
单个产品的价格与授权细节以该产品仓库的 `PRICING.md` / `docs/licensing-model.md` 为准。

**总原则：收费归属是前置决策，一开始就定死。** 哪些产品适合收费（轨道 1–3）、哪些
永久免费（轨道 4），在进入推广阶段之前确定并随本档维护；推广开始后不再改结构。
当前全部产品处于打磨期，尚未进入推广阶段，不急于变现。授权形态现在定型（避免后期
反复），收费动作后置到产品稳定之后；commerce 部署后，所有付费形态统一走
offer/policy/issuance，产品侧零改动。

## 轨道与授权形态

### 1. 商业支柱 — B2B 专业工具，养活独立开发的主力

| 产品 | 源码许可 | 商业形态 |
|---|---|---|
| Autarx | 专有 | 永久买断 + 更新窗 + 试用 + 团队席位 |
| FlashPilot | AGPL-3.0 | 同 Autarx；硬件在环验证与刷写可靠性是护城河 |
| gPTP Studio | Apache-2.0 开源核心 | 已定调并落地：Pro = 官方签名构建 + 365 天更新窗 + 试用 + 团队席（见其 `PRICING.md`）|

- 共同点：买方是拿预算的工程师与团队；产品离线可用，**无托管成本，所以不做月订阅**——
  「续购更新窗即为续费」（gptp-studio 先例）。
- 开源边界：源码许可与官方分发权益分离——官方 Pro 卖的是签名构建、更新、支持与验证
  资产，不是「禁止读源码」（gptp-studio `docs/licensing-model.md` 的结论全家族适用）。

### 2. 消费买断 — BYO-key，无边际成本，一次性买断诚实可行

| 产品 | 源码许可 | 商业形态 |
|---|---|---|
| Booklight | AGPL-3.0 | 永久买断 + 更新窗 + 试用；模型自带 key，不自建托管 |
| PodLens | AGPL-3.0 | 同 Booklight |

### 3. 免费 + 托管 Pro — 只有真实服务成本才配收订阅

| 产品 | 源码许可 | 商业形态 |
|---|---|---|
| HackDigest | AGPL-3.0 | 自带 key 全功能免费；托管翻译/同步层走订阅 |
| Publy | AGPL-3.0（核心） | CLI 开源免费；托管发布服务后期订阅 |

订阅只存在于这一轨道：托管的持续成本与持续收入同源，才是诚实的订阅。

### 4. 社区与引流 — 永久免费，不作为收入来源

| 产品 | 许可 | 定位 |
|---|---|---|
| Fulcrum | BUSL-1.1 → MIT（2030-09-28 起或各版本首发四周年，以先到者为准） | 竞争品类（启动器），源码可得建信任、防闭源竞品；BUSL 期间定位免费 |
| Taskly | AGPL-3.0 | 免费；Pro 功能（如有）观望 |
| MoveBit / Payback | MIT | 完全赠送，建口碑 |
| Threadly / SyncPilot | AGPL-3.0 | 社区善意；SyncPilot 依附第三方 Resilio，不作为生意 |
| RegexMate | MIT | agent 生态分发器，最大化采用 |
| Pitboard | MIT | 汽车内容资产，为汽车线背书 |
| Keyward | AGPL-3.0 | 安全工具开源即信任；同时是家族自用的发布基础设施 |
| Racket 程序设计 / Yinwang Archive | — | 内容与生态引流 |

RelayPilot：架构 Alpha、无公开仓库，网络工具敏感度高——私有观望，不进收费计划。

### 基础设施 — 全部开源，是产品线的放大器，不是利润中心

rivet / glaze / keel（MIT）、permit / commerce（Apache-2.0）、
Racket 协议与数据格式库族（uds / isotp / dbc / crc / pcap / …）。

## 授权形态词汇（与 Permit/commerce 一一对应）

- 永久买断 + 更新窗：`updates_through`（commerce 已支持按支付证据派生 duration）
- 试用：全功能限时（Permit trial 语义）
- 团队席位：`named_seats`
- 订阅：commerce 订阅语义（paid-through）——仅轨道 3 使用

## 节奏

1. **现在（打磨期，推广未开始）**：打磨与定位对齐；全部产品免费/源码可得；不做任何价格预告，不做推广投放。
2. **第一棒**：gptp-studio — 模式已落地，等产品稳定即开卖。
3. **第二棒**：Booklight / PodLens — 买断制接入成本最低（两个 offer 即接入）。
4. **第三棒**：Autarx / FlashPilot — B2B 席位与验证服务，护城河最深，打磨期最长。
5. **commerce 部署后**：所有付费形态走统一 offer/policy/issuance。

## 文档同步约定

- 三个检查面：主站卡片 ↔ 产品 README ↔ GitHub About，改文案必须三面核对。
- 产品 README 必带 license badge；授权形态以本文档与产品站为准。
- 价格只进产品仓库 `PRICING.md`，且在收费开始时（而非之前）发布。
