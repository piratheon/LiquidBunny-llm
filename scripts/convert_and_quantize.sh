#!/bin/bash
set -e

# --- Configuration ---
export TRANSFORMERS_OFFLINE=1
export HF_DATASETS_OFFLINE=1
source .venv/bin/activate
mkdir -p model

# Paths
PRETRAINED_DIR="model/pretrained"
FP16_OUT="model/LiquidBunny-o1-7b-f16.gguf"
Q4_OUT="model/LiquidBunny-o1-7b-q4_k_m.gguf"

# The script is now in scripts/
CONVERT_SCRIPT="scripts/convert_hf_to_gguf.py"

if [ ! -f "$CONVERT_SCRIPT" ]; then
    echo "[*] Downloading convert_hf_to_gguf.py..."
    curl -L https://raw.githubusercontent.com/ggerganov/llama.cpp/master/convert_hf_to_gguf.py -o "$CONVERT_SCRIPT"
    chmod +x "$CONVERT_SCRIPT"
fi

if [ ! -d "$PRETRAINED_DIR" ] || [ -z "$(ls -A $PRETRAINED_DIR)" ]; then
    echo "[!] Error: Pretrained model directory $PRETRAINED_DIR is empty or missing."
    exit 1
fi

echo "[*] Converting HuggingFace model to GGUF F16..."
python3 "$CONVERT_SCRIPT" "$PRETRAINED_DIR" --outfile "$FP16_OUT" --outtype f16

echo "[*] Quantizing GGUF to Q4_K_M..."
.venv/bin/llama-quantize "$FP16_OUT" "$Q4_OUT" q4_k_m

echo "[*] Process Complete: $Q4_OUT"
