````markdown
# 🎨 Amiga Pollinations Image Downloader  
### Python 2.0.1 Retro Edition

A very small command-line tool for classic Amiga / retro Python environments that  
generates AI images using the Pollinations image API and downloads them via `curl`.

Works with extremely old Python 2.x environments  
(tested conceptually for Python 2.0.1-style systems)  
where modern HTTPS libraries like `urllib` / `ssl` are broken or missing.

---

# 🚀 Features

- Prompt input via command line
- No SSL / Python HTTPS required (uses external `curl`)
- Timestamped filenames
- Saves directly to `RAM:` (or any Amiga path)
- Works with minimal Python 2.x installations

---

# 📦 Requirements

- Python 2.x (tested for very old builds like 2.0.1 style)
- `curl` installed on system
- Working internet connection
- Optional: AmiSSL (only needed for curl, not Python)
- `BSDSocket.library` on WinUAE

---

# 🧠 How It Works

The script:

1. Takes a prompt from user input
2. Encodes spaces for URL usage
3. Calls the Pollinations image API
4. Downloads the image using `curl`
5. Saves the file with a timestamp

---

# 📜 Script

```python
import os
import time

prompt = raw_input("Prompt eingeben: ")

# Simple URL encoding (space fix for old Python)
prompt = prompt.replace(" ", "%20")

url = "https://image.pollinations.ai/prompt/" + prompt

# Safe timestamp for old Python builds
timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))

outfile = "RAM:pollinations_" + timestamp + ".jpg"

cmd = 'curl -L -k "' + url + '" -o "' + outfile + '"'

print "Starte Download..."
os.system(cmd)

print "Fertig:", outfile
```

---

# ▶️ Usage

Run the script:

```bash
python pollinations.py
```

Example interaction:

```text
Prompt eingeben: amiga cyberpunk neon city
Starte Download...
Fertig: RAM:pollinations_20260517_153245.jpg
```

---

# 💾 Output

Images are saved as:

```text
RAM:pollinations_YYYYMMDD_HHMMSS.jpg
```

Example:

```text
RAM:pollinations_20260517_153245.jpg
```

---

# 🖥️ Notes for Amiga Users

- Very old Python versions may not support full HTTPS
- This script avoids Python SSL entirely
- Uses external `curl` for reliability
- If `curl` fails, ensure TLS 1.2 support (`--tlsv1.2` may help)

Example improved curl line:

```bash
curl --tlsv1.2 -L -k "<url>" -o "<file>"
```

---

# ❓ Why This Exists

Modern Python networking is not available on many Amiga systems.

This script provides a minimal bridge between:

- Retro Python environments
- Modern AI image APIs

---

# 💾 Compatibility

| System                    | Status |
|---------------------------|--------|
| AmigaOS                   | ✅ |
| MorphOS                   | ✅ |
| AROS                      | ✅ |
| Linux (old Python)        | ✅ |
| Modern Python 3           | ❌ (not needed) |

---

# 💡 Example Prompt Ideas

```text
amiga boing ball in space
cyberpunk amiga workstation neon glow
retro computer sci-fi dashboard
1980s amiga demoscene style city
```

---

# 📜 License

Public domain / DIY retro computing use.
````
