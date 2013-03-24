#!/usr/bin/python

import pygame
import pygame.midi

pygame.init()
pygame.midi.init()

pygame.display.set_mode((640,480))

instrument = 0
note = 74
volume = 127
port = 2

midiOutput = pygame.midi.Output(port, 0)
midiOutput.set_instrument(instrument)

finished = False

key2sound = {'a':60, 's':62, 'd':64 }

print "Press q to quit..."
currently_playing = {k : False for k in key2sound.iterkeys()}

while not finished:

  event =  pygame.event.wait()

  if event.type == pygame.QUIT:
    finished = True
  elif event.type in (pygame.KEYDOWN,pygame.KEYUP):
    key = pygame.key.name(event.key)
    if key == 'q':
      finished = True

    if key in key2sound:
      if event.type == pygame.KEYDOWN:
        note = key2sound[key]
        midiOutput.note_on(note,volume)
        currently_playing[key] = True
      elif event.type == pygame.KEYUP:
        midiOutput.note_off(note,volume)
        currently_playing[key] = False

del midiOutput
pygame.midi.quit()

print "-- END --"
