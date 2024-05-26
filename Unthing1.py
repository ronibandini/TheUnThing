# The Unthing 1.0
# Roni Bandini @RoniBandini
# May 2024, Buenos Aires, Argentina

from openai import OpenAI
from art import *
from time import sleep
import random
import warnings
import os

warnings.filterwarnings('ignore')

# Settings
chatGPTKey      = ""
model           = "gpt-3.5-turbo-instruct"
temperature1    = 0.9
temperature2    = 0.5
audioQty	= 6
DfPlayerProUnit	= "D:"
nationality	= "Argentino"
age		= "30"
workAt		= "un restaurante"
sex		= "man"


prompt1          = "¿Qué producto o servicio tiene muy poca demanda ya sea porque no está a la moda o bien porque muy poca gente lo quiere? Responder solo con un producto o servicio, sin comillas ni texto agregado ni espacios"

prompt2          = "Sos un "+nationality+" de "+age+" años que habla por telefono desde su trabajo en "+workAt+" con un amigo. Escribí "+str(audioQty)+" monologos telefonicos, usando entre treinta y cuarenta palabras para cada monologo. El contenido de los monologos debe ser apreciaciones del clima o bien apreciaciones de compañeros de trabajo o bien noticias del día. En el 40% de estos monologos mencioná ITEM. Separá cada monologo con un asterisco. No uses comillas ni saltos de línea entre los monologos"

if sex=="man":
	selectedVoice="onyx"
else:
	selectedVoice="nova"

client = OpenAI(
        api_key=chatGPTKey,
    )

print(text2art("The Unthing", font="small"))
print("Roni Bandini - May 2024 - Buenos Aires Argentina")
print("")
input("Connect the Unthinhg and press Enter to continue...")


os.system("del "+DfPlayerProUnit+"*.mp3")
print("...DFPlayer Pro cleared")

completion = client.completions.create(
        model=model,
        prompt=prompt1,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=temperature1,
    )

selectedItem=completion.choices[0].text

print("Selected item: "+selectedItem)

prompt2=prompt2.replace("ITEM", selectedItem)

completion = client.completions.create(
        model=model,
        prompt=prompt2,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=temperature2,
    )

text=completion.choices[0].text

text=text.strip()

print("...ChatGPT texts: "+text)

if len(text)==0:
	print("No answer was obtained from ChatGPT")

arrayText = text.split("*")

counter=0

for oneText in arrayText:
	if len(oneText)>20:
		print("...Generating MP3 #"+str(counter))

		try:

			response = client.audio.speech.create(
			model="tts-1",
  			voice=selectedVoice,
  			input=oneText
			)

			response.stream_to_file(str(counter)+".mp3")
			os.system("copy "+str(counter)+".mp3 "+DfPlayerProUnit)
			counter=counter+1
		except:
			print("TTS error for "+oneText)

print("...Procedure finished")
print("")
print("Unplug the Unthing. Place it near your phone and press K0 button")