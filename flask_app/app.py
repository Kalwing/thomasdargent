from flask import Flask
from . import routes_api
from . import routes_pages


def create_app():
    app = Flask(
        __name__,
        static_folder="../dist/backend",  # test:"../public",  # Serve static files from /public
        template_folder="../dist/backend",  # test:"../flask_templates",
    )  # HTML templates in /templates

    # Import the routes
    app.register_blueprint(routes_api.bp, url_prefix="/api")  # test:no prefix
    app.register_blueprint(routes_pages.bp, url_prefix="/api")  # test:no prefix
    return app


app = create_app()
app.config["APPLICATION_ROOT"] = "/api"  # test: nothing

if __name__ == "__main__":
    app.run(debug=True)
