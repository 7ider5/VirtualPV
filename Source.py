__author__ = 'EBJ501'

# General dependency declarations
import os
from time import time
from time import timezone
# Raspi GPIO dependency declarations
import RPi.GPIO as GPIO
#Configure GPIO 7 AS output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial = GPIO.LOW)

# Production database loading -- Data format : Timestamp (POSIX) ; Prod (Wh/min) -- Separator = ";"
script_dir = os.path.dirname(__file__)
data_name = "Prod.csv"
path = os.path.join(script_dir, data_name)
Now = time()-timezone
Print(Now)
# Opening database and reading each line
with open(path, 'r') as f:
    for line in f:

        # Splitting line Conso[0]=Timestamp & Conso[1]=Prod
        Conso = [float(x) for x in line.split(";")]

        # Skip lines before now
        if Conso[1] < Now:
            pass
        else:
            # Begin prod meter emulation
            DeltaImp = (55-Conso[1]*0.6)/Conso[1]
            for i in range(Conso[1]):
                GPIO.output(7, 1)  # OUT = 1
                time.sleep(0.6)
                GPIO.output(7, 0)  # OUT = 0
                time.sleep(DeltaImp)
            # Wait for next minute
            while Conso[0]+60 > time.clock():
                time.sleep(0.1)