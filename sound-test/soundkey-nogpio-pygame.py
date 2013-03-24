#!/usr/bin/python
import os
 
os.environ['SDL_VIDEODRIVER'] = 'dummy'

import pygame
import pygame.midi

pygame.init()
pygame.midi.init()

pygame.display.set_mode((1,1))

instrument = 0
note = 74
volume = 127
port = 2

midiOutput = pygame.midi.Output(port, 0)
midiOutput.set_instrument(instrument)

finished = False

play = False
samekey = False
midion = False
oldplay = False
oldvolume = 0

print "Press q to quit..."

while not finished:
  pygame.event.pump()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      finished = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
          note = 60
      elif key == pygame.K_s: 
          note = 62
      elif key == pygame.K_d: 
          note = 64
      elif key == pygame.K_q: 
          finished = True

    if samekey == False and midion == True:
      midion =False
      midiOutput.note_off(oldnote,oldvolume)
    if play == True and oldplay == False:
      midiOutput.note_on(note,volume)
      midion = True
      sleep(.01)
    elif play == False:
      midiOutput.note_on(note,0)
      midion = True
      sleep(.01)

    oldkey = event.key
    oldnote = note
    oldvolume = volume
    oldplay = play
    samekey = (oldkey == event.key)

del midiOutput
pygame.midi.quit()

print "-- END --"
