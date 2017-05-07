# -- coding: utf-8 --
# #############################################################################
#                           YOUR INMOOV CUSTOM
# Here you can add your own commands to play and test with inmoov
# If you udpate the whole script, don't worry, those commands are safe
# ##############################################################################



talk("Bonjour ! comment ça va")


ear.addCommand(u"ouvre les yeux", "python", "paupiereOuvre")
ear.addCommand(u"ferme les yeux", "python", "paupiereFerme")
ear.addCommand(u"bouge les sourcils", "python", "monteSourcil")
ear.addCommand(u"baisse les sourcils", "python", "baisseSourcil")
ear.addCommand(u"regarde vers la droite", "python", "regardDroit")
ear.addCommand(u"regarde devant", "python", "regardDevant")
ear.addCommand(u"regarde vers la gauche", "python", "regardGauche")
ear.addCommand(u"lève la tête", "python", "hautTete")
ear.addCommand(u"baisse la tête", "python", "basTete")
ear.addCommand(u"tourner la tête à gauche", "python", "teteGauche")
ear.addCommand(u"tourner la tête à droite", "python", "tetedroite")
ear.addCommand(u"repositionne la tête", "python", "teteMilieu")
ear.addCommand(u"reposition la tête", "python", "teteMilieu")
ear.addCommand(u"incline la tête à droite", "python", "inclineDroite")
ear.addCommand(u"incline la tête à gauche", "python", "inclineGauche")

def inclineDroite():
  verinDroite.moveTo(0)
  verinGauche.moveTo(180)
  sleep(5)
  verinGauche.disable()
  verinDroite.disable()

def inclineGauche():
  verinDroite.moveTo(180)
  verinGauche.moveTo(0)
  sleep(5)
  verinGauche.disable()
  verinDroite.disable()

def teteMilieu():
  
  directionTete.moveTo(79)

def teteDroite():
  
  directionTete.moveTo(0)

def teteGauche():
  
  directionTete.moveTo(180)
  

def basTete():
  verinDroite.moveTo(0)
  verinGauche.moveTo(0)
  sleep(5)
  verinGauche.disable()
  verinDroite.disable()

def hautTete():
  verinDroite.moveTo(150)
  verinGauche.moveTo(140)
  sleep(5)
  verinGauche.disable()
  verinDroite.disable()
  
  
def paupiereOuvre():

  paupiereHautDroit.moveTo(180)
  paupiereHautGauche.moveTo(180)
  paupiereBasDroit.moveTo(180)
  paupiereBasGauche.moveTo(180)
  rotationCylindre.moveTo(180)
  berceau.moveTo(180)

def paupiereFerme():

  paupiereHautDroit.moveTo(0)
  paupiereHautGauche.moveTo(0)
  paupiereBasDroit.moveTo(0)
  paupiereBasGauche.moveTo(0)
  rotationCylindre.moveTo(0)
  berceau.moveTo(0)
  sourcilDroit.moveTo(90)
  sourcilGauche.moveTo(90)

def monteSourcil():
  
  sourcilDroit.moveTo(180)
  sourcilGauche.moveTo(180)
  
def baisseSourcil():
  
  sourcilDroit.moveTo(0)
  sourcilGauche.moveTo(0)
  
def regardDroit():
  
  oeilDroit.moveTo(0)
  oeilGauche.moveTo(0)
  
def regardGauche():
  
  oeilDroit.moveTo(180)
  oeilGauche.moveTo(180)

def regardDevant():
  
  oeilDroit.moveTo(113)
  oeilGauche.moveTo(98)
  
def open():
  rotationCylindre.moveTo(90)
  berceau.moveTo(180)
  paupiereBasDroit.moveTo(180)
  paupiereBasGauche.moveTo(180)
  paupiereHautDroit.moveTo(35)
  paupiereHautGauche.moveTo(35)
  sourcilDroit.moveTo(35)
  sourcilGauche.moveTo(35)
  verinGauche.moveTo(110)
  verinDroite.moveTo(115)
  sleep(3)
  verinGauche.disable()
  verinDroite.disable()
  
def curieu():
  rotationCylindre.moveTo(30)
  berceau.moveTo(0)
  paupiereBasDroit.moveTo(180)
  paupiereBasGauche.moveTo(180)
  paupiereHautDroit.moveTo(180)
  paupiereHautGauche.moveTo(180)
  sourcilDroit.moveTo(180)
  sourcilGauche.moveTo(70)
  verinGauche.moveTo(110)
  verinDroite.moveTo(50)
  sleep(3)
  verinGauche.disable()
  verinDroite.disable()
  
def surpris():
  rotationCylindre.moveTo(170)
  berceau.moveTo(180)
  paupiereBasDroit.moveTo(180)
  paupiereBasGauche.moveTo(180)
  paupiereHautDroit.moveTo(180)
  paupiereHautGauche.moveTo(180)
  sourcilDroit.moveTo(35)
  sourcilGauche.moveTo(35)
  verinGauche.moveTo(110)
  verinDroite.moveTo(115)
  sleep(3)
  verinGauche.disable()
  verinDroite.disable()
  
def mechant():

  rotationCylindre.moveTo(0)
  berceau.moveTo(0)
  paupiereBasDroit.moveTo(180)
  paupiereBasGauche.moveTo(180)
  paupiereHautDroit.moveTo(35)
  paupiereHautGauche.moveTo(35)
  paupiereBasDroit.moveTo(60)
  paupiereBasGauche.moveTo(60)
  sourcilDroit.moveTo(180)
  sourcilGauche.moveTo(180)
  verinGauche.moveTo(110)
  verinDroite.moveTo(115)
  sleep(3)
  verinGauche.disable()
  verinDroite.disable()
  
def cleinOeil():
  rotationCylindre.moveTo(0)
  berceau.moveTo(0)
  paupiereBasDroit.moveTo(0)
  paupiereHautDroit.moveTo(0)
  paupiereHautGauche.moveTo(180)
  sourcilDroit.moveTo(90)
  sourcilGauche.moveTo(120)
  verinGauche.moveTo(110)
  verinDroite.moveTo(35)
  sleep(1)
  rotationCylindre.moveTo(90)
  berceau.moveTo(180)
  paupiereBasDroit.moveTo(180)
  paupiereBasGauche.moveTo(180)
  paupiereHautDroit.moveTo(35)
  paupiereHautGauche.moveTo(35)
  sourcilDroit.moveTo(35)
  sourcilGauche.moveTo(35)
  verinGauche.moveTo(110)
  verinDroite.moveTo(115)
  sleep(3)
  verinGauche.disable()
  verinDroite.disable()
  
verinGauche.disable()
verinDroite.disable()