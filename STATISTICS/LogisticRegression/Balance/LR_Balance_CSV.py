import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.utils import shuffle

# Load data from CSV
balance = pd.read_csv('data2.csv', sep=';')
# Shuffle the data to ensure randomness
balance = shuffle(balance)

# Explore the data
print(balance.head())

# Test train split
X_train, X_test, y_train, y_test = train_test_split(balance.drop('Y', axis=1), balance['Y'])

# Train the model using the training data
LogReg = LogisticRegression(solver='lbfgs', class_weight='balanced')
LogReg.fit(X_train, y_train)

# Predicting1
input_data = pd.DataFrame(np.array([[0.1258223684, 0.8741776316, -277.2989309211, 0, 278.2989309211]]),
                          columns=X_train.columns)
y_pred = LogReg.predict(input_data)
print('\nPrediction1 =', y_pred[0])
# Predicting2
input_data = pd.DataFrame(np.array([[0.7322004237, 0.2677995763, -0.4964999539, 0, 1.4964999539]]),
                          columns=X_train.columns)
y_pred = LogReg.predict(input_data)
print('Prediction2 =', y_pred[0])

# Scoring the model
print(LogReg.score(X_test, y_test))

# Understanding the score
y_pred = (LogReg.predict(X_test) > 0.5).astype(int)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

feature_importance = pd.Series(LogReg.coef_[0], index=X_train.columns)
print("Feature Importance:\n", feature_importance)
