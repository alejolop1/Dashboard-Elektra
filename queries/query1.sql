WITH Analizadores_Unicos AS (
    SELECT DISTINCT Nombre_Analizador 
    FROM Analizadores
),
Ultima_Calibracion AS (
    SELECT 
        a.Nombre_Analizador, 
        a.ID_Analizadores, 
        a.ID_Calibracion, 
        a.ID_Cambio,
        ROW_NUMBER() OVER (PARTITION BY a.Nombre_Analizador ORDER BY a.ID_Calibracion DESC) AS rn
    FROM Analizadores a
)
SELECT 
    au.Nombre_Analizador,
    cp.Fecha_Conexion_Panel,
    ip.Tecnologia,
    ip.Potencia_W,
    ip.Fabricante,
    ip.Referencia_Fab,
    c.Fecha_Calibracion,
    c.Parametros_Calibracion,
    c.Implicados_Calibracion
FROM Analizadores_Unicos au
LEFT JOIN Ultima_Calibracion uc ON au.Nombre_Analizador = uc.Nombre_Analizador AND uc.rn = 1
LEFT JOIN Calibracion c ON uc.ID_Calibracion = c.ID_Calibracion
LEFT JOIN Cambios_Panel cp ON uc.ID_Cambio = cp.ID_Cambio
LEFT JOIN Info_Paneles ip ON cp.ID_Panel = ip.ID_Panel
ORDER BY au.Nombre_Analizador;


