# 🎵 Song Lyric Generator

A desktop GUI application built with Python and Tkinter that uses OpenAI’s API to generate original song lyrics or poems based on a user prompt.

This project demonstrates:
- API integration
- GUI development with Tkinter
- Environment variable management
- Clean, reproducible project structure

---

## ✨ Features

- Generate **song lyrics or poems**
- Choose from **token length presets**
  - Short (100)
  - Medium (200)
  - Long (400)
- View **generation history**
- Save generated lyrics to a `.txt` file
- Simple, clean desktop UI

---

## 🧰 Tech Stack

- **Python 3.11+**
- **Tkinter** – GUI framework
- **OpenAI API**
- `python-dotenv` – environment variables

---

## 📁 Project Structure

```text
SongLyricGenerator/
│
├── api/                    # OpenAI API logic
│   ├── __init__.py
│   └── openai.py
│
├── gui/                    # Tkinter UI
│   ├── __init__.py
│   └── main_window.py
│
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files/folders
├── .env.example            # Environment variable template
├── song-lyrics.ico         # App icon
└── README.md               # Project documentation
```

## 🚀 Setup Instructions

---
1. Clone the repository

```
git clone https://github.com/yourusername/SongLyricGenerator.git
cd SongLyricGenerator
```

2. Create a virtual environment
```
python -m venv .venv
```

Activate it:
Windows
```
.venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Set up environment variables
```
cp .env.example .env
```

Edit .env and add your OpenAI key:
```
OPENAI_API_KEY=your_real_key_here
```

▶️ Running the App
```
python main.py

```

## 🧪 Example Usage

---
- Enter a prompt like:

A song about learning to code at 2am

- Choose:

Song or Poem

- Token length (Short / Medium / Long)

- Click Generate Lyrics

Optionally:

View history

Save output to a file

## 🔐 Security Notes

---
- Your real API key lives in .env

- .env is ignored by Git

- .env.example shows required variables for others

- This ensures secrets are never committed.