#Source Sink Diffusion Project Setting file
#Grid Properties
number_of_itterations = 100 #Like time
grid_hight = (0,100)
grid_width = (0,100)

#molecule properties
step_size = 3  #keep generally greater than molecule radius
number_of_substarte_molecules =100
molecule_radius = 1
allowed_repetation = 1000  #To randomize when there is clash

#Enzyme properties
Sink_Positions = [(20,20)]
Sink_Size = 5 #Radius

#Plotting Controls
live_simulation = 0  #Live view calculations will be much slower
all_different_color_molecules = 0  #1=yes, 0=no
get_heatmap = 1
