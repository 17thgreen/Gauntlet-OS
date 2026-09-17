# Idea ticket schema

One idea per file. Lives in `records/inbox/` until KILL, PIVOT, or KEEP.

```yaml
ticket_id: IDEA-YYYYMMDD-<slug>
object_sentence: <who pays, for what>
working_machine: <named thing we refuse to copy, or none>
copy_ban: <what we will not build>
critical_uncertainty: <the first question>
proposer: <human or agent>
status: INBOX | IN_FLIGHT | KILL | PIVOT | KEEP
admission: DRAFT | ADMITTED | RETURNED | BAN
execution: NOT_STARTED | IN_FLIGHT | FINISHED
evidence: UNTESTED | INCONCLUSIVE | FAIL | PASS
authority: NONE
pivot_of: <prior ticket id or none>
superseded_by: <new ticket id or none>
challenge_ref: <CHAL-... or none>
verdict_reason: <one paragraph after FINISHED>
survivor_ref: <FUTURE_IDEAS row or VC OPP- id after KEEP>
```

INBOX is not an official idea. KEEP is not an Experiment pack.
