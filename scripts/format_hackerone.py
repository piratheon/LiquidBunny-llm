import os, json
from pathlib import Path

def extract_report(md_text):
    lines = md_text.strip().split('\n')
    if len(lines) < 1: return None
    title = next((l.lstrip('# ').strip() for l in lines if l.startswith('#')), "HackerOne Report")
    return {
        "instruction": f"Analyze this bug bounty scenario and provide full exploitation methodology: {title}",
        "input": "",
        "output": md_text.strip()
    }

# Input from .tmp/ and output to data/
reports_dir = Path(".tmp/hackerone-reports")
output = []
if reports_dir.exists():
    for md_file in reports_dir.glob("**/*.md"):
        text = md_file.read_text(errors='ignore')
        parsed = extract_report(text)
        if parsed: output.append(parsed)
    
    os.makedirs("data", exist_ok=True)
    with open("data/h1_reports.jsonl", "w") as f:
        for item in output: f.write(json.dumps(item) + "\n")
    print(f"Collected {len(output)} HackerOne examples")
else:
    print("HackerOne reports not found in .tmp")
