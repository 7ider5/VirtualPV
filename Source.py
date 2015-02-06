__author__ = 'EBJ501'

# General dependency declarations
import os
import time
# Raspi GPIO dependency declarations

# Production database loading
# Data format :|Timestamp (POSIX)|Prod (Wh/min)|
# Separator : ";"
script_dir = os.path.dirname(__file__)
data_name = "Prod.txt"
path = os.path.join(script_dir, data_name)

# Opening database and reading each line
with open(path, 'r') as f:
    for line in f:

        # Splitting line Conso[0]=Timestamp & Conso[1]=Prod
        Conso = [float(x) for x in line.split(";")]
        DeltaImp = (55-Conso[1]*0.6)/Conso[1]
        for i in range(Conso[1]):
            # OUT = 1
            time.sleep(0.6)
            # OUT = 0
            time.sleep(DeltaImp)
        while Conso[0]+60 > time.clock():
            # Wait for next minute
            time.sleep(0.1)