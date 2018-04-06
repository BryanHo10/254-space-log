# Aaron Jimenez-Lopez
# CPSC 254
# Tuesday/Thursday 8-9:50

import re

def get_lightyears(content:str) -> float:
	pattern = re.compile("\"JumpDist\":(\d+\.\d+)")
	result = pattern.findall(content)
	traveled_LY = 0
	if result:
		for r in result:
			traveled_LY+=float(r)
	return traveled_LY
