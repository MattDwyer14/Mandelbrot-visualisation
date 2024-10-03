import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_depth):
    """
    Determines if a point is in the Mandelbrot set based on the number of iterations.
    
    Parameters:
    - c: Complex number to be tested.
    - max_depth: Maximum number of iterations to check for divergence.
    
    Returns:
    - The number of iterations it took for the value to diverge, or max_depth if it didn't diverge.
    """
    z = 0
    for depth in range(max_depth):
        z = z**2 + c
        if abs(z) > 2:
            return depth
    return max_depth

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_depth):
    """
    Generates the Mandelbrot set for a given range and resolution.
    
    Parameters:
    - xmin, xmax: The range of x-axis (real part).
    - ymin, ymax: The range of y-axis (imaginary part).
    - width, height: The resolution of the output image.
    - max_depth: Maximum number of iterations to check for each point.
    
    Returns:
    - A 2D numpy array representing the Mandelbrot set.
    """
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    
    for i in range(width):
        for j in range(height):
            c = r1[i] + 1j * r2[j]
            n3[i, j] = mandelbrot(c, max_depth)
    
    return n3

def plot_mandelbrot(xmin, xmax, ymin, ymax, width=800, height=800, max_depth=100):
    """
    Plots the Mandelbrot set.
    
    Parameters:
    - xmin, xmax: The range of x-axis (real part).
    - ymin, ymax: The range of y-axis (imaginary part).
    - width, height: The resolution of the output image.
    - max_depth: Maximum number of iterations to check for each point.
    """
    mandelbrot_img = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_depth)
    
    plt.imshow(mandelbrot_img.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
    plt.colorbar(label='Depth')
    plt.title(f'Mandelbrot Set (Depth={max_depth})')
    plt.xlabel('Real part')
    plt.ylabel('Imaginary part')
    plt.show()

# Adjustable parameters for visualization
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
width, height = 800, 800
max_depth = int(input("Enter the maximum depth for Mandelbrot set visualization: "))

# Generate and plot Mandelbrot set
plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_depth)
