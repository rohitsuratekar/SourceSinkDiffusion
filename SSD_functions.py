#Source Sink Diffusion Project function file
import SSD_settings as ss
from random import randrange
from numpy import cos, sin, radians

#Randomization with bounce from boundary conditions
def GoRandom(x,y,step):
    angle = radians(randrange(360))  #Generate Random direction
    new_x = x + step*cos(angle)  #Convert to cartesian
    new_y = y + step*sin(angle)  #Convert to cartesian

    #Check for boundry conditions. IF outside boundary, take different random direction.
    if new_x < ss.grid_width[0]:
        while new_x <= ss.grid_width[0]:
            angle = radians(randrange(360))
            new_x = x + step*cos(angle)
    if new_x > ss.grid_width[1]:
        while new_x >= ss.grid_width[1]:
            angle = radians(randrange(360))
            new_x = x + step*cos(angle)
    if new_y < ss.grid_hight[0]:
        while new_y <= ss.grid_hight[0]:
            angle = radians(randrange(360))
            new_y = y + step*sin(angle)
    if new_y > ss.grid_hight[1]:
        while new_y >= ss.grid_hight[1]:
            angle = radians(randrange(360))
            new_y = y + step*sin(angle)
    return new_x, new_y

def CheckClashing(molecule1, molecule2):  #Input should be molecule(x,y,radius)
    distance_between_center = ((molecule1[0]-molecule2[0])**2 + (molecule1[1]-molecule2[1])**2)**(0.5)

    if distance_between_center < (molecule1[2]+molecule2[2]):
        clashing = 1
    if distance_between_center >= (molecule1[2]+molecule2[2]):
        clashing = 0

    return clashing
