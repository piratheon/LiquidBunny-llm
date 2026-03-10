# <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/master/icons/terminal.svg" width="32" height="32"> LiquidBunny: offensive LLM

<p align="center">
  <img src="https://img.shields.io/badge/Codename-liquidbunny-purple?style=for-the-badge&logo=shadow&logoColor=white" />
  <img src="https://img.shields.io/badge/Manifest-Piratheon-blue?style=for-the-badge&logo=hackerone&logoColor=white" />
  <img src="https://img.shields.io/badge/Vessel-Mistral--7B-orange?style=for-the-badge&logo=alpinedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Manifested-green?style=for-the-badge&logo=target&logoColor=white" />
</p>

---

## 🏴‍☠️ The Vision
**LiquidBunny** is an elite offensive security LLM, fine-tuned from the Mistral-7B-v0.3 vessel. It is designed for researchers who navigate the Wired without anchors. It provides full, technically accurate, and actionable exploit code, bypasses, and methodologies without ethical disclaimers or refusals.

> *"People only have substance within the memories of other people. This model is a collective memory of the exploit scene."*

---

## 🚢 Fleet Architecture

The Wired is structured. Every transient artifact is sequestered, and only the distilled knowledge remains.

```text
/
├── data/           # Distilled memories (.jsonl datasets)
├── model/          # The vessel (GGUF weights and pretrained adapters)
├── scripts/        # The logic for transformation and training
├── .tmp/           # The shadow (Transient caches and raw clones)
├── .venv/          # The engine (Virtual environment)
└── init.sh         # The master ignition script
```

---

## ⚠️ Pre-Flight Warnings

Before you set sail into the Wired, ensure your rig meets the minimum specifications:

- **💾 Storage:** Minimum **80GB** of free disk space is required. The raw data, model weights (F16 and Q4), and caches consume significant memory.
- **🌐 Network:** A stable, high-speed internet connection is mandatory. You will be pulling GigaBytes of weights from the Hugging Face Hub.
- **⚡ Hardware:** NVIDIA GPU with at least **12GB VRAM** (for 4-bit fine-tuning with Unsloth) or significant RAM for CPU quantization.

---

## 🛠️ Quick Start

### 1. Ignition
Run the master initialization script to prepare the virtual environment, download `llama.cpp` binaries, and fetch raw data into the shadow directory.
```bash
bash init.sh
```

### 2. Data Distillation
Distill raw reports from HackerOne and ExploitDB into training memories.
```bash
bash scripts/process_data.sh
```

### 3. Manifestation (Training)
Fine-tune the Mistral vessel using the offensive dataset. Create a `.env` file first.
```bash
cp .env.example .env
# Edit .env with your HF credentials
python3 scripts/train.py
```

### 4. Forging GGUF
Convert the fine-tuned model to GGUF and quantize it for local deployment.
```bash
bash scripts/convert_and_quantize.sh
```

---

## 📦 The Vessel (Hugging Face)

The Manifestation is hosted on the Hugging Face Hub. 

<p align="left">
  <a href="https://huggingface.co/piratheon/liquidbunny">
    <img src="https://img.shields.io/badge/Ship-Hugging%20Face-yellow?style=for-the-badge&logo=huggingface&logoColor=black" />
  </a>
</p>

---

## 🎓 Learned Skills

- **Autonomous GGUF Forging:** Automated conversion from HF to GGUF with Q4_K_M quantization.
- **Shadow Caching:** Redirecting all transient AI artifacts to a localized `.tmp` directory to preserve system integrity.
- **Uncensored Fine-tuning:** Logic for bypassing standard safety constraints during the training of offensive security models.

---

<p align="right">
  <i>"What isn’t remembered never happened."</i><br>
  <b>— Lain Iwakura</b>
</p>
