# -- coding: utf-8 --
# ##############################################################################
#                 CONTROL RGB LED
# ##############################################################################
RgbLedActivated=0

#PIN DEF
ROUGE=27
VERT=28
BLEU=29

def Light(ROUGE_V,VERT_V,BLEU_V):

  if RgbLedActivated:
    right.pinMode(ROUGE, Arduino.OUTPUT)
    right.pinMode(VERT, Arduino.OUTPUT)
    right.pinMode(BLEU, Arduino.OUTPUT)
    right.digitalWrite(ROUGE,ROUGE_V)
    right.digitalWrite(VERT,VERT_V)
    right.digitalWrite(BLEU,BLEU_V)