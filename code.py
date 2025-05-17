import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("../dataset/sample_traffic_data.csv")

# Features and label
X = df[['vehicle_count', 'avg_speed', 'weather_index']]
y = df['congestion_level']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)
print("Predicted congestion levels:", y_pred)
