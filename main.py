import pygame
from pygame.locals import *
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Maddie")

#set bg color
bg = 'darkslateblue'
screen.fill(bg)

# load sprite images
idle_sprite = [pygame.image.load('assets/maddie_idle1.png'),
               pygame.image.load('assets/maddie_idle2.png')]
blink_sprite = [pygame.image.load('assets/maddie_blink1.png'),
                pygame.image.load('assets/maddie_blink2.png')]
meow_sprite = [pygame.image.load('assets/maddie_meow.png')]
sleeping_sprite = [pygame.image.load('assets/maddie_sleeping1.png'),
                   pygame.image.load('assets/maddie_sleeping2.png')]
yawn_sprite = [pygame.image.load('assets/maddie_yawn1.png'),
               pygame.image.load('assets/maddie_yawn2.png'),
               pygame.image.load('assets/maddie_yawn3.png'),
               pygame.image.load('assets/maddie_yawn4.png'),
               pygame.image.load('assets/maddie_yawn5.png'),
               pygame.image.load('assets/maddie_yawn6.png'),
               pygame.image.load('assets/maddie_yawn7.png')]

# load sounds
meow_sound= pygame.mixer.Sound('assets/meow.wav')
purr_sound = pygame.mixer.Sound('assets/purr.wav')


def main():

    # create a clock object to track the amount of time
    clock = pygame.time.Clock()

    # regulate animation speed vs. framerate
    IMAGE_INTERVAL = 500 # constant time in miliseconds between images
    last_update = 0 # time in miliseconds that image was last updated

    # keep track of current frame for animations
    frame = 0

    # sprites to cycle at random
    sprites = [idle_sprite, blink_sprite, yawn_sprite, sleeping_sprite]

    # load idle sprite at start-up
    sprite = idle_sprite

    # create rect around sprite 
    area = pygame.Rect(75, 75, 150, 150)

    # create timed event -- randomize sprite every 10 secs
    randomize_sprite = pygame.USEREVENT + 1
    pygame.time.set_timer(randomize_sprite, 10000)
    
    done = False

    while not done: # main loop

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if sprite != sleeping_sprite:
                    if event.button == 1: # left mouse button
                        if area.collidepoint(event.pos):
                            pygame.mixer.Sound.play(meow_sound)
                            sprite = meow_sprite

            elif event.type == randomize_sprite:
                sprite = random.choice(sprites)
                if sprite == sleeping_sprite:
                    pygame.mixer.Sound.play(purr_sound)

        # set framerate
        clock.tick(40)

        # loop animation frames
        if frame >= len(sprite):
            frame = 0

        # store sprite image (resized) -- override garbage collection
        img = pygame.transform.scale(sprite[frame], (150, 150))

        # display image
        screen.blit(img, img.get_rect(center = screen.get_rect().center))

        # update screen
        pygame.display.update()

        # fill window with bg color
        screen.fill(bg)

        # next frame
        if pygame.time.get_ticks() - last_update > IMAGE_INTERVAL:
           frame += 1
           last_update = pygame.time.get_ticks()

        # reset sprite to idle
        if sprite != idle_sprite and sprite != sleeping_sprite and frame == len(sprite):
            sprite = idle_sprite


if __name__ == '__main__':
    main()
    pygame.quit()


