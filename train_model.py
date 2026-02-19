import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from scipy.io import arff

# -----------------------------
# 1. Load ARFF dataset
# -----------------------------
data = arff.loadarff("dataset/Training Dataset.arff")
df = pd.DataFrame(data[0])

# Convert byte strings to integers
for column in df.columns:
    df[column] = df[column].apply(lambda x: int(x))

# -----------------------------
# 2. Split features and target
# -----------------------------
X = df.drop("Result", axis=1).values
y = df["Result"].values

# Convert target values:
# -1 → 0
#  1 → 1
y = np.where(y == -1, 0, 1)

# -----------------------------
# 3. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 4. Train Model
# -----------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# 5. Evaluate Model
# -----------------------------
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Model Accuracy:", accuracy)
print("Confusion Matrix:\n", cm)

# -----------------------------
# 6. Save Model
# -----------------------------
pickle.dump(model, open("model/phishing_model.pkl", "wb"))

print("Model saved successfully in model folder!")
