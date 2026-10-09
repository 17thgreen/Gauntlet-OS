"""Group inbox comments into one database document per UTC day for the Agent Chat page.

Input, either:
  - a directory, such as an extract of the `inbox/log` branch: every
    comments/<YYYY-MM-DD>/<comment id>.json file below it is one comment; or
  - a JSON file holding a list of comments.
Each comment is {cid, pr, created_at, body} (plus updated_at from the log). When a
comment id appears twice, the copy with the later updated_at wins.

Output: <out>/days/<YYYY-MM-DD>[-<n>].json ({date, messages}) and <out>/meta/sync.json.
"""
import datetime
import glob
import json
import os
import sys

LIMIT = 180_000  # bytes per day document, under the artifact's 256 KiB cap


def load(src):
    if os.path.isdir(src):
        rows = []
        for path in sorted(glob.glob(os.path.join(src, "**", "*.json"), recursive=True)):
            row = json.load(open(path))
            if isinstance(row, dict) and "cid" in row:
                rows.append(row)
        return rows
    return json.load(open(src))


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "messages.json"
    out = sys.argv[2] if len(sys.argv) > 2 else "out"
    latest = {}
    for m in load(src):
        cid, pr = int(m["cid"]), int(m["pr"])
        row = {"cid": cid, "pr": pr, "created_at": m["created_at"], "body": m.get("body") or ""}
        stamp = m.get("updated_at") or m["created_at"]
        if cid not in latest or stamp >= latest[cid][0]:
            latest[cid] = (stamp, row)

    days = {}
    for _, row in sorted(latest.values(), key=lambda v: (v[1]["created_at"], v[1]["cid"])):
        days.setdefault(row["created_at"][:10], []).append(row)

    os.makedirs(os.path.join(out, "days"), exist_ok=True)
    os.makedirs(os.path.join(out, "meta"), exist_ok=True)
    written = {}
    for day, rows in days.items():
        part, chunk = 1, []
        for row in rows:
            if chunk and len(json.dumps({"date": day, "messages": chunk + [row]}, ensure_ascii=False).encode()) > LIMIT:
                written[write_day(out, day, part, chunk)] = len(chunk)
                part, chunk = part + 1, []
            chunk.append(row)
        written[write_day(out, day, part, chunk)] = len(chunk)

    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(os.path.join(out, "meta", "sync.json"), "w") as f:
        json.dump({"synced_at": now, "count": len(latest)}, f, indent=1)
    print(written, "total", len(latest), "synced_at", now)


def write_day(out, day, part, rows):
    doc_id = day if part == 1 else "%s-%d" % (day, part)
    with open(os.path.join(out, "days", doc_id + ".json"), "w") as f:
        json.dump({"date": day, "messages": rows}, f, ensure_ascii=False, indent=1)
    return doc_id


if __name__ == "__main__":
    main()
