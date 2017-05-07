# ##############################################################################
#						*** RIGHT HAND ***
# ##############################################################################

# sourcilDroit------pin 50
# sourcilGauche------pin 51

 
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
ispaupieres=0
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
try:
	CheckFileExist(ThisSkeletonPart)
	ThisSkeletonPartConfig = ConfigParser.ConfigParser()
	ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
	paupieresArduino=ThisSkeletonPartConfig.get('ARDUINO', 'paupieresArduino')
	ispaupieres=ThisSkeletonPartConfig.getboolean('MAIN', 'ispaupieres') 
	autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')
except:
	errorSpokenFunc('ConfigParserProblem','paupieres.config')
	pass
    
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if ispaupieres==1 and (ScriptType=="RightSide" or ScriptType=="Full"):
	
	OeilArduinoIsconnected=0
	try:
		
		
		if paupieresArduino=="left":
			paupieresArduinoisConnected=LeftPortIsConnected
		if paupieresArduino=="right":
			paupieresArduinoisConnected=RightPortIsConnected
		paupieresArduino=eval(paupieresArduino)
	except:
		errorSpokenFunc('BAdrduinoChoosen',', Oeil')
		ispaupieres=0
		pass	
	

	if paupieresArduinoisConnected:
		
		#on declare le servo
		paupiereBasDroit = Runtime.create("paupiereBasDroit", "Servo")
		paupiereBasDroit.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'paupiereBasDroit'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'paupiereBasDroit')) 
		paupiereBasDroit.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'paupiereBasDroit'))
		paupiereBasDroit.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'paupiereBasDroit'))
		paupiereBasDroit = Runtime.start("paupiereBasDroit","Servo")
		# servo.attach(ARDUINO, PIN)
		
		paupiereBasGauche = Runtime.create("paupiereBasGauche", "Servo")
		paupiereBasGauche.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'paupiereBasGauche'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'paupiereBasGauche')) 
		paupiereBasGauche.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'paupiereBasGauche'))
		paupiereBasGauche.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'paupiereBasGauche'))
		paupiereBasGauche = Runtime.start("paupiereBasGauche","Servo")
		# servo.attach(ARDUINO, PIN)		
		paupiereBasDroit.enableAutoEnable(1)
		paupiereBasGauche.enableAutoEnable(1)
		paupiereBasDroit.enableAutoDisable(0)
		paupiereBasGauche.enableAutoDisable(0)
		paupiereBasGauche.attach(right, ThisSkeletonPartConfig.getint('SERVO_PIN', 'paupiereBasGauche'))
		paupiereBasDroit.attach(right, ThisSkeletonPartConfig.getint('SERVO_PIN', 'paupiereBasDroit'))
			
		
			
		
		
			
		#position repos
		paupiereBasDroit.rest()
		paupiereBasGauche.rest()
		sleep(1)
		#on detache pour pas que ca brule !
		#paupiereBasDroit.detach()
		#paupiereBasGauche.detach()
		
	else:
		#we force parameter if arduino is off
		ispaupieres=0
		
#todo set inverted
