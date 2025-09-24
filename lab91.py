# -------------------------
# Imports
# -------------------------
import pandas as pd
import numpy as np
from sklearn.ensemble import StackingClassifier, RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import lime
import lime.lime_tabular

# -------------------------
# Load dataset
# -------------------------
df = pd.read_csv(r"C:\Users\kadal\Downloads\ml lab\cleaned_audio_features.csv")

# Features & target
label_col = [c for c in df.columns if c.lower() == "label"][0]
X = df.drop(columns=[label_col])
y = df[label_col]

# -------------------------
# Handle missing values
# -------------------------
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# -------------------------
# Encode target labels if needed
# -------------------------
if y.dtype == 'object' or y.dtype.name == 'category':
    le = LabelEncoder()
    y = le.fit_transform(y)

# -------------------------
# Train/Test split
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -------------------------
# Define base + meta models
# -------------------------
base_models = [
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('gb', GradientBoostingClassifier(random_state=42)),
    ('svc', SVC(probability=True, random_state=42))
]
meta_model = LogisticRegression(max_iter=1000)

# -------------------------
# Stacking classifier (with scaling)
# -------------------------
stacking_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('stacking', StackingClassifier(
        estimators=base_models,
        final_estimator=meta_model,
        passthrough=True
    ))
])

# -------------------------
# Fit and predict
# -------------------------
stacking_pipeline.fit(X_train, y_train)
y_pred = stacking_pipeline.predict(X_test)

print("\n=== Stacking Classifier ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# -------------------------
# LIME Explanation
# -------------------------
explainer = lime.lime_tabular.LimeTabularExplainer(
    training_data=X_train,
    feature_names=[f"f{i}" for i in range(X_train.shape[1])],
    class_names=[str(cls) for cls in np.unique(y)],
    mode="classification"
)

sample_index = 5
sample = X_test[sample_index]

exp = explainer.explain_instance(
    data_row=sample,
    predict_fn=stacking_pipeline.predict_proba
)

print("\n=== LIME Explanation ===")
exp.save_to_file("lime_explanation.html")
print("Saved explanation to lime_explanation.html (open in browser)")
