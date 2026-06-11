# Question Index

Purpose: a compact answer map for user questions that are easy to lose across
task packets, derivation notes, logs, and transparency files. This file does
not replace task outcomes or derivations. It points to the first place to read.

## Update Rule

Add a row only when a question is likely to be searched for later. Keep the
answer short, and point to the detailed task outcome, derivation note, draft
section, or log entry. Do not duplicate long arguments here.

## Recent Answer Map

| Question | Short answer | First place to read | Supporting trail |
|---|---|---|---|
| How should repository cleanup proceed slowly? | Add navigation and traceability layers first. Do not migrate, archive, rename, or delete historical material until a separate cleanup task says to do that. | `manuscript/tasks/M58-start-here-navigation/outcome.md` | `manuscript/START-HERE.md`; `manuscript/decision-log.md` |
| Can each task have a low-overhead note on what was done and which questions were answered? | Yes. New substantial tasks should use a folder with `task.md` and compact `outcome.md`; legacy flat packets remain valid. | `manuscript/tasks/M57-task-folder-workflow/outcome.md` | `manuscript/tasks/README.md`; `manuscript/manuscript-rules.md` |
| Where should someone start when the project feels hard to overview? | Open `manuscript/START-HERE.md`, then follow its table to the dashboard, paper map, task board, task outcomes, or logs. | `manuscript/START-HERE.md` | `manuscript/project-dashboard.md` |
| Are the robust fourth-cumulant sample moments ordinary row-level GMM moments? | No. Concentrated fourth-cumulant entries are generated smooth functions of primitive sample moments; M52 implements the central-delta route after the M56 audit. | `manuscript/derivations/m56-robust-cumulant-gmm-generated-moment-audit.md` | `manuscript/tasks/M56-robust-cumulant-gmm-generated-moment-audit.md`; `manuscript/simulations/m52_source_correct_evidence.md` |
| How should Section 4 explain why the robust moments hold at `B0` and how they are computed? | Section 4 should distinguish transformed-noise covariance `Omega(B)` from transformed-residual covariance `S(B)`, then explain the candidate-by-candidate generated-moment computation. | `manuscript/tasks/M55-main-text-robust-moment-explanation.md` | `manuscript/draft.md`; `manuscript/derivations/m54-stepwise-transformed-noise-moments.md` |
| Should the paper switch from the `diag(B)=1` chart to unit structural-shock variance normalization? | No, not for the first paper. M54 keeps the manuscript in the common `diag(B)=1` chart; DW's unit-variance scaling stays internal to recovered-shock standardization. | `manuscript/derivations/m54-stepwise-transformed-noise-moments.md` | `manuscript/tasks/M54-stepwise-moment-derivation-and-normalization-audit.md`; `manuscript/decision-log.md` |
| What is the source-correct bivariate Drautzburg-Wright moment menu? | GMM1 uses `112`, `122`, `1112`, `1122`, and `1222`; GMM2 drops only `1122`. The no-noise covariance restriction is treated as a separate B-plane screen. | `manuscript/derivations/m49-dw-source-and-noisy-moment-audit.md` | `manuscript/tasks/M49-dw-source-and-noisy-moment-audit.md`; `manuscript/simulations/m52_source_correct_evidence.md` |
| Was the M48 DW moment-normalization audit reliable enough to rely on? | No. M48 is historical and source-insufficient; M49 supersedes it as the source-backed DW audit. | `manuscript/derivations/m48-dw-moment-normalization-audit.md` | `manuscript/derivations/m49-dw-source-and-noisy-moment-audit.md`; `manuscript/decision-log.md` |
| What are the old flat task packets now? | They are labeled in place. Most M47 and M49-M56 packets are current references; `_template.md` is historical; M48 remains superseded by M49. | `manuscript/tasks/LEGACY-STATUS.md` | `manuscript/tasks/M60-legacy-status-labels/outcome.md` |
| How will the question index stay current? | Future task outcomes now include an index-update decision: update `QUESTION-INDEX.md` only for answers likely to be searched for later, otherwise mark it not needed. | `manuscript/tasks/M61-question-index-maintenance/outcome.md` | `manuscript/tasks/_folder-template/outcome.md`; `.codex/skills/write-standalone-manuscript/SKILL.md` |
| What cleanup remains after M58-M61? | The main navigation, question index, legacy status labels, and future closeout rule are in place. Future cleanup can add archive guidance only if old files still feel noisy in practice. | `manuscript/tasks/M61-question-index-maintenance/outcome.md` | `manuscript/tasks/M58-start-here-navigation/outcome.md`; `manuscript/tasks/M59-question-index/outcome.md`; `manuscript/tasks/M60-legacy-status-labels/outcome.md` |
