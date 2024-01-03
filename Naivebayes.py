# Import necessary libraries
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Data from CSV
data = pd.read_csv("p_tennis.csv")
print("The first 5 Values of data are:\n", data.head())

# Obtain train data and train output
X = data.iloc[:, :-1].copy()  # Create a copy to avoid SettingWithCopyWarning
print("\nThe First 5 values of the train data are\n", X.head())

y = data.iloc[:, -1].copy()  # Create a copy to avoid SettingWithCopyWarning
print("\nThe First 5 values of train output are\n", y.head())

# Convert them to numbers using LabelEncoder and loc
le_outlook = LabelEncoder()
X.loc[:, 'Outlook'] = le_outlook.fit_transform(X['Outlook'])

le_Temperature = LabelEncoder()
X.loc[:, 'Temperature'] = le_Temperature.fit_transform(X['Temperature'])

le_Humidity = LabelEncoder()
X.loc[:, 'Humidity'] = le_Humidity.fit_transform(X['Humidity'])

le_Windy = LabelEncoder()
X.loc[:, 'Windy'] = le_Windy.fit_transform(X['Windy'])

print("\nNow the Train data is\n", X.head())

le_PlayTennis = LabelEncoder()
y = le_PlayTennis.fit_transform(y)
print("\nNow the Train output is\n", y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Create and train the Gaussian Naive Bayes classifier
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Evaluate the accuracy
accuracy = accuracy_score(classifier.predict(X_test), y_test)
print("Accuracy is:", accuracy)
