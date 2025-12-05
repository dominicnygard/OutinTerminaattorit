CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  type TEXT,
  title TEXT,
  author TEXT,
  year TEXT
);

CREATE TABLE articles (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  month TEXT,
  journal TEXT,
  volume INTEGER,
  number INTEGER,
  pages TEXT,
  notes TEXT
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  publisher TEXT,
  address TEXT
);

CREATE TABLE booklets (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  month TEXT,
  address TEXT,
  notes TEXT,
  howpublished TEXT,
  editor TEXT
);

CREATE TABLE conferences (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  month TEXT,
  booktitle TEXT,
  publisher TEXT,
  address TEXT,
  pages TEXT,
  notes TEXT,
  editor TEXT,
  organization TEXT
);

CREATE TABLE inbooks (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  booktitle TEXT,
  publisher TEXT,
  pages TEXT,
  notes TEXT,
  editor TEXT,
  edition INTEGER
);

CREATE TABLE incolletions (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  month TEXT,
  booktitle TEXT,
  publisher TEXT,
  address TEXT,
  series TEXT,
  volume INTEGER,
  number INTEGER,
  pages TEXT,
  editor TEXT
);

CREATE TABLE inproceedings (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  month TEXT,
  booktitle TEXT,
  publisher TEXT,
  address TEXT,
  series TEXT,
  volume INTEGER,
  number INTEGER,
  pages TEXT,
  editor TEXT,
  organization TEXT
);

CREATE TABLE manuals (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  month TEXT,
  address TEXT,
  notes TEXT,
  organization TEXT,
  edition TEXT
);

CREATE TABLE mastertheseses (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  month TEXT,
  address TEXT,
  notes TEXT,
  school TEXT,
  type TEXT
);

CREATE TABLE miscs (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items
);

CREATE TABLE phdtheseses (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  month TEXT,
  address TEXT,
  notes TEXT,
  school TEXT,
  type TEXT
);

CREATE TABLE proceedings (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  month TEXT,
  publisher TEXT,
  address TEXT,
  series TEXT,
  volume INTEGER,
  number INTEGER,
  editor TEXT
);

CREATE TABLE techreports (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  institution TEXT,
  number INTEGER
);

CREATE TABLE unpublished (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  institution TEXT
);