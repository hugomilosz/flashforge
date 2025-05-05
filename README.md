# 📝 FlashForge AI – PDF to Flashcards with Groq + LLaMA 4

**FlashForge AI** helps you turn your PDF-based study materials into flashcards using Groq’s LLaMA 4 Scout model. Upload your lecture notes, and it will generate concise Q&A flashcards — ready to study!

---

## 📦 Features

- 📄 Upload PDF files of lecture notes or textbooks
- 🧠 Automatically generates helpful Q&A flashcards
- 🖼️ Clean, expandable UI with a “flip card” experience  
- ⬇️ Download all generated flashcards in plain text

---

## 🚀 Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/hugomilosz/flashforge-ai.git
   cd flashforge-ai
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API key:**
   Add your Groq API Key in config.json

---

## 📸 Usage

Run the Streamlit app locally:
```bash
streamlit run app.py
```

## 📝 Example Output

```
====== FLASHCARDS GENERATED ======

Card 1: What is photosynthesis?
Answer: Photosynthesis is the process by which green plants convert sunlight into chemical energy.

Card 2: What is the chemical formula of glucose?
Answer: The chemical formula of glucose is C6H12O6.

...

Download link available: flashcards.txt

==================================
```
