import numpy as np
from sklearn.preprocessing import FunctionTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import joblib

iris = load_iris()

X, y = iris.data , iris.target

def logisticComposer(x):
  return np.log1p(x)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

logisticTransformer = FunctionTransformer(logisticComposer)

pipeline = Pipeline([
    ("logisticComposer", logisticTransformer),
    ("classifier", LogisticRegression())
])

pipeline.fit(X_train,y_train)

#Modelname
modlename = "irisprediction.pkl"
joblib.dump(pipeline,modlename)

score = pipeline.score(X_test,y_test)

print(f"Score value is {score}")
