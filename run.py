import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Step 1: Load the dataset
data = pd.read_csv("C:\\Users\\Akhila\\Desktop\\Projects\\Cricket\\ipl.csv")  # Replace "your_dataset.csv" with the actual path to your dataset file

# Step 2: Data preprocessing
# Convert the 'date' column to a pandas datetime object
data['date'] = pd.to_datetime(data['date'])

# Step 3: Feature selection
X = data[['runs', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5', 'striker', 'non-striker']]
y = data['total']

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

model_filename = "linear_regression_model.joblib"
joblib.dump(model, model_filename)

# Step 8: You can now use the trained model to predict the score for new data points
# For example, to predict the score for a new data point:
new_data = pd.DataFrame({
    'runs': [5],
    'wickets': [1],
    'overs': [10],
    'runs_last_5': [35],
    'wickets_last_5': [2],
    'striker': [20],
    'non-striker': [20]
})

predicted_score = model.predict(new_data)

print("Predicted Score:", predicted_score[0])
