CREATE DATABASE Evidencia2;
USE Evidencia2;
CREATE TABLE usuario (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    username NVARCHAR(50) NOT NULL,
    password NVARCHAR(50) NOT NULL,
    email NVARCHAR(50) NOT NULL
);

CREATE TABLE accesos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    fechaIngreso DATETIME NOT NULL,
    fechaSalida DATETIME,
    usuarioLogueado INT,
    FOREIGN KEY (usuarioLogueado) REFERENCES usuario(ID) ON DELETE CASCADE
);
