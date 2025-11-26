CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  type TEXT
);

CREATE TABLE articles (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  author TEXT,
  title TEXT,
  year TEXT,
  month TEXT,
  journal TEXT,
  volume INTEGER,
  number INTEGER,
  pages INTEGER,
  notes TEXT
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  author TEXT,
  title TEXT,
  year TEXT,
  publisher TEXT,
  address TEXT
);

CREATE TABLE booklets (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  author TEXT,
  title TEXT,
  year TEXT,
  month TEXT,
  address TEXT,
  notes TEXT,
  howpublished TEXT,
  editor TEXT
);

CREATE TABLE conferences (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  author TEXT,
  title TEXT,
  year TEXT,
  month TEXT,
  booktitle TEXT,
  publisher TEXT,
  address TEXT,
  pages INTEGER,
  notes TEXT,
  editor TEXT,
  organization TEXT
);

CREATE TABLE inbooks (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  author TEXT,
  title TEXT,
  year TEXT,
  booktitle TEXT,
  publisher TEXT,
  pages INTEGER,
  notes TEXT,
  editor TEXT,
  edition INTEGER
);

CREATE TABLE incolletions (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  author TEXT,
  title TEXT,
  year TEXT,
  month TEXT,
  booktitle TEXT,
  publisher TEXT,
  address TEXT,
  series TEXT,
  volume INTEGER,
  number INTEGER,
  pages INTEGER,
  editor TEXT
);

CREATE TABLE inproceedings (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  author TEXT,
  title TEXT,
  year TEXT,
  month TEXT,
  booktitle TEXT,
  publisher TEXT,
  address TEXT,
  series TEXT,
  volume INTEGER,
  number INTEGER,
  pages INTEGER,
  editor TEXT,
  organization TEXT
);

CREATE TABLE manuals (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  author TEXT,
  title TEXT,
  year TEXT,
  month TEXT,
  address TEXT,
  notes TEXT,
  organization TEXT,
  edition TEXT
);

CREATE TABLE mastertheseses (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  author TEXT,
  title TEXT,
  year TEXT,
  month TEXT,
  address TEXT,
  notes TEXT,
  school TEXT,
  type TEXT
);

CREATE TABLE miscs (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  author TEXT,
  title TEXT,
  year TEXT
);

CREATE TABLE phdtheseses (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  author TEXT,
  title TEXT,
  year TEXT,
  month TEXT,
  address TEXT,
  notes TEXT,
  school TEXT,
  type TEXT
);

CREATE TABLE proceedings (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  author TEXT,
  title TEXT,
  year TEXT,
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
  author TEXT,
  title TEXT,
  year TEXT,
  institution TEXT,
  number INTEGER
);

CREATE TABLE unpublished (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  author TEXT,
  title TEXT,
  year TEXT,
  institution TEXT
);