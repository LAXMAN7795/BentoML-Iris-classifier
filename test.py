import bentoml

iris_clf_runner = bentoml.sklearn.get("iris_svc:latest").to_runner()
iris_clf_runner.init_local() # Initialize the runner
print(iris_clf_runner.predict.run([[5.1, 3.5, 4.4, 5.2]]))