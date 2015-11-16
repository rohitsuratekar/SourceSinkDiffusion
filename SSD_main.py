#Source Sink Diffusion Project
#November 2015
import SSD_settings as ss
import SSD_functions as sfuc
from matplotlib.patches import Circle
import math, random, time, matplotlib, colorsys
matplotlib.use('TkAgg') #For interactive plots
import numpy as np
import matplotlib.pyplot as plt

#Generate distict colors
number_of_colors = ss.number_of_substarte_molecules
HSV = [(x*1.0/number_of_colors, 0.5, 0.5) for x in range(number_of_colors)]
RGB = map(lambda x: colorsys.hsv_to_rgb(*x), HSV)

molecules =[] #make empty list

#Initialize starting points of molecules
for m in range(ss.number_of_substarte_molecules):
    molecules.append((random.uniform(ss.grid_width[0],ss.grid_width[1]), random.uniform(ss.grid_hight[0],ss.grid_hight[1]), ss.molecule_radius, RGB[m]))

for i in range(ss.number_of_itterations):
    random.shuffle(molecules)  #Randomize molecue order
    for element in range(len(molecules)):
        temp_store = molecules[element]  #Store old molecule
        temp_store2 = sfuc.GoRandom(temp_store[0],temp_store[1], ss.step_size ) #Get new randomized location
        molecules[element] =[temp_store2[0], temp_store2[1], temp_store[2], temp_store[3]]  #add radius and color information

    for element in molecules:
        c = plt.Circle((element[0],element[1]),element[2], color = element[3] ) #create circle
        plt.gca().add_patch(c)  #add to plot

    plt.xlim([ss.grid_width[0],ss.grid_width[1]]) #set axis limit
    plt.ylim([ss.grid_hight[0],ss.grid_hight[1]]) #set axis limit
    plt.draw() #Draw
    plt.pause(0.00001) #Pause for visualization
    plt.clf() #clear plot for next use
