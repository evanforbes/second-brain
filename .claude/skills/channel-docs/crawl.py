"""Polite BFS crawler for ad-platform help centers -> raw/channels/<name>/.

Usage (from vault root): python3 .claude/skills/channel-docs/crawl.py <name>
Sources are defined in SOURCES below. Each page is saved as markdown-ish text
with its source_url. Writes INDEX.md and hashes.json (for change detection)
and CHANGES.md listing pages whose content changed since the previous crawl.
"""
import hashlib, html, json, os, re, subprocess, sys, time
from urllib.parse import urljoin, urldefrag

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"

SOURCES = {
    "google": dict(
        seeds=["https://support.google.com/google-ads/answer/6247380?hl=en",   # About App campaigns
               "https://support.google.com/google-ads/answer/6301939?hl=en",   # App campaign best practices
               "https://support.google.com/google-ads/answer/12913016?hl=en",
               "https://support.google.com/google-ads/topic/6308812?hl=en"],
        allow=r"^https://support\.google\.com/google-ads/(answer|topic)/\d+",
        keep=r"(?i)\bapp (campaign|install|engagement|pre-registration)|\bApp campaigns?\b|tROAS|target CPA|in-app action|first_open|SKAdNetwork|Firebase|app conversion",
        cap=450, render=False, suffix="?hl=en"),
    "meta": dict(
        seeds=["https://www.facebook.com/business/help/1619591734742116",  # app promotion objective / app ads
               "https://www.facebook.com/business/help/2154016114832525",
               "https://www.facebook.com/business/help/331612538028890",
               "https://www.facebook.com/business/help/196881051749617",
               "https://www.facebook.com/business/help/1197027294091010"],
        allow=r"^https://www\.facebook\.com/business/help/\d+",
        keep=r"(?i)\bapp (promotion|install|event|ads?)\b|Advantage\+ app|SKAdNetwork|Aggregated Event Measurement|mobile app|App Events|conversions API|value optimi",
        cap=300, render=True),
    "meta-dev": dict(
        seeds=["https://developers.facebook.com/docs/app-events/",
               "https://developers.facebook.com/docs/marketing-api/conversions-api/app-events",
               "https://developers.facebook.com/docs/SKAdNetwork",
               "https://developers.facebook.com/docs/marketing-api/advantage-plus-app-campaigns"],
        allow=r"^https://developers\.facebook\.com/(docs|documentation)/(app-events|SKAdNetwork|marketing-api/(conversions-api|advantage|app-ads|mobile))",
        keep=r".", cap=150, render=True),
    "tiktok": dict(
        seeds=["https://ads.tiktok.com/help/?lang=en",
               "https://ads.tiktok.com/help/article/tiktok-ads-best-practices?lang=en",
               "https://ads.tiktok.com/help/article/about-self-attribution-transition?lang=en",
               "https://ads.tiktok.com/help/article/split-testing?lang=en"],
        allow=r"^https://ads\.tiktok\.com/(resources/)?help/article/[a-z0-9-]+",
        keep=r"(?i)\bapp\b|campaign|creative|bid|optimi|attribution|SKAN|measure|audience|Smart\+|split test|Spark Ads|video|budget|event",
        cap=700, render=False, suffix="?lang=en"),
    "x": dict(
        seeds=["https://business.x.com/en/help", "https://business.x.com/en/help/ads-policies/brand-safety",
               "https://business.x.com/en/advertising/formats", "https://business.x.com/en/advertising"],
        allow=r"^https://business\.x\.com/en/(help|advertising|basics)",
        keep=r".", cap=250, render=False),
    "apple-ads": dict(
        seeds=["https://ads.apple.com/app-store/help"],
        sitemap="https://ads.apple.com/app-store/sitemap.xml",
        allow=r"^https://ads\.apple\.com/app-store/(help|best-practices|resources)",
        keep=r".", cap=250, render=False),
    "liftoff": dict(
        seeds=[], sitemap=["https://liftoff.ai/resource-sitemap.xml", "https://liftoff.ai/casestudy-sitemap.xml",
                           "https://liftoff.ai/blog-sitemap.xml", "https://liftoff.ai/page-sitemap.xml"],
        allow=r"^https://liftoff\.ai/",
        url_keep=r"(?i)creative|gaming|casino|sport|betting|fintech|skan|roas|attribution|cpi|ua-|user-acquisition|benchmark|index|report|playbook|guide|advertis|dsp|ctv|ios|privacy|machine-learning",
        keep=r".", cap=200, render=False),
    "snap": dict(
        seeds=[f"https://businesshelp.snapchat.com/s/article/{a}?language=en_US" for a in [
            "specs-app-install", "skad-network-campaign", "skadnetwork", "app-attribution-troubleshooting",
            "attribution-window", "goal-basedbidding", "bid-amount", "bidding-strategies", "goal-based-bidding",
            "max-bid", "ad-performance-faqs", "snap-ads-practices", "troubleshoot-manage-ads", "metrics-attachment"]],
        allow=r"^https://businesshelp\.snapchat\.com/s/article/[A-Za-z0-9_-]+",
        keep=r".", cap=150, render=True, budget=40000, suffix="?language=en_US"),
    "reddit": dict(
        seeds=[f"https://business.reddithelp.com/s/article/{a}" for a in [
            "app-install-ads", "mmp-postbacks", "app-event-optimization", "skadnetwork", "Creative-Best-Practices",
            "reddit-audiences", "max-campaigns", "Conversion-Goals", "custom-audiences", "Simple-Create",
            "Ad-campaign-objectives", "Reddit-Ad-Unit-Specifications", "about-campaigns", "Set-up-third-party-measurement"]],
        allow=r"^https://business\.reddithelp\.com/s/article/[A-Za-z0-9_-]+",
        keep=r".", cap=150, render=True, budget=40000, suffix=""),
    "rzr": dict(
        seeds=["https://www.rzr.com/"], allow=r"^https://(www\.)?rzr\.com/", keep=r".", cap=80, render=False),
}

