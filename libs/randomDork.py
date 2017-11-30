import random

def randomDork():
    dorkPath = "dics/dorks.txt"
    dorkFile = open(dorkPath, "r")
    line = next(dorkFile)
    
    for num, dorkLine in enumerate(dorkFile):
        if random.randrange(num + 2): continue
        line = dorkLine
    
    return line
