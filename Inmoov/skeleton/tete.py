# -- coding: utf-8 --
# ##############################################################################
#            *** RIGHT HAND ***
# ##############################################################################

# rotationCylindre------pin 46
# berceau------pin 49

 
isHeadActivated=1
isEyeLidsActivated=0
isLeftArmActivated=1
isLeftHandActivated=1
isRightArmActivated=1
isRightHandActivated=1
isTorsoActivated=1


# ##############################################################################
#               PERSONNAL PARAMETERS
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
#                 SERVO FUNCTIONS
# ##############################################################################

if isTete==1 and (ScriptType=="RightSide" or ScriptType=="Full"):

  TeteArduinoIsconnected=0
  
  try:
    
    
    if TeteArduino=="left":
      TeteArduinoIsconnected=LeftPortIsConnected
    if TeteArduino=="right":
      TeteArduinoIsconnected=RightPortIsConnected
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
  
    verinGauche = Runtime.create("verinGauche", "Servo")
    verinGauche.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'verinGauche'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'verinGauche')) 
    verinGauche.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'verinGauche'))
    verinGauche.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'verinGauche'))
    verinGauche = Runtime.start("verinGauche","Servo")
    # servo.attach(ARDUINO, PIN)
    
    
    verinDroite = Runtime.create("verinDroite", "Servo")
    verinDroite.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'verinDroite'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'verinDroite')) 
    verinDroite.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'verinDroite'))
    verinDroite.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'verinDroite'))
    verinDroite = Runtime.start("verinDroite","Servo")
    verinDroite.attach(TeteArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'verinDroite'))
    verinGauche.attach(TeteArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'verinGauche'))  
    directionTete.attach(TeteArduino, ThisSkeletonPartConfig.getint('SERVO_PIN', 'directionTete'))
    # servo.attach(ARDUINO, PIN)    
    verinGauche.setAutoDisable(True)
    verinDroite.setAutoDisable(True)
    directionTete.setInverted(True)
    directionTete.setAutoDisable(True)
    
    
    # déclaration des servo virtuel  

    #virtualVerin
    virtualVerin = Runtime.start("virtualVerin","Servo")
    virtualVerin.attach(virtualServoController.getName(), 41)
    virtualVerin.eventsEnabled(True);
    virtualVerin.addListener("publishServoEvent",python.name,"onVirtualVerinEvent")
    virtualVerin.map(0,125,0,125)
    
    #virtualDirectionTete
    virtualDirectionTete = Runtime.start("virtualDirectionTete","Servo")
    virtualDirectionTete.attach(virtualServoController.getName(), 42)
    virtualDirectionTete.eventsEnabled(True);
    virtualDirectionTete.addListener("publishServoEvent",python.name,"onVirtualDirectionTeteEvent")
    virtualDirectionTete.map(0,125,0,125)

   
  else:
    #we force parameter if arduino is off
    isTete=0
    
def onVirtualVerinEvent(position):
    verinGauche.moveTo(position)
    verinDroite.moveTo(position)
    if not virtualVerin.isMoving():
      verinGauche.broadcastState()
      verinDroite.broadcastState()
      
def onVirtualDirectionTeteEvent(position):
    directionTete.moveTo(position)
    oeil.moveTo(position)
    if not virtualDirectionTete.isMoving():
      directionTete.broadcastState()
      oeil.broadcastState()