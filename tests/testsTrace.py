import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial


class TestsTrace:
    x = np.linspace(-1000, 1000, 50)
    #p=np.poly1d([10, -8, 7])
    #plt.plot(x, np.tan(x))  # on utilise la fonction sinus de Numpy
    plt.plot(x, np.sin(np.cos(np.tan(x/8))))
    #plt.plot(p(x))
    #plt.plot(np.sin([20,0]))  # on utilise la fonction sinus de Numpy
    plt.show()
