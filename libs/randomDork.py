import random


def random_dork():
    dork_path = "dicts/dorks.txt"
    dork_file = open(dork_path, "r")
    line = next(dork_file)
    
    for num, dorkLine in enumerate(dork_file):
        if random.randrange(num + 2): continue
        line = dorkLine
    
    return line
