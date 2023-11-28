import control
import matplotlib.pyplot as plt
import numpy as np

def place_poles():
    angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
    poles = np.exp(1j * angles)
    return poles

# Convert poles to transfer function
poles = place_poles()
tf = control.TransferFunction([1], np.poly(poles))

control.pzmap(tf)
plt.show()

dtf=control.sample_system(tf, 0.1, method='tustin')
control.pzmap(dtf)
plt.show()