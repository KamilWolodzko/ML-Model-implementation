
## ML Dev interview

The web service predicts traffic (requests per second) in the next time window based on the n previous time window traffic values.

# Description

The repository contains the following files:

* prediction.model: simple XGBRegressor model. For usage, for example, see predict.py file.
* predict.py: a class simple model to predict the traffic. This is an example code to load and use the prediction.model file.
* webapp.py: example Flask application with endpoint definition.

# Requirenments:

1. The application must be delivered in the Python language.

2. The Python version libraries are to the candidate choice.

3. The application should be delivered as a Pull Request to this git repository by creating a fork first.

4. The application should contain basic logging and tests.

5. The application must expose 2 endpoints:

/predict
  - in:  JSON array with a list of previous values 
  - out: predicted value. The prediction has to be calculated by the model loaded from the prediction.model file.

/metrics
  - out: Predictions performance metric. Return requests per second metric on the /predict endpoint

6. The candidate has to deliver a script or command to create a runnable docker container.
