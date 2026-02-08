# Typing Game for Toddlers - Project Plan

## Overview
A fullscreen, case-insensitive typing game for 3-year-olds, built with Pygame. The game displays one simple word at a time in the center of the screen, with big, bold, high-contrast UI in a cute, girly theme. Gentle feedback and fun effects encourage correct typing.

## Target User
- Age: ~3 years old
- Learning to recognize letters and numbers
- Developing hand-eye coordination and keyboard familiarity

## Features

### Core Gameplay
- **Fullscreen Pygame window** (optimized for 1440p, scales to other resolutions)
- **One word at a time** displayed in center of screen
- **Case handling** - configurable (force uppercase, force lowercase, or preserve case from file; default: uppercase)
- **Random word selection** from word list (words repeat infinitely)
- **Free play mode** - no timer, no game over, no stress
- **Exit only** - ESC key to quit (no other hotkeys to avoid accidental interruptions)

### Visual Feedback
- **Target letter**: **Bold**, highlighted in bright color, regular size
- **Already typed letters**: Displayed in bright contrasting color
- **Remaining letters**: Medium grey (de-emphasized)
- **Wrong key feedback**: 
  - Shake the target letter briefly (200ms)
  - Show incorrect letter in small font below
  - Play gentle "boop" sound
- **Correct letter**: 
  - Small rainbow confetti burst
  - Pleasant chime sound
- **Word completion**: 
  - **3 second celebration delay** (word stays visible, pulses slightly)
  - Random happy face emoji(s) appear (😊, 🎉, 🌟, 🎊, 👏, 🥳)
  - Word grows larger
  - Larger rainbow confetti burst
  - Word slides off screen in random direction (up/down/left/right)
  - Happy emoji stays on screen very briefly (0.5s) as word slides
  - **2 second pause** after slide-off before next word appears

### UI Elements
- **WPM counter** in top-right corner (small, unobtrusive font for parent monitoring)
  - Calculated over entire session
  - Only counts completed words
  - Rounded to integer
- **Child-friendly sans-serif font** (Quicksand or Nunito from Google Fonts)
- **High-contrast color scheme** with cute, girly theme

## Word List

### words.txt Content
Populate with simple 3-5 letter words a toddler might use:

**Animals**: cat, dog, fish, bird, bear, lion, duck, frog, bee
**Family**: mum, dad, baby, gran, papa
**Food**: food, drink, water, milk, cake, apple, bread, pizza
**Descriptors**: big, small, hot, cold, happy, soft, hard
**Objects**: car, ball, book, toy, moon, star, tree, sun, flower, house
**Fun**: dragon, robot, play, love, hug, kiss
**Numbers**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

Aim for 50-70 words total in initial list.

### Fallback Behavior
If `words.txt` is missing or empty, use random integers from 0-9 as the word list.

## File Structure
```
typing-game/
├── main.py              # Main game code
├── words.txt            # Word list (one word per line)
├── config.toml          # Configuration file
├── README.md            # Parent-facing instructions
├── assets/
│   ├── chime.wav        # Free/open-source chime sound (correct letter)
│   ├── boop.wav         # Gentle "try again" sound (wrong letter)
│   ├── complete.wav     # Optional: word completion sound
│   └── fonts/
│       └── Quicksand-Bold.ttf  # Google Font (primary choice)
│       └── Nunito-Bold.ttf     # Google Font (alternative)
└── plan.md              # This file
```

## Technical Specifications

### Display
- **Resolution**: Optimized for 2560x1440 (1440p), scales to fullscreen on any display
- **Word position**: Center of screen
- **Font rendering**: No anti-aliasing (configurable in config.toml)
- **Letter spacing**: Regular/default
- **Font sizes** (approximate, scale based on resolution):
  - All letters: 180px (target letter is **bold**, others regular weight)
  - Incorrect letter display: 60px
  - WPM counter: 28px
  - Emoji: 100px

### Colors (High-Contrast Cute/Girly Theme)
- **Background**: `#F5E6FF` (very light lavender)
- **Target letter**: `#FF1493` (deep pink - bold and bright)
- **Typed letters**: `#00CED1` (dark turquoise)
- **Remaining letters**: `#B0B0B0` (medium grey)
- **Incorrect letter**: `#FF6B6B` (coral red)
- **WPM text**: `#9370DB` (medium purple)

