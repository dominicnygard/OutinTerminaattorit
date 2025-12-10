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
  journal TEXT,
  volume TEXT,
  number TEXT,
  pages TEXT,
  month TEXT,
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
  howpublished TEXT,
  address TEXT,
  editor TEXT,
  volume TEXT,
  number TEXT,
  series TEXT,
  organization TEXT,
  month TEXT,
  notes TEXT
);

CREATE TABLE conferences (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  booktitle TEXT,
  editor TEXT,
  volume TEXT,
  number TEXT,
  series TEXT,
  pages TEXT,
  address TEXT,
  month TEXT,
  organization TEXT,
  publisher TEXT,
  notes TEXT
);

CREATE TABLE inbooks (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  booktitle TEXT,
  publisher TEXT,
  editor TEXT,
  volume TEXT,
  number TEXT,
  series TEXT,
  address TEXT,
  edition TEXT,
  month TEXT,
  pages TEXT,
  notes TEXT
);

CREATE TABLE incollections (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  booktitle TEXT,
  publisher TEXT,
  editor TEXT,
  volume TEXT,
  number TEXT,
  series TEXT,
  pages TEXT,
  address TEXT,
  month TEXT
);

CREATE TABLE inproceedings (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  booktitle TEXT,
  editor TEXT,
  volume TEXT,
  number TEXT,
  series TEXT,
  pages TEXT,
  address TEXT,
  month TEXT,
  organization TEXT,
  publisher TEXT
);

CREATE TABLE manuals (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  organization TEXT,
  address TEXT,
  edition TEXT,
  month TEXT,
  notes TEXT
);

CREATE TABLE mastertheseses (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  school TEXT,
  address TEXT,
  month TEXT,
  notes TEXT
);

CREATE TABLE phdtheseses (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  school TEXT,
  address TEXT,
  month TEXT,
  notes TEXT
);

CREATE TABLE proceedings (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  editor TEXT,
  volume TEXT,
  number TEXT,
  series TEXT,
  address TEXT,
  month TEXT,
  publisher TEXT
);

CREATE TABLE techreports (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  institution TEXT,
  number TEXT
);

CREATE TABLE unpublisheds (
  id SERIAL PRIMARY KEY,
  general_id INTEGER REFERENCES items,
  institution TEXT,
  number TEXT
);