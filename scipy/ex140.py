from scipy import integrate
import numpy as np
from math import sqrt


if __name__ == "__main__":
    # set  fuction f(x)
    f = lambda x, y : 64 *x*y
    # lower limit of second integral
    p = lambda x : 0
    # upper limit of first integral
    q = lambda y : sqrt(1 - 2*y**2)
    # perform double integration
    integration = integrate.dblquad(f , 0 , 2/4,  p, q)
    print(integration)