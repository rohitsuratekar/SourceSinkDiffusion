#Source Sink Diffusion Project function file
import SSD_settings as ss
from random import randrange
from numpy import cos, sin, radians

def GoRandom(x,y,step):
    angle = radians(randrange(360))
    new_x = x + step*cos(angle)
    new_y = y + step*sin(angle)
    if new_x < ss.grid_width[0]:
        while new_x <= ss.grid_width[0]:
            angle = radians(randrange(360))
            new_x = x + step*cos(angle)
    if new_x > ss.grid_width[1]:
        while new_x >= ss.grid_width[0]:
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
