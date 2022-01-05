import pygame
from time import sleep

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer_music.play()
sleep(10)
pygame.event.wait()


'''Correção Guanabara

import pygame
pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
pygame.event.wait()

'''