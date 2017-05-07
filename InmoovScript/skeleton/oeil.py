# ##############################################################################
#						*** RIGHT HAND ***
# ##############################################################################

# rotationCylindre------pin 46
# berceau------pin 49

 
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
isOeil=0
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
try:
	CheckFileExist(ThisSkeletonPart)
	ThisSkeletonPartConfig = ConfigParser.ConfigParser()
	ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
	OeilArduino=ThisSkeletonPartConfig.get('ARDUINO', 'OeilArduino')
	isOeil=ThisSkeletonPartConfig.getboolean('MAIN', 'isOeil') 
	autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')
except:
	errorSpokenFunc('ConfigParserProblem','oeil.config')
	pass
    
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isOeil==1 and (ScriptType=="RightSide" or ScriptType=="Full"):
	
	OeilArduinoIsconnected=0
	try:
		
		
		if OeilArduino=="left":
			OeilArduinoisConnected=LeftPortIsConnected
		if OeilArduino=="right":
			OeilArduinoIsconnected=RightPortIsConnected
		OeilArduino=eval(OeilArduino)
	except:
		errorSpokenFunc('BAdrduinoChoosen',', Oeil')
		isOeil=0
		pass	
	

	if OeilArduinoIsconnected:
		
		#on declare le servo
		oeilDroit = Runtime.create("oeilDroit", "Servo")
		oeilDroit.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'oeilDroit'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'oeilDroit')) 
		oeilDroit.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'oeilDroit'))
		oeilDroit.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'oeilDroit'))
		oeilDroit = Runtime.start("oeilDroit","Servo")
		# servo.attach(ARDUINO, PIN)
		
		
		oeilGauche = Runtime.create("oeilGauche", "Servo")
		oeilGauche.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'oeilGauche'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'oeilGauche')) 
		oeilGauche.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'oeilGauche'))
		oeilGauche.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'oeilGauche'))
		oeilGauche = Runtime.start("oeilGauche","Servo")
		# servo.attach(ARDUINO, PIN)		
		
		oeilDroit.enableAutoEnable(1)
		oeilGauche.enableAutoEnable(1)
		oeilDroit.enableAutoDisable(0)
		oeilGauche.enableAutoDisable(0)
			
		oeilGauche.attach(right, ThisSkeletonPartConfig.getint('SERVO_PIN', 'oeilGauche'))
		oeilDroit.attach(right, ThisSkeletonPartConfig.getint('SERVO_PIN', 'oeilDroit'))	
		
			
	
		#position repos
		oeilDroit.rest()
		oeilGauche.rest()
		sleep(1)
		#on detache pour pas que ca brule !
		#oeilDroit.detach()
		#oeilGauche.detach()
		
	else:
		#we force parameter if arduino is off
		isOeil=0
		
#todo set inverted
