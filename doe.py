#!/usr/bin/env python
# coding: utf-8

import csv
import pandas as pd
import pyDOE2
import cid

class ActiveSys(object):
    def __init__(self, name, min, max, type):
        self.name=name
        self.min = min
        self.max = max
        self.type = type

# Read user input
input = pd.read_csv('input_max.csv')

# DOE options
myFF = pyDOE2.fullfact([2,2,2,2,2,2,2,2,2,2])
# myCCD= pyDOE2.ccdesign(10, center=[0,1],alpha='o', face='ccf')
myCCD = pyDOE2.ccdesign(len(input), face='ccf')
myBBD = pyDOE2.bbdesign(len(input), center=1)
myGSD = pyDOE2.gsd([2,2,2,3,2,2,2,2,2,2], 2)

# Options write to csv
# with open("ff.csv","w+") as my_csv:
#     csvWriter = csv.writer(my_csv,delimiter=',')
#     csvWriter.writerows(myFF)

# with open("ccd.csv","w+") as my_csv:
#     csvWriter = csv.writer(my_csv,delimiter=',')
#     csvWriter.writerows(myCCD)
    
# with open("bbd.csv","w+") as my_csv:
#     csvWriter = csv.writer(my_csv,delimiter=',')
#     csvWriter.writerows(myBBD)
    
# with open("gsd.csv","w+") as my_csv:
#     csvWriter = csv.writer(my_csv,delimiter=',')
#     csvWriter.writerows(myGSD)

print("FF is %d rows" % len(myFF))
print("CCD is %d rows" % len(myCCD))
print("BBD is %d rows" % len(myBBD))
print("GSD is %d rows" % len(myGSD))

# Create Systems
systems = []
# Iterate over input, create a list of cid systems
for row in input.itertuples():
    print(row)
    systems.append(ActiveSys(row.Name, row.Min, row.Max, row.Type))


SystemNames=input.iloc[:,0].tolist()

# Make DOE
# if not len(systems) == len(myDOE.columns):
#     print("DOE does not match input...")
#     exit()
# else:
myDOE = pd.DataFrame(myCCD, columns=input.iloc[:,0].tolist())
from matplotlib import pyplot as plt
import numpy as np

# Set the figure size
plt.rcParams["figure.figsize"] = [3.00, 7.50]
# plt.rcParams["figure.autolayout"] = True

# Random data points
data = np.random.rand(5, 5)

# Plot the data using imshow with gray colormap
plt.imshow(myDOE, cmap='gray',  aspect='auto')

# Display the plot
plt.show()

for i, system in enumerate(systems):
    # print (system.name)
    # print (system.min)
    # print (system.max)
    myDOE.loc[myDOE[SystemNames[i]] == -1, SystemNames[i]] = systems[i].min
    myDOE.loc[myDOE[SystemNames[i]] == 0, SystemNames[i]] = (systems[i].min+systems[i].max)/2
    myDOE.loc[myDOE[SystemNames[i]] == 1, SystemNames[i]] = systems[i].max
    
myDOE

myDOE.to_csv("CCD_DOE.csv")

