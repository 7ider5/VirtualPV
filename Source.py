__author__ = 'EBJ501'

import os
from time import sleep

script_dir = os.path.dirname(__file__)
data_name = "Prod.txt"
path = os.path.join(script_dir, data_name)

with open(path, 'r') as f:
    for line in f:
        for i in range(int(line)):
			print(line) #<-- Allumage et extinction de la LED en fonction de l(intervale line
			sleep(int(line)/10)
