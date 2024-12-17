/*EMPRESA DE DISEÑO DE PROTOTIPOS*/

CREATE OR REPLACE DATABASE PROTOTIPOS;
USE PROTOTIPOS;

CREATE OR REPLACE TABLE gestores(
	ID INT AUTO_INCREMENT,
	DNI_NIF CHAR(9)unique not null,
	Nombre VARCHAR(20)not null,
	Apellidos VARCHAR(40)not null,
	email varchar(60)unique not null,
	contraseña varchar(10)not null,
	PRIMARY KEY(ID)
);
create or replace table telefono_gestores(	
	id_gestores int,
	telefono_gestores char(9),
	primary key(id_gestores,telefono_gestores),
	constraint tlf_gestores foreign key (id_gestores)
		references gestores(id)
		on delete cascade
);

CREATE OR REPLACE TABLE empleados(
	ID INT AUTO_INCREMENT,
	DNI CHAR(9),
	Nombre VARCHAR(20),
	Titulacion VARCHAR(20),
	email varchar(60)unique,
	Años_experiencia TINYINT UNSIGNED,
	tipo_via enum('plaza', 'avenida', 'calle'),
	nombre_via varchar(30),
	codigo_postal char(6),
	localidad varchar(30),
	provincia varchar(30),
	PRIMARY KEY(ID),
	UNIQUE(DNI)
);

describe empleados ;
INSERT INTO empleados (dni, nombre, titulacion, email, años_experiencia, tipo_via, nombre_via, codigo_postal, localidad, provincia)
VALUES ('11117890C', 'Luis Fernández', 'Arquitecto', 'luis.fernandez1@example.com', 3, 'plaza', 'Avenida de la Paz', '28003', 'Madrid', 'Madrid');


create or replace table telefono_empleados(	
	id_empleado int,
	telefono_emp char(9),
	primary key(id_empleado,telefono_emp),
	constraint tlf_emlpe foreign key (id_empleado)
		references empleados(id)
		on delete cascade
);

CREATE OR REPLACE TABLE prototipos(
	id INT AUTO_INCREMENT,
	id_proto_rel INT,
	Nombre VARCHAR(20)unique,
	Descripción VARCHAR(200),
	Fecha_inicio DATE,
	Fecha_fin DATE,
	Presupuesto FLOAT(10,2) UNSIGNED,
	Horas_est INT(6),
	PRIMARY KEY(id),
	CONSTRAINT rel FOREIGN KEY(id_proto_rel)
		REFERENCES prototipos(id)				
		ON DELETE set null,
		-- Si se borra un proyecto no desaparecen sus relacionados
	CONSTRAINT fecha CHECK (Fecha_fin > Fecha_inicio),
	CONSTRAINT max_horas CHECK (Horas_est >= 30)
);

CREATE OR REPLACE TABLE gastos(
	id INT AUTO_INCREMENT,
	id_emp INT,
	id_proto INT,
	Descripcion VARCHAR(200),
	Fecha DATE,
	Importe FLOAT(7,2) UNSIGNED,
	Tipo VARCHAR(20),
	PRIMARY KEY(id),
	CONSTRAINT FKemp FOREIGN KEY(id_emp)
		REFERENCES empleados(id)		
		ON DELETE cascade,
	CONSTRAINT FKproto FOREIGN KEY(id_proto)
		REFERENCES prototipos(id)
		ON DELETE CASCADE,		
	CONSTRAINT lim_gasto CHECK (Importe <= 20000)
);

CREATE OR REPLACE TABLE etapas(
	id INT AUTO_INCREMENT,
	id_proto INT,	
	Nombre VARCHAR(20),
	Fecha_inicio DATE,
	Fecha_fin DATE,
	Estado ENUM ('En desarrollo', 'Finalizada'),
	PRIMARY KEY(id),
	CONSTRAINT FKproy2 FOREIGN KEY(id_proto)
		REFERENCES prototipos(id)		
		ON DELETE CASCADE	
);

CREATE OR REPLACE TABLE recursos(
	id INT AUTO_INCREMENT,
	Nombre VARCHAR(20),
	Descripción VARCHAR(200),
	Tipo VARCHAR(20),
	PRIMARY KEY(id)
);

