from flask import Blueprint, render_template, url_for, request, current_app, jsonify
import json
import random
from pathlib import Path

bp = Blueprint("api", __name__)


@bp.route("/error_brevo", methods=["GET", "POST"])
def brevo_error():
    return {"code": "error_access"}, 400


@bp.route("/success_brevo", methods=["GET", "POST"])
def brevo_success():
    prefix = "brevo/"
    return render_template(f"{prefix}brevo_success_2.html"), 200


# QUOTE GIVER
def pick_quote(tag=None):
    if tag is None:
        path = Path(current_app.static_folder)/'data/quotes.json'
        with open(path, 'r') as file:
            return random.choice(json.loads(file.read()))
    else:
        path = Path(current_app.static_folder)/'data/quotes_sorted.json'
        with open(path, 'r') as file:
            quotes = json.loads(file.read())
            return random.choice(quotes[tag])

@bp.route("/get_quote", methods=["GET"])
@bp.route("/get_quote/<tag>", methods=["GET"])
def quote_giver(tag=None):
    response = jsonify(pick_quote(tag))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response