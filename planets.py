#RJ Andaya
#CPSC 254


import re

def get_planet_names(content:str) -> list:
        pattern = re.compile("\"BodyName\":(\"(.+?)\")")
        result = pattern.findall(content)
        planets = [] 
        if result:
                for r in result:
                        planets.append(r[1])
        return planets
