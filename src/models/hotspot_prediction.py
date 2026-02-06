import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load dataset (make sure sample_aqi.csv exists in data/ folder)
data = pd.read_csv("data/sample_aqi.csv")

# Features: adjust column names to match your dataset
X = data[["temperature", "humidity", "traffic_index"]]
y = data["hotspot"]  # 1 = hotspot, 0 = normal

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train baseline logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
print("Hotspot Prediction Accuracy:", accuracy)
