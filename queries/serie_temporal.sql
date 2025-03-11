SELECT Datetime, Voc, Voce, FF, Isc, Pmax, Vmpp, Impp, Vmin, Imin, Analizador
FROM Parameters_Grupo_Solar
WHERE Datetime BETWEEN '{start_date}' AND '{end_date}'
AND Analizador IN ({analizadores});
