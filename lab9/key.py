import pygame
import os
pygame.init()
pygame.mixer.init()
W, H = 800, 600
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Player")
music_dir = r'C:\Users\Сания\desktop\pp2\lab9\music'
music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]

current_music = 0

pygame.mixer.music.load(os.path.join(music_dir, music_files[current_music]))

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_music():
    global current_music
    current_music = (current_music + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_music]))
    play_music()

def prev_music():
    global current_music
    current_music = (current_music - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_music]))
    play_music()

clock = pygame.time.Clock()
FPS = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        play_music()
    if keys[pygame.K_s]:
        stop_music()
    if keys[pygame.K_d]:
        next_music()
    if keys[pygame.K_a]:
        prev_music()

    pygame.display.update()
    clock.tick(FPS)