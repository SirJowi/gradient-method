class optimierungsaufgabe(object):
    def __init__(self, z):
        """
        abstrakte Klasse fuer Optimierungsaufgaben verschiedener Typen
        -> __init__ wird aufgerufen sobald eine Instanz dieser Klasse
        initialisiert wird

        :param z: Zielfunktion
        """

        # Speicherung von Variable die dem Objekt zugeordnet ist
        self.z = z # Zielfunktion -> jede Optimieurngsuafgabe benoetigt eine definierte Zielfunktion

class gradientenbasierte_optimierung(optimierungsaufgabe):
    def __init__(self, z, startpunkt, **kwargs):
        """
        Klasse fuer Optimierungsaufgabe, die durch gradientenbasierte
        Optimierung geloest werden soll. Diese Klasse ist eine Instanz
        der abstrakten Klasse optimierungsaufgabe, erbt also alle
        Variablen und Methoden. Zusaetzlich zur abstrakten Klasse
        werden beispielsweise der Gradient der Zielfunktion und
        ein Startpunkt benoetigt.

        :param z: Zielfunktion
        :param startpunkt: Beginn der Optimierung, Format: [x1, x2, .... xn]
        """

        optimierungsaufgabe.__init__(self, z) # Initialisierung der abst. Klasse
        self.startpunkt = startpunkt

    def print_startpunkt(self):
        """
        Beispiel fuer Methode einer Klasse
        """

        print("Startpunkt", self.startpunkt) # Verwendung von Variablen

# Test mit Zielfunktion Beispiel
def z(x):
    return x*2

optimierung_Uebung2 = gradientenbasierte_optimierung(z, [3, 2])
optimierung_Uebung2.print_startpunkt()