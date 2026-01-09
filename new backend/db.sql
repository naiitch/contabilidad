-- sudo mysql -u root -p

CREATE DATABASE contabilidad;

USE contabilidad;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(100)
);
CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    type ENUM('ingreso', 'gasto'),
    usuario_id INT
);
CREATE TABLE ingresos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cantidad DECIMAL(10,2),
    date DATE,
    nota TEXT,
    categoria_id INT,
    usuario_id INT
);
CREATE TABLE gastos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cantidad DECIMAL(10,2),
    date DATE,
    nota TEXT,
    categoria_id INT,
    usuario_id INT
);
CREATE TABLE presupuestos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cantidad DECIMAL(10,2),
    periodo ENUM('semanal', 'mensual'),
    usuario_id INT
);
