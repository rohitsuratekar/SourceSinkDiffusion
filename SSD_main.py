#Source Sink Diffusion Project
#November 2015
import SSD_settings as ss
import SSD_functions as sfuc
import math, random, time, matplotlib
matplotlib.use('TkAgg') #For interactive plots
import numpy as np
import matplotlib.pyplot as plt

starting_point1 = [50,50]
starting_point2 = [50,50]

fig = plt.figure()
for i in range(50):
    grid = np.zeros(shape=(ss.grid_width[1],ss.grid_hight[1]))
    starting_point1 = sfuc.GoRandom(starting_point1[0],starting_point1[1],20)
    starting_point2 = sfuc.GoRandom(starting_point2[0],starting_point2[1],20)
    grid[starting_point1[0]][starting_point1[1]] = 1
    grid[starting_point2[0]][starting_point2[1]] = 1
    plt.scatter(starting_point1[0],starting_point1[1],color='r')
    plt.scatter(starting_point2[0],starting_point2[1],color='b')
    plt.ylim([0,100])
    plt.xlim([0,100])
    plt.draw()
    plt.pause(0.00001)
    plt.clf()