CREATE OR REPLACE TABLE asigna_recurso(	
	id_etapa INT,
	id_recu INT,
	PRIMARY KEY(id_etapa,id_recu),
	CONSTRAINT FKasig_etapa FOREIGN KEY(id_etapa)
		REFERENCES etapas(id)		
		ON DELETE CASCADE,
	CONSTRAINT FKasig_rec FOREIGN KEY(id_recu)
		REFERENCES recursos(id)		
		ON DELETE CASCADE 		
);


/*Por la propiedad de integridad referencial
 * se han de borrar en orden inverso al
 * de creación

DROP TABLE asigna_recurso, 
recursos,
etapas,
gastos,
prototipos,
telefono_empleados,
empleados;
*/

INSERT INTO empleados (DNI, Nombre, Titulacion, email, Años_experiencia, tipo_via, nombre_via, codigo_postal, localidad, provincia) VALUES
('12345678A', 'Juan Pérez', 'Ingeniero', 'juan.perez@example.com', 5, 'calle', 'Calle Mayor', '28001', 'Madrid', 'Madrid'),
('23456789B', 'Ana Gómez', 'Diseñadora', 'ana.gomez@example.com', 3, 'avenida', 'Avenida de la Paz', '28002', 'Madrid', 'Madrid'),
('34567890C', 'Luis Fernández', 'Arquitecto', 'luis.fernandez@example.com', 8, 'plaza', 'Plaza de España', '28003', 'Madrid', 'Madrid'),
('45678901D', 'María López', 'Ingeniera', 'maria.lopez@example.com', 2, 'calle', 'Calle Gran Vía', '28004', 'Madrid', 'Madrid'),
('56789012E', 'Pedro Torres', 'Diseñador', 'pedro.torres@example.com', 6, 'avenida', 'Avenida de América', '28005', 'Madrid', 'Madrid'),
('67890123F', 'Laura Martínez', 'Arquitecta', 'laura.martinez@example.com', 4, 'plaza', 'Plaza Cibeles', '28006', 'Madrid', 'Madrid'),
('78901234G', 'Sergio Ruiz', 'Ingeniero', 'sergio.ruiz@example.com', 7, 'calle', 'Calle de Vallehermoso', '28007', 'Madrid', 'Madrid'),
('89012345H', 'Cristina Sánchez', 'Diseñadora', 'cristina.sanchez@example.com', 1, 'avenida', 'Avenida de los Reyes', '28008', 'Madrid', 'Madrid'),
('90123456I', 'Javier Martín', 'Arquitecto', 'javier.martin@example.com', 9, 'plaza', 'Plaza de Castilla', '28009', 'Madrid', 'Madrid'),
('01234567J', 'Elena Jiménez', 'Ingeniera', 'elena.jimenez@example.com', 10, 'calle', 'Calle de Serrano', '28010', 'Madrid', 'Madrid');

INSERT INTO telefono_empleados (id_empleado, telefono_emp) VALUES
(1, '612345678'),
(1, '623456789'),
(2, '634567890'),
(3, '645678901'),
(4, '656789012'),
(5, '667890123'),
(6, '678901234'),
(7, '689012345'),
(8, '690123456'),
(9, '601234567');

INSERT INTO prototipos (id_proto_rel, Nombre, Descripción, Fecha_inicio, Fecha_fin, Presupuesto, Horas_est) VALUES
(NULL, 'Prototipo 1', 'Descripción del prototipo 1', '2023-01-01', '2023-03-01', 15000.00, 40),
(NULL, 'Prototipo 2', 'Descripción del prototipo 2', '2023-02-01', '2023-04-01', 20000.00, 50),
(NULL, 'Prototipo 3', 'Descripción del prototipo 3', '2023-03-01', '2023-05-01', 12000.00, 30),
(NULL, 'Prototipo 4', 'Descripción del prototipo 4', '2023-04-01', '2023-06-01', 18000.00, 60),
(NULL, 'Prototipo 5', 'Descripción del prototipo 5', '2023-05-01', '2023-07-01', 25000.00, 70),
(NULL, 'Prototipo 6', 'Descripción del prototipo 6', '2023-06-01', '2023-08-01', 16000.00, 35),
(NULL, 'Prototipo 7', 'Descripción del prototipo 7', '2023-07-01', '2023-09-01', 22000.00, 45),
(NULL, 'Prototipo 8', 'Descripción del prototipo 8', '2023-08-01', '2023-10-01', 11000.00, 35),
(NULL, 'Prototipo 9', 'Descripción del prototipo 9', '2023-09-01', '2023-11-01', 19000.00, 55),
(NULL, 'Prototipo 10', 'Descripción del prototipo 10', '2023-10-01', '2023-12-01', 13000.00, 65);

