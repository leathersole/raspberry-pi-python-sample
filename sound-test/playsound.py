import pygame.mixer
from time import sleep

pygame.mixer.init(48000,-16,1,1024)

sound = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Center.wav")
channelA = pygame.mixer.Channel(1)
channelA.play(sound)
sleep(2.0)
