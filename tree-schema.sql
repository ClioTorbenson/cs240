-- Tree database
-- Version 1.0
-- Date 2/23/2026
-- Sidra Wernli and Clio Torbenson

DROP DATABASE IF EXISTS tree;
CREATE DATABASE tree;
USE tree;

CREATE TABLE tree (
	tree_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	species VARCHAR(100) NOT NULL,
	mature_size VARCHAR(10) NOT NULL,
	functional_type VARCHAR(100) NOT NULL,
	diameter DECIMAL(2, 1) NOT NULL,
	tree_condition CHAR(10) NOT NULL,
	date_inventoried DATETIME NOT NULL,
	PRIMARY KEY (tree_id)
);

CREATE TABLE bird (
	bird_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	bird_name VARCHAR(100) NOT NULL,
	species VARCHAR(100) NOT NULL,
	PRIMARY KEY (bird_id)
);

CREATE TABLE nests_in (
	bird_id INT UNSIGNED,
	tree_id INT UNSIGNED,
	yearCreated SMALLINT UNSIGNED,
	FOREIGN KEY (bird_id) 
		REFERENCES bird(bird_id)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
	FOREIGN KEY (tree_id) 
		REFERENCES tree(tree_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE site (
	site_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	size VARCHAR(10) NOT NULL,
	width TINYINT UNSIGNED NOT NULL,
	wires VARCHAR(50) NOT NULL,
	improvement VARCHAR(20),
	site_type VARCHAR(50) NOT NULL,
	PRIMARY KEY (site_id)
);

CREATE TABLE location (
	address VARCHAR(100) NOT NULL,
	neighborhood VARCHAR(50) NOT NULL,
	PRIMARY KEY (address, neighborhood)
);