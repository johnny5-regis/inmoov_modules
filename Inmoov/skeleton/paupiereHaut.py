# ##############################################################################
#            *** RIGHT HAND ***
# ##############################################################################

# sourcilDroit------pin 50
# sourcilGauche------pin 51

 
  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
ispaupiereHaut=0
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
  paupiereHautArduino=ThisSkeletonPartConfig.get('ARDUINO', 'paupiereHautArduino')
  ispaupiereHaut=ThisSkeletonPartConfig.getboolean('MAIN', 'ispaupiereHaut') 
  autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')
except:
  errorSpokenFunc('ConfigParserProblem','paupiere.config')
  pass
    
  
  
  
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if ispaupiereHaut==1 and (ScriptType=="RightSide" or ScriptType=="Full"):
  
  paupiereHautArduinoIsconnected=0
  try:
    
    
    if paupiereHautArduino=="left":
      paupiereHautArduinoIsconnected=LeftPortIsConnected
    if paupiereHautArduino=="right":
      paupiereHautArduinoIsconnected=RightPortIsConnected
    paupiereHautArduino=eval(paupiereHautArduino)
  except:
    errorSpokenFunc('BAdrduinoChoosen',', Oeil')
    isOeil=0
    pass  
  

  if paupiereHautArduinoIsconnected:
    
    #on declare le servo
    paupiereHautDroit = Runtime.create("paupiereHautDroit", "Servo")
    paupiereHautDroit.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'paupiereHautDroit'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'paupiereHautDroit')) 
    paupiereHautDroit.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'paupiereHautDroit'))
    paupiereHautDroit.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'paupiereHautDroit'))
    paupiereHautDroit = Runtime.start("paupiereHautDroit","Servo")
    # servo.attach(ARDUINO, PIN)
    
    paupiereHautGauche = Runtime.create("paupiereHautGauche", "Servo")
    paupiereHautGauche.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'paupiereHautGauche'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'paupiereHautGauche')) 
    paupiereHautGauche.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'paupiereHautGauche'))
    paupiereHautGauche.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'paupiereHautGauche'))
    paupiereHautGauche = Runtime.start("paupiereHautGauche","Servo")
    paupiereHautGauche.attach(right, ThisSkeletonPartConfig.getint('SERVO_PIN', 'paupiereHautGauche'))
    paupiereHautDroit.attach(right, ThisSkeletonPartConfig.getint('SERVO_PIN', 'paupiereHautDroit'))
    paupiereHautDroit.setAutoDisable(True)
    paupiereHautGauche.setAutoDisable(True)
    

    
  else:
    #we force parameter if arduino is off
    ispaupiereHaut=0
    
#todo set inverted
