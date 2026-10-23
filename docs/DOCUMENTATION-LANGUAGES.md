# Documentation languages

**English** · [简体中文](DOCUMENTATION-LANGUAGES.zh-CN.md)

Status: adopted family documentation policy, 2026-10-23. This policy serves Chinese-speaking users and the global English-speaking community. It does not change software behavior, wire identifiers, source licenses or product prices.

## Public entry points

Use English for default public documentation (`README.md`, `PRICING.md`, `docs/getting-started.md`). Provide complete Simplified Chinese counterparts (`README.zh-CN.md`, `PRICING.zh-CN.md`, `docs/getting-started.zh-CN.md`) with reciprocal language links near the title. Chinese is a supported user path, not a short appendix; English must not be only a summary of a Chinese commercial plan.

For a library, prioritize the README, installation/first useful example, supported-platform limits, troubleshooting and a path to API/reference documentation. A global contributor must be able to understand and use the library without reading Chinese or private chat history. English public API and protocol references already present remain the authoritative technical definitions; Chinese guides link to them explicitly.

For a product, keep getting started, use/recovery/update instructions, free/paid scope, trial/expiry, renewal/cancellation, quotas, privacy and key/data destinations equally discoverable in both languages. Translate the entire applicable promise, including limitations and launch status, rather than only feature headlines. Product websites keep equivalent Chinese/English content and language-aware links to documentation.

## One technical meaning

English API/protocol/security semantics are the normative technical source, with one set of examples, schema fixtures and test vectors. A translation explains the same contract; it cannot change accepted inputs, failure behavior or maturity. Preserve API names, CLI flags, paths, schema identifiers and copyable commands. Do not create separate Chinese/English implementations or queues.

Public English and Chinese product policies must agree on prices/currencies, quantities, supported platforms, time windows, trial/expiry, cancellation, renewal, data retention, free scope and implementation status. Neither translation may invent a live purchase, unlimited allowance, hardware qualification or supported mobile platform. The underlying reviewed offer/policy and repository specification own behavior; prose does not silently modify it. Translate a changed user promise in the same PR/commit, or explicitly leave it unshipped until its paired public text is ready.

If a translation conflicts with a technical reference, correct it before claiming the path ready. Do not use the English technical-reference convention to dismiss an inconsistent Chinese purchase promise: block that offer until both languages agree. Public checkout terms require their own explicit precedence and applicable consumer protections; this engineering policy does not decide those terms.

## Scope and maintenance

Not every historical issue, commit message, incident note or internal scratch document needs two full copies. New reusable maintainer guidance, contribution guides and issue/PR summaries should be accessible in English; local working notes may use either language. A single English roadmap/ADR/changelog is acceptable. Do not translate protocol specifications into a second normative specification merely to count files.

Prioritize complete public journeys over translating the entire archive. The current known gap is Chinese-heavy internal agent material and historical review/issues; these are not evidence that all repository documentation is bilingual. Mark a missing or stale translation plainly; link to the available document without silently switching language or claiming parity.

## Review checklist

1. Open the English and Chinese entry paths; check reciprocal links and the intended language of linked files.
2. Compare commands/examples and all quantitative or contractual facts: price, quota, retention, platform, time and status. Preserve pending/failed/unrun limitations.
3. Check website strings in both language modes, including plans, help, feedback and privacy; a localized page should link to its corresponding document language when available.
4. Run relevant documentation/link/build checks. A translation-only change needs no new runtime tests unless a command, generated example or executable documentation changes; existing required CI still applies.
5. Record files translated and remaining gaps. Do not report every document or platform as complete based on README pairs alone.
