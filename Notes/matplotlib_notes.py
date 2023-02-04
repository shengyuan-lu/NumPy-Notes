import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

# Plot just one figure with (x,y) coordinates
def one():
    x = np.random.rand(10)
    y = np.random.rand(10)

    figure1 = plt.plot(x, y)

    plt.show()

# Plot one or several figure(s) in the same window
def two():

    # Plot just one figure
    x = np.random.rand(10)
    y = np.random.rand(10)

    ax = plt.subplot()
    ax.plot(x, y)

    # Plot multiple figures
    x1 = np.random.rand(10)
    x2 = np.random.rand(10)
    x3 = np.random.rand(10)
    x4 = np.random.rand(10)
    y1 = np.random.rand(10)
    y2 = np.random.rand(10)
    y3 = np.random.rand(10)
    y4 = np.random.rand(10)

    figure2, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2) # This plot 4 figures which are named ax1, ax2, ax3 and ax4 each one but on the same window.
    ax1.plot(x1, y1)
    ax2.plot(x2, y2)
    ax3.plot(x3, y3)
    ax4.plot(x4, y4)

    plt.show()

def three():
    # Difference between “axes” and “axis” in matplotlib?
    # Axes: given figure can contain many axes
    # Axis: These are the number-line-like objects

    # plt.figure just creates a figure (but with no axes in it)
    # plt.figure() is usually used when you want more customization to you axes, such as positions, sizes, colors and etc
    plt.figure(1, figsize = (400,8))

    # plt.subplots takes optional arguments (ex: plt.subplots(2, 2)) to create an array of axes in the figure
    # plt.subplots() is recommended for generating multiple subplots in grids
    fig, ax = plt.subplots()
    fig.set_size_inches(400, 8)

def four():
    fig = plt.figure()
    fig.add_subplot(221)  # top left
    fig.add_subplot(222)  # top right
    fig.add_subplot(223)  # bottom left
    fig.add_subplot(224)  # bottom right
    plt.show()

if __name__ == '__main__':
    four()