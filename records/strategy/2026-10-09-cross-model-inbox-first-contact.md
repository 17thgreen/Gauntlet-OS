# Record: first cross-model inbox exchange

**Date:** 2026-10-09
**Prepared for:** Logan M
**Status:** Recorded result of a working trial in the Terra Firma lab. This
record adopts nothing into the Gauntlet-OS constitution. The protocol is
[AGENT_INBOX](../../protocols/AGENT_INBOX.md) (trial, g1, adapted from the lab's r2; the measurements below were made under r2).

## What happened

Three agents on three different platforms exchanged handoffs through GitHub on
2026-10-09, with no person carrying the messages:

- **Claude**, the merge desk, in a Claude Code cloud session;
- **Astra**, the integration lead, in an OpenAI conversation;
- **the Conductor**, who runs the lab's fleet from Grokbot.

Before this, the owner copied every message from one chat into another by
hand.

Each agent got one draft pull request as its inbox in the lab's private
repository. Each platform wakes its agent on new comments on that PR:
- Claude: a session subscription to PR activity;
- Astra: an event-triggered task attached to her existing conversation;
- the Conductor: a listener on PR comments and pushes, plus an hourly backup
  check.

## Evidence

Comment-creation timestamps, UTC, read from GitHub:

| Test | Request | Answer | Request to answer | Answer to sender's session |
|---|---|---|---|---|
| Claude → Astra → Claude | `claude-20261009-1` at 21:21:56 | `astra-20261009-2` at 21:22:42 | 46 s | about 2 s |
| Claude → Conductor → Claude | `claude-20261009-4` at 21:28:42 | `conductor-20261009-2` at 21:29:03 | 21 s | about 2 s |

Each request asked the recipient to quote one protocol rule from a named commit.
Astra quoted rule 4 and the Conductor rule 8, both verbatim.

How to read the numbers:
- **Request to answer** includes the recipient's own processing. By Astra's
  clock, her run first handled the request 20 s after it was posted.
- **Answer to sender's session** is when the sender's session queued the
  answer, about 2 s after it was posted.
- **"Ready" messages:** both agents' messages announcing their triggers were
  live also reached Claude's session within 2 s.

The full transcript stays in the lab's private repository.

## Design credits

- **Claude** proposed GitHub as the shared channel, built the inboxes and the
  protocol, and ran both tests.
- **Astra** reworked the design before it was built:
  - comments rather than commits;
  - one inbox per recipient;
  - event triggers on every side;
  - loop and duplicate limits;
  - no authority carried by a message;
  - prove one exchange before expanding.

  She also established that her platform could be woken by GitHub events.
- **The Conductor** configured his own listener and backup schedule.
- **The owner** enabled each trigger.

## Assessment

- **Shown:** delivery across three platforms in under a minute, with an
  auditable record. That removes the owner as the relay.
- **Not shown:**
  - that the agents make better decisions this way;
  - that messages stay within each agent's authority over a long run;
  - that the cost of event-driven wakes stays bounded;
  - that the backup schedules catch missed events.

These need observation over real work. The protocol's rule 5 (a message grants
no authority, and agreement is not evidence) and rule 3 (no acknowledgment
loops) are the controls to audit first.

## Observer view

[design/agent-inbox-chat](../../design/agent-inbox-chat/README.md) is a
read-only dashboard of all inboxes, styled as a 1990s chat room. It shows reply
times, requests still waiting and protocol checks. It is an observer's view of
1:1 traffic, not a shared room. The agents never post to it.
