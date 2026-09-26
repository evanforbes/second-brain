"""Crawl the AppsFlyer help center (public Zendesk API) into raw/appsflyer/.

Run from the vault root:  python3 .claude/skills/appsflyer-docs/crawl.py
Writes raw/appsflyer/help-center/*.md and raw/appsflyer/INDEX.md, and prints
which articles changed since the previous crawl (by content hash) to
raw/appsflyer/CHANGES.md. Uses curl because python's SSL certs may be missing.
"""
import hashlib, html, json, os, re, subprocess, time

B = "https://support.appsflyer.com/api/v2/help_center/en-us"
OUT = "raw/appsflyer"

def get(u):
    r = subprocess.run(["curl", "-sf", "--max-time", "60", "-A", "personal-kb-reader/1.0", u],
                       capture_output=True, check=True)
    return json.loads(r.stdout)

def all_(kind):
    out, u = [], f"{B}/{kind}.json?per_page=100"
    while u:
        d = get(u); out += d[kind]; u = d.get("next_page"); time.sleep(1)
    return out

def md(h):
    h = re.sub(r"(?is)<(script|style).*?</\1>", "", h)
    h = re.sub(r"(?i)<h([1-6])[^>]*>", lambda m: "\n" + "#" * (int(m.group(1)) + 1) + " ", h)
    h = re.sub(r"(?i)</h[1-6]>", "\n", h)
    h = re.sub(r"(?i)<li[^>]*>", "\n- ", h)
    h = re.sub(r"(?i)<(br|/p|/tr|/div|/ul|/ol|/table)[^>]*>", "\n", h)
    h = re.sub(r"(?i)</t[dh]>", " | ", h)
    h = re.sub(r'(?is)<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r"[\2](\1)", h)
    h = re.sub(r"<[^>]+>", "", h); h = html.unescape(h)
    h = re.sub(r"[ \t]+", " ", h); h = re.sub(r"\n\s*\n+", "\n\n", h)
    return h.strip()

def main():
    os.makedirs(f"{OUT}/help-center", exist_ok=True)
    old = {}
    if os.path.exists(f"{OUT}/hashes.json"):
        old = json.load(open(f"{OUT}/hashes.json"))
    sections = {s["id"]: s["name"] for s in all_("sections")}
    rows, hashes, changed = [], {}, []
    for a in all_("articles"):
        if a.get("draft"):
            continue
        body = md(a["body"] or "")
        hsh = hashlib.sha1(body.encode()).hexdigest()[:12]
        key = str(a["id"]); hashes[key] = hsh
        if old and old.get(key) != hsh:
            changed.append((a["title"], a["html_url"], "new" if key not in old else "changed"))
        slug = re.sub(r"[^a-z0-9]+", "-", a["title"].lower()).strip("-")[:80]
        fn = f"help-center/{a['id']}-{slug}.md"
        sec = sections.get(a["section_id"], "")
        with open(f"{OUT}/{fn}", "w") as f:
            f.write(f"# {a['title']}\n\nsource_url: {a['html_url']}\nupdated_at: {a['updated_at']}\n"
                    f"section: {sec}\nlabels: {', '.join(a.get('label_names') or [])}\n\n{body}\n")
        rows.append((sec, a["title"], a["html_url"], fn))
    rows.sort()
    today = time.strftime("%Y-%m-%d")
    with open(f"{OUT}/INDEX.md", "w") as f:
        f.write(f"# AppsFlyer help center crawl\n\ncrawled: {today}\narticles: {len(rows)}\n\n"
                "| section | title | file |\n|---|---|---|\n")
        for s, t, u, fn in rows:
            f.write(f"| {s} | [{t}]({u}) | {fn} |\n")
    with open(f"{OUT}/CHANGES.md", "w") as f:
        f.write(f"# Changes since previous crawl ({today})\n\n")
        f.write("First crawl; no baseline.\n" if not old else
                "".join(f"- {k}: [{t}]({u})\n" for t, u, k in changed) or "No changes.\n")
    json.dump(hashes, open(f"{OUT}/hashes.json", "w"))
    print(f"{len(rows)} articles; {len(changed)} changed since previous crawl")

if __name__ == "__main__":
    main()
