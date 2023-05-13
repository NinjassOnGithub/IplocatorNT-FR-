#!/usr/bin/python

########################### <--- Coded by Zanyar jamal --->

import os
from urllib.request import urlopen
import json

###########################

os.system("reset")

print ("\033[93m  _______  .__            __                     ___________           .__  ")
print ("\033[93m  \      \ |__| ____     |__|____    ______ _____\__    ___/___   ____ |  |   ")
print ("\033[93m  /   |   \|  |/    \    |  \__  \  /  ___//  ___/ |    | /  _ \ /  _ \|  |")
print ("\033[93m /    |    \  |   |  \   |  |/ __ \_\___ \ \___ \  |    |(  <_> |  <_> )  |_")
print ("\033[93m \____|__  /__|___|  /\__|  (____  /____  >____  > |____| \____/ \____/|____/")
print ("\033[93m          \/        \/\______|    \/     \/     \/ ")

while True:
	ip1=input("\033[93m Veuillez entrez l'addresse ip afin de la localiser (Code modifié par Ninjass): ")
	url = "http://ip-api.com/json/"
	response = urlopen(url + ip1)
	data = response.read()
	values = json.loads(data)
	os.system("reset")
	
	
	print("\033[93m" + "\n IP: " + values['query'])
	print("\033[93m" + " Status: " + values['status'])
	print("\033[93m" + " Region(sur): " + values['regionName'])
	print("\033[93m" + " Pays(sur): " + values['country'])
	print("\033[93m" + " Ville: " + values['city'])
	print("\033[93m" + " ISP: " + values['isp'])
	print("\033[93m" + " Latitude,Longitude: " + str(values['lat']) + "," + str(values['lon']))
	print("\033[93m" + " Code Postal: " + values['zip'])
	print("\033[93m" + " Fuseau Horaire: " + values['timezone'])
	print("\033[93m" + " AS: " + values['as'] + "\n")

	print("\033[93m Merci d'utiliser ce NinjassTool ^_^ !! \n")
	print("\033[93m (Code modifié par Ninjass#5922)\n")

