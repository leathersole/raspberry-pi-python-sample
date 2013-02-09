from SimpleCV import Camera,Display,Image
from time import sleep

myCamera = Camera(prop_set={'width':320,'height':240})
myDisplay = Display(resolution=(320,240))
stache = Image("mustache-small.bmp")
stacheMask = stache.createBinaryMask(color1=(0,0,0),color2=(254,254,254))
stacheMask = stacheMask.invert()
while not myDisplay.isDone():
  frame = myCamera.getImage()
  faces = frame.findHaarFeatures('face')
  if faces:
    for face in faces:
      print "Face at: " + str(face.coordinates())
      myFace=face.crop()
      noses = myFace.findHaarFeatures('nose')
      if noses:
        nose=noses.sortArea()[-1]
        print "Nose at: " + str(nose.coordinates())
        xmust=face.points[0][0] + nose.x - (stache.width/2)
        ymust=face.points[0][1] + nose.y + (stache.height/3)
        frame = frame.blit(stache,pos=(xmust,ymust),mask=stacheMask)
        frame.save(myDisplay)
  else:
    print "No faces detected."
  sleep(1)
