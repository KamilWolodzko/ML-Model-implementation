import datetime
import numpy as np

from abstract.abstract_classes import DataProcessor


class DataProcessorXGBRegressor(DataProcessor):
    """
        Prepares user data for XGBRegressor model.
    """

    def __init__(self, data):
        """
        Parameters
        ----------
        :param data list[float]: Data provided by user.
        """

        self.data = data
        self.date = datetime.datetime.now()

    def process_data(self):
        """
            Process user data for actual time to fit the XGBRegressor model.
        :return (ndarray): Numpy array containing [day, hour, minute, day of the week, user data].
        """

        proccesed_date = [self.date.day, self.date.hour, self.date.minute, self.date.weekday()]
        return np.array([proccesed_date + self.data])
