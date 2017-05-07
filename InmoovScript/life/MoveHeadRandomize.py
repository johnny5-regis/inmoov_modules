# ##############################################################################
#						*** ROBOT MOVE THE HEAD ( ex WHILE SPEAKIN ) ***
# ##############################################################################
	
MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")

def MoveHead(timedata):

	if RobotCanMoveHeadWhileSpeaking:
		#redefine next loop
		MoveHeadTimer.setInterval(random.randint(200,1000))
		if isHeadActivated:
			
			#wait servo last move
			#une meme position pour les 2
			sourcilsPos=random.uniform(30,65)
			if not sourcilDroit.isMoving():
				sourcilDroit.moveTo(sourcilsPos)
				sourcilGauche.moveTo(sourcilsPos)
			paupierePos=random.uniform(120,155)
			if not sourcilDroit.isMoving():
				paupiereHautGauche.moveTo(paupierePos)
				paupiereHautDroit.moveTo(paupierePos)
			
			if not verinDroite.isMoving():verinDroite.moveTo(random.uniform(75,115))
			if not verinGauche.isMoving():verinGauche.moveTo(random.uniform(70,110))
		if isRollNeckActivated:
			rollneck.setVelocity(random.randint(5,25))
			if not directionTete.isMoving():directionTete.moveTo(random.uniform(69,89))
	else:
		MoveHeadTimer.stopClock()
	
#initial function
def MoveHeadStart():
	print "MoveHeadStart"

	if RobotCanMoveHeadWhileSpeaking:
		if isHeadActivated:
			paupiereHautGauche.setAcceleration(20)
			paupiereHautDroit.setAcceleration(20)
			sourcilDroit.setAcceleration(20)
			sourcilGauche.setAcceleration(20)
			paupiereHautDroit.enableAutoDetach(0)
			paupiereHautGauche.enableAutoDetach(0)
			sourcilDroit.enableAutoDetach(0)
			sourcilGauche.enableAutoDetach(0)
		if isRollNeckActivated:
			directionTete.enableAutoDetach(0)
			directionTete.setAcceleration(20)
	else:
		MoveHeadTimer.stopClock()
		
def MoveHeadStop():
	
	if RobotCanMoveHeadWhileSpeaking:
		print "stop"
		#on remet les servo au milieu si on veut :)
		
		
		

MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")	
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStop")