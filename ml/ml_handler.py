import os
import joblib
import pandas as pd


class MLPredictor:
    def __init__(self, model_path=None):
        if model_path is None:
            self.model_path = os.path.join(os.path.dirname(__file__), "student_risk_model.pkl")
        else:
            self.model_path = model_path
        self.pipeline = None
        self.label_encoder = None
        self.feature_names = None
        self.load_model()

    def load_model(self):
        if not os.path.exists(self.model_path):
            print(f"Warning: Model file {self.model_path} not found. Predictor is inactive.")
            return False

        try:
            saved_data = joblib.load(self.model_path)
            self.pipeline = saved_data["pipeline"]
            self.label_encoder = saved_data["label_encoder"]
            self.feature_names = saved_data["features"]
            print("ML model loaded successfully.")
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False

    def predict(self, student_data):
        """
        Accepts a dictionary of student features.
        Returns predicted risk level string: 'Low', 'Medium', or 'High'.
        """
        if self.pipeline is None or self.label_encoder is None:
            # Fallback if model is not trained yet (returns Low as safe default)
            print("Warning: ML model not initialized. Returning default 'Low'.")
            return "Low"

        try:
            # Ensure the dict has all features required by the model
            input_df = pd.DataFrame([student_data])

            # Reorder columns to match training features exactly
            input_df = input_df[self.feature_names]

            # Predict
            pred_encoded = self.pipeline.predict(input_df)[0]

            # Decode
            pred_label = self.label_encoder.inverse_transform([pred_encoded])[0]
            return pred_label
        except Exception as e:
            print(f"Error during prediction: {e}")
            return "Low"


# Singleton instance
predictor = MLPredictor()
