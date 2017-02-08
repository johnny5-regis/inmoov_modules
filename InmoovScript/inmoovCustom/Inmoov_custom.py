# -- coding: utf-8 --
# #############################################################################
#                           YOUR INMOOV CUSTOM
# Here you can add your own commands to play and test with inmoov
# If you udpate the whole script, don't worry, those commands are safe
# ##############################################################################



talk("Bonjour ! comment ça va")


ear.addCommand("ouvre les yeux", "python", "paupiereOuvre")
ear.addCommand("ferme les yeux", "python", "paupiereFerme")
ear.addCommand("bouge les sourcils", "python", "monteSourcil")
ear.addCommand("baisse les sourcils", "python", "baisseSourcil")
ear.addCommand("regarde vers la droite", "python", "regardDroit")
ear.addCommand("regarde devant", "python", "regardDevant")
ear.addCommand("regarde vers la gauche", "python", "regardGauche")
	
def paupiereOuvre():
	paupiereHautDroit.attach()
	paupiereBasGauche.attach()
	rotationCylindre.attach()
	paupiereBasDroit.attach()
	paupiereHautGauche.attach()
	berceau.attach()
	paupiereHautDroit.moveTo(180)
	paupiereHautGauche.moveTo(180)
	paupiereBasDroit.moveTo(180)
	paupiereBasGauche.moveTo(180)
	rotationCylindre.moveTo(180)
	berceau.moveTo(180)

def paupiereFerme():
	paupiereHautDroit.attach()
	paupiereBasGauche.attach()
	rotationCylindre.attach()
	paupiereBasDroit.attach()
	paupiereHautGauche.attach()
	paupiereHautDroit.moveTo(0)
	paupiereHautGauche.moveTo(0)
	paupiereBasDroit.moveTo(0)
	paupiereBasGauche.moveTo(0)
	rotationCylindre.moveTo(0)
	berceau.moveTo(0)

def monteSourcil():
	sourcilDroit.attach()
	sourcilGauche.attach()
	sourcilDroit.moveTo(180)
	sourcilGauche.moveTo(180)
	
def baisseSourcil():
	sourcilDroit.attach()
	sourcilGauche.attach()
	sourcilDroit.moveTo(0)
	sourcilGauche.moveTo(0)
	
def regardDroit():
	oeilDroit.attach()
	oeilGauche.attach()
	oeilDroit.moveTo(0)
	oeilGauche.moveTo(0)
	
def regardGauche():
	oeilDroit.attach()
	oeilGauche.attach()
	oeilDroit.moveTo(180)
	oeilGauche.moveTo(180)

def regardDevant():
	oeilDroit.attach()
	oeilGauche.attach()
	oeilDroit.moveTo(113)
	oeilGauche.moveTo(98)