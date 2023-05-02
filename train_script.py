import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.compose import ColumnTransformer
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import joblib


"""### Reading the database"""

file_path = r"D:\Sicherung\pythonProject\venv\Lib\data2.csv"
file = pd.read_csv(file_path, sep=',', encoding='utf-8')

df = pd.DataFrame(file)
df = df.fillna('-')
df = df[~df.iloc[:, 0].str.startswith('** Entfallen **')]
df.reset_index(drop=True, inplace=True)

"""### Feature processing"""

inputs = df.iloc[:, :-1]
target = pd.DataFrame(df.iloc[:, -1])

numerical_columns = inputs.select_dtypes(include=['int', 'float']).columns.tolist()

all_columns = list(inputs.columns)

if numerical_columns is not None:
    text_columns = [col for col in all_columns if col not in numerical_columns]
    text_transformers = [('text' + str(i), CountVectorizer(), column) for i, column in enumerate(text_columns, start=1)]
    numerical_transformers = [('numerical' + str(i), MinMaxScaler(), [column]) for i, column in enumerate(numerical_columns, start=1)]
    transformers = text_transformers + numerical_transformers
else:
    text_columns = all_columns
    transformers = [('text' + str(i), CountVectorizer(), column) for i, column in enumerate(text_columns, start=1)]

preprocessor = ColumnTransformer(transformers=transformers)

"""### Train test split"""
x_train, x_test, y_train, y_test = train_test_split(inputs, target,
                                                    test_size=0.2,
                                                    random_state=42)

"""### Tokenizing the Input Room Names"""
# The 'fit_transform()' method is to be applied *only* on the training data!
x_train_transf = preprocessor.fit_transform(x_train)
x_test_transf = preprocessor.transform(x_test)


# Check how the 'x_train_transf' matrix looks like.
print(x_train_transf.shape)
print(x_test_transf.shape)
print(x_test_transf)

"""### Performing the classification"""

# Create an instance of the Multinomial Naive Bayes classifier
clf = MultinomialNB()

# Fit the model to the training data
clf.fit(x_train_transf, y_train)

"""### Performing the evaluation on the test dataset"""

# Predict the target of the observations in the test set
y_test_pred = clf.predict(x_test_transf)
y_test_pred_prob = clf.predict_proba(x_test_transf)

# The classification report consists of the precision, recall and f1-score of each class as well as
# the overall accuracy of the model.
print(classification_report(y_test, y_test_pred))

# Export the heatmap
def save_heatmap(y_true, y_pred, file_name, figsize=(10, 7)):
    conf_matrix = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=figsize)
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')

    plt.title("Confusion Matrix Heatmap")
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")

    plt.savefig(file_name)
    print(f"Heatmap saved as {file_name}")
    plt.close()

y_pred = clf.predict(x_test_transf)
save_heatmap(y_test, y_pred, 'heatmap.png')



# Export the model
def save_model(model, preprocessor, model_file_name, preprocessor_file_name):
    joblib.dump(model, model_file_name)
    joblib.dump(preprocessor, preprocessor_file_name)
    print(f"Model saved as {model_file_name}")
    print(f"Preprocessor saved as {preprocessor_file_name}")


save_model(clf, preprocessor, 'trained_classifier.joblib','preprocessor.joblib')