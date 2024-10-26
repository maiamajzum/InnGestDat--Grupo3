-- Poblar la tabla departamento
INSERT INTO Turnero.Departamento (Nombre_Departamento) VALUES ('Clínica Médica'); -- 1
INSERT INTO Turnero.Departamento (Nombre_Departamento) VALUES ('Cirugía'); -- 2
INSERT INTO Turnero.Departamento (Nombre_Departamento) VALUES ('Guardia'); -- 3
INSERT INTO Turnero.Departamento (Nombre_Departamento) VALUES ('Salud Mental'); -- 4
INSERT INTO Turnero.Departamento (Nombre_Departamento) VALUES ('Diagnóstico por Imágenes'); -- 5
INSERT INTO Turnero.Departamento (Nombre_Departamento) VALUES ('Laboratorio'); -- 6

-- Poblar la tabla especialidad
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Medicina Física y Rehabilitación',1); -- 1
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Clínica Médica',1); -- 2
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Terapia Intensiva',1); -- 3
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Infectología',1); -- 4
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Pediatría',1); -- 5
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Neurología',1); -- 6
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Ortopedia y Traumatología',1); -- 7
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Reumatología',1); -- 8
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Cardiología',1); -- 9
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Neumonología',1); -- 10
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Psiquiatría',4); -- 11
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Urología',1); -- 12
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Sexología',1); -- 13
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Cirugía Cardiovascular',2); -- 14
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Cirugía General',2); -- 15
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Neurocirugía',2); -- 16
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Oftalmología',1); -- 17
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Otorrinolaringología',1); -- 18
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Dermatología',1); -- 19
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Gastroenterología',1); -- 20
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Endocrinología',1); -- 21
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Hematología',6); -- 22
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Microbiología',6); -- 23
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Bioquímica',6); -- 24
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Inmunología',6); -- 25
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Parasitología',6); -- 26
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Radiología',5); -- 27
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Ecografía',5); -- 28
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Tomografía',5); -- 29
INSERT INTO Turnero.Especialidad (Nombre_Especialidad, Departamento_id_departamento) VALUES ('Resonancia Magnética',5); -- 30

-- Poblar la tabla horario
INSERT INTO Turnero.Horario (hora_inicio, hora_fin) VALUES (0,4); -- 1
INSERT INTO Turnero.Horario (hora_inicio, hora_fin) VALUES (4,8); -- 2
INSERT INTO Turnero.Horario (hora_inicio, hora_fin) VALUES (8,12); -- 3
INSERT INTO Turnero.Horario (hora_inicio, hora_fin) VALUES (12,16); -- 4
INSERT INTO Turnero.Horario (hora_inicio, hora_fin) VALUES (16,20); -- 5
INSERT INTO Turnero.Horario (hora_inicio, hora_fin) VALUES (20,0); -- 6

-- Poblar la tabla medico
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Mario', 'Sánchez', 1); -- 1
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Juan', 'Pérez', 2); -- 2
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('María', 'González', 3); -- 3
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Carlos', 'Gómez', 4); -- 4
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Ana', 'Martínez', 5); -- 5
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Pedro', 'Rodríguez', 6); -- 6
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Marta', 'López', 1); -- 7
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Jorge', 'Fernández', 2); -- 8
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Silvia', 'Díaz', 3); -- 9
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Luis', 'Alvarez', 4); -- 10
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Laura', 'Romero', 5); -- 11
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Fernando', 'Suárez', 6); -- 12
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Gabriela', 'Torres', 1); -- 13
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Ricardo', 'Giménez', 2); -- 14
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Verónica', 'Paz', 3); -- 15
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Hernán', 'Ríos', 4); -- 16
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Cecilia', 'Vega', 5); -- 17
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Gustavo', 'Luna', 6); -- 18
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Dario', 'Medina', 1); -- 19
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Carlos', 'Leguizamon', 2); -- 20
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Erika', 'Costa', 3); -- 21
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Ariel', 'Fernandez', 4); -- 22
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Alicia', 'Martínez', 5); -- 23
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Pablo', 'Casanova', 6); -- 24
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Soledad', 'Clementi', 1); -- 25
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Martin', 'Correa', 2); -- 26
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Sebastian', 'Alonso', 3); -- 27
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Enzo', 'Fernandez', 4); -- 28
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Leticia', 'Ramirez', 5); -- 29
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Omar', 'Riachi', 6); -- 30
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Melina', 'Guerrido', 1); -- 31
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Agustina', 'Olguin', 2); -- 32
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Carolina', 'Medina', 3); -- 33
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Hernán', 'Casado', 4); -- 34
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Nicolas', 'Vazquez', 5); -- 35
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Juan Pablo', 'Luna', 6); -- 36
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Marisol', 'Campos', 1); -- 37
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Maria Jose', 'Accordia', 2); -- 38
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Damian', 'Villareal', 3); -- 39
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Gisela', 'Gómez', 4); -- 40
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Noelia', 'Ojeda', 5); -- 41
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Myriam', 'Ghirardi', 6); -- 42
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Diego', 'Moltoni', 1); -- 43
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Veronica', 'Loria', 2); -- 44
INSERT INTO Turnero.Medico (Nombre, Apellido, Horario_id_Horario) VALUES ('Esteban', 'Acosta', 3); -- 45

