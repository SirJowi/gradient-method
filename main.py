""" Gradient Method - 11/04/23 """

import numpy as np
import matplotlib.pyplot as plt  # Paket fürs grafische Darstellen
from matplotlib import rc


#  Überprüft, ob im zulässigen Bereich der Schrittweiten
def boundary(bound):
    if bound < 0:  # untere Grenze
        bound = 0
    elif bound > len(s) - 1:  # obere Grenze
        bound = len(s) - 1
    return bound


# Randbedingungen festlegen --------------------------------------------------------------------------------------------
def z(x):  # Zielfunktion
    return 100 * x[0] * x[1] + x[0] / x[1] + 1 / (x[0] * x[1])


def grad(x):  # Gradient der Zielfunktion (manuell abgeleitet)
    return np.asanyarray([100 * x[1] + 1 / x[1] - 1 / (x[1] * x[0] ** 2),
                          100 * x[0] - x[0] / x[1] ** 2 - 1 / (x[0] * x[1] ** 2)])


# Schrittweiten-Array
s = np.array([0.01, 0.005, 0.0025, 0.001])  # vorgegebene Schrittweiten lambda

# Nebenbedingungen
upper_border = 1.0
lower_border = 0.25

# Startbedingungen -----------------------------------------------------------------------------------------------------
x_vorher = np.array([0.5, 0.5])  # Startpunkt x_0 (2-dim vektor)
print("Startpunkt eingeben x1:")
x_vorher[0] = input()
print("Startpunkt eingeben x2:")
x_vorher[1] = input()
b = 0  # Index des Schrittweiten-Arrays auf die maximale Schrittweite setzen
i = 0  # Anzahl Grundlösungen (Der Iterator)

# Ausgabe -------------------------------------------------------------------------------
xSpeicher = [x_vorher]
zSpeicher = []

while True:
    print("--------------------------------")
    i = i + 1
    print("Schritt:", i)
    print("Lambda:", s[b])

    # Koordinaten des neuen Punktes berechnen
    x_aktuell = x_vorher - s[b] * grad(x_vorher) / np.linalg.norm(grad(x_vorher))

    print("Gradient:", grad(x_vorher))
    print("x_vorher:", x_vorher)
    print("x_aktuell:", x_aktuell)

    # Überprüfen der Randbedingungen verletzt
    if ((x_aktuell[0] or x_aktuell[1]) < lower_border) or ((x_aktuell[0] or x_aktuell[1]) > upper_border):
        b = b + 1
        b = boundary(b)
        continue
    # falls nicht verletzt, dann
    else:
        # Zielfunktionswerte berechnen
        f_vorher = z(x_vorher)
        f_aktuell = z(x_aktuell)

        print("f_vorher:", f_vorher)
        print("f_aktuell:", f_aktuell)

        verbesserung = f_vorher - f_aktuell  # Verbesserung, wenn positiv

        print("Verbesserung:", verbesserung)

        # Abbruchkriterium
        if abs(verbesserung) <= 0.01:
            break

        if verbesserung < 0:
            b = b + 1
            b = boundary(b)
        elif verbesserung > 0:
            b = b - 1
            b = boundary(b)
            x_vorher = x_aktuell
            xSpeicher.append(x_vorher)
            zSpeicher.append(f_vorher)

# Ausgabe des gefundenen Minimums und dessen Ort
print("-----------------------------")
print("Es wurde ein Minimum gefunden")
print("Minimum:", f_aktuell)
print("Ort des Minimum:", x_aktuell)
print("-----------------------------")


# Anpassung Schriftart & -größe für Plots
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

plt.rcParams['figure.figsize'] = [7, 3.5]  # Anpassung der Plot-Größe

# Plot der Zielfunktion und des Eingabevektors über Iterationsschritte
# Erstellung der Grafik
fig, ax = plt.subplots(1, 2)
# plot des input Vektors über Iterationsschritte
xArray = np.asanyarray(xSpeicher)
ax[0].plot(xArray[:, 0], xArray[:, 1], 'r.-')
# Überschrift und Achsenbeschriftungen
ax[0].set_title('Entwurfsraum')
ax[0].set_xlabel(r'$x_1\ [\textrm{cm}^2]$')
ax[0].set_ylabel(r'$x_2\ [\textrm{cm}^2]$')
ax[0].set_xlim(lower_border, upper_border)
ax[0].set_ylim(lower_border, upper_border)
# plot der Zielfunktion über Iterationsschritte
ax[1].plot(zSpeicher, 'b.-')
# Überschrift und Achsenbeschriftungen
ax[1].set_title('Ergebnisraum')
ax[1].set_xlabel('Iterationen')
ax[1].set_ylabel(r'$z(x_1,\,x_2)\ [\textrm{cm}^3]$')
ax[1].set_xlim(0, i)
# erstelle Raster
for axi in ax:
    axi.grid()
# positioniere subplots
fig.tight_layout()
fig.subplots_adjust(wspace=0.65)
plt.show()
