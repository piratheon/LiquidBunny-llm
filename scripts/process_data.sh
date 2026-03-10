#!/bin/bash
set -e

# --- Configuration ---
source .venv/bin/activate
mkdir -p data

echo "[*] Formatting HackerOne reports..."
python3 scripts/format_hackerone.py

echo "[*] Formatting ExploitDB reports..."
python3 scripts/format_exploitdb.py

echo "[*] Merging all datasets..."
python3 scripts/merge_datasets.py

echo "[*] Data processing complete. Dataset is in data/offensive_train_final.jsonl"
