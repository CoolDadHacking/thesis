#### converToInt.py
#### shapes labels to integers
## Rambo You
## University of Minnesota
## Capstone MSST 2017

## converting character array to integers
import numpy as np
import csv
data_file = 'longTract.csv'
save_file = 'longTractIntKey.csv'
keysPressed = np.genfromtxt(data_file, delimiter=',', usecols=0, dtype=str)
#intKeysPressed = np.array([],dtype=int)


with open(save_file, 'w') as csvfile:
    fieldnames = ['keyPressed']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for keyPressed in keysPressed:
        if keyPressed == '\\x7f':
            writer.writerow({'keyPressed': 32})
            #intKeysPressed = np.append(intKeysPressed, 32)
        elif keyPressed == 'back\\x7f':
            writer.writerow({'keyPressed': 8})
            #intKeysPressed = np.append(intKeysPressed, 8)
        elif keyPressed == 'space':
            writer.writerow({'keyPressed': 32})
        elif keyPressed == 'backspace':
            writer.writerow({'keyPressed': 127})
        else:
            writer.writerow({'keyPressed': ord(keyPressed)})
            #intKeysPressed = np.append(intKeysPressed, ord(keyPressed))
  