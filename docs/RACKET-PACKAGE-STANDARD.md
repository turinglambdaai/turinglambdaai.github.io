# Racket package documentation and quality standard

**English** · [简体中文](RACKET-PACKAGE-STANDARD.zh-CN.md)

Status: maintainer guidance, 2026-10-27. This is **not** a product landing-page template or a mandate to restructure every repository. It complements [documentation languages](DOCUMENTATION-LANGUAGES.md) and is tracked under [package-quality issue #7](https://github.com/turlamai/turinglambdaai.github.io/issues/7); customer applications and their sites remain in [public presentation](PUBLIC-PRESENTATION.md) / [issue #5](https://github.com/turlamai/turinglambdaai.github.io/issues/5).

## Classification before any edit

- **First-party Racket package** (e.g., `crc`, `ihex`, `srec`, `isotp`, `uds`, `pcap`): maintain a package-native README, normative Scribble, tests and accurate catalog metadata. **No independent marketing website needed.**
- **Desktop/service application:** apply the product homepage, install, privacy, support and screenshot rules instead. Some apps use Racket internally; this does not make them packages.
- **Books, archives and community content:** maintain provenance, accessibility, links and errata, without fabricating an API.
- **Imported/forked/archived Racket projects:** check repository provenance, license and actual ownership before changing. Do not sweep third-party mirrors or wholesale Racket upstream forks into first-party standards.

## The README is a useful entry point, not a second manual

Suggested lightweight ordering (omit sections that do not apply):

1. Name + one-line **purpose**, one or two concrete use cases, truthful stability/platform/system dependencies; short language link.
2. **Install** using the actual catalog *if verified* (`raco pkg install <package>`) or a repository source, clearly distinguished; no invented badges, docs URLs or claims of catalog publication.
3. **A complete and runnable minimal example** with `#lang`, the exact `require` collection, copyable input and a checked outcome. Link to an executable file or evaluated Scribble example, and have CI run it.
4. **API documentation** in Scribble with contracts, side effects, error behavior, resource ownership, limits and version compatibility. README gives a brief overview and links to it, rather than duplicating `@defproc` pages.
5. **Development**: the correct install/link command, tests and documentation/dependency checks, plus how to report bugs. State real supported Racket versions/platform restrictions where evidence exists.
6. License and attribution. Keep only useful badges; don't promise high performance without reproducible benchmark environment/data.

For paired English/Chinese README files, keep install commands, module names, semantics, limitations and tested outputs the same. Technical API identifiers remain normative in code/Scribble; no forced translation of every `@defproc` entry.

## Idiomatic package structure and tools

A single-collection package may keep `info.rkt`, `main.rkt`, `scribblings/` and `tests/` in one collection. A multi-collection package uses a package-root `info.rkt` with `(define collection 'multi)` and collection-level `info.rkt` for its `scribblings`. Do not assume package and collection names are interchangeable. Prefer correct `deps` / `build-deps`, avoiding unnecessary runtime dependencies, but assess an existing package's published layout before moving tests or docs.

Typical commands **after confirming the real package/collection names**:

```sh
raco pkg install --auto --link .
raco test -p <actual-package-name>
raco setup -l <collection-name> --check-pkg-deps
racket examples/quickstart.rkt   # only when this file exists
```

The `<...>` terms above are placeholders, **not** commands to paste literally. `raco test -p` runs package tests; `raco setup` compiles the collection, renders its registered Scribble manual and checks dependencies. For larger packages, choose a scoped docs build that resolves all subcollections. Reuse already working CI matrices; do not add irrelevant GUI tests to protocol libraries.

## Quality gates tied to observable failures

- **API/semantics**: RackUnit unit/contract tests, negative/error cases, edge cases and domain-specific reference vectors; use property/round-trip tests where helpful.
- **Examples**: run the exact committed quickstart on CI, or use `scribble/example` and render the documentation to evaluate it. Do not leave invalid pseudo-Racket snippets, undeclared files, or undocumented network/hardware requirements.
- **Package integrity**: clean `raco pkg install`, `require` public module, `raco test -p`, Scribble build and dependency check. Do not silently weaken existing CI to green.
- **Compatibility**: test actual supported Racket and OS matrix, no speculative platform badges; report skipped environmental tests and hardware/network gates explicitly.
- **Documentation trust**: distinguish a verified release/catalog entry from plans; link source docs when the published docs URL is not confirmed; preserve old public API semantics or document migration with tests.

## Incremental rollout

Pilot in `crc` and `ihex`, which already have Scribble/test infrastructure: fix observed executable-doc errors, build docs/dependency checks in CI and add concise, helpful README developer paths. Then select other **verified first-party** packages by meaningful gaps, not an undifferentiated count of modified repositories. No new website, design framework, marketing hero or runtime feature should be introduced solely for documentation consistency.

Official references: [Creating packages](https://docs.racket-lang.org/pkg/getting-started.html), [package metadata](https://docs.racket-lang.org/pkg/metadata.html), [Scribble setup](https://docs.racket-lang.org/scribble/how-to-doc.html), [raco test](https://docs.racket-lang.org/raco/test.html), [dependency checking](https://docs.racket-lang.org/raco/setup-check-deps.html).
