import bentoml 
import numpy as np 
from bentoml.io import NumpyNdarray 
iris_clf_runner = bentoml.sklearn.get("iris_svc:latest").to_runner() 
svc = bentoml.Service("iris_classifier", runners=[iris_clf_runner]) # Create a BentoML service 
@svc.api(input=NumpyNdarray(), output=NumpyNdarray()) 
def classify(iris_data: np.ndarray) -> np.ndarray: 
    return iris_clf_runner.predict.run(iris_data)