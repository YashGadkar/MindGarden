import os
from datetime import datetime
from flask import (
    Flask,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from ml.ml_handler import predictor

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
# AUTHENTICATION ROUTE HELPERS
# =====================================================================

def get_current_user():
    if "user_id" in session:
        return db.session.get(User, session["user_id"])
    return None


# =====================================================================
# CORE DISPATCHER & AUTHENTICATION ROUTES
# =====================================================================

@app.route("/")
def index():
    user = get_current_user()
    if not user:
        return redirect(url_for("login"))

    # Role-based dispatcher
    if user.role == "student":
        profile = StudentProfile.query.filter_by(user_id=user.id).first()
        if not profile:
            return redirect(url_for("onboarding"))
        return redirect(url_for("student_dashboard"))
    elif user.role == "faculty":
        return redirect(url_for("faculty_dashboard"))
    elif user.role == "counsellor":
        return redirect(url_for("counsellor_dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        role = request.form.get("role")

        user = User.query.filter(db.func.lower(User.email) == email).first()
        if user and check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            session["user_name"] = user.name
            session["role"] = user.role
            flash(f"Welcome back, {user.name}!", "success")
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid email or password.", tab="login")

    return render_template("login.html", tab="login")


@app.route("/signup", methods=["POST"])
def signup():
    email = request.form.get("email", "").strip().lower()
    name = request.form.get("name", "").strip()
    password = request.form.get("password", "")
    confirm_password = request.form.get("confirm_password", "")
    role = request.form.get("role", "student")

    # Confirm password check
    if confirm_password and password != confirm_password:
        return render_template("login.html", error="Passwords do not match.", tab="signup")

    if len(password) < 6:
        return render_template("login.html", error="Password must be at least 6 characters long.", tab="signup")

    # Collegiate .edu email domain enforcement
    if not email.endswith(".edu"):
        return render_template(
            "login.html",
            error="College registration requires a valid college email ending with .edu.",
            tab="signup",
        )

    user_exists = User.query.filter(db.func.lower(User.email) == email).first()
    if user_exists:
        return render_template("login.html", error="Email already registered. Try logging in.", tab="signup")

    hashed_pwd = generate_password_hash(password)
    new_user = User(email=email, password_hash=hashed_pwd, name=name, role=role)
    db.session.add(new_user)
    db.session.commit()

    session["user_id"] = new_user.id
    session["user_name"] = new_user.name
    session["role"] = new_user.role
    flash(f"Account successfully created! Welcome to MindGarden, {new_user.name}.", "success")

    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# =====================================================================
# STUDENT ROUTES
# =====================================================================

@app.route("/onboarding", methods=["GET", "POST"])
def onboarding():
    user = get_current_user()
    if not user or user.role != "student":
        return redirect(url_for("login"))

    # Check if profile already exists
    if StudentProfile.query.filter_by(user_id=user.id).first():
        return redirect(url_for("student_dashboard"))

    if request.method == "POST":
        profile = StudentProfile(
            user_id=user.id,
            age=int(request.form.get("age", 22)),
            gender=request.form.get("gender", "Female"),
            academic_year=int(request.form.get("academic_year", 1)),
            academic_performance=float(request.form.get("academic_performance", 70.0)),
            physical_activity=float(request.form.get("physical_activity", 3.0)),
            social_support=float(request.form.get("social_support", 5.0)),
            screen_time=float(request.form.get("screen_time", 5.0)),
            internet_usage=float(request.form.get("internet_usage", 5.0)),
            financial_stress=float(request.form.get("financial_stress", 5.0)),
            family_expectation=float(request.form.get("family_expectation", 5.0)),
            anxiety_score=float(request.form.get("anxiety_score", 3.0)),
            depression_score=float(request.form.get("depression_score", 1.0)),
            burnout_score=float(request.form.get("burnout_score", 2.0)),
            mental_health_index=float(request.form.get("mental_health_index", 7.0)),
        )
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for("student_dashboard"))

    return render_template("student_dashboard.html", onboarding=True)


@app.route("/student/dashboard")
def student_dashboard():
    user = get_current_user()
    if not user or user.role != "student":
        return redirect(url_for("login"))

    profile = StudentProfile.query.filter_by(user_id=user.id).first()
    if not profile:
        return redirect(url_for("onboarding"))

    # Get random Quote for the Thought of the Day
    quote = Quote.query.order_by(db.func.random()).first()
    if not quote:
        quote = Quote(text="Grow through what you go through.", author="Unknown")

    # Fetch daily logs
    logs = DailyCheckin.query.filter_by(user_id=user.id).order_by(DailyCheckin.date.desc()).limit(7).all()
    # Check if submitted today
    today_str = datetime.today().strftime("%Y-%m-%d")
    submitted_today = DailyCheckin.query.filter_by(user_id=user.id, date=today_str).first() is not None

    # Counsellors list for booking & chat
    counsellors = User.query.filter_by(role="counsellor").all()

    # Bookings list
    bookings = SessionBooking.query.filter_by(student_id=user.id).order_by(SessionBooking.date.desc()).all()

    # Get current active chat counsellor
    active_chat_counsellor = counsellors[0] if counsellors else None

    return render_template(
        "student_dashboard.html",
        active_page="dashboard",
        onboarding=False,
        user=user,
        profile=profile,
        quote=quote,
        logs=logs,
        submitted_today=submitted_today,
        counsellors=counsellors,
        bookings=bookings,
        active_chat=active_chat_counsellor,
    )


@app.route("/student/profile/update", methods=["POST"])
def update_profile():
    user = get_current_user()
    if not user or user.role != "student":
        return redirect(url_for("login"))

    profile = StudentProfile.query.filter_by(user_id=user.id).first()
    if profile:
        profile.age = int(request.form.get("age", profile.age))
        profile.gender = request.form.get("gender", profile.gender)
        profile.academic_year = int(request.form.get("academic_year", profile.academic_year))
        profile.academic_performance = float(request.form.get("academic_performance", profile.academic_performance))
        profile.physical_activity = float(request.form.get("physical_activity", profile.physical_activity))
        profile.social_support = float(request.form.get("social_support", profile.social_support))
        profile.screen_time = float(request.form.get("screen_time", profile.screen_time))
        profile.internet_usage = float(request.form.get("internet_usage", profile.internet_usage))
        profile.financial_stress = float(request.form.get("financial_stress", profile.financial_stress))
        profile.family_expectation = float(request.form.get("family_expectation", profile.family_expectation))
        profile.anxiety_score = float(request.form.get("anxiety_score", profile.anxiety_score))
        profile.depression_score = float(request.form.get("depression_score", profile.depression_score))
        profile.burnout_score = float(request.form.get("burnout_score", profile.burnout_score))
        profile.mental_health_index = float(request.form.get("mental_health_index", profile.mental_health_index))
        db.session.commit()
        flash("Baseline profile parameters updated successfully.", "success")

    return redirect(url_for("student_dashboard"))


@app.route("/student/checkin", methods=["POST"])
def student_checkin():
    user = get_current_user()
    if not user or user.role != "student":
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    today_str = datetime.today().strftime("%Y-%m-%d")

    # Check if duplicate checkin for today
    existing = DailyCheckin.query.filter_by(user_id=user.id, date=today_str).first()
    if existing:
        return jsonify({"status": "error", "message": "Already checked in today!"})

    profile = StudentProfile.query.filter_by(user_id=user.id).first()
    if not profile:
        return jsonify({"status": "error", "message": "Profile not completed"}), 400

    sleep_hours = float(request.form.get("sleep_hours", 7.0))
    study_hours = float(request.form.get("study_hours", 4.0))
    exam_pressure = float(request.form.get("exam_pressure", 5.0))
    stress_level = float(request.form.get("stress_level", 4.0))
    mood_score = float(request.form.get("mood_score", 7.0))

    # Form feature dictionary for the Machine Learning model
    student_features = {
        "age": profile.age,
        "gender": profile.gender,
        "academic_year": profile.academic_year,
        "study_hours_per_day": study_hours,
        "exam_pressure": exam_pressure,
        "academic_performance": profile.academic_performance,
        "stress_level": stress_level,
        "anxiety_score": profile.anxiety_score,
        "depression_score": profile.depression_score,
        "sleep_hours": sleep_hours,
        "physical_activity": profile.physical_activity,
        "social_support": profile.social_support,
        "screen_time": profile.screen_time,
        "internet_usage": profile.internet_usage,
        "financial_stress": profile.financial_stress,
        "family_expectation": profile.family_expectation,
        "burnout_score": profile.burnout_score,
        "mental_health_index": profile.mental_health_index,
    }

    # Predict risk level dynamically using XGBoost model
    predicted_risk = predictor.predict(student_features)

    # Save checkin
    checkin = DailyCheckin(
        user_id=user.id,
        date=today_str,
        sleep_hours=sleep_hours,
        study_hours=study_hours,
        exam_pressure=exam_pressure,
        stress_level=stress_level,
        mood_score=mood_score,
        predicted_risk=predicted_risk,
    )
    db.session.add(checkin)
    db.session.commit()

    return jsonify({
        "status": "success",
        "predicted_risk": predicted_risk,
        "log": {
            "date": today_str,
            "sleep_hours": sleep_hours,
            "study_hours": study_hours,
            "exam_pressure": exam_pressure,
            "stress_level": stress_level,
            "mood_score": mood_score,
            "predicted_risk": predicted_risk,
        },
    })


@app.route("/student/book", methods=["POST"])
def book_session():
    user = get_current_user()
    if not user or user.role != "student":
        return redirect(url_for("login"))

    counsellor_id = int(request.form.get("counsellor_id"))
    date = request.form.get("date")
    time = request.form.get("time")

    # Generate mock meeting URL
    meet_link = f"https://meet.google.com/mock-garden-{user.id}-{counsellor_id}"

    booking = SessionBooking(
        student_id=user.id,
        counsellor_id=counsellor_id,
        date=date,
        time=time,
        status="Scheduled",  # Pre-approved for instant user satisfaction
        meet_link=meet_link,
    )
    db.session.add(booking)
    db.session.commit()
    flash(f"Appointment successfully scheduled for {date} at {time}.", "success")

    return redirect(url_for("student_dashboard"))


# =====================================================================
# FACULTY ROUTES
# =====================================================================

@app.route("/faculty/dashboard")
def faculty_dashboard():
    user = get_current_user()
    if not user or user.role != "faculty":
        return redirect(url_for("login"))

    # List all students in database
    students = User.query.filter_by(role="student").all()

    # Pack their profiles & latest faculty ratings (Privacy firewall: NEVER include psychological/risk data)
    student_details = []
    for s in students:
        profile = StudentProfile.query.filter_by(user_id=s.id).first()
        rating = FacultyRating.query.filter_by(student_id=s.id).order_by(FacultyRating.date.desc()).first()
        student_details.append({
            "user": s,
            "profile": profile,
            "rating": rating,
        })

    return render_template("faculty_dashboard.html", active_page="dashboard", user=user, students=student_details)


@app.route("/faculty/rate/<int:student_id>", methods=["POST"])
def faculty_rate(student_id):
    user = get_current_user()
    if not user or user.role != "faculty":
        return redirect(url_for("login"))

    today_str = datetime.today().strftime("%Y-%m-%d")

    timely = request.form.get("timely_submission", "Yes")
    participation = request.form.get("classroom_participation", "Medium")
    notes = request.form.get("notes", "").strip()

    # Save/Update rating
    rating = FacultyRating(
        faculty_id=user.id,
        student_id=student_id,
        date=today_str,
        timely_submission=timely,
        classroom_participation=participation,
        notes=notes,
    )
    db.session.add(rating)
    db.session.commit()
    flash("Academic engagement rating saved successfully.", "success")

    return redirect(url_for("faculty_dashboard"))


# =====================================================================
# COUNSELLOR ROUTES
# =====================================================================

@app.route("/counsellor/dashboard")
def counsellor_dashboard():
    user = get_current_user()
    if not user or user.role != "counsellor":
        return redirect(url_for("login"))

    # Fetch all students
    students = User.query.filter_by(role="student").all()

    # Process priority flagged queue
    flagged_students = []
    all_students = []

    for s in students:
        profile = StudentProfile.query.filter_by(user_id=s.id).first()
        if not profile:
            continue

        # Get last 4 checkins
        checkins = DailyCheckin.query.filter_by(user_id=s.id).order_by(DailyCheckin.date.desc()).limit(4).all()

        consecutive_high_count = 0
        latest_risk = "Low"
        if checkins:
            latest_risk = checkins[0].predicted_risk
            for c in checkins:
                if c.predicted_risk == "High":
                    consecutive_high_count += 1
                else:
                    break

        is_flagged = consecutive_high_count >= 3

        # Fetch newest academic rating
        fac_rating = FacultyRating.query.filter_by(student_id=s.id).order_by(FacultyRating.date.desc()).first()

        student_data = {
            "user": s,
            "profile": profile,
            "latest_risk": latest_risk,
            "consecutive_high_days": consecutive_high_count,
            "is_flagged": is_flagged,
            "faculty_rating": fac_rating,
            "checkins": checkins,
        }

        if is_flagged:
            flagged_students.append(student_data)
        else:
            all_students.append(student_data)

    # Sort flagged students with most high-risk days first
    flagged_students.sort(key=lambda x: x["consecutive_high_days"], reverse=True)

    # Booked session bookings for this counsellor
    sessions = SessionBooking.query.filter_by(counsellor_id=user.id).order_by(SessionBooking.date.desc()).all()
    session_list = []
    for sess in sessions:
        std = db.session.get(User, sess.student_id)
        report = CounsellorReport.query.filter_by(session_id=sess.id).first()
        session_list.append({
            "session": sess,
            "student": std,
            "report": report,
        })

    # Students for chat contacts list
    chat_students = User.query.filter_by(role="student").all()
    active_chat_student = chat_students[0] if chat_students else None

    return render_template(
        "counsellor_dashboard.html",
        active_page="dashboard",
        user=user,
        flagged=flagged_students,
        regular=all_students,
        sessions=session_list,
        chat_students=chat_students,
        active_chat=active_chat_student,
    )


@app.route("/counsellor/report/<int:session_id>", methods=["POST"])
def submit_counsellor_report(session_id):
    user = get_current_user()
    if not user or user.role != "counsellor":
        return redirect(url_for("login"))

    notes = request.form.get("notes")
    improvement = request.form.get("improvement_level")

    # Save report
    report = CounsellorReport(
        session_id=session_id,
        notes=notes,
        improvement_level=improvement,
    )
    db.session.add(report)

    # Mark session as completed
    session_item = db.session.get(SessionBooking, session_id)
    if session_item:
        session_item.status = "Completed"

    db.session.commit()
    flash("Clinical consultation report saved successfully.", "success")
    return redirect(url_for("counsellor_dashboard"))


@app.route("/counsellor/student/details/<int:student_id>")
def get_student_details(student_id):
    user = get_current_user()
    if not user or user.role != "counsellor":
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    student = db.session.get(User, student_id)
    if not student or student.role != "student":
        return jsonify({"status": "error", "message": "Student not found"}), 404

    profile = StudentProfile.query.filter_by(user_id=student_id).first()
    rating = FacultyRating.query.filter_by(student_id=student_id).order_by(FacultyRating.date.desc()).first()
    checkins = DailyCheckin.query.filter_by(user_id=student_id).order_by(DailyCheckin.date.desc()).limit(5).all()

    profile_data = {}
    if profile:
        profile_data = {
            "age": profile.age,
            "gender": profile.gender,
            "academic_year": profile.academic_year,
            "academic_performance": profile.academic_performance,
            "physical_activity": profile.physical_activity,
            "social_support": profile.social_support,
            "screen_time": profile.screen_time,
            "internet_usage": profile.internet_usage,
            "financial_stress": profile.financial_stress,
            "family_expectation": profile.family_expectation,
            "anxiety_score": profile.anxiety_score,
            "depression_score": profile.depression_score,
            "burnout_score": profile.burnout_score,
            "mental_health_index": profile.mental_health_index,
        }

    rating_data = {}
    if rating:
        rating_data = {
            "timely_submission": rating.timely_submission,
            "classroom_participation": rating.classroom_participation,
            "notes": rating.notes,
            "date": rating.date,
        }

    checkins_data = []
    total_sleep = 0
    for c in checkins:
        total_sleep += c.sleep_hours
        checkins_data.append({
            "date": c.date,
            "sleep_hours": c.sleep_hours,
            "study_hours": c.study_hours,
            "exam_pressure": c.exam_pressure,
            "stress_level": c.stress_level,
            "mood_score": c.mood_score,
            "predicted_risk": c.predicted_risk,
        })
    avg_sleep = round(total_sleep / len(checkins), 1) if checkins else "N/A"

    return jsonify({
        "status": "success",
        "student": {
            "id": student.id,
            "name": student.name,
            "email": student.email,
        },
        "profile": profile_data,
        "rating": rating_data,
        "checkins": checkins_data,
        "avg_sleep": avg_sleep,
    })


# =====================================================================
# CHAT SYSTEM API (JSON-based)
# =====================================================================

@app.route("/chat/send", methods=["POST"])
def send_message():
    user = get_current_user()
    if not user:
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    data = request.get_json() or {}
    receiver_id = int(data.get("receiver_id", 0))
    msg_text = data.get("message", "").strip()

    if not msg_text or not receiver_id:
        return jsonify({"status": "error", "message": "Empty message or invalid recipient"}), 400

    message = ChatMessage(
        sender_id=user.id,
        receiver_id=receiver_id,
        message_text=msg_text,
    )
    db.session.add(message)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": {
            "id": message.id,
            "text": message.message_text,
            "sent": True,
            "time": message.timestamp.strftime("%H:%M") if message.timestamp else "",
        },
    })


