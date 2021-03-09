import matplotlib.pyplot as ptt
import numpy as np

x = np.linspace(0, 5, 10)
y = x ** 2
ptt.plot(x, y, 'r', x, x ** 3, 'g', x, x ** 4, 'b')
