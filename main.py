""" Gradient Method - 11/04/23 """

import numpy as np


# Startpunkt x_0
x_0 = np.array([0.5, 0.5])

# Zielfunktion
def z(x):
    return 100 * x[0] * x[1] + x[0]/x[1] + 1/(x[0] * x[1])

def grad(x):
    return np.array(100*x[1] + 1/x[1] - 1/(x[1] * x[0]**2),
                    100 * x[0] - x[0] / x[1] - 1 / (x[0] * x[1]**2))

def lmbda(x, b, verbesserung):

    def boundary(b):
        if(b<0):
            b = b + 1
        elif(b>3):
            b = b - 1
        else:
            b = b
        return b

    # vorgegebene Schrittweiten lambda
    s = np.array([0.01, 0.005, 0.0025, 0.001])

    if(((x[0] and x[1]) < 0.25) or ((x[0] and x[1]) > 1.0)):
        b = b + 1
        boundary(b)

    if(verbesserung < 0):
        b = b + 1
        boundary(b)

    if(verbesserung > 0):
        b = b - 1
        boundary(b)

    return s[b]


b = 0
lmbda_temp = 0.01
x_vorher = x_0
f_vorher = z(x_vorher)
f_aktuell = f_vorher


while(True):
    x_aktuell = x_vorher - lmbda_temp * grad(x_vorher)/np.linalg.norm(grad(x_vorher))
    f_aktuell = z(x_aktuell)
    f_vorher = z(x_vorher)

    verbesserung = f_aktuell - f_vorher

    lmbda_temp = lmbda(x_aktuell, b, verbesserung)

    print("x_vorher:", x_vorher)
    print("f_vorher:", f_vorher)
    print("x_aktuell:", x_aktuell)
    print("f_aktuell:", f_aktuell)
    print("Verbesserung:", verbesserung)
    print("Lambda:", lmbda_temp)
    print("----------------")

    x_vorher = x_aktuell

    if(abs(verbesserung) <= 0.01):
        break

