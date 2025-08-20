import bentoml

from sklearn import svm
from sklearn import datasets

#Load training dataset

iris = datasets.load_iris()
X,y = iris.data, iris.target

#train the model
clf = svm.SVC(gamma='scale')#gamma=scale is a parameter that defines how much influence a single training example has
clf.fit(X, y)

#save model to the bentoml local model store
model_store = bentoml.sklearn.save_model("iris_svc", clf)
print(f'Model saved to: {model_store}')

# Model saved to: Model(tag="iris_svc:gmbgfct5vkns7daw")