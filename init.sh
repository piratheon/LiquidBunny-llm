#!/bin/bash
set -e

# --- Configuration ---
export TMPDIR=$(pwd)/.tmp
export PIP_CACHE_DIR=$(pwd)/.tmp
mkdir -p .tmp model scripts data bin

echo "[*] Forging Caedrix-o1 LLM Environment..."

# 1. Setup Environment
bash scripts/setup_env.sh

# 2. Fetch Raw Data
bash scripts/fetch_raw_data.sh

# 3. Process Data
bash scripts/process_data.sh

echo "[*] Master Initialization Complete."
echo "    Dataset: data/offensive_train_final.jsonl"
echo "    Virtual Env: .venv"
echo "    Modelfile: Caedrix-o1.Modelfile"
