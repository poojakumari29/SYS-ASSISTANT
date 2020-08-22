import pyttsx3
import os

print("HELLO USERS")
pyttsx3.speak("Hello User !! How may I help you!!")
print("THE TOOLS AVAILABLE IN YOUR PC ARE : ")
print("1.) Chrome")
print("2.) Window Media Player")
print("3.) Notepad")
print("4.) Mozilla FireFox")

while True:
	print("HOW MAY I HEPL YOU !: "  , end='')
	p = input()
	

	if ("DO NOT" in p) or ("NOT" in p) or ("DON'T" in p) or ("DONT" in p) or ("dont" in p) or ("do not" in p) or ("no need to" in p) and (("RUN" in p) or ("run" in p) ("launch" in p) or ("LAUNCH" in p) or ("chrome" in p) or ("CHROME" in p) or ("browser" in p) or ("BROWSER" in p)):
		print("okay")

	    
	elif (("launch" in p) or ("LAUNCH" in p) or ("run" in p) or ("RUN" in p) or ("EXECUTE" in p) or("execute" in p) or ("open" in p)) and (("chrome" in p) or ("CHROME" in p) or ("browser" in p) or ("BROWSER" in p)):
		pyttsx3.speak("launching chrome for you")
		print("launching chrome for you")
		os.system("chrome")
	        
	elif ("DO NOT" in p) or ("NOT" in p) or ("DON'T" in p) or ("DONT" in p) or ("dont" in p) or ("do not" in p) or ("no need to" in p) and (("RUN" in p) or ("run" in p) ("launch" in p) or ("LAUNCH" in p) or ("firefox" in p) or ("mozillafirefox" in p) or ("mozilla" in p) or ("MOZILLAFIREFOX" in p)):
		print("okay")

 
	elif (("launch" in p) or ("LAUNCH" in p) or ("run" in p) or ("RUN" in p) or ("EXECUTE" in p) or("execute" in p) or ("open" in p)) and (("firefox" in p) or ("mozillafirefox" in p) or ("browser" in p) or ("BROWSER" in p) or ("MOZILLAFIREFOX" in p) or ("MOZILLA")):
		pyttsx3.speak("launching MOZILLA FIREFOX for you")
		print("launching mozilla firefox for you")
		os.system("mozillafirefox")
        


	elif ("DO NOT" in p) or ("NOT" in p) or ("DON'T" in p) or ("DONT" in p) or ("dont" in p) or ("do not" in p) or ("no need to" in p) and (("open" in p) or ("OPEN" in p) or ("RUN" in p) or ("run" in p) or ("NOTEPAD" in p) or ("notepad" in p) or ("EDITOR" in p) or ("editor" in p)):
		print("okay")
        
	elif (("launch" in p) or ("LAUNCH" in p) or ("run" in p) or ("RUN" in p) or ("EXECUTE" in p) or  ("execute" in p ) or("OPEN" in p) or ("open" in p)) and  (("notepad" in p) or ("NOTEPAD" in p) or ("editor" in p) or ("EDITOR" in p)):	
		pyttsx3.speak("launching notepad for you")
		print("launching notepad for you")
		os.system("notepad")

	elif ("DO NOT" in p) or ("NOT" in p) or ("DON'T" in p) or ("DONT" in p) or ("dont" in p) or ("do not" in p) or ("no need to" in p) and (("open" in p) or ("OPEN" in p) or ("play" in p) or ("PLAY" in p) or ("RUN" in p) or ("run" in p) or ("WMPLAYER" in p) or ("wmplayer" in p) or ("music" in p) or ("MUSIC" in p)):
		print("okay")
        
        
	elif (("play" in p) or ("PLAY" in p) or ("open" in p) or ("OPEN" in p) or ("launch" in p) or ("LAUNCH" in p) or ("run" in p) or ("RUN" in p) or ("EXECUTE" in p) or ("execute" in p ) or ("OPEN" in p) or ("open" in p)) and (("wmplayer" in p) or ("WMPLAYER" in p) or ("MUSIC" in p) or ("music" in p)):
		pyttsx3.speak("launching wmplayer for you")
		print("launching wmplayer for you")
		os.system("wmplayer")

       
	elif ("exit" in p)  or ("quit" in p) or ("stop" in p) or ("STOP" in p) or ("QUIT" in p) or ("EXIT" in p):
		break

	else:
		print("ERROR !! TOOL NOT AVAILABLE")


