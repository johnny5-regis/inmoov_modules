# ##############################################################################
#            *** ROBOT MOVE THE HEAD ( ex WHILE SPEAKIN ) ***
# ##############################################################################
RobotCanMoveHeadWhileSpeaking=1
MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")
isHeadActivated=1
isRollNeckActivated=1
def MoveHead(timedata):
 
  if RobotCanMoveHeadWhileSpeaking and not J5istracking and not i01.RobotIsTrackingSomething():
    #redefine next loop
    MoveHeadTimer.setInterval(random.randint(200,1000))
    if isHeadActivated:
      verinDroite.setVelocity(random.randint(8,25))
      verinGauche.setVelocity(random.randint(8,25))
      directionTete.setVelocity(random.randint(15,30))
      rotationCylindre.setVelocity(random.randint(8,25))
      berceau.setVelocity(random.randint(8,25))
      sourcilDroit.setVelocity(30)
      sourcilGauche.setVelocity(30)
      paupiereBasDroit.setVelocity(30)
      paupiereBasGauche.setVelocity(30)
      #wait servo last move
      #une meme position pour les 2
      sourcilsPos=random.uniform(30,65)
      if not sourcilDroit.isMoving():
        sourcilDroit.moveTo(sourcilsPos)
        sourcilGauche.moveTo(sourcilsPos)
      paupierePos=random.uniform(120,155)
      if not paupiereHautGauche.isMoving():
        paupiereHautGauche.moveTo(paupierePos)
        paupiereHautDroit.moveTo(paupierePos)
      paupiereBasPos=random.uniform(190,80)
      if not paupiereBasDroit.isMoving():
        paupiereBasDroit.moveTo(paupiereBasPos)
        paupiereBasGauche.moveTo(paupiereBasPos)
      
      if not verinDroite.isMoving():verinDroite.moveTo(random.uniform(75,100))
      if not verinGauche.isMoving():verinGauche.moveTo(random.uniform(70,95))
      if not directionTete.isMoving():directionTete.moveTo(random.uniform(60,120))
      if not rotationCylindre.isMoving():rotationCylindre.moveTo(random.uniform(100,175))
      if not berceau.isMoving():berceau.moveTo(random.uniform(100,175))
      
  else:
    MoveHeadTimer.stopClock()
  
def MoveHeadStop():
  
  if RobotCanMoveHeadWhileSpeaking:
    print "MoveHeadstop"
    #on remet les servo au milieu si on veut :)
    
 
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStop")