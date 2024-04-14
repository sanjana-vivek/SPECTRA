import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import plot_tree
import graphviz
import seaborn as sns

# Load the dataset
import chardet
with open('algal.csv', 'rb') as f:
    enc = chardet.detect(f.read())
data=pd.read_csv('algal.csv', encoding = enc['encoding'])

# Convert 'Time of Occurrence' column to datetime with dayfirst=True
data['Time of Occurrence'] = pd.to_datetime(data['Time of Occurrence'], dayfirst=True, errors='coerce')
data = data.dropna(subset=['Time of Occurrence'])
data = data.apply(pd.to_numeric, errors='coerce')
data = data.dropna()
data = data.drop(columns=['Day of year'])

# Split features and target variable
X = data.drop(columns=['Cells per litre'])
y = data['Cells per litre']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Feature importances
importances = rf_model.feature_importances_
features = X.columns
indices = np.argsort(importances)[::-1]

# Plot the feature importances
plt.figure(figsize=(10, 6))
plt.title("Feature Importances")
plt.bar(range(X.shape[1]), importances[indices], color="b", align="center")
plt.xticks(range(X.shape[1]), [features[i] for i in indices], rotation=90)
plt.xlim([-1, X.shape[1]])
plt.tight_layout()
plt.show()

# Plot actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.show()

# Plot decision tree
estimator = rf_model.estimators_[0]
plt.figure(figsize=(45,22))
plot_tree(estimator, feature_names=X.columns, filled=True, class_names=["low", "medium", "high"], rounded=True, precision=2)
plt.title("Decision Tree", fontsize=15)
plt.show()

# Plot based on given values
column_to_plot = ' SST'  # Change this to any other column if needed

plt.figure(figsize=(10, 6))
plt.scatter(data[column_to_plot], data['Cells per litre'], color='green')
plt.xlabel(column_to_plot)
plt.ylabel('Cells per litre')
plt.title(f'Cells per litre vs {column_to_plot}')
plt.show()
