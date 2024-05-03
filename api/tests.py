from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)

def test_null_prediction():
    response = client.post('/v1/salaryPrediction', json = {
                                                    'YearsExperience': 8,                                                   
                                                    })
    assert response.status_code == 200
    assert response.json()['worldwide_gross'] == 0

def test_random_prediction():
    response = client.post('/v1/salaryPrediction', json = {
                                                    'YearsExperience': 8,                                                   
                                                })
    assert response.status_code == 200
    assert response.json()['worldwide_gross'] != 0 