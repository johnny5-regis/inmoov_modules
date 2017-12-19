def whataboutstarwars():
  x = (random.randint(1, 3))
  if x == 1:
      AudioPlayer.playFile(RuningFolder+'/system/sounds/R2D2.mp3')
  if x == 2:
      AudioPlayer.playFile(RuningFolder+'/system/sounds/Hello sir, I am C3po unicyborg relations.mp3')
  if x == 3:
      AudioPlayer.playFile(RuningFolder+'/system/sounds/mmmmmmh, from the dark side you are.mp3')