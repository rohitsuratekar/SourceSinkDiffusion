#Source Sink Diffusion Project function file
import SSD_settings as ss
from random import randrange
from numpy import cos, sin, radians

def GoRandom(x,y,step):
     angle = radians(randrange(360))
     new_x = x + step*cos(angle)
     new_y = y + step*sin(angle)
     return new_x, new_y
