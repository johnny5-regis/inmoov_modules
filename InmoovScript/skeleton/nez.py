# ##############################################################################
#            *** RIGHT HAND ***
# ##############################################################################

# rotationCylindre------pin 46
# berceau------pin 49

 
  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
isNez=0
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
  NezArduino=ThisSkeletonPartConfig.get('ARDUINO', 'NezArduino')
  isNez=ThisSkeletonPartConfig.getboolean('MAIN', 'isNez') 
  autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')
except:
  errorSpokenFunc('ConfigParserProblem','nez.config')
  pass
    
  
  
  
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isNez==1 and (ScriptType=="RightSide" or ScriptType=="Full"):

  NezArduinoIsconnected=0
  
  try:
    
    
    if NezArduino=="left":
      NezArduinoIsconnected=LeftPortIsConnected
    if NezArduino=="right":
      NezArduinoIsconnected=RightPortIsConnected
    NezArduino=eval(NezArduino)
  except:
    errorSpokenFunc('BAdrduinoChoosen',', nez')
    isNez=0
    pass  
  

  if NezArduinoIsconnected:
    
    #on declare le servo
    rotationCylindre = Runtime.create("rotationCylindre", "Servo")
    rotationCylindre.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'rotationCylindre'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'rotationCylindre')) 
    rotationCylindre.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'rotationCylindre'))
    rotationCylindre.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'rotationCylindre'))
    rotationCylindre = Runtime.start("rotationCylindre","Servo")
    # servo.attach(ARDUINO, PIN)
    
    berceau = Runtime.create("berceau", "Servo")
    berceau.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'berceau'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'berceau')) 
    berceau.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'berceau'))
    berceau.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'berceau'))
    berceau = Runtime.start("berceau","Servo")
    # servo.attach(ARDUINO, PIN)    
    
      
    
      
    
    rotationCylindre.enableAutoEnable(1)
    berceau.enableAutoEnable(1)
    rotationCylindre.enableAutoDisable(0)
    berceau.enableAutoDisable(0)
    berceau.attach(NezArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'berceau'))
    rotationCylindre.attach(right, ThisSkeletonPartConfig.getint('SERVO_PIN', 'rotationCylindre'))
      
    #position repos
    rotationCylindre.rest()
    berceau.rest()
    sleep(1)
    #on detache pour pas que ca brule !
    #rotationCylindre.detach()
    #berceau.detach()
    
  else:
    #we force parameter if arduino is off
    isNez=0
    
#todo set inverted
