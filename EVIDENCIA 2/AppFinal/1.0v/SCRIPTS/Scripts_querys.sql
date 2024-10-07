--Create
INSERT INTO usuario (username, password, email) VALUES ('nuevo_usuario', 'mi_contraseña', 'nuevo@ejemplo.com'); --Insertar un nuevo usuario

INSERT INTO accesos (fechaIngreso, usuarioLogueado) VALUES (NOW(), (SELECT ID FROM usuario WHERE username = 'nuevo_usuario')); --Insertar acceso (no lo usaría manual, porque pierde la gracia)

--Read
SELECT * FROM usuario; --El mejor amigo del debugger, selecciona todo
SELECT * FROM accesos;

SELECT * FROM usuario WHERE ID = 1;  -- Cambiar el 1 por el ID del usuario que deseas BUSCAR
SELECT * FROM accesos WHERE ID = 1;

--Update
UPDATE usuario 
SET username = 'usuario_actualizado', password = 'nueva_contraseña', email = 'actualizado@ejemplo.com' 
WHERE ID = 1;  -- Cambia 1 por el ID del usuario que deseas actualizar

--Delete
DELETE FROM usuario WHERE ID = 1;  -- Cambia el 1 por el ID del usuario que deseas BORRAR


-- ACCESOS de USUARIOS
SELECT a.ID, a.fechaIngreso, a.fechaSalida, u.username 
FROM accesos a
JOIN usuario u ON a.usuarioLogueado = u.ID;




	