-- Poblar la tabla medico_has_especialidad
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (1,1); -- 1
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (1,2); -- 2
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (2,4); -- 3
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (2,5); -- 4
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (3,7); -- 5
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (3,8); -- 6
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (4,10); -- 7
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (4,11); -- 8
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (5,13); -- 9
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (5,14); -- 10
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (6,16); -- 11
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (6,17); -- 12
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (7,19); -- 13
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (7,20); -- 14
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (8,22); -- 15
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (8,23); -- 16
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (9,25); -- 17
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (9,26); -- 18
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (10,28); -- 19
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (10,29); -- 20
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (11,1); -- 21
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (11,2); -- 22
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (12,4); -- 23
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (12,5); -- 24
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (13,7); -- 25
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (13,8); -- 26
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (14,10); -- 27
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (14,11); -- 28
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (15,13); -- 29
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (15,14); -- 30
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (16,16); -- 31
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (16,17); -- 32
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (17,19); -- 33
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (17,20); -- 34
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (18,22); -- 35
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (18,23); -- 36
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (19,1); -- 37
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (19,2); -- 38
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (20,3); -- 39
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (20,4); -- 40
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (21,5); -- 41
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (21,6); -- 42
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (22,7); -- 43
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (22,8); -- 44
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (23,9); -- 45
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (23,10); -- 46
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (24,11); -- 47
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (24,12); -- 48
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (25,13); -- 49
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (25,14); -- 50
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (26,15); -- 51
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (26,16); -- 52
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (27,17); -- 53
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (27,18); -- 54
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (28,19); -- 55
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (28,20); -- 56
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (29,21); -- 57
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (29,22); -- 58
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (30,23); -- 59
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (30,24); -- 60
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (31,25); -- 61
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (31,26); -- 62
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (32,27); -- 63
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (32,28); -- 64
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (33,29); -- 65
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (33,30); -- 66
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (34,1); -- 67
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (34,2); -- 68
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (35,3); -- 69
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (35,4); -- 70
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (36,5); -- 71
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (36,6); -- 72
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (37,7); -- 73
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (37,8); -- 74
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (38,9); -- 75
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (38,10); -- 76
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (39,11); -- 77
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (39,12); -- 78
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (40,13); -- 79
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (40,14); -- 80
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (41,15); -- 81
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (41,16); -- 82
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (42,17); -- 83
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (42,18); -- 84
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (43,19); -- 85
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (43,20); -- 86
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (44,21); -- 87
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (44,22); -- 88
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (45,23); -- 89
INSERT INTO Turnero.Medico_has_Especialidad (Medico_id_medico, Especialidad_id_especialidad) VALUES (45,24); -- 90


-- Poblar la tabla paciente
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Lucía', 'Gómez', 12345678); -- 1
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Martín', 'Pérez', 25456789); -- 2
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Sofía', 'Martínez', 34567890); -- 3
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Mateo', 'González', 45678901); -- 4
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Valentina', 'Rodríguez', 56789012); -- 5
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Benjamín', 'López', 67890123); -- 6
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Isabella', 'Fernández', 78901234); -- 7
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Tomás', 'Díaz', 89012345); -- 8
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Olivia', 'Suárez', 90123456); -- 9
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Agustín', 'Torres', 12345679); -- 10
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Emma', 'Giménez', 23456789); -- 11
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Dylan', 'Paz', 34567090); -- 12
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Mía', 'Ríos', 45675891); -- 13
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Lucas', 'Vega', 56787012); -- 14
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Renata', 'Luna', 67890923); -- 15
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Joaquín', 'Alvarez', 75901234); -- 16
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Emilia', 'Romero', 89012545); -- 17
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Bautista', 'Martínez', 90153456); -- 18
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Catalina', 'González', 45345678); -- 19
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Felipe', 'Pérez', 23756789); -- 20
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Mario', 'Abdala', 28740858); -- 21
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Luisa', 'Aguero', 29651813); -- 22
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Carlos', 'Aguilera', 40184442); -- 23
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Adriana', 'Alfonso', 26104249); -- 24
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Eugenia', 'Aleu', 32997809); -- 25
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Daniela', 'Algan', 35794895); -- 26
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Pablo', 'Barlesi', 27589790); -- 27
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Ariel', 'Barnech', 38354542); -- 28
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Gustavo', 'Barrios', 34180521); -- 29
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Erik', 'Baum', 24021740); -- 30
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Sergio', 'Barreto', 17999076); -- 31
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Gabriel', 'Barreiro', 11765715); -- 32
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Marcela', 'Blasco', 26104497); -- 33
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Carolina', 'Cabral', 25351240); -- 34
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Juana', 'Caceres', 27848583); -- 35
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Gerardo', 'Caci', 22539579); -- 36
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Amadeo', 'Caballero', 33784897); -- 37
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Valeria', 'Bustos', 10576347); -- 38
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Luis', 'Calcagno', 24500499); -- 39
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Florencia', 'Camejo', 25731636); -- 40
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Carlos', 'Capasso', 25735636); -- 41
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Vanina', 'Capurro', 21508387); -- 42
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Leonardo', 'Capittini', 26563332); -- 43
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Carmen', 'Conde', 23775426); -- 44
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Ruth', 'Cruz', 26563177); -- 45
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Juana', 'De Luca', 30939823); -- 46
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Cecilia', 'De Tomaso', 25686951); -- 47
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Paula', 'Delgado', 37230172); -- 48
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Graciela', 'Dobal', 21340242); -- 49
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Adelina', 'Dobler', 31761452); -- 50
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Beatriz', 'Evalan', 35722250); -- 51
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Omar', 'Elia', 28273738); -- 52
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Marina', 'Dutroc', 36072543); -- 53
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Cynthia', 'Ganz', 23775279); -- 54
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Silvina', 'Gallardo', 30647460); -- 55
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Adriana', 'Galafassi', 30074549); -- 56
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('David', 'Juncos', 33115290); -- 57
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Marcela', 'Leiva', 23115592); -- 58
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Teresa', 'Lombardi', 35942988); -- 59
INSERT INTO Turnero.Paciente (Nombre, Apellido, DNI) VALUES ('Ruben', 'Mansilla', 36917329); -- 60


