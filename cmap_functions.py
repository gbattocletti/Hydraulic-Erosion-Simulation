import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def generate_colormap():
    """Generates custom colormap for the heightmap visualization. """
    # Reference: https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html
    custom_colors = np.array([[216, 189, 12],
                       [87, 155, 11],
                       [68, 119, 10],
                       [41, 70, 9],
                       [57, 99, 9],
                       [81, 75, 8],
                       [133, 126, 54],
                       [158, 154, 109],
                       [196, 193, 165],
                       [220, 219, 208]])
    custom_colors = custom_colors/255
    nodes = [0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    cmap = LinearSegmentedColormap.from_list('mountain_cmap', list(zip(nodes, custom_colors)))  # --> nodes can be used to change the spacing between the 10 colors anchor points
    # cmap = LinearSegmentedColormap.from_list('mountain_cmap', custom_colors) # --> to obtain an evenly distributed cmap
    return cmap


def plot_examples(colormaps):
    """ Helper function to plot data with associated colormap. """
    np.random.seed(19680801)
    data = np.random.randn(30, 30)
    n = len(colormaps)
    fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3),
                            constrained_layout=True, squeeze=False)
    for [ax, cmap] in zip(axs.flat, colormaps):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
        fig.colorbar(psm, ax=ax)
    plt.show()

### Test functions:
# test_cmap = generate_colormap()
# plot_examples([test_cmap])