# Kurt Prutsman
# CPSC 254 T TH 8pm-9:45

import re

#!/usr/bin/env python3

def getStarSystems(content:str)->list:
	starsfound = re.compile("\"StarSystem\":(\"(.+?)\")")
	result = starsfound.findall(content)
	stars = []
	if result:
		for r in result:
			stars.append(r[1])
		print(result)
	return stars

