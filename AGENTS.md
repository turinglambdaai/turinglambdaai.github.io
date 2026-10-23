# Main-site maintainer contract

**English** · [简体中文](AGENTS.zh-CN.md)

This repository is the TuringLambdaAI family front door at jrtx.site: hand-written static HTML/CSS, no dependencies or build step, served by GitHub Pages.

## Source map and local preview

- `index.html`: page structure, product cards and the Chinese/English i18n dictionaries.
- `assets/`: self-hosted variable fonts and images.
- `CNAME`: custom-domain binding.
- `README.md` / `README.zh-CN.md`: paired public introductions.

Open the HTML locally or use a static server such as `python3 -m http.server`.

## Verification and release

Pushing the default branch `master` deploys GitHub Pages: a push is a publication action. Check tag balance after every HTML edit; a missing closing paragraph previously broke product cards. For broad changes, preview every affected card. Check homepage cards, the corresponding product site, GitHub About and relevant Rivet documentation when product claims change.

Do not add external JS/CSS frameworks. Fonts stay self-hosted; external Google Fonts can block the first render in mainland China. Keep versions out of the main header; version details belong to product repositories/About. Update Chinese/English `data-i18n` content together.

## Portfolio and delivery ownership

`PORTFOLIO.md` and `PORTFOLIO.zh-CN.md` describe the same portfolio decisions. Delivery rules live in `docs/PRODUCT-STANDARD.md`, the dated product evidence/issue map in `docs/PRODUCT-REVIEW-2026-10.md`, and the website brief in `docs/HOME-PAGE-PLAN.md`. The dependency graph remains owned by Keel's `docs/family-architecture.md`; do not duplicate protocols or product implementation queues here.

## Documentation languages

Follow [the language policy](docs/DOCUMENTATION-LANGUAGES.md). Default public docs are English with complete Chinese entry paths, reciprocal links and the same user promises. API/protocol references have one normative English meaning; localized guides must preserve commands, identifiers and limits. Prices, quotas, expiry, cancellation, support scope, privacy and platform maturity must agree in both languages. Historical internal notes are not automatically a translation obligation.
