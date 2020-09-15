CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    account_id INTEGER REFERENCES accounts,
    topic TEXT,
    content TEXT,
    posted_at TIMESTAMP,
    posted_by TEXT
);
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages,
    account_id INTEGER REFERENCES accounts,
    content TEXT,
    posted_at TIMESTAMP,
    posted_by TEXT
);
CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages,
    comment_id INTEGER REFERENCES comments,
    account_id INTEGER REFERENCES accounts
);
