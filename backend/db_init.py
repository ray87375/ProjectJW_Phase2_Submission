import sqlite3
import pathlib

# Define paths to the database and schema file
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "coachkat.db"
SCHEMA_PATH = pathlib.Path(__file__).parent / "schema.sql"


def main():
    """Initialize the database by creating tables and adding sample videos."""
    connection = sqlite3.connect(str(DB_PATH))
    
    # Read and execute the SQL schema to create tables
    with open(SCHEMA_PATH, "r", encoding="utf-8") as schema_file:
        connection.executescript(schema_file.read())

    cursor = connection.cursor()
    video_count = cursor.execute("SELECT COUNT(*) FROM videos").fetchone()[0]
    
    
    connection.commit()
    connection.close()
    print(f"Database initialized: {DB_PATH}")


if __name__ == "__main__":
    main()
