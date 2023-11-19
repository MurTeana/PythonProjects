import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load data from CSV
titanic = pd.read_csv('titanic.csv')

# Explore the data
print(titanic.head())

# Feature Engineering (one-hot encoding)
titanic = pd.get_dummies(titanic, drop_first=True)

# Test train split
X_train, X_test, y_train, y_test = train_test_split(titanic.drop('survived_yes', axis=1), titanic['survived_yes'])

# Train the model using the training data
LogReg = LogisticRegression(solver='lbfgs')
LogReg.fit(X_train, y_train)

# Predicting if a class=1 child-age girl survived
input_data = pd.DataFrame(np.array([[0, 0, 1, 1]]), columns=X_train.columns)
prediction = LogReg.predict(input_data)
print('\nPrediction =', prediction[0])

# Predicting if a class=3 adult-age male survived
input_data = pd.DataFrame(np.array([[0, 1, 0, 0]]), columns=X_train.columns)
prediction = LogReg.predict(input_data)
print('Prediction =', prediction[0])

# Scoring the model
print(LogReg.score(X_test, y_test))

# Understanding the score
prediction = (LogReg.predict(X_test) > 0.5).astype(int)
result = np.sum(prediction == y_test) / len(y_test)
print(result)