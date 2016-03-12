import os

DATA_FILE = "julyTemps.txt"

def load_data(datafile=DATA_FILE):

    with datafile as f:
        for line in f.readlines():
            print(line)