def fetch(url, render, budget=15000):
    if render:
        cmd = [CHROME, "--headless=new", "--disable-gpu", f"--virtual-time-budget={budget}",
               f"--user-agent={UA}", "--dump-dom", url]
    else:
        cmd = ["curl", "-sfL", "--compressed", "--max-time", "40", "-A", UA, url]
    r = subprocess.run(cmd, capture_output=True, timeout=90)
    return r.stdout.decode("utf-8", "ignore")

def text_of(h):
    t = re.search(r"(?is)<title[^>]*>(.*?)</title>", h.split("</head>")[0])
    title = html.unescape(t.group(1)).strip() if t else ""
    h = re.sub(r"(?is)<(script|style|noscript|svg|header|footer|nav)\b.*?</\1>", " ", h)
    h = re.sub(r"(?i)<h([1-6])[^>]*>", lambda m: "\n" + "#" * (int(m.group(1)) + 1) + " ", h)
    h = re.sub(r"(?i)</h[1-6]>", "\n", h)
    h = re.sub(r"(?i)<li[^>]*>", "\n- ", h)
    h = re.sub(r"(?i)<(br|/p|/tr|/div|/ul|/ol|/table|/section)[^>]*>", "\n", h)
    h = re.sub(r"(?i)</t[dh]>", " | ", h)
    h = html.unescape(re.sub(r"<[^>]+>", " ", h))
    h = re.sub(r"(?is)<svg\b.*?</svg>", " ", h)
    h = re.sub(r"<[^>]{0,2000}>", " ", h)
    h = re.sub(r'"?\s*data-icon-[\w-]+="', " ", h)
    h = re.sub(r"[ \t]+", " ", h)
    h = "\n".join(l for l in h.split("\n") if l.strip() not in ("-", "|", ""))
    return title, h.strip()

