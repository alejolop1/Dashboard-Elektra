SELECT 
    Datetime, 
    Voc, 
    Voce, 
    FF, 
    Isc, 
    Pmax, 
    Vmpp, 
    Impp, 
    Vmin, 
    Imin.
    Analizador
FROM 
    Parameters_Grupo_Solar 
WHERE 
    Analizador = '{analizador}'
ORDER BY 
    Datetime;