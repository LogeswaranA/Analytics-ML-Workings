import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)
X = 2 * np.random.rand(100,1)
y = 4 + 3 * X + np.random.rand(100,1)

print("X Value is ---")
print(X)
print("Y value is ---")
print(y)
#Split the dataset into train and test

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.8,random_state=42)

print("XTrain")
print(X_train)
print("X_test")

print(X_test)
print("y_train")

print(y_train)
print("y_test")

print(y_test)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

#Evaluate the model using mean squared root
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print(f"Mean squared error {mse}")
print(f"R2 Score is {r2}")

plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()