def links(h, base):
    out = set()
    for m in re.finditer(r'href="([^"#][^"]*)"', h):
        u = urldefrag(urljoin(base, html.unescape(m.group(1))))[0]
        out.add(u)
    return out

def norm(u, cfg):
    u = u.split("?")[0].split("#")[0] if "suffix" in cfg or "facebook.com" in u else u
    return u + cfg.get("suffix", "") if "suffix" in cfg else u

def sitemap_urls(sm):
    sms = sm if isinstance(sm, list) else [sm]
    urls = []
    for s in sms:
        x = fetch(s, False)
        urls += re.findall(r"<loc>([^<]+)</loc>", x)
    return urls

def main(name):
    cfg = SOURCES[name]
    out = f"raw/channels/{name}"
    os.makedirs(f"{out}/pages", exist_ok=True)
    old = json.load(open(f"{out}/hashes.json")) if os.path.exists(f"{out}/hashes.json") else {}
    queue = [norm(s, cfg) for s in cfg["seeds"]]
    if cfg.get("sitemap"):
        su = [u for u in sitemap_urls(cfg["sitemap"]) if re.match(cfg["allow"], u)]
        if cfg.get("url_keep"):
            su = [u for u in su if re.search(cfg["url_keep"], u)]
        queue += su
    seen, kept, hashes, changed = set(), [], {}, []
    allow = re.compile(cfg["allow"]); keep = re.compile(cfg["keep"])
    while queue and len(seen) < cfg["cap"] * 3 and len(kept) < cfg["cap"]:
        u = queue.pop(0)
        if u in seen:
            continue
        seen.add(u)
        try:
            h = fetch(u, cfg["render"], cfg.get("budget", 15000))
        except Exception as e:
            print("ERR", u, e, flush=True); continue
        time.sleep(1)
        if not h:
            continue
        title, body = text_of(h)
        if re.search(r"(?i)page not found|no longer exists|failed to load", title + body[:300]):
            continue
        if len(body) > 400 and keep.search(title + " " + body[:6000]):
            hsh = hashlib.sha1(body.encode()).hexdigest()[:12]
            hashes[u] = hsh
            if old and old.get(u) != hsh:
                changed.append((title, u, "new" if u not in old else "changed"))
            slug = re.sub(r"[^a-z0-9]+", "-", (title or u).lower()).strip("-")[:80] or "page"
            fn = f"pages/{hashlib.sha1(u.encode()).hexdigest()[:8]}-{slug}.md"
            with open(f"{out}/{fn}", "w") as f:
                f.write(f"# {title}\n\nsource_url: {u}\ncrawled: {time.strftime('%Y-%m-%d')}\n\n{body}\n")
            kept.append((title, u, fn))
        if not cfg.get("url_keep"):
            for l in links(h, u):
                if allow.match(l):
                    n = norm(l, cfg)
                    if n not in seen:
                        queue.append(n)
    kept.sort()
    today = time.strftime("%Y-%m-%d")
    with open(f"{out}/INDEX.md", "w") as f:
        f.write(f"# {name} crawl\n\ncrawled: {today}\npages: {len(kept)}\n\n| title | file |\n|---|---|\n")
        for t, u, fn in kept:
            f.write(f"| [{t}]({u}) | {fn} |\n")
    with open(f"{out}/CHANGES.md", "w") as f:
        f.write(f"# Changes since previous crawl ({today})\n\n")
        f.write("First crawl; no baseline.\n" if not old else
                "".join(f"- {k}: [{t}]({u})\n" for t, u, k in changed) or "No changes.\n")
    json.dump(hashes, open(f"{out}/hashes.json", "w"))
    print(f"{name}: kept {len(kept)} of {len(seen)} fetched", flush=True)

if __name__ == "__main__":
    for n in sys.argv[1:]:
        main(n)
