# Typing Game for Toddlers
# Main game code will be implemented here following plan.md specs.


import pygame
import toml
import os
import random
import sys

# --- Configuration and Asset Loading ---
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.toml')
WORDS_PATH = os.path.join(os.path.dirname(__file__), 'words.txt')
ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'assets')
FONTS_PATH = os.path.join(ASSETS_PATH, 'fonts')

DEFAULT_CONFIG = {
    'display': {'anti_aliasing': False, 'fullscreen': True},
    'gameplay': {'force_case': 'upper'},
    'colors': {
        'background': '#F5E6FF',
        'target_letter': '#FF1493',
        'typed_letter': '#00CED1',
        'remaining_letter': '#B0B0B0',
        'incorrect_letter': '#FF6B6B',
        'wpm_text': '#9370DB',
    },
    'font': {'family': 'Quicksand-Bold'},
    'audio': {'sound_enabled': True},
    'effects': {'confetti_enabled': True},
}

def load_config():
    try:
        return toml.load(CONFIG_PATH)
    except Exception:
        return DEFAULT_CONFIG

def load_words(force_case):
    try:
        with open(WORDS_PATH, 'r') as f:
            words = [w.strip() for w in f if w.strip()]
        if not words:
            raise ValueError('Empty word list')
    except Exception:
        words = [str(i) for i in range(10)]
    if force_case == 'upper':
        words = [w.upper() for w in words]
    elif force_case == 'lower':
        words = [w.lower() for w in words]
    # preserve: do nothing
    random.shuffle(words)
    return words

