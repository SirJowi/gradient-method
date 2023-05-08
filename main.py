""" Gradientenmethode - 11/04/23 """

import numpy as np
import matplotlib.pyplot as plt  # Paket für grafische Darstellen
from matplotlib import rc


# Unterprogramm: Verhindert, dass das Schrittweiten-Array verlassen wird -----------------------------------------------
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
s = np.array([0.01, 0.005, 0.0025, 0.001])  # vorgegebene Schrittweiten

# Nebenbedingungen
upper_border = 1.0
lower_border = 0.25

# Startbedingungen -----------------------------------------------------------------------------------------------------
x_vorher = np.array([0.5, 0.5])  # Startpunkt x_0 (2-dim vektor)
print("Startpunkt eingeben [", lower_border, "< x1 <", upper_border, "] :")
x_vorher[0] = input()
print("Startpunkt eingeben [", lower_border, "< x2 <", upper_border, "] :")
x_vorher[1] = input()
b = 0  # Index des Schrittweiten-Arrays auf die größte Schrittweite setzen
i = 0  # Anzahl Iterationsschritte
rb_alert = 0    # Soll das unendliche Suchen außerhalb der Randbedingungen verhindern

# Gradientenmethode ----------------------------------------------------------------------------------------------------
xSpeicher = [x_vorher]  # Abspeichern des Ortes in jedem Iterationsschritt
zSpeicher = []  # Abspeichern des Wertes der Zielfunktion in jedem Iterationsschritt

while True:
    print("--------------------------------")
    i = i + 1   # Iterationsschritt hochzählen
    print("Schritt:", i)
    print("Lambda:", s[b])  # Schrittweite ausgeben

    # Koordinaten des neuen Punktes berechnen
    x_aktuell = x_vorher - s[b] * grad(x_vorher) / np.linalg.norm(grad(x_vorher))

    print("Gradient:", grad(x_vorher))
    print("x_vorher:", x_vorher)
    print("x_aktuell:", x_aktuell)

    # Überprüfen, ob Randbedingungen verletzt
    if ((x_aktuell[0] or x_aktuell[1]) < lower_border) or ((x_aktuell[0] or x_aktuell[1]) > upper_border):
        b = b + 1
        b = boundary(b)
        rb_alert = rb_alert + 1
        if rb_alert == 1000:    # nach 1000 Schritten ohne neue Berechnung des Ortes wird abgebrochen
            print("|-----------------------------")
            print("| Aufgrund von verletzten Randbedingungen kann keine Lösung gefunden werden.")
            print("| Bitte wählen Sie einen anderen Startpunkt. ¯\_(ツ)_/¯ ")
            print("|-----------------------------")
            break
        continue
    # falls Randbedingungen nicht verletzt, dann
    else:
        # Zielfunktionswerte berechnen
        f_vorher = z(x_vorher)
        f_aktuell = z(x_aktuell)

        print("f_vorher:", f_vorher)
        print("f_aktuell:", f_aktuell)

        verbesserung = f_vorher - f_aktuell  # Verbesserung, wenn positiv

        print("Verbesserung:", verbesserung)

        # Abbruchkriterium
        if abs(verbesserung) <= 0.01:   # Betrag der Verbesserung
            # Ausgabe des gefundenen Minimums und dessen Ort
            print("|-----------------------------")
            print("| Es wurde ein Minimum gefunden (◠‿◠)")
            print("| Minimum:", f_aktuell)
            print("| Ort des Minimum:", x_aktuell)
            print("|-----------------------------")
            break

        if verbesserung < 0:    # Verschlechterung der Zielfunktion
            b = b + 1           # Schrittweite verringern
            b = boundary(b)     # Überprüfen ob außerhalb des Schrittweiten-Arrays
        elif verbesserung > 0:  # Verbesserung der Zielfunktion
            b = b - 1           # Schrittweite vergrößern
            b = boundary(b)     # Überprüfen ob außerhalb des Schrittweiten-Arrays

            x_vorher = x_aktuell        # neuer Ort wird für den nächsten Iterationsschritt übernommmen
            xSpeicher.append(x_vorher)  # Ort wird abgespeichert
            zSpeicher.append(f_vorher)  # Wert der Zielfunktion wird abgespeichert


# Darstellung ----------------------------------------------------------------------------------------------------------

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
ax[0].set_xlim(lower_border, upper_border)      # Dargestellter Bereich begrenzt durch Grenzen der Randbedingungen
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
