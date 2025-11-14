from flask import Flask, jsonify, request, send_from_directory
import sqlite3
import pathlib

# Set up the project directory paths
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "coachkat.db"
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

app = Flask(__name__, static_folder=str(STATIC_DIR))


def get_db_connection():
    """Create a database connection with a 30-second timeout."""
    connection = sqlite3.connect(str(DB_PATH), timeout=30)
    connection.row_factory = sqlite3.Row  # Return rows as dictionaries instead of tuples
    return connection


@app.get("/")
def index():
    """Serve the main HTML page."""
    return send_from_directory(str(TEMPLATES_DIR), "index.html")


@app.get("/api/videos")
def api_videos():
    """Get all videos from the database and return them as JSON."""
    with get_db_connection() as connection:
        rows = connection.execute(
            "SELECT id, title, url, durationSeconds FROM videos ORDER BY id"
        ).fetchall()
    return jsonify([dict(row) for row in rows])


@app.post("/api/contact")
def api_contact():
    """Handle contact form submissions and save messages to the database."""
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()
    
    # Basic validation to ensure all fields are filled and email contains @
    if not name or not email or not message or "@" not in email:
        return jsonify({"ok": False, "error": "Invalid input"}), 400
    
    with get_db_connection() as connection:
        connection.execute(
            "INSERT INTO messages(name, email, message) VALUES(?, ?, ?)",
            (name, email, message)
        )
        connection.commit()
    
    return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(debug=True)
