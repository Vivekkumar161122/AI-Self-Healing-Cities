import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load dataset (make sure Delhi_AQI_2026.csv exists in the data/ folder)
data = pd.read_csv("Delhi_AQI_2026.csv")

# Drop missing values
data = data.dropna()

# AQI categorization function
def categorize_aqi(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 200:
        return "Poor"
    else:
        return "Severe"

# Create AQI category column
data["AQI_Category"] = data["pollutant_avg"].apply(categorize_aqi)

# Features
X = data[["latitude", "longitude", "pollutant_min", "pollutant_max"]]
y = data["AQI_Category"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)

print("AQI Category Classification Accuracy:", accuracy)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# What-if intervention: reduce pollutant_max by 20%
intervention_data = X.copy()
intervention_data["pollutant_max"] = intervention_data["pollutant_max"] * 0.8

intervention_predictions = model.predict(intervention_data)

print("\nSample Intervention Predictions:")
print(intervention_predictions[:10])
