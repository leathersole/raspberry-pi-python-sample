#!/usr/bin/python

import os, sys
import tty
from select import select
import pygame
import pygame.midi
from time import sleep

class NotTTYException(Exception): pass

class TerminalFile:
    def __init__(self,infile):
        if not infile.isatty():
            raise NotTTYException()
        self.file=infile

        #prepare for getch
        self.save_attr=tty.tcgetattr(self.file)
        newattr=self.save_attr[:]
        newattr[3] &= ~tty.ECHO & ~tty.ICANON
        tty.tcsetattr(self.file, tty.TCSANOW, newattr)

    def __del__(self):
        #restoring stdin
        import tty  #required this import here
        tty.tcsetattr(self.file, tty.TCSADRAIN, self.save_attr)

    def getch(self):
        if select([self.file],[],[],0)[0]:
            c=self.file.read(1)
        else:
            c=''
        return c

if __name__=="__main__":
    s=TerminalFile(sys.stdin)
    print "Press q to quit..."

    pygame.init()
    pygame.midi.init()

    instrument = 0
    note = 74
    volume = 127
    port = 2
    
    midiOutput = pygame.midi.Output(port, 0)
    midiOutput.set_instrument(instrument)

    key = s.getch()
    play = False
    samekey = False
    midion = False
    oldplay = False
    oldvolume = 0
    while key!="q":
      if key =="":
        play = False
      else:
        play = True

      if key == "a":
          note = 60
      elif key == "s": 
          note = 62
      elif key == "d": 
          note = 64

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

      oldkey = key
      oldnote = note
      oldvolume = volume
      oldplay = play
      key = s.getch()
      samekey = (oldkey == key)


    del midiOutput
    pygame.midi.quit()
    
    print "-- END --"
