import pygame
import pygame.midi
from time import sleep

instrument = 0
note = 74
volume = 127

pygame.init()
pygame.midi.init()

for id in range(pygame.midi.get_count()):
  print pygame.midi.get_device_info(id)

port = 2
midiOutput = pygame.midi.Output(port, 1)
midiOutput.set_instrument(instrument)
for note in range(0,127):
  midiOutput.note_on(note,volume)
  sleep(.25)
  midiOutput.note_off(note,volume)
del midiOutput
pygame.midi.quit()
