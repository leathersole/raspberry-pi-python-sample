from SimpleCV import Image,Display
from time import sleep

myDisplay = Display()
raspberryImage = Image("test.jpg")
raspberryImage.save(myDisplay)
while not myDisplay.isDone():
  sleep(0.1)
