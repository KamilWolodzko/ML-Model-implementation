from abc import ABC, abstractmethod


class DataValidator(ABC):
    """
        Used as a template for validating user data.
    """

    @abstractmethod
    def validate_data(self) -> bool:
        pass


class DataProcessor(ABC):
    """
        Used as a template for data processing.
    """

    @abstractmethod
    def process_data(self):
        pass


class ModelLoader(ABC):
    """
        Used as a template for loading a model_xgb_regressor.
    """

    @abstractmethod
    def model_loader(self):
        pass
