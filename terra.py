# Bryan Ho 
# CPSC 254 
# TuTh 8:00-9:50

import re

def get_total_terraformable(content:str) -> int:
	pattern = re.compile("\"TerraformState\":(\"(.*?)\")")
	result = pattern.findall(content)
	total = 0
	if result:
		for r in result:
			if r[1] == 'Terraformable':
				total+=1
	return total