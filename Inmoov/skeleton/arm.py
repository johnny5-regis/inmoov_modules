# ##############################################################################
#            *** RIGHT HAND ***
# ##############################################################################

# rotationCylindre------pin 46
# berceau------pin 49

 
  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
isArm=0
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')

CheckFileExist(ThisSkeletonPart)
ThisSkeletonPartConfig = ConfigParser.ConfigParser()
ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
ArmArduino=ThisSkeletonPartConfig.get('ARDUINO', 'ArmArduino')
isArm=ThisSkeletonPartConfig.getboolean('MAIN', 'isArm') 
autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')

  
  
  
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isArm==1 and (ScriptType=="RightSide" or ScriptType=="Full"):

  ArmArduinoIsconnected=0
  
  try:
    
    if ArmArduino=="left":
      ArmArduinoIsconnected=LeftPortIsConnected
    if ArmArduino=="right":
      ArmArduinoIsconnected=RightPortIsConnected
    ArmArduino=eval(ArmArduino)
  except:
    errorSpokenFunc('BAdrduinoChoosen',', Arm')
    isArm=0
    pass  
  

  if ArmArduinoIsconnected:
    
    #on declare le servo
    epauleGauche = Runtime.create("epauleGauche", "Servo")
    epauleGauche.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'epauleGauche'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'epauleGauche')) 
    epauleGauche.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'epauleGauche'))
    epauleGauche.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'epauleGauche'))
    epauleGauche = Runtime.start("epauleGauche","Servo")
    # servo.attach(ARDUINO, PIN)
  
    epauleDroit = Runtime.create("epauleDroit", "Servo")
    epauleDroit.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'epauleDroit'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'epauleDroit')) 
    epauleDroit.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'epauleDroit'))
    epauleDroit.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'epauleDroit'))
    epauleDroit = Runtime.start("epauleDroit","Servo")
    # servo.attach(ARDUINO, PIN)
    
    
    brasGauche = Runtime.create("brasGauche", "Servo")
    brasGauche.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'brasGauche'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'brasGauche')) 
    brasGauche.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'brasGauche'))
    brasGauche.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'brasGauche'))
    brasGauche = Runtime.start("brasGauche","Servo")
    
    brasDroit = Runtime.create("brasDroit", "Servo")
    brasDroit.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'brasDroit'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'brasDroit')) 
    brasDroit.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'brasDroit'))
    brasDroit.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'brasDroit'))
    brasDroit = Runtime.start("brasDroit","Servo")    
    
    HomoplateGauche = Runtime.create("HomoplateGauche", "Servo")
    HomoplateGauche.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'HomoplateGauche'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'HomoplateGauche')) 
    HomoplateGauche.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'HomoplateGauche'))
    HomoplateGauche.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'HomoplateGauche'))
    HomoplateGauche = Runtime.start("HomoplateGauche","Servo")    
    
    HomoplatetDroit = Runtime.create("HomoplatetDroit", "Servo")
    HomoplatetDroit.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'HomoplatetDroit'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'HomoplatetDroit')) 
    HomoplatetDroit.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'HomoplatetDroit'))
    HomoplatetDroit.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'HomoplatetDroit'))
    HomoplatetDroit = Runtime.start("HomoplatetDroit","Servo")
    # servo.attach(ARDUINO, PIN)
    epauleGauche.attach(ArmArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'epauleGauche'))
    epauleDroit.attach(ArmArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'epauleDroit'))  
    brasGauche.attach(ArmArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'brasGauche'))
    brasDroit.attach(ArmArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'brasDroit'))
    HomoplateGauche.attach(ArmArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'HomoplateGauche'))
    HomoplatetDroit.attach(ArmArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'HomoplatetDroit'))
    epauleGauche.setAutoDisable(True)
    epauleDroit.setAutoDisable(True)
    brasGauche.setAutoDisable(True)
    brasDroit.setAutoDisable(True)
    HomoplateGauche.setAutoDisable(True)
    HomoplatetDroit.setAutoDisable(True)
    
    #delais avant coupure auto
    epauleDroit.setDefaultDisableDelayNoVelocity(20000) 
    epauleGauche.setDefaultDisableDelayNoVelocity(20000)
    epauleDroit.setDisableDelayIfVelocity(20000) 
    epauleGauche.setDisableDelayIfVelocity(20000)
    brasGauche.setDefaultDisableDelayNoVelocity(5000) 
    brasDroit.setDefaultDisableDelayNoVelocity(5000)
    brasGauche.setDisableDelayIfVelocity(5000) 
    brasDroit.setDisableDelayIfVelocity(5000)    

    
  else:
    #we force parameter if arduino is off
    isArm=0
    
#todo set inverted
