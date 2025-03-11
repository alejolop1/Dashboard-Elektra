SELECT Voc, Isc, Analizador
FROM Parameters_Grupo_Solar
WHERE Datetime BETWEEN '{start_date}' AND '{end_date}'
AND Analizador IN ({analizadores});