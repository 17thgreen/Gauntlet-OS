# Univer Office Harness — kit, not a tape

**Status:** `KIT / NOT A BUSINESS`  
**Authority:** none  
**Fleet:** none  
**Parked:** 2026-09-18  
**Source post:** https://x.com/shmidtqq/status/2100982569147814300  
**Upstream (OSS):** https://github.com/dream-num/univer  
**License:** Apache-2.0 on the core. **Univer Pro** is a separate commercial layer (collaboration, some import/export, server-side calc). Do not treat Pro as free.

This is a document runtime for agents. It is not two clocks, not a buyer, not a first dollar. Do not open an opportunities folder for it. Do not sell “Gauntlet Office Cloud.”

## What it actually is

Univer is an open-source Office engine (spreadsheets, docs, slides, canvas, relational tables) with a Facade API for browser and Node, Canvas rendering, and a formula engine. In 2026 they repositioned the README as “The Office Harness for AI Agents”: programmatic edit, output verification, isolated worktrees, human review.

That is the same instinct as no-self-grade: the model does not get to declare a workbook or deck **done**. Something else has to render it and fail it.

Launch-thread claims (“massive lead,” “100% of layout verification,” “true computer vision”) are copy. Use the repo and a spike, not the video.

## When to implement (allowed)

Use Univer only when an *existing* experiment already owes a real Office artifact:

| Experiment | Artifact Univer may own |
|------------|-------------------------|
| Lag Desk Examiner pack | `.xlsx` residue / hit table, not markdown theater |
| ALMANAC / tax-appeal | Rate tables, mail-merge source sheets, proof packets |
| Any playbook that must ship a deck | `.pptx` the Examiner can screenshot |

If the tape has no buyer yet, do not add Univer.

## When not to implement

- As a standalone product or marketplace.
- On the Lag Desk recorder hot path (or any 5-second poll).
- As a substitute for `cost.json` / JSONL (those stay text).
- Before reading the Apache vs Pro split. If the spike needs Pro-only import of `.xlsx` from Excel, stop and decide spend. Do not wrap a paid SDK and call it OSS.

## How to implement correctly

### 1. Pin and isolate

- Depend on a **pinned commit or release** of `dream-num/univer`, not `main`.
- Agent writes only inside an **isolated worktree / draft branch**. Production playbooks and `cost.json` stay untouched until a human merges.
- One artifact path per job: `records/.../artifacts/<cycle>/<name>.xlsx`. No rewriting INDEX.md from the harness.

### 2. Fail-closed verify (this is the point)

Do not accept “the agent said the slide is fine.”

Minimum gate before an Examiner pack is marked ready:

1. Programmatic edit via Facade / headless runtime.
2. Render (screenshot or export).
3. Lint: overflow, overlap, empty required sheets, schema columns match `cost.json` / pack schema.
4. Human visual diff (their “visual PR”). Merge is a Governor/Conductor act, not the writer agent.

If step 3 or 4 fails, the job is `not ready`. Same marking rules as the constitution: writer does not grade itself.

### 3. Seats

| Seat | Allowed |
|------|--------|
| Writer / Refiner | Edit inside the worktree |
| Examiner | Run lint + attach screenshot |
| Conductor | Queue the job after a tape exists |
| Recorder / Clock | **Never** |
| Live wallet / mail send | **Never** through Univer |

Grok may *drive* the Facade after a tape is live. Grok may not invent work so that Univer has something to do.

### 4. Spike before any fleet wiring (one evening)

```text
[ ] Clone pinned univer; hello-world sheet in Node headless
[ ] Write 7-row Lag Desk examine table to .xlsx; screenshot exists
[ ] Deliberately break a column; lint fails closed
[ ] Confirm no Pro API was required
[ ] Stop. Do not productize.
```

If the hello-world needs Pro or a browser-only path we cannot run on a VPS, cemetery the integration and keep Examiner output as markdown + CSV.

### 5. What “done” looks like

Done is **not** “Univer is installed.” Done is: one existing pack emits a verified Office file that failed a bad input and passed a good one, with a screenshot in the cycle folder. Anything short of that is a bookmark.

## Relation to the shop

Lag Desk and Pace Desk are tapes. This is furniture. Yaman rule still applies: we sell outcomes (leads, residue histograms, tax packets), not an office runtime.
