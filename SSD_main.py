#Source Sink Diffusion Project
#November 2015
import SSD_settings as ss
import SSD_functions as sfuc
import math, random, time, matplotlib
matplotlib.use('TkAgg') #For interactive plots
import numpy as np
import matplotlib.pyplot as plt

starting_point1 = [25,25]
starting_point2 = [25,25]
plt.ion()
graph = plt.plot(starting_point1[0],starting_point1[1])
plt.ylim([0,100])
plt.xlim([0,100])
for i in range(100):
    starting_point1 = sfuc.GoRandom(starting_point1[0],starting_point1[1],10)
    starting_point2 = sfuc.GoRandom(starting_point2[0],starting_point2[1],10)
    plt.scatter(starting_point1[0],starting_point1[1],color='r')
    plt.scatter(starting_point2[0],starting_point2[1],color='b')
    plt.draw()
    plt.pause(0.001)
