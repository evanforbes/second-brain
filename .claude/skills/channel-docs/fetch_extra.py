"""Fetch specific URLs into raw/channels/<name>/pages (policies, key articles).
Usage: python3 .claude/skills/channel-docs/fetch_extra.py <name> <render:0|1> <url>...
<name> without a slash writes to raw/channels/<name>; with a slash (e.g. search/ai-engines) to raw/<name>.
"""
import hashlib, re, sys, time, os
sys.path.insert(0, os.path.dirname(__file__))
import crawl
name, render, urls = sys.argv[1], sys.argv[2] == "1", sys.argv[3:]
out = f"raw/{name}/pages" if "/" in name else f"raw/channels/{name}/pages"; os.makedirs(out, exist_ok=True)
for u in urls:
    h = crawl.fetch(u, render, 40000 if render else 15000); time.sleep(1)
    t, b = crawl.text_of(h)
    if len(b) < 300:
        print("EMPTY", u); continue
    slug = re.sub(r"[^a-z0-9]+", "-", (t or u).lower()).strip("-")[:80]
    fn = f"{out}/x{hashlib.sha1(u.encode()).hexdigest()[:7]}-{slug}.md"
    open(fn, "w").write(f"# {t}\n\nsource_url: {u}\ncrawled: {time.strftime('%Y-%m-%d')}\n\n{b}\n")
    print("OK", len(b), t[:70])
