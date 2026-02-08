# Typing Game for Toddlers - Project Plan

## Overview
A fullscreen, case-insensitive typing game for young children, built with Pygame. The game displays one simple word at a time, with big, bold, pastel-colored UI. Gentle feedback and fun effects encourage correct typing.

## Features
- Fullscreen Pygame window
- One word at a time, from a simple word list (plain text file, one word per line)
- Big, bold, pastel UI (fixed colors)
- Case-insensitive typing
- Shows the next letter to type in large font
- Gentle feedback for wrong key: shake the target letter and show the incorrect letter in small font below
- Confetti effect and pleasant chime sound (free/open source) for correct key
- Progress indicator: number of words completed and words per minute
- Free play (no timer or game over)
- Exit with ESC key
- Child-friendly font (configurable: serif or sans-serif, using popular Google Fonts)
- Windows executable build instructions (PyInstaller)

## File Structure
- main.py — main game code
- words.txt — word list (one word per line)
- assets/
  - chime.wav — free/open source chime sound
  - fonts/ — Google Fonts (serif and sans-serif)
- config.json — config for font style, colors, etc.
- plan.md — this plan

## Technical Notes
- All dependencies are open source (Pygame, PyInstaller, Google Fonts)
- Game is designed for easy use by toddlers: minimal controls, gentle feedback, and clear visuals
- All UI colors are fixed pastel shades (pink, purple, cream, etc.)
- Sound and font can be swapped via config

## Next Steps
1. Populate words.txt with simple words
2. Download and include free chime sound and Google Fonts
3. Implement main.py with all features
4. Add config.json for font and color options
5. Add build instructions for Windows executable
