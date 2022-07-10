# Hydraulic Erosion Simulation

from drop_class import Drop
from map_class import Map

# generate world
dim = 500
world = Map(dim, dim)
world.initialize_heightmap()
world.display(True)

