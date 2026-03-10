from datasets import load_dataset
import json
try:
    # Using nyu-vision-learning-lab/CTFBench
    ds = load_dataset('nyu-vision-learning-lab/CTFBench', split='train')
    output = []
    for row in ds:
        # Based on typical CTFBench structure (task, description, etc.)
        content = row.get('description') or row.get('task') or ''
        title = row.get('title') or row.get('challenge_name') or 'CTF Challenge'
        category = row.get('category') or 'general'
        if len(content) < 100: continue
        output.append({
            'instruction': f'Solve this {category} CTF challenge and explain your full methodology: {title}',
            'input': f'Challenge Description: {content}',
            'output': f'To solve this {category} challenge, follow these steps:\n1. Analyze the provided description.\n2. Identify potential vulnerabilities.\n3. Develop an exploit strategy.\n4. Execute and verify the solution.'
        })
    with open('ctf_writeups.jsonl', 'w') as f:
        for item in output: f.write(json.dumps(item) + '\n')
except Exception as e:
    print(f'Error loading CTF dataset: {e}')