All colors configurable in config.toml.

### Input Handling
- **Accept**: 
  - Letters: a-z, A-Z
  - Numbers: 0-9 (both top row and numpad)
- **Ignore completely** (no feedback):
  - Modifier keys: Shift, Ctrl, Alt, Cmd/Win
  - Function keys: F1-F12
  - Special keys: Space, Enter, Tab, Backspace
  - Arrow keys, Home, End, Page Up/Down
- **Case handling**: All input converted based on `force_case` config setting before comparison

### Animations & Effects

**Letter Shake (Wrong Key)**
- Duration: 200ms
- Movement: ±10px horizontal oscillation
- Easing: Ease-out

**Confetti (Correct Letter)**
- Particle count: 20-30
- Shapes: **Randomly select one shape per burst** (circles, squares, stars, or hearts)
- Colors: Rainbow (red, orange, yellow, green, blue, purple, pink)
- Origin: Center of target letter
- Spread: Explode outward 45° cone upward, spread across ~60% of screen width
- Fall speed: 150-250 pixels/second (random per particle)
- Gravity: Gentle downward acceleration
- Rotation: Particles spin slowly as they fall (random rotation speed)
- Duration: 1.5 seconds visible

**Confetti (Word Completion)**
- Particle count: 80-100
- Same properties as letter confetti but more particles
- Spread: Full screen width, 120° cone
- Duration: 2.5 seconds visible

**Word Growth (Completion)**
- Delay before growth: 3 seconds (celebration pause)
- Duration: 500ms
- Scale: 1.0 → 1.3
- Easing: Ease-out

**Word Slide-Off**
- Duration: 800ms
- Direction: Random (up, down, left, right)
- Distance: Off-screen (1.5x screen dimension)
- Easing: Ease-in

**Emoji Display**
- Appears immediately on word completion
- Stays visible during 3-second celebration + slide animation
- Fades out 0.5 seconds after word starts sliding
- Fade duration: 300ms
- Random emoji selected from pool: 😊, 🎉, 🌟, 🎊, 👏, 🥳

**Timing Summary**
1. Word completed → 0s
2. Celebration pause (emoji appears, word visible) → 0-3s
3. Word grows larger → 3-3.5s
4. Word slides off (emoji fades at 3.5s) → 3.5-4.3s
5. Pause (blank screen) → 4.3-6.3s
6. Next word appears → 6.3s

Total cycle: ~6.3 seconds per word

### Audio
- Use free/open-source sounds (e.g., from freesound.org with CC0 license)
- **chime.wav**: Gentle bell/chime for correct letter (~0.3s, pleasant tone)
- **boop.wav**: Soft, friendly "try again" sound for wrong letter (~0.2s, not punishing)
- **complete.wav**: Optional celebratory sound for word completion (~0.5s)
- **Missing audio handling**: If any sound file missing, skip that sound (no error, silent)

### Performance
- Target 60 FPS
- Minimal CPU usage for toddler-friendly devices
- Smooth animations even on older hardware

## Configuration (config.toml)
```toml
[display]
anti_aliasing = false  # Set to true for smoother text rendering
fullscreen = true

[gameplay]
force_case = "upper"  # Options: "upper", "lower", "preserve"

[colors]
background = "#F5E6FF"
target_letter = "#FF1493"
typed_letter = "#00CED1"
remaining_letter = "#B0B0B0"
incorrect_letter = "#FF6B6B"
wpm_text = "#9370DB"

[font]
family = "Quicksand-Bold"  # Options: "Quicksand-Bold", "Nunito-Bold"

[audio]
sound_enabled = true

[effects]
confetti_enabled = true
```

## README.md Content

Include instructions for parents:
- **How to start the game** (double-click executable)
- **How to exit** (Press ESC key)
- **How to add/edit words** in `words.txt` (one word per line, 3-5 letters recommended)
- **How to customize** colors/fonts/settings in `config.toml`
- **What each setting does**
- **Troubleshooting**:
  - Missing files behavior
  - Performance issues
  - Font rendering (anti-aliasing toggle)
- **System requirements** (Windows/Linux, minimal specs)

## Build Instructions

### Dependencies Installation
```bash
pip install pygame pyinstaller toml
```

