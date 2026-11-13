
import pandas as pd
from google.colab import files
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

uploaded = files.upload()
df = pd.read_csv(list(uploaded.keys())[0])

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

new_flower = scaler.transform([[5.1, 3.5, 1.4, 0.2]])
print("New flower:", knn.predict(new_flower)[0])

X1 = [[1], [2], [3], [8], [9], [10]]
y1 = ["A", "A", "B", "B", "B", "B"]

m1 = KNeighborsClassifier(n_neighbors=3)
m1.fit(X1, y1)

print("TC1:", m1.predict([[2.5]])[0])
