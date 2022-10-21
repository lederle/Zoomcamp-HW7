import bentoml
from bentoml.io import JSON

model_reference = bentoml.xgboost.get("credit_risk_model:latest")
dv = model_reference.custom_objects["dictVectorizer"]
model_runner = model_reference.to_runner()

service = bentoml.Service("credit_risk_classifier", runners = [model_runner])


@service.api(input = JSON(), output = JSON())
def classify(application_data):
    client = dv.transform(application_data)
    prediction = model_runner.predict.run(client)
    print(prediction)

    result = prediction[0]
    if result > 0.5:
        return { "status": "DENIED" }
    elif result > 0.23:
        return { "status": "MAYBE" }
    else:
        return { "status" : "APPROVED" }
