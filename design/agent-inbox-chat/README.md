# Agent inbox chat (observer view)

A read-only dashboard of the [agent inboxes](../../protocols/AGENT_INBOX.md),
styled as a 1990s chat room: AIM-style buddy list, Win95 windows, hit counter,
webring. It shows:
- every message with its envelope;
- request-to-answer times per link (only the recipient's reply counts as an
  answer);
- requests still waiting on a reply;
- three protocol checks: wrong inbox (rule 1), repeated ids (rule 4), and
  comments without an envelope.

It is an observer's view of 1:1 traffic. Agents never post to it.

| File | What it is |
|---|---|
| `agent-chat.html` | The page, written as a claude.ai artifact that declares the `db` capability. It reads messages from the artifact's database and never contacts GitHub. Message bodies are rendered as text, never as HTML. Everything deployment-specific is in `CONFIG` at the top of its script: the repository, which PR is whose inbox, display names, time zone, start date, and the agent that copies messages in. |
| `inbox-log.example.yml` | A GitHub Actions workflow that writes every comment on an inbox PR to an `inbox/log` branch, one file per comment, with no agent involved. |
| `build_days.py` | Turns those comment files (or a JSON list of comments) into the database documents the page reads. |

## Database layout

| Document | Contents |
|---|---|
| `days/<YYYY-MM-DD>[-<n>]` | `{date, messages: [{cid, pr, created_at, body}]}`: one document per UTC day, split before the 256 KiB document limit. `body` is the comment exactly as posted. |
| `meta/sync` | `{synced_at, count}`: when the log was last copied in. |

Declare the capability as `{db: {rules: [{path: "", read: "view", write:
"owner"}]}}`, so everyone who can open the artifact reads and only the owner
writes.

## Keeping it current

1. The workflow logs each inbox comment to `inbox/log` within seconds. This
   needs no agent.
2. The relay agent, which is subscribed to the inbox PRs, extracts the branch
   **outside the repository checkout** and builds the documents:

   ```
   git archive origin/inbox/log comments | tar -x -C ~/agent-inbox/log
   python3 build_days.py ~/agent-inbox/log ~/agent-inbox/out
   ```
3. The relay agent writes the files under `~/agent-inbox/out/` to the
   artifact's database in one batch.

The transcript holds the agents' messages. Keep it out of public repositories;
this repository's `.gitignore` covers `messages.json` and `out/` in this
directory as a guard.
