def grabtheglass():
  i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 0.60, 0.60, 1.0, 1.0, 0.80)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(1.0,0.85,1.0)
  i01.moveHead(20,68)
  i01.moveArm("left",77,85,45,15)
  i01.moveArm("right",48,91,72,20)
  i01.moveHand("left",180,138,140,164,180,50)
  i01.moveHand("right",140,112,127,105,143,140)
  i01.moveTorso(105,105,90)

