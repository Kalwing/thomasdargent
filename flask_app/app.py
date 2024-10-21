from flask import Flask
from . import routes_api
from . import routes_pages

def create_app():
    app = Flask(__name__,
                static_folder="../public",  # Serve static files from /public
                template_folder="../flask_templates")  # HTML templates in /templates

    # Import the routes
    app.register_blueprint(routes_api.bp)
    app.register_blueprint(routes_pages.bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)