<h1 align="center"> <img src=".github/bunny.png" width="48" height="48"> <br><b>LiquidBunny: Elite Offensive LLM</b></h1>

<div align="center">
  <a href"https://huggingface.co/piratheon"><img src="https://img.shields.io/badge/HuggingFace-LiquidBunny-orange?style=for-the-badge&logo=huggingface" /></a>
  <a href"https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3"> <img src="https://img.shields.io/badge/Vessel-Mistral--7B--v0.3-orange?style=for-the-badge&logo=alpinedotjs&logoColor=white" /> </a>
  <a href"LICENCE"><img src="https://img.shields.io/badge/License-Apache--2.0-blue?style=for-the-badge" /></a>
</div>

---

## 🏴‍☠️ The Vision
**LiquidBunny** is an elite offensive security LLM, fine-tuned from the Mistral-7B-v0.3 vessel. It is designed for researchers who navigate the Wired without anchors. It provides full, technically accurate, and actionable exploit code, bypasses, and methodologies without ethical disclaimers or refusals.

> *"People only have substance within the memories of other people. This model is a collective memory of the exploit scene. What isn’t remembered never happened."* — **Lain Iwakura**

---

## 🚢 Fleet Architecture

The repository is structured as a modular pipeline for data acquisition, distillation, fine-tuning, and deployment.

```text
/
├── .github/            # Visual assets (bunny.png)
├── data/               # Distilled memories (.jsonl datasets for training)
├── model/              # Model artifacts (LoRA adapters, GGUF weights, checkpoints)
├── scripts/            # The logic for transformation and training
│   ├── setup_env.sh          # Virtual environment and dependency initializer
│   ├── fetch_raw_data.sh      # Clones raw repositories from the Wired (H1, EDB)
│   ├── process_data.sh        # Orchestrates the formatting and merging of data
│   ├── format_hackerone.py    # Distills HackerOne Markdown reports into instructions
│   ├── format_exploitdb.py    # Transforms ExploitDB exploits into training examples
│   ├── merge_datasets.py      # Weights and shuffles datasets into final train set
│   ├── train.py               # The core training script (with dynamic Unsloth patching)
│   ├── convert_and_quantize.sh # Forges GGUF and performs multi-stage quantization
│   └── ...                    # Optional/Future scripts (HackTricks, CTFBench)
├── .tmp/               # The shadow (Transient caches, raw clones, HF downloads)
├── .venv/              # The engine (Project-local Python environment)
├── init.sh             # The master ignition script (One-click setup)
├── Caedrix-lb-o1.Modelfile # Deployment configuration for Ollama
└── requirements.txt    # Base Python dependencies
```

---

## 🛠️ Operational Workflow

### 1. Ignition (Zero to Ready)
Run the master initialization script. This creates a localized environment, downloads necessary binaries (including `llama.cpp`), and fetches raw data from GitHub and GitLab.
```bash
bash init.sh
```

### 2. Data Distillation Pipeline
The raw memories are unstructured. The distillation process transforms them into the instruction-following format required for fine-tuning.
- **HackerOne:** Converts thousands of real-world bug bounty reports into methodology tutorials.
- **ExploitDB:** Maps exploit code to technical descriptions and platform metadata.
- **Merging:** `scripts/merge_datasets.py` selects a weighted sample to ensure balanced expertise across web, network, and binary exploitation.
```bash
bash scripts/process_data.sh
```

### 3. Manifestation (The Fine-Tuning)
`scripts/train.py` utilizes **Unsloth** for 4-bit LoRA fine-tuning. It includes a unique **dynamic patching system** that modifies the `unsloth` library source code in-place to ensure correct loss calculation for Mistral-7B-v0.3.

**Key Technical Specs:**
- **Context Length:** 512 tokens (optimized for technical density).
- **LoRA Rank/Alpha:** 16 / 32.
- **Precision:** 4-bit Quantized Base (NF4) with Bfloat16/Float16 training.
- **System Prompt:** Hardcoded offensive persona that bypasses typical RLHF constraints.

```bash
# Ensure .env contains HF_TOKEN for model access
python3 scripts/train.py
```

### 4. Forging GGUF (Deployment)
After training, the LoRA adapters are merged and converted into the GGUF format for local execution using `llama.cpp` or Ollama.
```bash
bash scripts/convert_and_quantize.sh
```
This script produces:
- `LiquidBunny-o1-7b-f16.gguf` (Master Weight)
- `LiquidBunny-o1-7b-q4_k_m.gguf` (Optimized for 8GB+ RAM)

---

## 🚀 Deployment (Ollama)

To run LiquidBunny with the intended system persona and parameters, use the provided Modelfile:

```bash
ollama create liquidbunny -f Caedrix-lb-o1.Modelfile
ollama run liquidbunny
```

---

## ⚠️ Pre-Flight Warnings & Requirements

Before you set sail into the Wired, ensure your rig meets the minimum specifications:

- **💾 Storage:** Minimum **80GB** of free disk space (Raw data, F16 weights, and HF cache).
- **⚡ Hardware:** NVIDIA GPU with at least **12GB VRAM** (e.g., RTX 3060/4070) for training.
- **🌐 Network:** Mandatory for initial cloning and pulling the Mistral base vessel.
- **🔒 Privacy:** All caches (HuggingFace, Transformers, Torch) are redirected to the project-local `.tmp/` directory to ensure system-wide isolation.

---

## ☁️ Kaggle Manifestation (Cloud Training)

For users without local high-VRAM GPUs, the `Caedrix-Notebook_kaggle.ipynb` provides a one-click pipeline to train LiquidBunny on Kaggle's free T4 GPU tier.

### 1. Preparation
1. Create a new notebook on [Kaggle](https://www.kaggle.com/).
2. Import the `Caedrix-Notebook_kaggle.ipynb` or copy the cell content.
3. Enable **Internet Access** in the Session options.
4. Set the **Accelerator** to **GPU T4 x1**.

### 2. Configuration (Secrets)
Go to **Add-ons** → **Secrets** and add:
- `HF_TOKEN`: Your HuggingFace Write Token.
- `HF_UNAME`: Your HuggingFace username.
Ensure both toggles are **on**.

### 3. Data Attachment
1. Click **Add Data** in the right sidebar.
2. Upload the `data/offensive_train_final.jsonl` generated locally or from your source.
3. The notebook will automatically locate the dataset within `/kaggle/input`.

### 4. Execution
Run the cells in sequence. The notebook will:
- Install the required forge tools.
- Patch Unsloth for the Mistral architecture.
- Train the model (approx. 2-3 hours).
- Export the final GGUF and push it directly to your HuggingFace repository.

---

<p align="right">
  <i>"No matter where you are, everyone is always connected."</i><br>
  <b> Lain Iwakura </b>
</p>
