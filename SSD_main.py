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
    temp_coord = [random.uniform(ss.grid_width[0],ss.grid_width[1]), random.uniform(ss.grid_hight[0],ss.grid_hight[1])]
    for item in molecules:
        isClashing = sfuc.CheckClashing( (temp_coord[0],temp_coord[1],ss.molecule_radius), (item[0],item[1],item[2]) )
        while isClashing == 1:
            temp_coord = [random.uniform(ss.grid_width[0],ss.grid_width[1]), random.uniform(ss.grid_hight[0],ss.grid_hight[1])]
            isClashing = sfuc.CheckClashing( (temp_coord[0],temp_coord[1],ss.molecule_radius), (item[0],item[1],item[2]) )

    molecules.append((temp_coord[0],temp_coord[1], ss.molecule_radius,RGB[m]))
    print "created molecule no :%d , if this is taking long time, check grid size and molecule radius "%(m)

print "all molecules successfully created"
print "If you don't see plot check step size/grid size/molecular radius"
for i in range(ss.number_of_itterations):
    random.shuffle(molecules)  #Randomize molecue order
    for element in range(len(molecules)):
        all_other_molecules = [i for i in molecules if i != molecules[element]]
        temp_store = molecules[element]  #Store old molecule
        coord_store = sfuc.GoRandom(temp_store[0],temp_store[1], ss.step_size ) #Get new randomized location
        for item in all_other_molecules:
            isClashing = sfuc.CheckClashing([item[0],item[1],item[2]],[coord_store[0],coord_store[1],temp_store[2]])
            if isClashing == 1:
                while isClashing == 1:
                    #print "here"
                    coord_store = sfuc.GoRandom(temp_store[0],temp_store[1], ss.step_size ) #Get new randomized location
                    isClashing = sfuc.CheckClashing([item[0],item[1],item[2]],[coord_store[0],coord_store[1],temp_store[2]])

        molecules[element] =[coord_store[0], coord_store[1], temp_store[2], temp_store[3]]  #add radius and color information

    for element in molecules:
        c = plt.Circle((element[0],element[1]),element[2], color = element[3] ) #create circle
        plt.gca().add_patch(c)  #add to plot

    plt.xlim([ss.grid_width[0],ss.grid_width[1]]) #set axis limit
    plt.ylim([ss.grid_hight[0],ss.grid_hight[1]]) #set axis limit
    plt.draw() #Draw
    plt.pause(0.00001) #Pause for visualization
    plt.clf() #clear plot for next use
