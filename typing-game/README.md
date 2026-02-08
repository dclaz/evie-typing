# Typing Game for Toddlers

## How to Start
- Run `main.py` with Python or double-click the executable.

## How to Exit
- Press ESC key.

## How to Add/Edit Words
- Edit `words.txt` (one word per line, 3-5 letters recommended).

## Customization
- Edit `config.toml` for colors, fonts, and settings.

## Settings Reference
- `anti_aliasing`: Smooth text rendering
- `fullscreen`: Fullscreen mode
- `force_case`: Letter case handling
- Color settings: UI color customization
- `family`: Font selection
- `sound_enabled`: Toggle sounds
- `confetti_enabled`: Toggle confetti effects

## Troubleshooting
- If `words.txt` is missing, game uses numbers 0-9.
- Missing sounds/fonts: Game runs silently or with default font.
- Performance: Game targets 60 FPS, runs on most hardware.
- Font rendering: Toggle anti-aliasing in config.

## System Requirements
- Windows or Linux
- Python 3.7+
- Minimal specs (runs on most devices)

## Build Instructions
- Install dependencies: `pip install pygame pyinstaller toml`
- Build executable: See plan.md for PyInstaller commands.

## Distribution
- Package executable, `words.txt`, `config.toml`, `assets/`, and `README.md` in a ZIP.
