CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT, password TEXT, role INTEGER);

CREATE TABLE bands (id SERIAL PRIMARY KEY, name TEXT UNIQUE NOT NULL);

CREATE TABLE reviews (id SERIAL PRIMARY KEY, user_id INTEGER REFERENCES users, band_id INTEGER REFERENCES bands, comment TEXT);

CREATE TABLE info (id SERIAL PRIMARY KEY, band_name TEXT REFERENCES bands(name), info_text TEXT);

CREATE TABLE favourites (id SERIAL PRIMARY KEY, user_id INTEGER REFERENCES users, band_id INTEGER REFERENCES bands);

INSERT INTO bands (name) VALUES ('Queen');
INSERT INTO info (band_name, info_text) VALUES ('Queen', 'Rockin klassikkobändi! Perustettu Englannissa vuonna 1970. Kokoonpanoon kuului laulaja Freddie Mercury, kitaristi Brian May, rumpali Roger Taylor ja basisti John Deacon.');
