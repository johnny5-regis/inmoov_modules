def stopTracking():
  global J5istracking
  if (J5istracking):
    tracker.stopTracking()
    verinGauche.setVelocity(30)
    verinDroite.setVelocity(30)
    directionTete.setVelocity(30)
    verinGauche.moveTo(90)
    verinDroite.moveTo(90)
    directionTete.moveTo(90)
    sleep(3)
    J5istracking=False