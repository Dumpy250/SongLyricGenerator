# 🎵 Song Lyric Generator

A Python/Tkinter desktop application designed to request song lyrics or poems from OpenAI based on a user prompt. It demonstrates GUI development, API integration and process-environment configuration.

## ✨ Features

- Select **Song** or **Poem**.
- Enter a prompt of up to **50 characters**; blank/whitespace-only prompts are rejected.
- Choose output-token presets: **Short (100)**, **Medium (200)** or **Long (400)**. These are maximum token settings, not guaranteed word counts or output lengths.
- Adjust the token spinbox, which displays a **16–2000** range and defaults to **200**. Manual input is not fully validated.
- View successful generations in **session-only history**.
- Save the current output text through **Save Lyrics** to a chosen `.txt` file.

## Compatibility status

The source uses the modern `OpenAI` client and `client.chat.completions.create(...)`, with **`gpt-4o-mini` hard-coded**. This call style exists in the declared SDK's lower-bound version, `openai` 2.0.0; it is not the removed legacy `openai.Completion.create` interface.

**Model lifecycle checked November 17, 2026:** OpenAI marks [GPT-4o mini](https://platform.openai.com/docs/models/gpt-4o-mini) deprecated and lists its model family/snapshot for **January 14, 2027 shutdown** in the [API deprecation schedule](https://platform.openai.com/docs/deprecations). Deprecated is not the same as already shut down, but this integration needs a separately reviewed model update before continued use beyond that date. Actual account access and successful generation have not been verified here.

The source also sends `max_tokens`, a parameter deprecated in favor of `max_completion_tokens`. A replacement model must be checked for endpoint, message-role and parameter compatibility; changing only a model name is not a verified migration. No SDK, model or code changes are included in this README update.

## 🧰 Tech Stack

- **Python / Tkinter** — requires a graphical desktop and a Python installation with Tcl/Tk support.
- **OpenAI Python SDK** — `requirements.txt` contains `openai>=2.0.0`; no lockfile or upper bound is supplied.
- **Environment variables** — the code reads `OPENAI_API_KEY` directly with `os.getenv`.

The previous Python **3.11+** guidance is a suggested baseline, not an enforced or tested minimum. Choose a [supported Python version](https://devguide.python.org/versions/) compatible with the SDK version actually resolved by installation. `python-dotenv` is neither a dependency nor imported by the application.

## 📁 Project Structure

```text
SongLyricGenerator/
├── api/
│   ├── __init__.py
│   └── openai.py            # API request and retry wrapper
├── gui/
│   ├── __init__.py
│   └── main_window.py       # Tkinter UI and session history
├── main.py                 # Application entry point
├── requirements.txt        # openai>=2.0.0
├── .gitignore
├── song-lyrics.ico         # Optional window icon
└── README.md
```

**No `.env.example` is included.** A `.env` file is not loaded automatically by this code, so creating one alone will not configure the API key.

## 🚀 Setup Instructions

These are **source-checked, unexecuted instructions**, not a fresh-install or live-generation verification. Installing requirements downloads dependencies; clicking Generate sends the prompt to an external service and can incur API charges. Review the compatibility notice before doing either.

### 1. Clone the repository

```sh
git clone https://github.com/Dumpy250/SongLyricGenerator.git
cd SongLyricGenerator
```

### 2. Prepare a virtual environment and dependencies

Use a Python installation that includes Tkinter/Tcl/Tk. On some platforms, Tk support is a separate operating-system package; installing `requirements.txt` does not install it. See the [Python Tkinter documentation](https://docs.python.org/3.11/library/tkinter.html).

Windows PowerShell, from the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

macOS/Linux shell, from the repository root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

These examples use the environment's interpreter directly; activation and shell execution-policy changes are not required. The open-ended requirement is not a reproducible SDK pin, and compatibility with every future SDK release is not established.

### 3. Configure the process environment

Set **`OPENAI_API_KEY`** in your private IDE run configuration or another secure process-environment mechanism, using your own API credential. Ensure the Python process launched below inherits it. Do not put the real value in source files, shared launch settings, shell history, screenshots or logs.

The key is checked when generating text, not when opening the window. A missing key raises an error displayed by the GUI. A visible window alone does not prove API access, billing availability or model compatibility. There is no model-selection environment setting in this application.

## ▶️ Running the App

From the repository root, in the configured environment:

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe main.py
```

macOS/Linux:

```sh
.venv/bin/python main.py
```

The icon path is relative to the working directory. Icon-loading failures are silently ignored, so the application may open without its icon on some platforms. Desktop/platform rendering has not been verified by this documentation pass.

## 🧪 Example Usage

After prerequisites and API access are established:

1. Enter a prompt such as **“A song about learning to code at 2am”**.
2. Select **Song** or **Poem**, then a token preset or numeric limit.
3. Click **Generate Lyrics**. Successful text appears in the editable output box and is added to the current session's history.
4. Optionally use **Show History** or **Save Lyrics**.

This is an example interaction, not recorded successful API output. History contains mode/text pairs in memory and disappears when the app closes. Saving writes only the current output text—not the whole history, original prompt or generation settings—to the selected file. Generated text is not guaranteed to be unique or suitable without review.

## Limitations

- API requests and retries run synchronously on the GUI thread; the window can be unresponsive while waiting. There is no background generation or cancel control.
- The wrapper makes up to three attempts, and SDK-level retries may add requests. It does not distinguish retryable errors from permanent failures such as unavailable models.
- Manual token entry can bypass the displayed range; nonnumeric input is converted before the API-error handler and lacks a friendly validation path.
- File saving uses the platform's default text encoding and does not handle write errors explicitly.
- No automated tests or retained successful-generation evidence are supplied with this documentation pass.

## 🔐 Security Notes

- `.env` and `.env.*` are ignored by Git, but the app does not read them. Do not rely on the missing `.env.example` or a nonexistent dotenv loader.
- Ignore rules do not prevent forced commits, remove existing Git history or revoke exposed credentials. Keep keys private and rotate any exposed key through its provider.
- Prompts are sent to OpenAI when generating. Avoid confidential content unless that external processing is authorized, and review saved output before sharing.
