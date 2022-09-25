import logging
import time

from collections import deque
from flask import request, jsonify
from multiprocessing import Value

from model.xgb_regressor_model import MODEL
from process_data.validate_data import DataValidatorXGBRegressor
from process_data.process_data import DataProcessorXGBRegressor


logger = logging.getLogger(__name__)

# Global variables #
# queue used to store dict data timestamp: request per second.
QUEUE_RPS = deque(iterable=[], maxlen=5)
# start application time.
START = int(time.time())
# number of endpoint /predict requests.
COUNTER = Value('i', 1)


def count_endpoint_requests():
    """
        Function using global variables for counting how many incoming request happened in each second.
    :return: None
    """

    global START, COUNTER, QUEUE_RPS
    now = int(time.time())
    if now - START >= 1:
        QUEUE_RPS.append({now: COUNTER.value})
        COUNTER = Value('i', 0)
        START = now

    with COUNTER.get_lock():
        COUNTER.value += 1


def register_model_routes(app):
    """
        Function to register routes in application.
    :param app: Flask application.
    :return: None
    """

    @app.route('/predict', methods=["POST"])
    def predict():
        """
            /predict endpoint to make a prediction using user json data previous_values.
        :return (float): Predicted value.
        """

        count_endpoint_requests()

        try:
            previous_values = request.json.get('previous_values', [])
            data_validator = DataValidatorXGBRegressor(previous_values)
            if data_validator.validate_data():
                processed_data = DataProcessorXGBRegressor(previous_values).process_data()
                predicted = MODEL.predict(processed_data)[0]
                return jsonify({"predicted": float(predicted)})
        except (TypeError, ValueError) as e:
            logger.exception(e)
            return f"You provided wrong data!\n{e}", 400
        except Exception as e:
            logger.exception(e)
            return "Internal server error", 500

    @app.route('/metrics', methods=["GET"])
    def metrics():
        """
            /metrics endpoint to get predictions performance metric.
        :return list[dict]: List containing up to 5 dictionaries data -> timestamp: request per second
        """

        if len(QUEUE_RPS) < 1:
            return {'msg': 'Please use the /predict endpoint firstly'}, 400
        return {"List up to 5 Requests Per Second": list(QUEUE_RPS)}
