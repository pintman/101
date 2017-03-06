-- Hilfe erhalten
-- sqlite
.help
-- MySQL
-- help;

-- Tabellen erstellen
CREATE TABLE person(id INT PRIMARY KEY, name varchar);

-- Daten in Tabellen eintragen
INSERT INTO person VALUES (1,'Max');
INSERT INTO person VALUES (2,'Peter'), (3, 'Petara');
UPDATE person SET name = 'Petra' WHERE id=3;

-- Tabelle mit Fremdschlüssel erzeugen
CREATE TABLE anschrift (
       id INT PRIMARY KEY,
       strasse VARCHAR(255),
       hausnr VARCHAR(5),
       plz VARCHAR(5)); 
CREATE TABLE person_mit_anschrift(
       id INT PRIMARY KEY,
       name VARCHAR(50),
       anschrift_id INT,
       FOREIGN KEY (anschrift_id) REFERENCES anschrift(id));

-- Tabelle löschen
DROP TABLE anschrift;


