# ##############################################################################
#            *** RIGHT HAND ***
# ##############################################################################

# sourcilDroit------pin 50
# sourcilGauche------pin 51

 
  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
isSourcil=0 
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
  Sourcilarduino=ThisSkeletonPartConfig.get('ARDUINO', 'SourcilArduino')
  isSourcil=ThisSkeletonPartConfig.getboolean('MAIN', 'isSourcil') 
  autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')
except:
  errorSpokenFunc('ConfigParserProblem','sourcil.config')
  pass
    
  
  
  
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isSourcil==1 and (ScriptType=="RightSide" or ScriptType=="Full"):
  
  SourcilArduinoIsconnected=0
  try:
    
    
    if Sourcilarduino=="left":
      SourcilArduinoIsconnected=LeftPortIsConnected
    if Sourcilarduino=="right":
      SourcilArduinoIsconnected=RightPortIsConnected
    Sourcilarduino=eval(Sourcilarduino)
  except:
    errorSpokenFunc('BAdrduinoChoosen',', sourcil')
    isSourcil=0
    pass  
  

  if SourcilArduinoIsconnected:
    
    #on declare le servo
    sourcilDroit = Runtime.create("sourcilDroit", "Servo")
    sourcilDroit.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'sourcilDroit'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'sourcilDroit')) 
    sourcilDroit.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'sourcilDroit'))
    sourcilDroit.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'sourcilDroit'))
    sourcilDroit = Runtime.start("sourcilDroit","Servo")
    # servo.attach(ARDUINO, PIN)
    
    
    sourcilGauche = Runtime.create("sourcilGauche", "Servo")
    sourcilGauche.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'sourcilGauche'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'sourcilGauche')) 
    sourcilGauche.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'sourcilGauche'))
    sourcilGauche.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'sourcilGauche'))
    sourcilGauche = Runtime.start("sourcilGauche","Servo")
    # servo.attach(ARDUINO, PIN)    
    sourcilDroit.enableAutoEnable(1)
    sourcilGauche.enableAutoEnable(1)
    sourcilDroit.enableAutoDisable(0)
    sourcilGauche.enableAutoDisable(0)
    sourcilGauche.attach(right, ThisSkeletonPartConfig.getint('SERVO_PIN', 'sourcilGauche'))
    sourcilDroit.attach(right, ThisSkeletonPartConfig.getint('SERVO_PIN', 'sourcilDroit'))  
      
    
    
      
    #position repos
    sourcilDroit.rest()
    sourcilGauche.rest()
    sleep(1)
    #on detache pour pas que ca brule !
    #sourcilDroit.detach()
    #sourcilGauche.detach()
    
  else:
    #we force parameter if arduino is off
    isSourcil=0
    
#todo set inverted
