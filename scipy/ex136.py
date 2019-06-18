# %matplotlib inline
from matplotlib import pyplot as plt
import numpy as np 
from scipy import fftpack


if __name__ == "__main__":
    #Frequency in terms of Hertz
    fre = 5 
    #Sample rate
    fre_samp = 50
    t = np.linspace(0, 2, 2 * fre_samp, endpoint = False )
    a = np.sin(fre  * 2 * np.pi * t)
    figure, axis = plt.subplots()
    axis.plot(t, a)
    axis.set_xlabel ('Time (s)')
    axis.set_ylabel ('Signal amplitude')
    plt.show()

    ## Discrete Fourier Transform
    # A = fftpack.fft(a)
    # frequency = fftpack.fftfreq(len(a)) * fre_samp
    # figure, axis = plt.subplots()

    # axis.stem(frequency, np.abs(A))
    # axis.set_xlabel('Frequency in Hz')
    # axis.set_ylabel('Frequency Spectrum Magnitude')
    # axis.set_xlim(-fre_samp / 2, fre_samp/ 2)
    # axis.set_ylim(-5, 110)
    # plt.show()