import re

def get_planet_names(content:str) -> list:
        pattern = re.compile("\"BodyNames\":(?P<quote>['\"]).*?(?P=quote))")
        result = pattern.findall(content)
        planets = [] 
        if result:
                for r in result:
                        planets.append(r)
#		print(result)
        return planets
