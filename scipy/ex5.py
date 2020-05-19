import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np


def function(a):
       return   a*2 + 20 * np.sin(a)

if __name__ == "__main__":
    #Frequency in terms of Hertz
    fre = 5 
    #Sample rate
    fre_samp = 50
    t = np.linspace(0, 2, 2 * fre_samp, endpoint = False )
    a = np.sin(fre  * 2 * np.pi * t)

    # Scaler function
    plt.plot(a, function(a))
    plt.show()
    #use BFGS algorithm for optimization
    optimize.fmin_bfgs(function, 0) 
