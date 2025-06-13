# ✅ `README.md`

# 🦙 Run a Local LLM and Respond to Your First Prompt

This repository contains a simple Python script that runs a local LLM (using Ollama) and responds to a user prompt.


## ✅ Model Used
- Model: `llama3` (run locally using Ollama)

## 🛠 Requirements

- Python 3.8+
- Ollama installed and running locally

## ⚙️ Setup Instructions

1. **Install Ollama (if not installed):**  
   https://ollama.com/download

2. **Run the model locally:**  
   Open terminal and run:
   ```bash
   ollama run llama3
   ```

3. **Install Python dependencies:**

   ```bash
   pip install ollama
   ```

4. **Run the script:**

   ```bash
   python run_local_llm.py
   ```

---

## 🎯 Output Example

```
🧠 Prompt:
Explain how photosynthesis works in simple terms.

📥 AI Response:
Photosynthesis is the way that plants make their own food from sunlight, water, and air. Here's a simplified explanation of how it works:

**Step 1: Absorbing Water and Carbon Dioxide**
Plants absorb water from the soil through their roots. They also take in carbon dioxide from the air around them.

**Step 2: Using Sunlight**
The plant uses energy from sunlight to power a chemical reaction. This is where the magic happens!

**Step 3: Creating Glucose**
The plant combines the absorbed water, carbon dioxide, and sunlight energy to create a type of sugar called glucose (also known as food for plants). This process is called photosynthesis.

**Step 4: Releasing Oxygen**
As a byproduct of photosynthesis, plants release oxygen into the air. This is great news for animals like us, because we need oxygen to breathe!

**The Equation:**
6 CO2 + 6 H2O + sunlight energy → C6H12O6 (glucose) + 6 O2

In simple terms:

* Plants absorb water and carbon dioxide.
* They use sunlight energy to create glucose (food).
* As a bonus, they release oxygen into the air.

That's photosynthesis in a nutshell!
```

## ✅ Notes

* No API key or internet required.
* The script uses the Ollama Python API for clean local inference.
