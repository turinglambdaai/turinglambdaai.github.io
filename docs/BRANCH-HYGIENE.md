# Branch hygiene / 分支清理

Source policy: [GitHub issue #7](https://github.com/turinglambdaai/turinglambdaai.github.io/issues/7) for Racket libraries and [site Issue #5](https://github.com/turinglambdaai/turinglambdaai.github.io/issues/5) for product documentation. This repo's **default branch is `master`**.

Keep the default branch, all protected branches, and every actively developed branch (including open PRs). A closed-but-unmerged branch and a branch with no corresponding merged PR **must not be deleted automatically**, because they can contain unpublished work. Never infer obsolescence solely from the branch name or age.

The [`prune-merged-branches.yml` workflow](../.github/workflows/prune-merged-branches.yml) is deliberately restricted to this single GitHub repository and starts on installation, on merged PRs, or by manual dispatch. For each local branch, it refuses to delete unless:
- the branch is nondefault and unprotected;
- no open PR uses it;
- a **merged PR in the same repository** names this branch and has an **exact matching current head SHA**.

This covers squash merges while preventing deletion of work pushed after the merge. Workflow outcome must be checked; policies that deny Actions `contents: write` may leave all branches untouched. Forked heads and unreviewed/unmerged branches stay intact. **It does not clean 100 other repositories.** Apply per repository only after reviewing the actual branch and PR topology. For a human-verified abandoned branch without a merged PR, archive/cherry-pick unique commits before manual deletion. No force pushes, no active-work pruning.

中文说明：只自动删除本仓已合并 PR、HEAD SHA 未变、非受保护且没有开放 PR 的分支；默认分支、未合并、来源不明、有新提交或开发中的分支保留。不同仓库需要分别验证并执行，不能因为名字旧就删除。
