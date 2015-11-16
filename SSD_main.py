#Source Sink Diffusion Project
#November 2015
import SSD_settings as ss
import SSD_functions as sfuc
from matplotlib.patches import Circle
import math, random, time, matplotlib, colorsys
matplotlib.use('TkAgg') #For interactive plots
import numpy as np
import matplotlib.pyplot as plt

N = ss.number_of_substarte_molecules
HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)

molecules =[]
#Initialize starting points of molecules
for m in range(ss.number_of_substarte_molecules):
    molecules.append((random.uniform(ss.grid_width[0],ss.grid_width[1]), random.uniform(ss.grid_hight[0],ss.grid_hight[1]), ss.molecule_radius, RGB_tuples[m]))

plt.axes()

for i in range(50):
    random.shuffle(molecules)  #Randomize molecue order
    for element in range(len(molecules)):
        temp_store = molecules[element]
        temp_store2 = sfuc.GoRandom(temp_store[0],temp_store[1],2)
        molecules[element] =[temp_store2[0], temp_store2[1], temp_store[2], temp_store[3]]

    for element in molecules:
        c = plt.Circle((element[0],element[1]),element[2], color = element[3] )
        plt.gca().add_patch(c)

    plt.xlim([ss.grid_width[0],ss.grid_width[1]])
    plt.ylim([ss.grid_hight[0],ss.grid_hight[1]])
    plt.draw()
    plt.pause(0.00001)
    plt.clf()
