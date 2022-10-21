import bentoml
from bento.io import JSON

model_reference = bentoml.xgboost.get("credit_risk_model:dmp4bfsq5c7bpl56")

model_runner = model_reference.to_runner()

service = bentoml.Service("credit_risk_classifier", runners = [model_runner])


@service.api(input = JSON(), output = JSON())
def classify(application_data):
    prediction = model_runner.predict.run(application_data)
    return { "status" : "APPROVED" }
