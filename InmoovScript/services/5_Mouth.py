# ##############################################################################
# 								MOUTH SERVICE FILE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

global VoiceError
VoiceError=0

i01.mouth = Runtime.createAndStart("i01.mouth", MyvoiceTTS)
if MyvoiceTTS=="VoiceRss":
	i01.mouth.setKey(VoiceRssApi)
	


mouth=i01.mouth



#vocal startup globalized so :
i01.setMute(1)

python.subscribe(mouth.getName(),"publishStartSpeaking")
python.subscribe(mouth.getName(),"publishEndSpeaking")

# ##############################################################################
# MRL SERVICE TWEAKS
# ##############################################################################

#functions to call about robot speak
def talk(data):
	if data:
		if data[0:2]=="l ":data=data.replace("l ", "l'")
		mouth.speak(unicode(data,'utf-8'))
		
def talkBlocking(data):
	if data:
		if data[0:2]=="l ":data=data.replace("l ", "l'")
		mouth.speakBlocking(unicode(data,'utf-8'))
		
def talkEvent(data):
	if IsMute==0:
		subconsciousMouth.speakBlocking(unicode(data,'utf-8'))

#stop autolisten
def onEndSpeaking(text):
	global RobotIsActualySpeaking
	global RobotCanMoveHeadWhileSpeaking
	RobotIsActualySpeaking=0
	if RobotIsStarted==1:
		ear.resumeListening()
		MoveHeadTimer.stopClock()
		
		RobotCanMoveHeadWhileSpeaking=1
	if AudioSignalProcessing:
		try:
			left.disablePin(AnalogPinFromSoundCard)
			head.jaw.setVelocity(40)
			head.jaw.moveTo(0)
		except:
			print "onEndSpeaking error"
			pass
	
	
def onStartSpeaking(text):
			
	global RobotIsActualySpeaking
	RobotIsActualySpeaking=1
	ear.pauseListening()
	if AudioSignalProcessing:
		try:
			left.enablePin(AnalogPinFromSoundCard,HowManyPollsBySecond)
		
		except:
			print "onStartSpeaking error"
			pass
	if RobotIsStarted:
		MoveHeadTimer.startClock()
		
		



# ##############################################################################
# MOUTH RELATED FUNCTIONS
# ##############################################################################

#to know what is marytts version
def getMaryttsVersion():
	try:
		versionMary=glob.glob(os.getcwd().replace("\\", "/")+'/libraries/jar/marytts-common-*.jar')[0].replace('.jar','').replace(os.getcwd().replace("\\", "/")+'/libraries/jar\marytts-common-','')
	except:
		versionMary=0
		pass
	return versionMary
	
#to check if marytts voice exist
def CheckMaryTTSVoice(voiceCheck):
	return os.access(os.getcwd().replace("\\", "/")+'/libraries/jar/voice-'+voiceCheck+'-'+getMaryttsVersion()+'.jar', os.R_OK)

#mouth functions
def setRobotLanguage():
	global LanguageError
	LanguageError=0
	print MyLanguage
	

	if MyLanguage!="en":
		try:
			mouth.setLanguage('fr-fr')
			if EarEngine!="Sphinx":
				i01.ear.setLanguage(MyLanguage)
		except:
			errorSpokenFunc('MyLanguage')
			LanguageError=1
			pass
	
			
def checkAndDownloadVoice():				
	if MyvoiceTTS=="MarySpeech":
		if not CheckMaryTTSVoice(MyvoiceType):
			mouth.installComponentsAcceptLicense(MyvoiceType)
			if os.access(os.getcwd().replace("\\", "/")+'/libraries/jar/voice-'+MyvoiceType+'-'+getMaryttsVersion()+'.jar', os.R_OK):
				errorSpokenFunc('VoiceDownloaded')
				sleep(4)
				runtime.exit()
			else:
				errorSpokenFunc('I_cannot_download_this_mary_T_T_S_voice',MyvoiceType)
				
		
def setCustomVoice():	
	global VoiceError
	VoiceError=0
	try:
		mouth.setVoice(MyvoiceType)
	except:
		errorSpokenFunc('MyvoiceType')
		VoiceError=1
		pass
		
#we start raw Inmoov ear and mouth service
i01.startMouth()
#set user language
setRobotLanguage()

#check and update marytts voices	
#no worky on linux
if not IuseLinux:
	checkAndDownloadVoice()
#set CustomVoice

#set english subconsious mouth to user globalised mouth now ( only if we found a language pack )



mouth.speak("test")


if languagePackLoaded==1 and LanguageError==0 and VoiceError==0:
	subconsciousMouth=mouth
if languagePackLoaded==0:
	errorSpokenFunc('BadLanguagePack')


talkEvent(lang_whatIsThisLanguage)
talkEvent(lang_startingEar+", "+EarEngine)