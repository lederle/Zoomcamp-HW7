import bentoml
from bentoml.io import JSON

from pydantic import BaseModel

class CreditApplication(BaseModel):
    seniority: int
    home: str
    time: int
    age: int
    marital: str
    records: str
    job: str
    expenses: int
    income: float
    assets: float
    debt: float
    amount: int
    price: int


model_reference = bentoml.xgboost.get("credit_risk_model:latest")
dv = model_reference.custom_objects["dictVectorizer"]
model_runner = model_reference.to_runner()

service = bentoml.Service("credit_risk_classifier", runners = [model_runner])


@service.api(input = JSON(pydantic_model = CreditApplication), output = JSON())
async def classify(credit_application):
    application_data = credit_application.dict()
    client = dv.transform(application_data)
    # TODO: naming is wack
    prediction = await model_runner.predict.async_run(client)
    print(prediction)

    result = prediction[0]
    if result > 0.5:
        return { "status": "DENIED" }
    elif result > 0.23:
        return { "status": "MAYBE" }
    else:
        return { "status" : "APPROVED" }
