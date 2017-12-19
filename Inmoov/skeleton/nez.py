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
    berceau = Runtime.create("berceau", "Servo")
    berceau.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'berceau'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'berceau')) 
    berceau.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'berceau'))
    berceau.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'berceau'))
    berceau = Runtime.start("berceau","Servo")


    berceau.attach(NezArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'berceau'))
    rotationCylindre.attach(right, ThisSkeletonPartConfig.getint('SERVO_PIN', 'rotationCylindre'))
    rotationCylindre.setAutoDisable(True)
    berceau.setAutoDisable(True)      
    #position repos

    
  else:
    #we force parameter if arduino is off
    isNez=0
    
#todo set inverted
