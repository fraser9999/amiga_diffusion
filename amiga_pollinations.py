# Amiga Diffusion Renderer
# Python 2.0.1 Version
# uses curl-8.11.2, bsdsocket.library
# on Amiga OS 3.1 (WinUAE)
# tested only on WINUAE

import os
import time
import random


a=1
while a==1:

    os.system("cls")    
    print "Amiga Diffusion Renderer v0.1a"
    print "by Hermann Knopp 2026"

    seed=random.randint(1,999999)

    # Prompt für Pollinations

    prompt = raw_input("prompt> ")


    # URL-Encoding (sehr simpel für Python 2.0.1)

    prompt = prompt.replace(" ", "%20")

    #url = "https://image.pollinations.ai/prompt/" + prompt
    url = "https://image.pollinations.ai/prompt/" + prompt + "?seed=" + str(seed)

    # Zeitstempel erzeugen (Dateiname-sicher)

    #timestamp = time.strftime("%Y%m%d_%H%M%S")
    timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))

    # Zieldatei mit Datum/Uhrzeit
    outfile = "RAM:img_" + timestamp + ".jpg"

    # curl Befehl (SSL tolerant für alte Systeme)
    cmd = 'curl -L -k "' + url + '" -o "' + outfile + '"'

    print "URL:", url
    print "Speichere nach:", outfile
    print "Starte Download..."

    os.system(cmd)

    print "Fertig."
    b=raw_input("wait key")
    a=1