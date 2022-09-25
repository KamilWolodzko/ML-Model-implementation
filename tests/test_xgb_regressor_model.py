import numpy as np
import pytest
import xgboost as xg

from process_data import validate_data


def test_model_load(model_xgb_regressor):
    """
        Test to check if model_xgb_regressor is loading correctly.
    """

    assert isinstance(model_xgb_regressor, xg.XGBRegressor)


def test_model_output_type(model_xgb_regressor):
    """
        Test to check whether model_xgb_regressor gives correct type output.
    """
    # Given
    data_xgb = np.array([[25, 9, 52, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

    # When
    xgb = model_xgb_regressor.predict(data_xgb)[0]

    # Then
    assert isinstance(xgb, np.float32)


def test_model_proper_output_value(model_xgb_regressor):
    """
        Test to check whether model_xgb_regressor gives correct value -> only applicable to given model_xgb_regressor.
    """
    # Given
    data_xgb = np.array([[25, 9, 52, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

    # When
    xgb = model_xgb_regressor.predict(data_xgb)[0]

    # Then
    assert np.float32(xgb) == np.float32(10.351504)

def test_model_invalid_data(model_xgb_regressor):
    """
        Test to check whether model_xgb_regressor will pass incorrect data.
    """

    # Given
    data_xgb = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # When
    with pytest.raises(ValueError) as err:
        validate_data.DataValidatorXGBRegressor(data_xgb).validate_data()
    # Then
    assert "Model expects exactly 10 last reads" in str(err)