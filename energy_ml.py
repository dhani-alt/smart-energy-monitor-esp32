# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 2: Load Dataset
data = pd.read_csv("energy_data.csv")

# Step 3: Define Input and Output
X = data[['Hour']]
y = data['Power_Consumption']

# Step 4: Train Machine Learning Model
model = LinearRegression()
model.fit(X, y)

# Step 5: Predict Values
predicted = model.predict(X)

# Step 6: Set Wastage Threshold
threshold = y.mean() + 1.5 * y.std()

# Step 7: Add Results to Table
data['Predicted'] = predicted
data['Wastage'] = data['Power_Consumption'] > threshold

# Step 8: Print Output
print("\n===== Energy Wastage Detection =====\n")
print(data)

# Step 9: Plot Graph
plt.figure()
plt.scatter(data['Hour'], data['Power_Consumption'])
plt.plot(data['Hour'], predicted)
plt.axhline(y=threshold)
plt.xlabel("Hour")
plt.ylabel("Power Consumption")
plt.title("Energy Wastage Detection")
plt.show()

# Step 10: Predict Future Energy Usage
future_hour = np.array([[11]])
future_prediction = model.predict(future_hour)

print("\nPredicted Energy for Hour 11:", future_prediction[0])