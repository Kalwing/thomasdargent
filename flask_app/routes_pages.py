from flask import Blueprint, render_template

bp = Blueprint('pages', __name__)

@bp.route("/brevo_form_example")
def brevo_form_example():
    return render_template("brevo/brevo_form.html")

@bp.route("/brevo_success_example")
def brevo_success_example():
    return render_template("brevo/brevo_success.html")

@bp.route("/brevo_error_example")
def brevo_error_example():
    return render_template("brevo/brevo_error.html")