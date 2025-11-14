-- SQLite Schema
-- Enable foreign key constraints for data integrity
PRAGMA foreign_keys = ON;

-- Table to store training videos
CREATE TABLE IF NOT EXISTS videos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  url TEXT NOT NULL,
  durationSeconds INTEGER DEFAULT 0,
  published_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Table to store contact form messages
CREATE TABLE IF NOT EXISTS messages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  message TEXT NOT NULL,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
