import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
import joblib


"""### Reading the database"""

file_path = r"D:\Sicherung\pythonProject\venv\Lib\data_predict.csv"
file = pd.read_csv(file_path, sep=',', encoding='utf-8')

df = pd.DataFrame(file)
df = df.fillna('-')
df = df[~df.iloc[:, 0].str.startswith('** Entfallen **')]
df.reset_index(drop=True, inplace=True)

"""### Feature processing"""

inputs = df.iloc[:, :-1]

# Load the pre-trained classifier
preprocessor = joblib.load('preprocessor.joblib')
loaded_clf = joblib.load('trained_classifier.joblib')

# Transform the input data using the same preprocessor
inputs_transf = preprocessor.transform(inputs)

# Generate predictions using the pre-trained classifier
predictions = loaded_clf.predict(inputs_transf)

# Save the predictions as a new CSV file
room_ids = df.iloc[:, -1]
prediction_df = pd.DataFrame({"Room_ID": room_ids, "Prediction": predictions})
prediction_df.to_csv("predictions.csv", index=False)
