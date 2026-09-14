import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.utils.class_weight import compute_sample_weight
import xgboost as xgb
from xgboost import XGBClassifier
import joblib


def main():
    print("--- Loading dataset ---")
    csv_path = os.path.join(os.path.dirname(__file__), "CEP_Train_Data.csv")
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    # Load the entire training CSV
    df = pd.read_csv(csv_path)
    print(f"Dataset shape: {df.shape}")

    # The target is 'risk_level'
    # Drop 'dropout_risk' and 'dropout_labels' (if present) to prevent target leakage
    features_to_drop = ["risk_level", "dropout_risk", "dropout_labels"]
    X = df.drop(columns=[col for col in features_to_drop if col in df.columns], errors="ignore")
    y = df["risk_level"]

    print("\n--- Encoding target variable ---")
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    # Class mappings
    for idx, class_name in enumerate(le.classes_):
        print(f"Class {idx} -> {class_name}")

    print("\n--- Splitting data ---")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )

    # Column definitions
    nominal_cat = ["gender"]
    num_cols = X_train.select_dtypes(include="number").columns.tolist()

    print(f"Nominal features: {nominal_cat}")
    print(f"Numerical features ({len(num_cols)}): {num_cols}")

    # Column transformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("nominal", OneHotEncoder(handle_unknown="ignore", sparse_output=False), nominal_cat),
            ("numerical", "passthrough", num_cols)
        ],
        remainder="passthrough"
    )

    print("\n--- Computing sample weights for class balance ---")
    sample_weights = compute_sample_weight(class_weight="balanced", y=y_train)

    print("\n--- Initializing and training XGBoost Classifier ---")
    model = XGBClassifier(
        n_estimators=100,
        max_depth=5,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="multi:softprob",
        eval_metric="mlogloss",
        num_class=3,
        learning_rate=0.05,
        random_state=42,
        n_jobs=-1
    )

    pipe = Pipeline([
        ("preprocess", preprocessor),
        ("clf_model", model)
    ])

    print("Fitting model...")
    pipe.fit(X_train, y_train, clf_model__sample_weight=sample_weights)
    print("Model fit complete!")

    # Evaluate
    train_acc = pipe.score(X_train, y_train)
    test_acc = pipe.score(X_test, y_test)
    print(f"Train Accuracy: {train_acc:.4f}")
    print(f"Test Accuracy: {test_acc:.4f}")

    # Save model pipeline, label encoder, and feature list
    model_filename = os.path.join(os.path.dirname(__file__), "student_risk_model.pkl")
    print(f"\n--- Saving model to {model_filename} ---")
    save_data = {
        "pipeline": pipe,
        "label_encoder": le,
        "features": X.columns.tolist()
    }
    joblib.dump(save_data, model_filename)
    print("Model saved successfully!")


if __name__ == "__main__":
    main()
