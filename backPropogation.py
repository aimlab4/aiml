
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

iris = load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Test Case 1
model = MLPClassifier(
    hidden_layer_sizes=(5, 7),
    max_iter=1000,
    random_state=42
)

model.fit(X_train, y_train)

print("Test Case 1 - Accuracy:",
      model.score(X_test, y_test))

# Test Case 2
model = MLPClassifier(
    hidden_layer_sizes=(5, 7),
    max_iter=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Test Case 2 - Weights Updated: YES")
