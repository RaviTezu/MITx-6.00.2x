from __future__ import print_function

import os
import pylab

# It is assumed that the 'julyTemps.txt' file is present along the side of this script and this script is
# executed at the root.
PWD = os.getcwd()
FILE_NAME = 'julyTemps.txt'
FILE = PWD + '/' + FILE_NAME

HIGH = []
LOW = []


def load_file(inFile=FILE):
    return open(inFile, 'r')


def read_data(fd=load_file()):
    for line in fd.readlines():
        fields = line.split()
        if len(fields) < 3 or not fields[0].isdigit():
            pass
        else:
            HIGH.append(fields[1])
            LOW.append(fields[2])


def calculate_diff(high=HIGH, low=LOW):
    diff_temps = [int(h) - int(l) for h,l in zip(high, low)]
    return diff_temps


def plotting(diff_temps):
    length = len(diff_temps)
    print(length)
    pylab.figure(1)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.plot(range(1, length + 1), diff_temps)
    pylab.show()


if __name__ == "__main__":
    read_data()
    plotting(calculate_diff())
