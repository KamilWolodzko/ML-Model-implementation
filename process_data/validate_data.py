from abstract.abstract_classes import DataValidator
from collections.abc import Iterable


class DataValidatorXGBRegressor(DataValidator):
    """
        Validates user data for XGBRegressor model.
    """
    
    def __init__(self, data: list[float]):
        """
        Parameters
        ----------
        :param data list[float]: Data provided by user.
        """

        self.last_values = data

    def validate_data(self) -> bool:
        """
            Validates user input.
        :return (bool): Validity of user data.
        """

        # logging is not used as it is captured inside routes.py
        if not isinstance(self.last_values, Iterable):
            raise TypeError("Provided data is not iterable!")
        if len(self.last_values) != 10:
            raise ValueError("Model expects exactly 10 last reads")
        if not all([isinstance(item, (int, float)) for item in self.last_values]):
            raise TypeError("Provided data contains other types than integer or float!")
        return True
