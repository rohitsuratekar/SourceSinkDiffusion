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
if ss.all_different_color_molecules == 1:
    HSV = [(x*1.0/number_of_colors, 0.5, 0.5) for x in range(number_of_colors)]
    RGB = map(lambda x: colorsys.hsv_to_rgb(*x), HSV)
if ss.all_different_color_molecules == 0:
    RGB = [(0.69,0.4,1)]*number_of_colors

molecules =[] #make empty list
enzymes = []
for_heat_map = []
#Initializinf Enzyme sites
for k in range(len(ss.Sink_Positions)):
    enzymes.append((ss.Sink_Positions[k][0],ss.Sink_Positions[k][1],ss.Sink_Size))

#Initialize starting points of molecules
for m in range(ss.number_of_substarte_molecules):
    temp_coord = [random.uniform(ss.grid_width[0],ss.grid_width[1]), random.uniform(ss.grid_hight[0],ss.grid_hight[1])]
    for item in molecules:
        isClashing = sfuc.CheckClashing( (temp_coord[0],temp_coord[1],ss.molecule_radius), (item[0],item[1],item[2]) )
        while isClashing == 1:
            temp_coord = [random.uniform(ss.grid_width[0],ss.grid_width[1]), random.uniform(ss.grid_hight[0],ss.grid_hight[1])]
            isClashing = sfuc.CheckClashing( (temp_coord[0],temp_coord[1],ss.molecule_radius), (item[0],item[1],item[2]) )

    molecules.append((temp_coord[0],temp_coord[1], ss.molecule_radius,RGB[m]))

print "all molecules successfully created"

#Calculations

afterEnzymeReaction = list(molecules)

for i in range(ss.number_of_itterations):
    molecules = []
    molecules = list(afterEnzymeReaction)
    for_heat_map.append(molecules)
    random.shuffle(molecules)  #Randomize molecue order
    afterEnzymeReaction = []
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
        enzymesite = 0
        for protein in enzymes:
            enzymesite = enzymesite + sfuc.CheckClashing([coord_store[0], coord_store[1], temp_store[2]],[protein[0],protein[1],protein[2]])

        if enzymesite == 0:
            molecules[element] =[coord_store[0], coord_store[1], temp_store[2], temp_store[3]]  #add radius and color information
            afterEnzymeReaction.append(molecules[element])





    for element in molecules:
        c = plt.Circle((element[0],element[1]),element[2], color = element[3] ) #create circle
        plt.gca().add_patch(c)  #add to plot
    for item in enzymes:
        c = plt.Circle((item[0],item[1]),item[2], color = 'k' ) #create circle
        plt.gca().add_patch(c)  #add to plot

    plt.xlim([ss.grid_width[0],ss.grid_width[1]]) #set axis limit
    plt.ylim([ss.grid_hight[0],ss.grid_hight[1]]) #set axis limit
    plt.title("Number of substrate molecules = %d/%d"%(len(molecules),ss.number_of_substarte_molecules))
    plt.draw() #Draw
    #plt.pause(0.000001) #Pause for visualization
    plt.clf() #clear plot for next use
alltime_molecule_poistions=[]
r = 0
if ss.get_heatmap == 1:
    for k in range(len(for_heat_map)):
        for m in range(len(for_heat_map[k])):
            alltime_molecule_poistions.append([r,for_heat_map[k][m][0],for_heat_map[k][m][1]])
            r = r+1
alltime_molecule_poistions= np.asarray(alltime_molecule_poistions)
all_x= alltime_molecule_poistions[:,1]
all_y= alltime_molecule_poistions[:,2]
plt.scatter(all_x,all_y)
plt.show()
