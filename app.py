import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

# =====================================================================
# FLASK & DATABASE INITIALIZATION
# =====================================================================

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "mindgarden_secret_session_key")

# Database Configuration (SQLite local database)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mindgarden.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# =====================================================================
# DATABASE MODELS
# =====================================================================

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'student', 'faculty', 'counsellor'


class StudentProfile(db.Model):
    __tablename__ = "student_profiles"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    age = db.Column(db.Integer, nullable=False, default=22)
    gender = db.Column(db.String(20), nullable=False, default="Female")
    academic_year = db.Column(db.Integer, nullable=False, default=1)
    academic_performance = db.Column(db.Float, nullable=False, default=70.0)
    physical_activity = db.Column(db.Float, nullable=False, default=3.0)
    social_support = db.Column(db.Float, nullable=False, default=5.0)
    screen_time = db.Column(db.Float, nullable=False, default=5.0)
    internet_usage = db.Column(db.Float, nullable=False, default=5.0)
    financial_stress = db.Column(db.Float, nullable=False, default=5.0)
    family_expectation = db.Column(db.Float, nullable=False, default=5.0)
    anxiety_score = db.Column(db.Float, nullable=False, default=3.0)
    depression_score = db.Column(db.Float, nullable=False, default=1.0)
    burnout_score = db.Column(db.Float, nullable=False, default=2.0)
    mental_health_index = db.Column(db.Float, nullable=False, default=7.0)


class DailyCheckin(db.Model):
    __tablename__ = "daily_checkins"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    date = db.Column(db.String(10), nullable=False)  # YYYY-MM-DD
    sleep_hours = db.Column(db.Float, nullable=False, default=7.0)
    study_hours = db.Column(db.Float, nullable=False, default=4.0)
    exam_pressure = db.Column(db.Float, nullable=False, default=5.0)
    stress_level = db.Column(db.Float, nullable=False, default=4.0)
    mood_score = db.Column(db.Float, nullable=False, default=7.0)  # 1 to 10
    predicted_risk = db.Column(db.String(20), nullable=False)  # 'Low', 'Medium', 'High'


class FacultyRating(db.Model):
    __tablename__ = "faculty_ratings"
    id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    date = db.Column(db.String(10), nullable=False)  # YYYY-MM-DD
    timely_submission = db.Column(db.String(10), nullable=False, default="Yes")  # 'Yes', 'No'
    classroom_participation = db.Column(db.String(10), nullable=False, default="Medium")  # 'High', 'Medium', 'Low'
    notes = db.Column(db.Text, nullable=True)


class SessionBooking(db.Model):
    __tablename__ = "session_bookings"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    counsellor_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    date = db.Column(db.String(10), nullable=False)  # YYYY-MM-DD
    time = db.Column(db.String(5), nullable=False)  # HH:MM
    status = db.Column(db.String(20), nullable=False, default="Pending")  # 'Pending', 'Scheduled', 'Completed'
    meet_link = db.Column(db.String(200), nullable=True)


class CounsellorReport(db.Model):
    __tablename__ = "counsellor_reports"
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey("session_bookings.id"), nullable=False)
    notes = db.Column(db.Text, nullable=False)
    improvement_level = db.Column(db.String(50), nullable=False)  # 'Significant', 'Moderate', 'No Change', 'Deterioration'


class ChatMessage(db.Model):
    __tablename__ = "chat_messages"
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    message_text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Quote(db.Model):
    __tablename__ = "quotes"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), nullable=False)
    author = db.Column(db.String(100), nullable=False)


# =====================================================================
# SEED INITIALIZATION DATA
# =====================================================================

def seed_db():
    # Only seed if quotes table is empty
    if Quote.query.first():
        return

    print("Seeding SQLite database with default data...")

    # 1. Seed motivational mental health quotes
    quotes_list = [
        Quote(text="You are stronger than you think. Keep taking one step at a time.", author="Unknown"),
        Quote(text="Mental health is not a destination, but a process. It's about how you drive, not where you're going.", author="Noam Shpancer"),
        Quote(text="There is hope, even when your brain tells you there isn't.", author="John Green"),
        Quote(text="This feeling will pass. You have survived all of your difficult days so far.", author="Unknown"),
        Quote(text="Your academic performance does not define your worth as a human being.", author="MindGarden Team"),
        Quote(text="Self-care is how you take your power back.", author="Lalah Delia"),
        Quote(text="It is okay to ask for help. Asking for support is a sign of strength.", author="Unknown"),
        Quote(text="Rest is not lazy; it is essential recovery.", author="Unknown"),
        Quote(text="Do what you can, with what you have, where you are.", author="Theodore Roosevelt"),
        Quote(text="Be gentle with yourself. You are doing the best you can.", author="Unknown")
    ]
    db.session.bulk_save_objects(quotes_list)

    # 2. Seed Default Users
    # Student Account (Needs onboarding)
    student_user = User(
        email="student@college.edu",
        password_hash=generate_password_hash("student123"),
        name="Alex Mercer",
        role="student"
    )
    # Faculty Account
    faculty_user = User(
        email="faculty@college.edu",
        password_hash=generate_password_hash("faculty123"),
        name="Prof. Vance",
        role="faculty"
    )
    # Counsellor Account
    counsellor_user = User(
        email="counsellor@college.edu",
        password_hash=generate_password_hash("counsellor123"),
        name="Dr. Sarah Jenkins",
        role="counsellor"
    )
    db.session.add_all([student_user, faculty_user, counsellor_user])
    db.session.commit()
    print("Database seeding completed.")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_db()