def main():
    config = load_config()
    words = load_words(config['gameplay'].get('force_case', 'upper'))

    pygame.init()
    info = pygame.display.Info()
    screen_width = info.current_w
    screen_height = info.current_h
    flags = pygame.FULLSCREEN if config['display'].get('fullscreen', True) else 0
    screen = pygame.display.set_mode((screen_width, screen_height), flags)
    pygame.display.set_caption('Typing Game for Toddlers')

    # Color parsing utility
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    colors = {k: hex_to_rgb(v) for k, v in config['colors'].items()}

    # Font loading
    font_family = config['font'].get('family', 'Quicksand-Bold')
    font_path = os.path.join(FONTS_PATH, f'{font_family}.ttf')
    if not os.path.exists(font_path):
        font_path = pygame.font.get_default_font()
    main_font = pygame.font.Font(font_path, int(screen_height * 0.13))
    wpm_font = pygame.font.Font(font_path, int(screen_height * 0.02))
    wrong_font = pygame.font.Font(font_path, int(screen_height * 0.045))

    # Sound loading
    def load_sound(name):
        path = os.path.join(ASSETS_PATH, f'{name}.wav')
        if os.path.exists(path):
            return pygame.mixer.Sound(path)
        return None
    chime_sound = load_sound('chime')
    boop_sound = load_sound('boop')
    complete_sound = load_sound('complete')

    # --- Gameplay State ---
    current_word_idx = 0
    typed_letters = ''
    wrong_letter = ''
    completed_words = 0
    start_ticks = pygame.time.get_ticks()

    # Animation state
    shake_start = 0
    shake_duration = 200
    shake_offset = 0
    confetti_particles = []
    confetti_time = 0
    celebration_start = 0
    celebration_duration = 3000
    emoji_pool = ['😊', '🎉', '🌟', '🎊', '👏', '🥳']
    show_emoji = ''
    word_grow = False
    grow_start = 0
    grow_duration = 500
    slide_start = 0
    slide_duration = 800
    slide_direction = None
    pause_start = 0
    pause_duration = 500
    word_complete = False

    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(60)
        now = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                key = event.unicode
                if not word_complete and (key.isalpha() or key.isdigit()):
                    target_word = words[current_word_idx]
                    next_letter = target_word[len(typed_letters)] if len(typed_letters) < len(target_word) else None
                    if next_letter and key.lower() == next_letter.lower():
                        typed_letters += next_letter
                        wrong_letter = ''
                        # Confetti burst
                        confetti_particles = []
                        confetti_time = now
                        for _ in range(25):
                            angle = random.uniform(-0.4, 0.4)
                            speed = random.uniform(150, 250)
                            color = random.choice([(255,0,0),(255,165,0),(255,255,0),(0,255,0),(0,0,255),(128,0,128),(255,105,180)])
                            confetti_particles.append({'x': screen_width//2, 'y': screen_height//2, 'vx': speed*angle, 'vy': -speed, 'color': color, 'shape': random.choice(['circle','square','star','heart']), 'rot': random.uniform(0,360), 'rot_speed': random.uniform(-2,2)})
                        if chime_sound:
                            chime_sound.play()
                        if typed_letters == target_word:
                            completed_words += 1
                            word_complete = True
                            celebration_start = now
                            show_emoji = random.choice(emoji_pool)
                            if complete_sound:
                                complete_sound.play()
                            grow_start = now + celebration_duration
                            slide_start = grow_start + grow_duration
                            pause_start = slide_start + slide_duration
                            slide_direction = random.choice(['up','down','left','right'])
                    else:
                        wrong_letter = key
                        shake_start = now
                        if boop_sound:
                            boop_sound.play()

        # --- Rendering ---
        screen.fill(colors['background'])
        target_word = words[current_word_idx]
        x_center = screen_width // 2
        y_center = screen_height // 2

        # Letter shake animation
        shake_offset = 0
        if wrong_letter and now - shake_start < shake_duration:
            shake_offset = int(10 * ((now - shake_start) / shake_duration) * (-1 if ((now//30)%2)==0 else 1))

        # Word grow/slide animation
        scale = 1.0
        slide_x = 0
        slide_y = 0
        if word_complete:
            if now < grow_start:
                # Celebration pause
                scale = 1.0 + 0.03 * ((now - celebration_start) / celebration_duration)
            elif now < slide_start:
                # Word grows
                scale = 1.0 + 0.3 * ((now - grow_start) / grow_duration)
            elif now < pause_start:
                # Word slides off
                frac = (now - slide_start) / slide_duration
                dist = int(frac * 1.5 * (screen_height if slide_direction in ['up','down'] else screen_width))
                if slide_direction == 'up':
                    slide_y = -dist
                elif slide_direction == 'down':
                    slide_y = dist
                elif slide_direction == 'left':
                    slide_x = -dist
                elif slide_direction == 'right':
                    slide_x = dist
            else:
                # Pause before next word - keep word off-screen
                dist = int(1.5 * (screen_height if slide_direction in ['up','down'] else screen_width))
                if slide_direction == 'up':
                    slide_y = -dist
                elif slide_direction == 'down':
                    slide_y = dist
                elif slide_direction == 'left':
                    slide_x = -dist
                elif slide_direction == 'right':
                    slide_x = dist
                
                if now - pause_start > pause_duration:
                    prev_idx = current_word_idx
                    # Pick a new word index different from previous
                    if len(words) > 1:
                        while True:
                            next_idx = random.randint(0, len(words)-1)
                            if next_idx != prev_idx:
                                break
                        current_word_idx = next_idx
                    else:
                        current_word_idx = (current_word_idx + 1) % len(words)
                    typed_letters = ''
                    wrong_letter = ''
                    word_complete = False
                    show_emoji = ''
                    scale = 1.0
                    slide_x = 0
                    slide_y = 0

        # Draw word letters
        letter_spacing = int(screen_width * 0.02 * scale)
        word_surface = []
        for i, letter in enumerate(target_word):
            if i < len(typed_letters):
                color = colors['typed_letter']
                font = main_font
            elif i == len(typed_letters):
                color = colors['target_letter']
                font = main_font
            else:
                color = colors['remaining_letter']
                font = main_font
            surf = font.render(letter, config['display'].get('anti_aliasing', False), color)
            if scale != 1.0:
                surf = pygame.transform.rotozoom(surf, 0, scale)
            word_surface.append(surf)

        total_width = sum([surf.get_width() for surf in word_surface]) + letter_spacing * (len(word_surface) - 1)
        x = x_center - total_width // 2 + shake_offset + slide_x
        y = y_center - main_font.get_height() // 2 + slide_y
        for surf in word_surface:
            screen.blit(surf, (x, y))
            x += surf.get_width() + letter_spacing

        # Draw wrong letter feedback
        if wrong_letter:
            wrong_surf = wrong_font.render(wrong_letter, config['display'].get('anti_aliasing', False), colors['incorrect_letter'])
            wx = x_center - wrong_surf.get_width() // 2
            wy = y_center + main_font.get_height() // 2 + 10
            screen.blit(wrong_surf, (wx, wy))

        # Draw confetti particles
        if confetti_particles and now - confetti_time < 1500:
            for p in confetti_particles:
                px = int(p['x'] + p['vx'] * ((now - confetti_time)/1000.0))
                py = int(p['y'] + p['vy'] * ((now - confetti_time)/1000.0) + 0.5 * 200 * ((now - confetti_time)/1000.0)**2)
                rot = p['rot'] + p['rot_speed'] * ((now - confetti_time)/1000.0)
                if p['shape'] == 'circle':
                    pygame.draw.circle(screen, p['color'], (px, py), 12)
                elif p['shape'] == 'square':
                    rect = pygame.Rect(px-10, py-10, 20, 20)
                    pygame.draw.rect(screen, p['color'], rect)
                elif p['shape'] == 'star':
                    pygame.draw.polygon(screen, p['color'], [(px,py-12),(px+5,py-2),(px+12,py),(px+5,py+2),(px,py+12),(px-5,py+2),(px-12,py),(px-5,py-2)])
                elif p['shape'] == 'heart':
                    pygame.draw.circle(screen, p['color'], (px-6, py-6), 7)
                    pygame.draw.circle(screen, p['color'], (px+6, py-6), 7)
                    pygame.draw.polygon(screen, p['color'], [(px-13,py-2),(px,py+14),(px+13,py-2)])

        # Draw emoji celebration
        if show_emoji:
            emoji_font = pygame.font.Font(font_path, int(screen_height * 0.07 * scale))
            emoji_surf = emoji_font.render(show_emoji, True, (0,0,0))
            ey = y_center - main_font.get_height() // 2 - emoji_surf.get_height() - 30 + slide_y
            ex = x_center - emoji_surf.get_width() // 2 + slide_x
            if word_complete and now > slide_start:
                # Fade out emoji
                fade = max(0, 255 - int(255 * ((now - slide_start)/500)))
                emoji_surf.set_alpha(fade)
            screen.blit(emoji_surf, (ex, ey))

        # Draw WPM counter (top-right)
        elapsed_sec = (pygame.time.get_ticks() - start_ticks) / 1000.0
        wpm = int(completed_words / elapsed_sec * 60) if elapsed_sec > 0 else 0
        wpm_text = f'WPM: {wpm}'
        wpm_surf = wpm_font.render(wpm_text, config['display'].get('anti_aliasing', False), colors['wpm_text'])
        screen.blit(wpm_surf, (screen_width - wpm_surf.get_width() - 20, 20))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()