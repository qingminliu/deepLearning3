import numpy as np
import matplotlib.pyplot as plt


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = w1*x1+w2*x2
    if tmp>theta:
        return 1
    else:
        return 0


def npAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    if np.sum(w*x)+b>0:
        return 1
    else:
        return 0


def npNAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x)+b
    if tmp>0:
        return 1
    else:
        return 0


def npOR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x)+b
    if tmp>0:
        return 1
    else:
        return 0


def npXOR(x1, x2):
    tmp1 = npNAND(x1, x2)
    tmp2 = npOR(x1, x2)
    tmp = npAND(tmp1, tmp2)
    return tmp


print(npXOR(1, 0))
print(npXOR(1, 1))
print(npXOR(0, 0))
