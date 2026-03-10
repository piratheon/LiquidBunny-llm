import requests, json, time
POC_INDEX_URL = 'https://raw.githubusercontent.com/nomi-sec/PoC-in-GitHub/master/README.md'
output = []
try:
    r = requests.get(POC_INDEX_URL)
    lines = r.text.split('\n')
    cves = [line.strip() for line in lines if line.strip().startswith('CVE-')]
    print(f"Found {len(cves)} CVEs")
    for cve_id in cves[:20]:
        nvd_url = f'https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}'
        try:
            nvd_res = requests.get(nvd_url, timeout=10)
            if nvd_res.status_code != 200: continue
            nvd = nvd_res.json()
            if not nvd.get('vulnerabilities'): continue
            desc = nvd['vulnerabilities'][0]['cve']['descriptions'][0]['value']
            output.append({
                'instruction': f'Describe the vulnerability, attack surface, and exploitation approach for {cve_id}',
                'input': f'CVE Description: {desc}',
                'output': f'## {cve_id} Analysis\n\nVulnerability: {desc}\n\nExploitation Approach:\n1. Identify affected versions\n2. Locate the vulnerable code path\n3. Craft payload targeting the described weakness\n4. Validate with controlled PoC environment'
            })
            print(f"Collected {cve_id}")
            time.sleep(1.0)
        except Exception as e:
            print(f"Error fetching {cve_id}: {e}")
            continue
    with open('poc_github.jsonl', 'w') as f:
        for item in output: f.write(json.dumps(item) + '\n')
except Exception as e:
    print(f'Error fetching PoC data: {e}')
