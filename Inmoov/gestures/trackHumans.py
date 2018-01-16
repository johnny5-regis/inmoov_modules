global J5istracking
J5istracking=False
def trackHumans():
  global J5istracking
  verinGauche.setVelocity(30)
  verinDroite.setVelocity(30)
  directionTete.setVelocity(30)
  verinGauche.moveTo(90)
  verinDroite.moveTo(90)
  directionTete.moveTo(90)
  oeil.moveTo(90)
  sleep(2)
  virtualVerin.moveTo(90)
  virtualDirectionTete.moveTo(90)
  tracker = Runtime.start("tracker", "Tracking")
  pid = tracker.getPID()
  # these are default setting
  # adjust to make more smooth
  # or faster
  pid.setPID("x",30.0, 5.0, 0.1)
  pid.setPID("y",30.0, 5.0, 0.1)
  tracker.connect(i01.opencv, virtualDirectionTete, virtualVerin)
  tracker.faceDetect(True)
  J5istracking=True
  verinGauche.setVelocity(-1)
  verinDroite.setVelocity(-1)
  directionTete.setVelocity(-1)
