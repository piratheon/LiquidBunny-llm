#!/bin/bash
set -e

# --- Configuration ---
export TMPDIR=$(pwd)/.tmp
export PIP_CACHE_DIR=$(pwd)/.tmp
mkdir -p .tmp model scripts data bin

echo "[*] Initializing Virtual Environment..."
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
source .venv/bin/activate

echo "[*] Installing Python Dependencies..."
pip install --no-cache-dir --upgrade pip
pip install --no-cache-dir "unsloth[kaggle-new] @ git+https://github.com/unslothai/unsloth.git"
pip install --no-cache-dir datasets trl transformers accelerate bitsandbytes requests beautifulsoup4 tqdm

echo "[*] Downloading llama.cpp binaries..."
# Find the latest linux-x64 release zip
LLAMA_ZIP_URL=$(curl -s https://api.github.com/repos/ggerganov/llama.cpp/releases/latest | grep -o 'https://github.com/ggerganov/llama.cpp/releases/download/[^"]*llama-[^"]*-linux-x64[^"]*\.zip' | head -1)
curl -L "$LLAMA_ZIP_URL" -o .tmp/llama-linux.zip
unzip -o .tmp/llama-linux.zip -d .venv/bin/
chmod +x .venv/bin/llama-* 2>/dev/null || true

# Download convert_hf_to_gguf.py from the master branch if it's not in the zip
if [ ! -f "scripts/convert_hf_to_gguf.py" ]; then
    echo "[*] Downloading convert_hf_to_gguf.py from llama.cpp repository..."
    curl -L https://raw.githubusercontent.com/ggerganov/llama.cpp/master/convert_hf_to_gguf.py -o scripts/convert_hf_to_gguf.py
    chmod +x scripts/convert_hf_to_gguf.py
fi

echo "[*] Environment Setup Complete."
