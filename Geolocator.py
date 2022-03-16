#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import googlemaps
import time

gmaps = googlemaps.Client(key='Your API key goes here')

def progress(progress):
	print('\rProgress: [{0:50s}] {1:.1f}%'.format('#' * int(progress * 50), progress * 100), end='', flush=True)

supr_total = 0

#Add below the exact url to the file containing addresses to be located as 'address1''address2'etc...
with open(r'''file_with_addresses.csv''', 'r') as inputfile:
    addresses = []
    for usern in inputfile:
        usern = usern.rstrip()
        addresses.append(usern)


# Para exportar los resultados
outfn = "resultados_Idealista.csv"
outfp = open(outfn, "a")
outfp.write('url;coordinates;precision' + '\n')
outfp.close()

total = 0
for address in addresses:
	try:
		direccion = gmaps.geocode(address)
		lat = direccion[0]["geometry"]["location"]["lat"]
		lon = direccion[0]["geometry"]["location"]["lng"]
		type = direccion[0]["geometry"]["location_type"]
	except:
		direccion = ''
	outfp = open(outfn, "a")
	outfp.write(str(address) + ';' + str(lat) + ',' + str(lon) + ';' + str(type) + "\n")
	outfp.close()
	total += 1
	if (total == 50):
		time.sleep(2)
		total = 0
		supr_total += 1
		progress((supr_total * 50)/len(addresses))
	if (supr_total == 50):
		print("Enough is enough for today!")
		break
