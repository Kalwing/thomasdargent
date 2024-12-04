from flask import Flask
from . import routes_api
from . import routes_pages

class DevelopmentConfig:
    """Development-specific configuration"""
    DEBUG = True
    STATIC_FOLDER = "../public"
    TEMPLATE_FOLDER = "../flask_templates"

class ProductionConfig:
    """Production-specific configuration"""
    DEBUG = False
    TESTING = False
    STATIC_FOLDER = "../dist/backend"
    TEMPLATE_FOLDER = "../dist/backend"
    APPLICATION_ROOT = "/api"


def create_app(config_name="prod"):
    config_map = {
        'dev': DevelopmentConfig,
        'prod': ProductionConfig
    }
    config_class = config_map[config_name]

    # Create app with environment-specific settings
    app = Flask(
        __name__,
        static_folder=config_class.STATIC_FOLDER,
        template_folder=config_class.TEMPLATE_FOLDER
    )

    # Load configuration
    app.config.from_object(config_class)

    # Register blueprints
    if config_name == 'prod':
        app.register_blueprint(routes_api.bp, url_prefix="/api")
        app.register_blueprint(routes_pages.bp, url_prefix="/api")
    else:
        app.register_blueprint(routes_api.bp)
        app.register_blueprint(routes_pages.bp)

    return app

# For development/local run
if __name__ == "__main__":  # pragma: no cover
    app = create_app('dev')
    app.run(debug=True)
