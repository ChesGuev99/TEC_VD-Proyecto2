# https://python-graph-gallery.com/150-parallel-plot-with-pandas/
# colors https://matplotlib.org/3.3.2/tutorials/colors/colormaps.html

# libraries
import matplotlib.pyplot as plt
from pandas.plotting._matplotlib import parallel_coordinates

# Take the iris dataset
import seaborn as sns

def sea():
    data = sns.load_dataset('iris')

    # Make the plot
    parallel_coordinates(data, 'species', colormap=plt.get_cmap("viridis"))
    plt.show()
