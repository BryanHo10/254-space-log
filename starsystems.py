Kurt Prutsman
CPSC 254 T TH 8pm-9:45

import re

#!/usr/bin/env python3

def getStarSystems():
	starsfound = re.compile("\Stars Visited\": (\alnum+\.\alnum+)")
	result = starsfound.findall(content)
	stars = []
	if result:
		for r in result:
			stars.append(r)
		print(result)
	return stars

