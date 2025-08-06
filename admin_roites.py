from flask import Blueprint, jsonify
from utils.database import get_db

admin_api = Blueprint('admin', __name__)

@admin_api.route("/dashboard", methods=["GET"])
def dashboard():
    db = get_db()
    open_tickets = db.execute("SELECT * FROM complaints WHERE status != 'Resolved'").fetchall()
    return jsonify([dict(row) for row in open_tickets])
