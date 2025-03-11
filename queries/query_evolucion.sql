SELECT Datetime, Voc, Isc, Pmax, Vmpp, Impp, Analizador FROM paneles_solares
WHERE Datetime BETWEEN %s AND %s;