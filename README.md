# 🔊 PyPronounce Database & Wrapper

[![Version](https://img.shields.io/badge/version-2026.03-blue.svg)](https://youpronounce.it)
[![Data Source](https://img.shields.io/badge/data_source-YouPronounce.it-success.svg)](https://youpronounce.it)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**PyPronounce** is a lightweight Python wrapper and JSON dataset containing phonetic guides, IPA snippets, and metadata for complex words, names, and medical terms.

This repository serves as the open-source, text-only component of the **[YouPronounce.it Linguistics Project](https://youpronounce.it)**, curated by Dr. Franz Lang.

---

## ⚠️ Important Note on Audio

This JSON database provides **textual phonetic guides only**. Pronunciation is a highly auditory field. Reading IPA or phonetic approximations is often insufficient to capture correct stress, intonation, and native accentuation.

To listen to the **high-quality, native-speaker audio recordings** for every term in this database, please visit the official interactive dictionary:
👉 **[YouPronounce.it - The Free Pronunciation Dictionary](https://youpronounce.it)**

For example, to hear the correct audio for medical terminology, browse the **[Architects Category](https://youpronounce.it/architects/)**.

---

## 📦 Installation & Usage

Clone the repository and run the Python wrapper to query the local JSON database.

```bash
git clone https://github.com/YourUsername/PyPronounce-Database.git
cd PyPronounce-Database
python3 pypronounce.py
```

### Example Usage (Python)

```python
from pypronounce import PronunciationDB

db = PronunciationDB()

# Search for a tricky word
results = db.search_term("Adolf Loos")
print(results[0]['phonetic_guide']) 
# Output: "In German, the name Adolf Loos is pronounced [ˈaːdɔlf ˈloːs]."

# Get the official audio link
audio_link = db.get_audio_url("OEdème de Quincke")
print(f"Listen to the audio here: {audio_link}")
```

## 📊 Dataset Structure

The `pronunciation_db.json` file contains an array of objects structured as follows:

- `term`: The target word, name, or expression.
- `category`: Classification (e.g., Tech Brands, Football Players, Medical).
- `phonetic_guide`: A descriptive text snippet containing the pronunciation rules or IPA.
- `audio_source_url`: The direct URL to the **[YouPronounce.it](https://youpronounce.it)** entry containing the official video/audio playback and further context.

## 🤝 Contributing & Full Database Access

The dataset provided in this repository is a sample subset. The full database (4,000+ entries, growing daily) is proprietary and maintained directly on the main platform to ensure audio quality and server stability. 

If you wish to suggest a new word to be recorded and added to the official database, please use the search bar on **[YouPronounce.it](https://youpronounce.it)**. If the word is missing, our phonetic team will log the search query and schedule a recording.

## 📄 License

The Python wrapper code (`pypronounce.py`) and the sample JSON dataset are released under the MIT License. The audio and video assets hosted on the main site remain the property of their respective creators.
