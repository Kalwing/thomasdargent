from flask import Blueprint, render_template, current_app
from .routes_api import pick_quote
bp = Blueprint("pages", __name__)


@bp.route("/brevo_form_example")
def brevo_form_example():
    prefix = "brevo/"
    return render_template(f"{prefix}brevo_form.html")

@bp.route("/brevo_success_example")
def brevo_success_example():
    prefix = "brevo/"
    return render_template(f"{prefix}brevo_success.html")  # test: brevo/....


@bp.route("/brevo_error_example")
def brevo_error_example():
    prefix = "brevo/"
    return render_template(f"{prefix}brevo_error.html")  # test: brevo/....

@bp.route("/mass_effect_quote/")
@bp.route("/mass_effect_quote")
def mass_effect_quote():
    quote = pick_quote(tag='mass_effect')
    for i in range(len(quote["lines"])):
        quote["lines"][i]["quote"] = quote["lines"][i]["quote"].replace('\n', "<br/>")
    prefix = "quotes/"
    return render_template(f"{prefix}mass_effect_quote.html", quote=quote)

@bp.route("/wisdom/")
@bp.route("/wisdom")
def show_quote():
    quote = pick_quote(to_avoid=["political", "mass_effect", "spiderman"])
    for i in range(len(quote["lines"])):
        quote["lines"][i]["quote"] = quote["lines"][i]["quote"].replace('\n', "<br/>")
    prefix = "quotes/"
    return render_template(f"{prefix}show_quote.html", quote=quote)