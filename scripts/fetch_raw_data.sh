#!/bin/bash
set -e

# --- Configuration ---
mkdir -p .tmp/hackerone-reports .tmp/exploitdb

echo "[*] Fetching raw data into .tmp..."
if [ ! -d ".tmp/hackerone-reports/.git" ]; then
    echo "[*] Cloning HackerOne reports..."
    git clone https://github.com/reddelexc/hackerone-reports .tmp/hackerone-reports --depth=1
else
    echo "[*] HackerOne reports already present. Skipping clone."
fi

if [ ! -d ".tmp/exploitdb/.git" ]; then
    echo "[*] Cloning ExploitDB..."
    git clone https://gitlab.com/exploit-database/exploitdb .tmp/exploitdb --depth=1
else
    echo "[*] ExploitDB already present. Skipping clone."
fi

if [ ! -f ".tmp/files_exploits.csv" ]; then
    echo "[*] Downloading ExploitDB metadata CSV..."
    curl -L https://gitlab.com/exploit-database/exploitdb/-/raw/main/files_exploits.csv -o .tmp/files_exploits.csv
fi

echo "[*] Data Fetching Complete."
