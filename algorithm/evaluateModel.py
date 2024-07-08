import numpy as np
import joblib

loaded_pipeline = joblib.load("irisprediction.pkl")

myrow = np.array([[4.5,3.5,2.5,1.4]])

predictedvalue = loaded_pipeline.predict(myrow)

