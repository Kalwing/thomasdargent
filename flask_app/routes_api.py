from flask import Blueprint, render_template, url_for, request, current_app, jsonify
import datetime
import json
import random
from pathlib import Path

bp = Blueprint("api", __name__)

@bp.route('/', methods=['GET'])
def home():
    return "", 200

@bp.route("/error_brevo", methods=["GET", "POST"])
def brevo_error():
    return {"code": "error_access"}, 400


@bp.route("/success_brevo", methods=["GET", "POST"])
def brevo_success():
    prefix = "brevo/"
    return render_template(f"{prefix}brevo_success_2.html"), 200


# QUOTE GIVER
def date_match(date: datetime.date, pattern: str) -> bool:
    """
    pattern: must follow this structure:
        "D dd/mm/YYYY" with: D the day of the week (monday=0, sunday=6)
                             dd the day of the month on two number
                             mm the month on two number
                             YYYY the year on 4 number
    if any element is equal to a single star, then all values matches for it
    """
    weekday, _date = pattern.split()
    dd, mm, yyyy = _date.split('/')
    match = True
    if weekday != '*':
        match = match and (date.weekday() == int(weekday))
    if match and dd != '*':
        match = match and (date.strftime("%d") == dd)
    if match and mm != '*':
        match = match and (date.strftime("%m") == mm)
    if match and yyyy != '*':
        match = match and (date.strftime("%Y") == yyyy)
    return match

def pick_quote(tag: str=None, date_freq: float=0.25):
    if tag is not None:
        # Decide if we have a tag or if we check on date related quote before reading a file for nothing
        test_date = tag == "date"  and random.random() < date_freq
        if test_date or tag != "date":
            try:  # Try if the tag is correct
                path = Path(current_app.static_folder)/'data/quotes_sorted.json'
                with open(path, 'r') as file:
                    quotes = json.loads(file.read())

                if test_date:
                    potential_quotes = []
                    today = datetime.date.today()
                    for quote in quotes[tag]:
                        if date_match(today, quote["date"]):
                            potential_quotes.append(quote)
                    if potential_quotes:
                        return random.choice(potential_quotes)
                elif not test_date:
                    return random.choice(quotes[tag])
                # Nothing was selected, return an unsorted quote
            except KeyError as e:  # tag incorrect
                return None
    path = Path(current_app.static_folder)/'data/quotes.json'
    with open(path, 'r') as file:
        return random.choice(json.loads(file.read()))

@bp.route("/get_quote", methods=["GET"])
@bp.route("/get_quote/<tag>", methods=["GET"])
def quote_giver(tag: str=None):
    _json = pick_quote(tag)
    if _json is None:
        return "Wrong tag", 404
    response = jsonify(_json)
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response