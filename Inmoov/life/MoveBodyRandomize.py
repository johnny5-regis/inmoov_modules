# ##############################################################################
#            *** ROBOT MOVE THE BODY ***
# ##############################################################################
  
MoveBodyTimer = Runtime.start("MoveBodyTimer","Clock")

def MoveBody(timedata):

  if i01.RobotCanMoveRandom and i01.RobotCanMoveBodyRandom and not i01.RobotIsSleeping and not i01.RobotIsTrackingSomething():
  
   
    #redefine next loop
    MoveBodyTimer.setInterval(random.randint(1000,5000))
    epauleGauche.setVelocity(random.randint(15,25))
    epauleDroit.setVelocity(random.randint(15,25))
    brasGauche.setVelocity(random.randint(15,35))
    brasDroit.setVelocity(random.randint(15,35))
    HomoplatetDroit.setVelocity(random.randint(15,20))
    HomoplateGauche.setVelocity(random.randint(15,20))
    PoignetGauche.setVelocity(random.randint(60,100))
    MainGauche.setVelocity(random.randint(60,100))
    MainDroit.setVelocity(random.randint(60,100))
    PoignetDroit.setVelocity(random.randint(60,100))
    if not epauleGauche.isMoving():epauleGauche.moveTo(random.uniform(20,120))
    if not epauleDroit.isMoving():epauleDroit.moveTo(random.uniform(50,150))
    if not brasGauche.isMoving():brasGauche.moveTo(random.uniform(40,100))
    if not brasDroit.isMoving():brasDroit.moveTo(random.uniform(40,100))
    if not HomoplatetDroit.isMoving():HomoplatetDroit.moveTo(random.uniform(0,180))
    if not HomoplateGauche.isMoving():HomoplateGauche.moveTo(random.uniform(0,180))
    if not PoignetGauche.isMoving():PoignetGauche.moveTo(random.uniform(0,180))
    if not MainGauche.isMoving():MainGauche.moveTo(random.uniform(0,130))
    if not MainDroit.isMoving():MainDroit.moveTo(random.uniform(180,50))
    if not PoignetDroit.isMoving():PoignetDroit.moveTo(random.uniform(80,180))


  else:
    MoveBodyTimer.stopClock()
  
    
def MoveBodyStopped():
  
  if i01.RobotCanMoveRandom and i01.RobotCanMoveBodyRandom and not i01.RobotIsSleeping and not i01.RobotIsTrackingSomething():
  
    if (ScriptType=="Full" or ScriptType=="Virtual"):
      print "MoveBodyStopped"

MoveBodyTimer.addListener("pulse", python.name, "MoveBody")
MoveBodyTimer.addListener("clockStopped", python.name, "MoveBodyStopped")
