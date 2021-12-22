import os
import cfg
import sys
import pygame
import random
from modules import *


def init_game():

    pygame.init()
    screen = pygame.display.set_mode(cfg.screensize)
    pygame.display.set_caption('Catch coins')

    game_images = {}
    for key, value in cfg.image_paths.items():
        if isinstance(value, list):
            images = []
            for item in value:
                images.append(pygame.image.load(item))
            game_images[key] = images
        else:
            game_images[key] = pygame.image.load(value)

    game_sounds = {}

    for key, value in cfg.audio_paths.items():
        if key == 'bgm':
            continue
        game_sounds[key] = pygame.mixer.Sound(value)

    return screen, game_images, game_sounds

def main():

    screen, game_images, game_sounds = init_game()

    pygame.mixer.music.load(cfg.audio_paths['bgm'])
    pygame.mixer.music.play(-1, 0.0)

    font = pygame.font.Font(cfg.font_path, 40)

    hero = Hero(game_images['hero'], position=(375, 520))

    food_sprites_group = pygame.sprite.Group()
    generate_food_freq = random.randint(10, 20)
    generate_food_count = 0

    score = 0
    highest_score = 0 if not os.path.exists(cfg.highest_score_record_filepath) else int(open(cfg.highest_score_record_filepath).read())

    clock = pygame.time.Clock()

    while True:

        screen.fill(0)
        screen.blit(game_images['background'], (0, 0))

        countdown_text = 'Count down: ' + str((90000 - pygame.time.get_ticks())// 60000) + ":" + str((90000 - pygame.time.get_ticks())// 1000 % 60).zfill(2)
        countdown_text = font.render(countdown_text, True, (0, 0, 0))
        countdown_rect = countdown_text.get_rect()
        countdown_rect.topright = [cfg.screensize[0] - 30, 5]
        screen.blit(countdown_text, countdown_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            hero.move(cfg.screensize, 'left')
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            hero.move(cfg.screensize, 'right')

        generate_food_count += 1

        if generate_food_count > generate_food_freq:
            generate_food_freq = random.randint(10, 20)
            generate_food_count = 0
            food = Food(game_images, random.choice(['gold']*10 + ['apple']), cfg.screensize)
            food_sprites_group.add(food)

        for food in food_sprites_group:
            if food.update():
                food_sprites_group.remove(food)

        for food in food_sprites_group:
            if pygame.sprite.collide_mask(food, hero):
                game_sounds['get'].play()
                food_sprites_group.remove(food)
                score += food.score
                if score > highest_score:
                    highest_score = score

        hero.draw(screen)

        food_sprites_group.draw(screen)

        score_text = f'Score: {score}, Highest: {highest_score}'
        score_text = font.render(score_text, True, (0, 0, 0))
        score_rect = score_text.get_rect()
        score_rect.topleft = [5, 5]
        screen.blit(score_text, score_rect)

        if pygame.time.get_ticks() >= 90000:
            break

        pygame.display.flip()
        clock.tick(cfg.fps)

    fp = open(cfg.highest_score_record_filepath, "w")
    fp.write(str(highest_score))
    fp.close()
    return show_end_interface(screen, cfg, score, highest_score)


if __name__ =="__main__":
    while main():
        pass

















