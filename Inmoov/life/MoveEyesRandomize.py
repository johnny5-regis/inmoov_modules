# ##############################################################################
#            *** ROBOT MOVE THE EYES ( ex WHILE SPEAKIN ) ***
# ##############################################################################
  
MoveEyesTimer = Runtime.start("MoveEyesTimer","Clock")

def MoveEyes(timedata):
  
  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsTrackingSomething():
    #redefine next loop
    MoveEyesTimer.setInterval(random.randint(200,1000))
    if isHeadActivated:
      oeil.setVelocity(random.randint(10,50))      
      #wait servo last move
      if not oeil.isMoving():oeil.moveTo(random.uniform(0,180))      
    else:
      MoveEyesTimer.stopClock()
  
#initial function
def MoveEyesStart():
  print "MoveEyesStart",i01.RobotIsTrackingSomething()

def MoveEyesStop():
  
  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsTrackingSomething():
    oeil.rest()
    oeil.setVelocity(-1)

    
MoveEyesTimer.addListener("pulse", python.name, "MoveEyes")
MoveEyesTimer.addListener("clockStarted", python.name, "MoveEyesStart")  
MoveEyesTimer.addListener("clockStopped", python.name, "MoveEyesStop")