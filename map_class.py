# MAP CLASS
# TODO: docstrings

import numpy as np
import matplotlib.pyplot as plt
from cmap_functions import generate_colormap
import datetime
import noise

class Map:

    def __init__(self, dim_x, dim_y):
        self.dim_x = dim_x                                          # number of points along x
        self.dim_y = dim_y                                          # number of points along y
        self.heightmap = np.zeros([dim_y, dim_x], dtype='float')    # heightmap --> each point in the grid is associated to a height value
        self.hardness = np.zeros([dim_y, dim_x], dtype='float')     # hardness --> each point in the grid is associated to a hardness value (determining how easy it is to erode it)

    def initialize_heightmap(self, seed=0):
        """ Function initialize_heightmap_CN() initializes the grid heightmap using a given noise pattern (which for the
            moment is a perlin noise, but could be modified in the future, for example by adding a number of additional
            noise types to choose from). The optional parameter seed can be modified to change the numpy random library
            seed and has the purpose of guaranteeing repeatability. """
        self.heightmap = self.perlin_noise(seed)

    def perlin_noise(self, seed):
        """ Returns matrix of coherent perlin noise based on the (optional) seed parameter. """
        # TODO: this implementation of the perlin noise is VERY slow and could be improved by using one of the implementations found in the perlin_noise_1 and _2 files
        shape = (self.dim_y, self.dim_x)    # size of the output noise matrix
        scale = 300.0                       # scale at which noise is observed
        octaves = 6                         # number of functions overlapped to obtain the noise --> can be imagined as harmonics of a sound signal
        persistence = 0.5                   # if <1 the amplitude of the functions decreases
        lacunarity = 2.0                    # if >1 the frequency of the functions increases
        scaling_factor = 1000               # to obtain a realistic heightmap in [m]

        np.random.seed(seed)
        noise_mat = np.zeros(shape)
        for i in range(shape[0]):
            for j in range(shape[1]):
                noise_mat[i][j] = noise.pnoise2(i/scale, j/scale, octaves=octaves, persistence=persistence,
                                            lacunarity=lacunarity, repeatx=shape[0], repeaty=shape[1], base=0)

        noise_mat *= scaling_factor
        return noise_mat


    def get_neighboring_nodes(self, x, y) -> list:
        # Function get_neighboring_nodes() takes as input two float coordinates [x, y] and retrieves the row and column
        # indexes of the 4 neighboring nodes (i.e. the indexes of the 4 neighboring grid points).
        pass

    def display(self, save=False):
        # Function visualize_heightmap() plots the heightmap in a matplotlib figure. The optional parameter save
        # determines if the resulting image is saved in memory. Default path is current folder, which can be changed
        # throught the second optional argument path.
        x = np.arange(0, self.dim_x)
        y = np.arange(0, self.dim_y)
        X, Y = np.meshgrid(x, y)
        colormap = generate_colormap()
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, self.heightmap, cmap=colormap)
        ax.xaxis.set_rotate_label(False)
        ax.yaxis.set_rotate_label(False)
        ax.zaxis.set_rotate_label(False)
        ax.set_xlabel('x', rotation='horizontal', labelpad=5)
        ax.set_ylabel('y', rotation='horizontal', labelpad=10)
        ax.set_zlabel('elevation', rotation='horizontal', labelpad=18)
        if save:
            now = datetime.datetime.now()
            name = f'heightmap{now.year}{now.month}{now.day}_{now.hour}{now.minute}{now.second}'
            save_path = f'Images/{name}.png'
            fig.savefig(save_path, dpi=600, facecolor='w', edgecolor='w')
        plt.show()

    def animate(self, save=False):
        # TODO: change AZ and EL at each time step to obtain a dynamic camera position (see link below)
        #  https://stackoverflow.com/questions/12904912/how-to-set-camera-position-for-3d-plots-using-python-matplotlib
        pass