SELECT * FROM paciente; -- Consulta de una sola tabla (mostrando todos los datos)

SELECT id_paciente, DNI FROM paciente; -- Consulta de una sola tabla (mostrando algunas columnas)

SELECT * FROM medico WHERE Horario_id_Horario = 1; -- Consulta de una sola tabla con WHERE

SELECT * FROM turno WHERE Especialidad_id_especialidad = 3 AND hora_turno BETWEEN 10 AND 14; -- Consulta de una sola tabla con WHERE utilizando BETWEEN

SELECT * -- Consulta de una sola tabla con WHERE utilizando LIMIT
FROM medico
WHERE Nombre LIKE 'A%'
LIMIT 3;

SELECT paciente.Nombre -- Consulta de mas de una tabla con INNER JOIN
FROM paciente
INNER JOIN turno ON paciente.DNI = turno.Paciente_DNI
INNER JOIN especialidad ON turno.Especialidad_id_especialidad = especialidad.id_especialidad
WHERE especialidad.Nombre_Especialidad = 'Clínica Médica';


SELECT tt.id_turno, tt.fecha_turno, tt.hora_turno, tp.Apellido, tp.Nombre, tp.DNI, te.Nombre_Especialidad -- Consulta de mas de una tabla con INNER JOIN y filtros
FROM Turnero.Turno tt
INNER JOIN Turnero.Especialidad te 
    ON te.id_especialidad = tt.Especialidad_id_especialidad
INNER JOIN Turnero.Paciente tp 
    ON tp.DNI = tt.Paciente_DNI
ORDER BY tt.fecha_turno, tt.hora_turno, tp.Apellido, tp.Nombre, tp.DNI, te.Nombre_Especialidad;


