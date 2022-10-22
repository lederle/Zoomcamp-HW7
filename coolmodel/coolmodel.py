import bentoml
from bentoml.io import NumpyNdarray

model_runner = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5").to_runner()

service = bentoml.Service("coolmodel", runners = [model_runner])

@service.api(input = NumpyNdarray(), output = NumpyNdarray())
def process(client_data):
    return model_runner.predict.run(client_data)
