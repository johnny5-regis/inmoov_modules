# ##############################################################################
#						*** RIGHT HAND ***
# ##############################################################################

# rotationCylindre------pin 46
# berceau------pin 49

 
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
isTete=0
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')

CheckFileExist(ThisSkeletonPart)
ThisSkeletonPartConfig = ConfigParser.ConfigParser()
ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
TeteArduino=ThisSkeletonPartConfig.get('ARDUINO', 'TeteArduino')
isTete=ThisSkeletonPartConfig.getboolean('MAIN', 'isTete') 
autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')

  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isTete==1 and (ScriptType=="RightSide" or ScriptType=="Full"):

	TeteArduinoIsconnected=0
	
	try:
		
		
		if TeteArduino=="left":
			TeteArduinoIsconnected=LeftPortIsConnected
		if TeteArduino=="right":
			TeteArduinoArduinoIsconnected=RightPortIsConnected
		TeteArduino=eval(TeteArduino)
	except:
		errorSpokenFunc('BAdrduinoChoosen',', tete')
		isTete=0
		pass	
	

	if TeteArduinoIsconnected:
		
		#on declare le servo
		directionTete = Runtime.create("directionTete", "Servo")
		directionTete.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'directionTete'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'directionTete')) 
		directionTete.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'directionTete'))
		directionTete.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'directionTete'))
		directionTete = Runtime.start("directionTete","Servo")
		# servo.attach(ARDUINO, PIN)
		directionTete.attach(TeteArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'directionTete'))
		
		verinGauche = Runtime.create("verinGauche", "Servo")
		verinGauche.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'verinGauche'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'verinGauche')) 
		verinGauche.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'verinGauche'))
		verinGauche.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'verinGauche'))
		verinGauche = Runtime.start("verinGauche","Servo")
		# servo.attach(ARDUINO, PIN)
		verinGauche.attach(TeteArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'verinGauche'))
		
		verinDroite = Runtime.create("verinDroite", "Servo")
		verinDroite.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'verinDroite'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'verinDroite')) 
		verinDroite.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'verinDroite'))
		verinDroite.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'verinDroite'))
		verinDroite = Runtime.start("verinDroite","Servo")
		# servo.attach(ARDUINO, PIN)		
		verinDroite.attach(TeteArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'verinDroite'))
			
		
			
		if autoDetach:
			verinGauche.enableAutoAttach(1)
			verinDroite.enableAutoAttach(1)
			directionTete.enableAutoAttach(1)
			
		#position repos
		verinGauche.rest()
		verinDroite.rest()
		directionTete.rest()
		sleep(1)
		#on detache pour pas que ca brule !
		#rotationCylindre.detach()
		#berceau.detach()
		
	else:
		#we force parameter if arduino is off
		isTete=0
		
#todo set inverted
