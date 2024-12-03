/*EMPRESA DE DISEÑO DE PROTOTIPOS*/

CREATE OR REPLACE DATABASE PROTOTIPOS;
USE PROTOTIPOS;

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


