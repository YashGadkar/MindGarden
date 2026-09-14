import os
import sys

# Ensure project root is on sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


def main():
    print("=== MindGarden App Integration Verification ===")

    # 1. Check model file existence
    model_path = os.path.join(PROJECT_ROOT, "ml", "student_risk_model.pkl")
    if not os.path.exists(model_path):
        print(f"FAIL: {model_path} not found! Run ml/train_and_save_model.py first.")
        sys.exit(1)
    print("SUCCESS: Trained XGBoost model file found.")

    # 2. Check Flask server imports & all 8 models
    try:
        from app import (
            ChatMessage,
            CounsellorReport,
            DailyCheckin,
            FacultyRating,
            Quote,
            SessionBooking,
            StudentProfile,
            User,
            app,
            db,
        )
        print("SUCCESS: Flask server and SQLAlchemy models imported successfully.")
    except Exception as e:
        print(f"FAIL: Error importing Flask server or models: {e}")
        sys.exit(1)

    # 3. Check ML Predictor loading
    try:
        from ml.ml_handler import predictor
        if predictor.pipeline is None:
            print("FAIL: ML Predictor failed to load pipeline.")
            sys.exit(1)
        print("SUCCESS: ML Predictor successfully loaded XGBoost pipeline.")
    except Exception as e:
        print(f"FAIL: Error loading ML Predictor: {e}")
        sys.exit(1)

    # 4. Check ML Prediction on a dummy student (Low risk)
    dummy_student_low = {
        "age": 22,
        "gender": "Female",
        "academic_year": 2,
        "study_hours_per_day": 8.0,
        "exam_pressure": 2.0,
        "academic_performance": 85.0,
        "stress_level": 1.0,
        "anxiety_score": 1.0,
        "depression_score": 0.0,
        "sleep_hours": 8.0,
        "physical_activity": 5.0,
        "social_support": 8.0,
        "screen_time": 2.0,
        "internet_usage": 3.0,
        "financial_stress": 1.0,
        "family_expectation": 2.0,
        "burnout_score": 0.0,
        "mental_health_index": 9.0,
    }

    # Check ML Prediction on a dummy student (High risk)
    dummy_student_high = {
        "age": 22,
        "gender": "Male",
        "academic_year": 4,
        "study_hours_per_day": 2.0,
        "exam_pressure": 9.0,
        "academic_performance": 50.0,
        "stress_level": 9.0,
        "anxiety_score": 8.0,
        "depression_score": 7.0,
        "sleep_hours": 4.0,
        "physical_activity": 0.5,
        "social_support": 1.0,
        "screen_time": 9.0,
        "internet_usage": 8.0,
        "financial_stress": 9.0,
        "family_expectation": 9.0,
        "burnout_score": 8.0,
        "mental_health_index": 2.0,
    }

    try:
        pred_low = predictor.predict(dummy_student_low)
        print(f"SUCCESS: Low risk prediction output: {pred_low}")
        assert pred_low in ["Low", "Medium", "High"]
        assert pred_low == "Low", f"Expected Low, got {pred_low}"

        pred_high = predictor.predict(dummy_student_high)
        print(f"SUCCESS: High risk prediction output: {pred_high}")
        assert pred_high in ["Low", "Medium", "High"]
        assert pred_high == "High", f"Expected High, got {pred_high}"
    except Exception as e:
        print(f"FAIL: Error during model prediction test: {e}")
        sys.exit(1)

    # 5. Check database creation and default seed counts
    try:
        from app import seed_db
        with app.app_context():
            db.create_all()
            seed_db()
            # Verify tables exist and counts
            users_count = User.query.count()
            quotes_count = Quote.query.count()
            print(f"SUCCESS: SQLite Database tables verified.")
            print(f"         Seed counts -> Users: {users_count}, Quotes: {quotes_count}")
            assert users_count >= 3
            assert quotes_count >= 10
    except Exception as e:
        print(f"FAIL: Database connection or seed verification failed: {e}")
        sys.exit(1)

    print("\nALL INTEGRATION VERIFICATION TESTS PASSED SUCCESSFULLY!")


if __name__ == "__main__":
    main()