-- Poblar la tabla turno 
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-01', '10:00', 12345678, 1); -- 1
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-03', '08:00', 25456789, 2); -- 2
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-02', '12:00', 34567890, 3); -- 3
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-04', '15:00', 45678901, 4); -- 4
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-05', '16:00', 56789012, 5); -- 5
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-06', '18:00', 67890123, 6); -- 6
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-07', '20:00', 28740858, 7); -- 7
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-08', '10:00', 89012345, 8); -- 8
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-09', '08:00', 90123456, 9); -- 9
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-10', '12:00', 12345679, 10); -- 10
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-11', '15:00', 23456789, 11); -- 11
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-12', '16:00', 34567090, 12); -- 12
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-13', '18:00', 21340242, 13); -- 13
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-14', '20:00', 56787012, 14); -- 14
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-15', '10:00', 67890923, 15); -- 15
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-16', '08:00', 75901234, 16); -- 16
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-17', '12:00', 89012545, 17); -- 17
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-18', '15:00', 90153456, 18); -- 18
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-19', '16:00', 45345678, 19); -- 19
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-20', '18:00', 23756789, 20); -- 20
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-01', '08:00', 28740858, 1); -- 21
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-03', '09:00', 29651813, 2); -- 22
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-02', '10:00', 40184442, 3); -- 23
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-04', '11:00', 26104249, 4); -- 24
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-05', '12:00', 32997809, 5); -- 25
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-06', '13:00', 35794895, 6); -- 26
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-07', '14:00', 27589790, 7); -- 27
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-08', '15:00', 38354542, 8); -- 28
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-09', '16:00', 34180521, 9); -- 29
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-10', '17:00', 24021740, 10); -- 30
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-11', '18:00', 17999076, 11); -- 31
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-12', '19:00', 11765715, 12); -- 32
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-13', '20:00', 26104497, 13); -- 33
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-14', '08:00', 25351240, 14); -- 34
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-15', '09:00', 27848583, 15); -- 35
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-16', '08:00', 22539579, 16); -- 36
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-17', '10:00', 33784897, 17); -- 37
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-18', '11:00', 10576347, 18); -- 38
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-19', '12:00', 24983684, 19); -- 39
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-20', '13:00', 21890871, 20); -- 40
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-21', '14:00', 45678912, 1); -- 41
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-22', '15:00', 56789012, 2); -- 42
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-23', '16:00', 67890123, 3); -- 43
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-24', '17:00', 78901234, 4); -- 44
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-25', '18:00', 89012345, 5); -- 45
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-26', '19:00', 90123456, 6); -- 46
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-27', '20:00', 12345678, 7); -- 47
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-28', '10:00', 23456789, 8); -- 48
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-29', '08:00', 34567890, 9); -- 49
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-30', '12:00', 45678901, 10); -- 50
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-31', '15:00', 56789012, 11); -- 51
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-08-01', '16:00', 67890123, 12); -- 52
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-08-02', '18:00', 78901234, 13); -- 53
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-08-03', '20:00', 89012345, 14); -- 54
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-08-04', '10:00', 90123456, 15); -- 55
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-08-05', '08:00', 12345678, 16); -- 56
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-08-06', '12:00', 23456789, 17); -- 57
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-18', '12:00', 23115592, 28); -- 58
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-19', '08:00', 35942988, 29); -- 59
INSERT INTO Turnero.Turno (fecha_turno, hora_turno, Paciente_DNI, Especialidad_id_especialidad) VALUES ('2024-07-20', '14:00', 36917329, 30); -- 60



