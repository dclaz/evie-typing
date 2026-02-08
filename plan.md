# Typing Game for Toddlers - Project Plan

## Overview
A fullscreen, case-insensitive typing game for 3-year-olds, built with Pygame. The game displays one simple word at a time in the center of the screen, with big, bold, pastel-colored UI. Gentle feedback and fun effects encourage correct typing.

## Target User
- Age: ~3 years old
- Learning to recognize letters and numbers
- Developing hand-eye coordination and keyboard familiarity

## Features

### Core Gameplay
- **Fullscreen Pygame window** (optimized for 1440p, scales to other resolutions)
- **One word at a time** displayed in center of screen
- **Case-insensitive typing**
- **Random word selection** from word list (words repeat infinitely)
- **Free play mode** - no timer, no game over, no stress
- **Exit only** - ESC key to quit (no other hotkeys to avoid accidental interruptions)

### Visual Feedback
- **Target letter**: Highlighted and displayed larger than other letters
- **Already typed letters**: Displayed in a different pastel color (e.g., soft green)
- **Remaining letters**: Grey or low-contrast (de-emphasized)
- **Wrong key feedback**: Shake the target letter briefly, show incorrect letter in small font below
- **Correct letter**: Small confetti effect and pleasant chime sound
- **Word completion**: 
  - Word grows larger
  - Happy face emoji(s) appear (🎉😊)
  - Word slides off screen in random direction (up/down/left/right)
  - Larger confetti burst
  - Next word appears immediately

### UI Elements
- **WPM counter** in top-right corner (small, unobtrusive font for parent monitoring)
- **Large, child-friendly font** (configurable: serif or sans-serif Google Fonts)
- **Fixed pastel color scheme** (pink, purple, cream, soft blue, etc.)

## Word List

### words.txt Content
Populate with simple 3-5 letter words a toddler might use:
- Animals: cat, dog, fish, bird, bear, lion
- Family: mum, dad, baby
- Food: food, drink, water, milk, cake, apple
- Descriptors: big, small, hot, cold
- Objects: car, ball, book, toy, moon, star, tree, sun
- Fun: dragon, robot, happy

**Plus single-digit numbers**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

### Fallback Behavior
If `words.txt` is missing or empty, use random integers from 0-9 as the word list.

## File Structure
```
typing-game/
├── main.py              # Main game code
├── words.txt            # Word list (one word per line)
├── config.json          # Configuration (font style, colors, etc.)
├── README.md            # Parent-facing instructions
├── assets/
│   ├── chime.wav        # Free/open-source chime sound (correct letter)
│   ├── complete.wav     # Optional: word completion sound
│   └── fonts/
│       ├── sans-serif.ttf  # Google Font (e.g., Quicksand, Nunito)
│       └── serif.ttf       # Google Font (e.g., Crimson Text)
└── plan.md              # This file
```

## Technical Specifications

### Display
- **Resolution**: Optimized for 2560x1440 (1440p), scales to fullscreen on any display
- **Word position**: Center of screen
- **Font sizes** (approximate, scale based on resolution):
  - Target letter: 240px
  - Typed/remaining letters: 120px
  - Incorrect letter display: 60px
  - WPM counter: 24px

### Colors (Fixed Pastel Palette)
- Background: Soft cream (#FFF8E7)
- Target letter: Bright pastel pink (#FFB3D9)
- Typed letters: Soft green (#B4E7B4)
- Remaining letters: Light grey (#CCCCCC)
- Incorrect letter: Soft red (#FFB3BA)
- WPM text: Muted purple (#D4C5E8)

### Animations
- **Letter shake** (wrong key): 10px horizontal shake, 200ms duration
- **Confetti** (correct letter): 15-20 small particles, fall for 1 second
- **Word completion confetti**: 50-80 particles, various colors, fall for 2 seconds
- **Word slide-off**: 800ms duration, random direction (up/down/left/right), ease-out

### Audio
- Use free/open-source sounds (e.g., from freesound.org with CC0 license)
- `chime.wav`: Gentle bell/chime for correct letter (~0.3s)
- Optional `complete.wav`: Celebratory sound for word completion

### Performance
- Target 60 FPS
- Minimal CPU usage for toddler-friendly devices
- Smooth animations even on older hardware

## Configuration (config.json)
```json
{
  "font_style": "sans-serif",
  "background_color": "#FFF8E7",
  "target_color": "#FFB3D9",
  "typed_color": "#B4E7B4",
  "remaining_color": "#CCCCCC",
  "incorrect_color": "#FFB3BA",
  "wpm_color": "#D4C5E8",
  "confetti_enabled": true,
  "sound_enabled": true
}
```

## README.md Content

Include instructions for parents:
- How to start the game
- How to exit (ESC key)
- How to add/edit words in `words.txt`
- How to customize colors/fonts in `config.json`
- Troubleshooting (missing files, performance issues)

## Build Instructions

### Windows
```bash
pip install pygame pyinstaller
pyinstaller --onefile --windowed --add-data "words.txt;." --add-data "assets;assets" main.py
```

### Linux
```bash
pip install pygame pyinstaller
pyinstaller --onefile --windowed --add-data "words.txt:." --add-data "assets:assets" main.py
```

Output executables will be in `dist/` folder.

## Dependencies
- **Pygame** (open source) - game framework
- **PyInstaller** (open source) - executable builder
- **Google Fonts** (open source) - child-friendly typography

## Success Criteria
- Toddler can easily see what letter to type next
- Positive reinforcement for every correct key press
- No frustration from wrong presses (gentle feedback only)
- Parents can easily customize word list
- Runs smoothly on common hardware
- Simple to build and distribute

## Next Steps
1. ✅ Create comprehensive plan.md
2. Implement main.py with all features
3. Populate words.txt with toddler-friendly words
4. Source free chime sound and Google Fonts
5. Create config.json with default settings
6. Write README.md for parents
7. Test with target age group
8. Build Windows and Linux executables
9. Package for distribution

---

**Notes for Implementation:**
- Keep code well-commented for future modifications
- Handle edge cases gracefully (empty words.txt, missing assets)
- Use clear variable names for maintainability
- Test thoroughly with keyboard input variations