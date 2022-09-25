import logging

from config import config
from flask import Flask
from routes.routes import register_model_routes


def create_app(app_config):
    app = Flask(__name__)
    app.config.update(app_config)
    logging.basicConfig(filename=app_config['LOGGING_FILE_NAME'])
    logging.getLogger().addHandler(logging.StreamHandler())
    register_model_routes(app)
    return app


if __name__ == "__main__":
    app = create_app(config)
    app.run(host='0.0.0.0')