import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Step 1: Load and Preprocess Data
file_path = "C:\\Users\\Akhila\\Desktop\\Projects\\Cricket\\IPL_Matches_2008_2022.csv"  # Replace with the actual path to your dataset file
data = pd.read_csv(file_path)

# Step 2: Drop unnecessary columns (if any)
data.drop(columns=['ID', 'Date', 'Season', 'MatchNumber', 'SuperOver', 'WonBy', 'Margin', 'method', 'Player_of_Match', 'Team1Players', 'Team2Players', 'Umpire1', 'Umpire2'], inplace=True)


# Drop rows with missing values in the 'WinningTeam' column
data.dropna(subset=['WinningTeam'], inplace=True)

print(data['Team1'])
print(data['TossWinner'])
print(data['Venue'])
# Step 3: Convert categorical variables to numerical labels using LabelEncoder
label_encoder = LabelEncoder()
data['Team1'] = label_encoder.fit_transform(data['Team1'])
data['Team2'] = label_encoder.transform(data['Team2'])
data['Venue'] = label_encoder.fit_transform(data['Venue'])

# Combine unique classes from both 'TossWinner' and 'WinningTeam'
all_classes = set(data['TossWinner'].unique()) | set(data['WinningTeam'].unique())

# Update the label encoding for 'TossWinner' and 'WinningTeam'
label_encoder.classes_ = sorted(all_classes)
data['TossWinner'] = label_encoder.transform(data['TossWinner'])
data['WinningTeam'] = label_encoder.transform(data['WinningTeam'])
# Step 5: Define the feature matrix X and target vector y
X = data[['Team1', 'Team2', 'Venue', 'TossWinner']]
y = data['WinningTeam']

# Step 6: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)


# Step 7: Make predictions
y_pred = model.predict(X_test)

# Step 8: Evaluate the model (optional)
accuracy = (y_pred == y_test).mean()
print("Accuracy:", accuracy)


# Step 8: Save the Trained Model (Optional)
model_filename = "toss_based_winner_prediction_model.joblib"
joblib.dump(model, model_filename)

# Step 9: Make Predictions for New Data
# Example of predicting the toss-based winner for a new data point
# new_data = pd.DataFrame({
#     'Venue': ['Narendra Modi Stadium, Ahmedabad'],
#     'Team1': ['Rajasthan Royals'],
#     'Team2': ['Gujarat Titans']
# })

# # Convert categorical variables to numerical labels using the same LabelEncoder
# new_data['Venue'] = label_encoder.transform(new_data['Venue'])
# new_data['Team1'] = label_encoder.transform(new_data['Team1'])
# new_data['Team2'] = label_encoder.transform(new_data['Team2'])

# # Make the prediction using the trained model
# predicted_toss_winner = model.predict(new_data)

# print("Predicted Toss-Based Winner:")
# if predicted_toss_winner[0] == 1:
#     print("Toss Winner is the Same as the Actual Match Winner.")
# else:
#     print("Toss Winner is Not the Same as the Actual Match Winner.")