SELECT id FROM prototipos;


INSERT INTO gastos (id_emp, id_proto, Descripcion, Fecha, Importe, Tipo) VALUES
(1, 1, 'Gastos de materiales', '2023-01-15', 5000.00, 'Material'),
(2, 2, 'Servicios externos', '2023-01-20', 3000.00, 'Servicio'),
(3, 3, 'Gastos de materiales', '2023-02-15', 7000.00, 'Material'),
(4, 4, 'Servicios externos', '2023-02-20', 2000.00, 'Servicio'),
(5, 5, 'Gastos de materiales', '2023-03-15', 4000.00, 'Material'),
(6, 6, 'Servicios externos', '2023-03-20', 1500.00, 'Servicio'),
(7, 7, 'Gastos de materiales', '2023-04-15', 8000.00, 'Material'),
(8, 8, 'Servicios externos', '2023-04-20', 2500.00, 'Servicio'),
(9, 9, 'Gastos de materiales', '2023-05-15', 6000.00, 'Material'),
(10, 10, 'Servicios externos', '2023-05-20', 3500.00, 'Servicio');


INSERT INTO etapas (id_proto, Nombre, Fecha_inicio, Fecha_fin, Estado) VALUES
(1, 'Etapa 1', '2023-01-01', '2023-01-15', 'Finalizada'),
(1, 'Etapa 2', '2023-01-16', '2023-02-01', 'En desarrollo'),
(2, 'Etapa 1', '2023-02-01', '2023-02-15', 'Finalizada'),
(2, 'Etapa 2', '2023-02-16', '2023-03-01', 'En desarrollo'),
(3, 'Etapa 1', '2023-03-01', '2023-03-15', 'Finalizada'),
(3, 'Etapa 2', '2023-03-16', '2023-04-01', 'En desarrollo'),
(4, 'Etapa 1', '2023-04-01', '2023-04-15', 'Finalizada'),
(4, 'Etapa 2', '2023-04-16', '2023-05-01', 'En desarrollo'),
(5, 'Etapa 1', '2023-05-01', '2023-05-15', 'Finalizada'),
(5, 'Etapa 2', '2023-05-16', '2023-06-01', 'En desarrollo');

INSERT INTO recursos (Nombre, Descripción, Tipo) VALUES
('Recurso 1', 'Descripción del recurso 1', 'Material'),
('Recurso 2', 'Descripción del recurso 2', 'Herramienta'),
('Recurso 3', 'Descripción del recurso 3', 'Equipo'),
('Recurso 4', 'Descripción del recurso 4', 'Material'),
('Recurso 5', 'Descripción del recurso 5', 'Herramienta'),
('Recurso 6', 'Descripción del recurso 6', 'Equipo'),
('Recurso 7', 'Descripción del recurso 7', 'Material'),
('Recurso 8', 'Descripción del recurso 8', 'Herramienta'),
('Recurso 9', 'Descripción del recurso 9', 'Equipo'),
('Recurso 10', 'Descripción del recurso 10', 'Material');

INSERT INTO asigna_recurso (id_etapa, id_recu) VALUES
(112, 102,
(155, 220),
(212, 310),
(32, 42),	
(35, 51),
(44, 63),
(52, 74),
(51, 85),
(61, 95),
(712, 190);

INSERT INTO gestores (DNI_NIF, Nombre, Apellidos, email, contraseña) 
VALUES 
('12345678A', 'Juan', 'Pérez García', 'juan.perez@gmail.com', 'abc1234567'),
('87654321B', 'María', 'López Martínez', 'maria.lopez@hotmail.com', 'secure9876'),
('11223344C', 'Carlos', 'González Ruiz', 'carlos.gr@gmail.com', 'pass2023!#');




