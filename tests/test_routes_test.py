import json


def test_correct_data_predict_endpoint_response(client):
    """
        Test response code with correct data for endpoint /predict.
    """

    # Given
    payload = json.dumps({
            'previous_values': [num for num in range(10)]
        })
    # When
    response = client.post("/predict", headers={"Content-Type": "application/json"}, data=payload)
    # Then
    assert response.status_code == 200


def test_wrong_size_data_predict_endpoint(client):
    """
        Test response with wrong data size for endpoint /predict.
    """

    # Given
    payload = json.dumps({
        'previous_values': [num for num in range(9)]
    })
    # When
    response = client.post("/predict", headers={"Content-Type": "application/json"}, data=payload)
    # Then
    assert b"Model expects exactly 10 last reads" in response.data
    assert response.status_code == 400

def test_wrong_data_type_predict_endpoint(client):
    """
     Test response with wrong data type for endpoint /predict.
    """

    # Given
    payload = json.dumps({
        'previous_values': [str(num) for num in range(10)]
    })
    # When
    response = client.post("/predict", headers={"Content-Type": "application/json"}, data=payload)
    # Then
    assert b"Provided data contains other types than integer or float!" in response.data
    assert response.status_code == 400

def test_non_iterable_data_predict_endpoint(client):
    """
     Test response with wrong not iterable data for endpoint /predict.
    """

    # Given
    payload = json.dumps({
        'previous_values': 0
    })
    # When
    response = client.post('/predict', headers={"Content-Type": "application/json"}, data=payload)
    # Then
    assert b"Provided data is not iterable!" in response.data
    assert response.status_code == 400

def test_metrics_endpoint_before_first_request_respone(client):
    """
        Test response for endpoint /metrics.
    """

    # When
    response = client.get('/metrics')
    # Then
    assert response.status_code == 400

