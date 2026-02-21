# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import joblib

# Step 2: Load Dataset
data = pd.read_csv("energy_data.csv")

# Step 3: Define Input (X) and Output (y)
X = data[["Hour"]]
y = data["Power_Consumption"]

# Step 4: Train Model
model = LinearRegression()
model.fit(X, y)

# Step 5: Save Model
joblib.dump(model, "energy_model.pkl")

# Step 6: Predict Values
predicted = model.predict(X)

# Step 7: Define Waste Threshold
threshold = y.mean() + 1.5 * y.std()

# Step 8: Detect Wastage
data["Predicted"] = predicted
data["Wastage"] = data["Power_Consumption"] > threshold

print("Energy Wastage Detection Result:\n")
print(data)

# Step 9: Plot Graph
plt.scatter(data["Hour"], data["Power_Consumption"])
plt.plot(data["Hour"], predicted)
plt.axhline(y=threshold)
plt.xlabel("Hour")
plt.ylabel("Power Consumption")
plt.title("Energy Wastage Detection")
plt.show()

print("\nModel Training Completed Successfully!")