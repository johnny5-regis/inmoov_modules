# ##############################################################################
#            *** ROBOT MOVE ACDC ***
# ##############################################################################
  
MoveAcdcTimer = Runtime.start("MoveAcdcTimer","Clock")

def MoveAcdc(timedata):
  if J5canMoveAcdc:   
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
    verinDroite.setVelocity(random.randint(8,25))
    verinGauche.setVelocity(random.randint(8,25))
    directionTete.setVelocity(random.randint(15,30))
    rotationCylindre.setVelocity(random.randint(8,25))
    berceau.setVelocity(random.randint(8,25))
    sourcilDroit.setVelocity(30)
    sourcilGauche.setVelocity(30)
    paupiereBasDroit.setVelocity(30)
    paupiereBasGauche.setVelocity(30)
    if not epauleGauche.isMoving():epauleGauche.moveTo(random.uniform(20,120))
    if not epauleDroit.isMoving():epauleDroit.moveTo(random.uniform(50,90))
    if not brasGauche.isMoving():brasGauche.moveTo(random.uniform(40,130))
    if not brasDroit.isMoving():brasDroit.moveTo(random.uniform(40,100))
    if not HomoplatetDroit.isMoving():HomoplatetDroit.moveTo(random.uniform(0,180))
    if not HomoplateGauche.isMoving():HomoplateGauche.moveTo(random.uniform(0,180))
    if not PoignetGauche.isMoving():PoignetGauche.moveTo(random.uniform(0,180))
    if not MainGauche.isMoving():MainGauche.moveTo(random.uniform(0,130))
    if not MainDroit.isMoving():MainDroit.moveTo(random.uniform(180,50))
    if not PoignetDroit.isMoving():PoignetDroit.moveTo(random.uniform(80,180))
    if not verinDroite.isMoving():verinDroite.moveTo(random.uniform(75,100))
    if not verinGauche.isMoving():verinGauche.moveTo(random.uniform(70,95))
    if not directionTete.isMoving():directionTete.moveTo(random.uniform(60,120))
    if not rotationCylindre.isMoving():rotationCylindre.moveTo(random.uniform(25,90))
    if not berceau.isMoving():berceau.moveTo(random.uniform(0,175))

    #wait servo last move
    #une meme position pour les 2
    sourcilsPos=random.uniform(150,160)
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
 
    
  else:
    J5canMoveAcdc=True
    MoveAcdcTimer.stopClock()
      
def MoveHeadStart():
    J5canMoveAcdc=True
    
     
MoveAcdcTimer.addListener("pulse", python.name, "MoveAcdc")
MoveAcdcTimer.addListener("clockStarted", python.name, "MoveAcdcStart")
