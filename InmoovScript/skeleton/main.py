# ##############################################################################
#						*** RIGHT HAND ***
# ##############################################################################

# rotationCylindre------pin 46
# berceau------pin 49

 
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
isMain=0
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')

CheckFileExist(ThisSkeletonPart)
ThisSkeletonPartConfig = ConfigParser.ConfigParser()
ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
MainArduino=ThisSkeletonPartConfig.get('ARDUINO', 'MainArduino')
isMain=ThisSkeletonPartConfig.getboolean('MAIN', 'isMain') 
autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')

  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isMain==1 and (ScriptType=="RightSide" or ScriptType=="Full"):

	MainArduinoIsconnected=0
	
	try:
		
		
		if MainArduino=="left":
			MainArduinoIsconnected=LeftPortIsConnected
		if MainArduino=="right":
			MainArduinoIsconnected=RightPortIsConnected
		MainArduino=eval(MainArduino)
	except:
		errorSpokenFunc('BAdrduinoChoosen',', Main')
		isMain=0
		pass	
	

	if MainArduinoIsconnected:
		
		#on declare le servo
		PoignetGauche = Runtime.create("PoignetGauche", "Servo")
		PoignetGauche.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'PoignetGauche'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'PoignetGauche')) 
		PoignetGauche.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'PoignetGauche'))
		PoignetGauche.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'PoignetGauche'))
		PoignetGauche = Runtime.start("PoignetGauche","Servo")
		# servo.attach(ARDUINO, PIN)
	
		MainGauche = Runtime.create("MainGauche", "Servo")
		MainGauche.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'MainGauche'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'MainGauche')) 
		MainGauche.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'MainGauche'))
		MainGauche.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'MainGauche'))
		MainGauche = Runtime.start("MainGauche","Servo")
		# servo.attach(ARDUINO, PIN)
		
		
		MainDroit = Runtime.create("MainDroit", "Servo")
		MainDroit.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'MainDroit'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'MainDroit')) 
		MainDroit.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'MainDroit'))
		MainDroit.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'MainDroit'))
		MainDroit = Runtime.start("MainDroit","Servo")
		
		PoignetDroit = Runtime.create("PoignetDroit", "Servo")
		PoignetDroit.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'PoignetDroit'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'PoignetDroit')) 
		PoignetDroit.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'PoignetDroit'))
		PoignetDroit.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'PoignetDroit'))
		PoignetDroit = Runtime.start("PoignetDroit","Servo")		
		# servo.attach(ARDUINO, PIN)		
		PoignetGauche.enableAutoAttach(1)
		MainGauche.enableAutoAttach(1)
		MainDroit.enableAutoAttach(1)
		PoignetDroit.enableAutoAttach(1)
		PoignetGauche.enableAutoDetach(1)
		MainGauche.enableAutoDetach(1)
		MainDroit.enableAutoDetach(1)
		PoignetDroit.enableAutoDetach(1)
		PoignetGauche.attach(MainArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'PoignetGauche'))
		MainGauche.attach(MainArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'MainGauche'))	
		MainDroit.attach(MainArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'MainDroit'))
		PoignetDroit.attach(MainArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'PoignetDroit'))
		
			
		
	
			
		#position repos
		PoignetGauche.rest()
		MainGauche.rest()
		MainDroit.rest()
		PoignetDroit.rest()
		
		#on detache pour pas que ca brule !
		#rotationCylindre.detach()
		#berceau.detach()
		
	else:
		#we force parameter if arduino is off
		isMain=0
		
#todo set inverted