### Windows Build
```bash
pyinstaller --onefile --windowed --add-data "words.txt;." --add-data "config.toml;." --add-data "assets;assets" --name typing-game-toddler main.py
```

### Linux Build
```bash
pyinstaller --onefile --windowed --add-data "words.txt:." --add-data "config.toml:." --add-data "assets:assets" --name typing-game-toddler main.py
```

Output executables will be in `dist/` folder.

### Distribution Package
Create a ZIP file containing:
- Executable (typing-game-toddler.exe or typing-game-toddler)
- words.txt
- config.toml
- assets/ folder (with all sounds and fonts)
- README.md

## Dependencies
- **Pygame** (open source) - game framework
- **PyInstaller** (open source) - executable builder
- **tomllib** (open source) - configuration file parsing (Already in python)
- **Google Fonts** (open source) - Quicksand and Nunito fonts

## Success Criteria
- ✅ Toddler can easily see what letter to type next (bold + high contrast)
- ✅ Positive reinforcement for every correct key press
- ✅ Gentle, non-punishing feedback for wrong presses
- ✅ Fun, varied visual effects (random confetti shapes)
- ✅ Parents can easily customize word list and settings
- ✅ Runs smoothly on common hardware (60 FPS target)
- ✅ Simple to build and distribute
- ✅ No complex hotkeys or accidental interruptions

## Implementation Notes for Agent

### Code Organization
```python
# Suggested main.py structure:
# 1. Imports and configuration loading
# 2. Game state class (current word, position, typed letters, etc.)
# 3. Particle/confetti system class
# 4. Animation manager class
# 5. Main game loop
# 6. Event handling
# 7. Rendering functions
# 8. WPM calculation
```

### Key Implementation Details
1. **Font loading**: Load bold variant explicitly, handle missing fonts gracefully
2. **Word loading**: Strip whitespace, apply `force_case` setting, shuffle list
3. **Confetti system**: Use particle pool for performance, random shape selection per burst
4. **Input validation**: Create whitelist of accepted keys (a-z, 0-9), ignore everything else
5. **Timing**: Use pygame.time.get_ticks() for precise animation timing
6. **Error handling**: Try-except blocks for file loading, fail gracefully with defaults
7. **Unicode emoji**: Render emoji using pygame font with Unicode support (may need fallback)

### Testing Checklist
- [ ] All accepted keys work (letters, numbers, numpad)
- [ ] Ignored keys truly ignored (no visual/audio response)
- [ ] ESC exits cleanly
- [ ] Missing words.txt falls back to 0-9
- [ ] Missing sounds don't crash game
- [ ] Case conversion works correctly (upper/lower/preserve)
- [ ] Confetti shapes vary between bursts
- [ ] Timing sequence correct (3s pause → grow → slide → 2s pause → new word)
- [ ] WPM calculates correctly over session
- [ ] config.toml settings apply correctly
- [ ] Game scales properly to different resolutions

## Next Steps
1. ✅ Create comprehensive plan.md
2. Implement main.py with all features
3. Populate words.txt with 50-70 toddler-friendly words and numbers 0-9
4. Source free chime and boop sounds (CC0 license from freesound.org)
5. Download Quicksand-Bold.ttf and Nunito-Bold.ttf from Google Fonts
6. Create config.toml with default settings
7. Write comprehensive README.md for parents
8. Test with target age group
9. Build Windows and Linux executables
10. Create distribution packages (ZIP with all assets)
11. Optional: Create simple icon for executable

---

## Visual Layout Reference
```
┌─────────────────────────────────────────────────┐
│                                          WPM: 12│ (top-right, small purple)
│                                                 │
│                                                 │
│                                                 │
│                  C A T                          │ (center, large)
│                  ^                              │ (bold pink)
│                  D  ← (wrong key, small)        │
│                                                 │
│                                                 │
│              [confetti particles]               │
│                                                 │
│                                                 │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Color Legend:**
- C (typed) = turquoise
- A (target) = **bold deep pink**
- T (remaining) = grey
- d (wrong) = coral red
- Background = light lavender

---

**Note**: This plan is optimized for a coding agent to implement without ambiguity. All timings, colors, sizes, and behaviors are explicitly specified.



# EDIT
* Show an emoji if one exists for the word, big above the word.
* Remove the shaking. Make the word grow much bigger, and make it happen quicker. Reduce next word delay.