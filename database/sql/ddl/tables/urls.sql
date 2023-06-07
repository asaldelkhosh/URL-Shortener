CREATE TABLE urls (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    url        VARCHAR(1024) NOT NULL,
    short      VARCHAR(1024) NOT NULL,
    count      INTEGER,
    created_at TEXT,
    updated_at TEXT
);
