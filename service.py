import bentoml
from bentoml.io import JSON

model_runner = bentoml.xgboost.get("credit_risk_model:latest").to_runner()

service = bentoml.Service("credit_risk_classifier", runners = [model_runner])


@service.api(input = JSON(), output = JSON())
def classify(application_data):
    prediction = model_runner.predict.run(application_data)
    return { "status" : "APPROVED" }
