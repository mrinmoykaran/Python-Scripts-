###
# Implemenation Text To Speech in Python
# Create a text file (In this case it presents in the same location where the python file present) named speech_file.txt and write some text 
###


from gtts import gTTS, lang
import os

fh=open("speech_file.txt","r")
myText=fh.read().replace("\n"," ")
language="en"
output=gTTS(text=myText,lang=language,slow=False)
output.save("output.mp3")
fh.close()
os.system("start output.mp3")
