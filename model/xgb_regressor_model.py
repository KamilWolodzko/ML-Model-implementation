import logging
import xgboost as xg

from abstract.abstract_classes import ModelLoader
from config import config
from xgboost.core import XGBoostError

logger = logging.getLogger(__name__)


class ModelLoaderXGBRegressor(ModelLoader):
    """
        Loads XGBRegressor model.
    """

    def __init__(self, model_path: str):
        """
        Parameters
        ----------
        :param model_path (str): Path to the saved model.
        """

        self.model_path = model_path
        self.xgb_r = xg.XGBRegressor()

    def model_loader(self) -> xg.XGBRegressor:
        """
            Loads XGBRegressor model.
        :return xgboost.XGBRegressor: model XGBRegressor
        """

        try:
            self.xgb_r.load_model(self.model_path)
        except (TypeError, FileNotFoundError, XGBoostError) as e:
            logger.exception(e)
            raise e
        return self.xgb_r


MODEL = ModelLoaderXGBRegressor(model_path=config['model_path']).model_loader()
