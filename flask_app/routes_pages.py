from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)


@bp.route("/brevo_form_example")
def brevo_form_example():
    return render_template("brevo_form.html")  # test: brevo/....


@bp.route("/brevo_success_example")
def brevo_success_example():
    return render_template("brevo_success.html")  # test: brevo/....


@bp.route("/brevo_error_example")
def brevo_error_example():
    return render_template("brevo_error.html")  # test: brevo/....
