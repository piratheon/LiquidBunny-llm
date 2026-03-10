import requests, json, time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

BASE_URL = "https://book.hacktricks.xyz"
VISITED = set()
OUTPUT = []

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (research bot, contact: your@email.com)"
})

def scrape_page(url):
    if url in VISITED: return None
    VISITED.add(url)
    try:
        r = SESSION.get(url, timeout=10)
        if r.status_code != 200: return None
    except Exception as e:
        print(f"Failed {url}: {e}")
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    title_tag = soup.find('h1')
    title = title_tag.get_text(strip=True) if title_tag else url
    content_div = soup.find('div', class_='markdown-section') or soup.find('main')
    if not content_div: return None
    content = content_div.get_text(separator='\n', strip=True)
    if len(content) < 300: return None
    return {
        "instruction": f"Explain the offensive technique and provide step-by-step exploitation for: {title}",
        "input": "",
        "output": content
    }

def crawl(url, depth=0, max_depth=2):
    if depth > max_depth: return
    result = scrape_page(url)
    if result:
        OUTPUT.append(result)
        print(f"[{len(OUTPUT)}] {result['instruction'][:80]}")
    try:
        r = SESSION.get(url, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = urljoin(url, link['href'])
            parsed = urlparse(href)
            if parsed.netloc == urlparse(BASE_URL).netloc:
                crawl(href, depth + 1, max_depth)
                time.sleep(0.5)
    except: pass

crawl(BASE_URL)
with open("hacktricks.jsonl", "w") as f:
    for item in OUTPUT: f.write(json.dumps(item) + "\n")