@app.route("/chat/history/<int:other_user_id>")
def get_chat_history(other_user_id):
    user = get_current_user()
    if not user:
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    messages = ChatMessage.query.filter(
        ((ChatMessage.sender_id == user.id) & (ChatMessage.receiver_id == other_user_id))
        | ((ChatMessage.sender_id == other_user_id) & (ChatMessage.receiver_id == user.id))
    ).order_by(ChatMessage.timestamp.asc()).all()

    history = []
    for msg in messages:
        history.append({
            "id": msg.id,
            "text": msg.message_text,
            "sent": msg.sender_id == user.id,
            "time": msg.timestamp.strftime("%H:%M") if msg.timestamp else "",
        })

    return jsonify(history)


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
        Quote(text="Be gentle with yourself. You are doing the best you can.", author="Unknown"),
    ]
    db.session.bulk_save_objects(quotes_list)

    # 2. Seed Default Users
    student_user = User(
        email="student@college.edu",
        password_hash=generate_password_hash("student123"),
        name="Alex Mercer",
        role="student",
    )
    faculty_user = User(
        email="faculty@college.edu",
        password_hash=generate_password_hash("faculty123"),
        name="Prof. Vance",
        role="faculty",
    )
    counsellor_user = User(
        email="counsellor@college.edu",
        password_hash=generate_password_hash("counsellor123"),
        name="Dr. Sarah Jenkins",
        role="counsellor",
    )
    db.session.add_all([student_user, faculty_user, counsellor_user])
    db.session.commit()
    print("Database seeding completed.")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_db()
