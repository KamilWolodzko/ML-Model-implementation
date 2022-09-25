import pytest

from app import create_app
from config import config
from model.xgb_regressor_model import ModelLoaderXGBRegressor


@pytest.fixture()
def client():
    """
        Creates flask application for tests.
    :yield: Flask application
    """
    app = create_app(config)
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


@pytest.fixture()
def model_xgb_regressor():
    """
        Creates model_xgb_regressor instance for tests.
    :yield: XBGRegressor model
    """

    model = ModelLoaderXGBRegressor(model_path=config['model_path']).model_loader()
    yield model






