CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    account_id INTEGER REFERENCES accounts,
    topic TEXT UNIQUE,
    content TEXT,
    posted_at TIMESTAMP,
    posted_by TEXT
);
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    content TEXT,
    message_id INTEGER REFERENCES messages ON DELETE CASCADE
);
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages ON DELETE CASCADE,
    account_id INTEGER REFERENCES accounts,
    content TEXT,
    posted_at TIMESTAMP,
    posted_by TEXT
);
CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages  ON DELETE CASCADE,
    account_id INTEGER REFERENCES accounts
);
CREATE TABLE blocks (
    id SERIAL PRIMARY KEY,
    blocking TEXT,
    blocked TEXT
);
