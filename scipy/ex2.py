import numpy as np
from scipy.special import cbrt, exp10, comb, perm


if __name__ == "__main__":
    #Find cubic root of 27 & 64 using cbrt() function
    cb = cbrt([27, 64])
    #print value of cb
    print(cb)

    #define exp10 function and pass value in its
    exp = exp10([1,10])
    print(exp)

    #find permutation of 5, 2 using perm (N, k) function
    per = perm(5, 2, exact = True)
    print(per)

    #find combinations of 5, 2 values using comb(N, k)
    com = comb(5, 2, exact = False, repetition=True)
    print(com)

