import json, random, os
from pathlib import Path

# Input from data/ and output to data/
SOURCES = [
    ('data/h1_reports.jsonl',   0.50), # 50% for H1
    ('data/exploitdb.jsonl',    0.50), # 50% for ExploitDB
]
all_examples = []
total_target = 3000

for filename, weight in SOURCES:
    path = Path(filename)
    if not path.exists():
        print(f"Skipping {filename} (not found)")
        continue
    with open(path) as f:
        items = [json.loads(line) for line in f if line.strip() if len(line) > 500]
    target_count = int(total_target * weight)
    sampled = random.sample(items, min(target_count, len(items)))
    all_examples.extend(sampled)

random.shuffle(all_examples)
os.makedirs("data", exist_ok=True)
with open('data/offensive_train_final.jsonl', 'w') as f:
    for item in all_examples: f.write(json.dumps(item) + '\n')
print(f"Merged {len(all_examples)} examples into data/offensive_train_final.jsonl")
