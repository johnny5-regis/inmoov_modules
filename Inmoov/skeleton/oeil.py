# ##############################################################################
#            *** RIGHT HAND ***
# ##############################################################################

# rotationCylindre------pin 46
# berceau------pin 49

 
  
# ##############################################################################
#               PERSONNAL PARAMETERS
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
#                 SERVO FUNCTIONS
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
    
    oeil = Runtime.create("oeil", "Servo")
    oeil.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'oeil'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'oeil')) 
    oeil.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'oeil'))
    oeil.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'oeil'))
    oeil = Runtime.start("oeil","Servo")
    # servo.attach(ARDUINO, PIN)    
    oeil.attach(right, ThisSkeletonPartConfig.getint('SERVO_PIN', 'oeil'))
    oeil.setAutoDisable(True)

    
  else:
    #we force parameter if arduino is off
    isOeil=0
    
#todo set inverted
