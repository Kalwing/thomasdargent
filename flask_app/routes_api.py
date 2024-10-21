from flask import Blueprint, render_template

bp = Blueprint('api', __name__)

@bp.route("/error_brevo", methods=['GET', 'POST'])
def brevo_error():
    return {
        "code" : "error_access"
    }, 400

@bp.route("/success_brevo", methods=['GET', 'POST'])
def brevo_success():
    return render_template("brevo/brevo_success_2.html"), 200