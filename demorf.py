import joblib
import pandas as pd
model = joblib.load("delivery_time_model.joblib")
print(model)
# dump can be cloud


sample = pd.DataFrame([{
    "Distance_km": 5/2, "Preparation_Time_min": 15,
    "Traffic_Level": "High", "Weather": "Rainy"
}])
print(model.predict(sample)[0])