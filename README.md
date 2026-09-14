<div align="center">

# 🌱 MindGarden: Student Mental Health Prediction & Support Platform
### *An Intelligent, Multi-Stakeholder Intervention Ecosystem Powered by XGBoost, Flask, and the Ditto Design System*

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask Framework](https://img.shields.io/badge/Flask-3.1.3-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![XGBoost](https://img.shields.io/badge/XGBoost-3.4.1-EB392E?style=for-the-badge&logo=xgboost&logoColor=white)](https://xgboost.readthedocs.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License: Academic / Educational](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

<br/>

> **MindGarden** is a full-stack, enterprise-grade, privacy-first collegiate wellness platform designed to proactively monitor, analyze, and predict student mental health vulnerability. By integrating multi-class gradient-boosted decision trees (`XGBoost`) with an accessible, human-centered UI ("Ditto" Design System), MindGarden bridges the communication gap between **Students**, **Faculty Mentors**, and **Campus Counsellors**.

<br/>

```
       🌱 Student Check-in  ───>  🤖 XGBoost Inference Pipeline  ───>  📊 Dynamic Risk Score
               │                                                              │
               ▼                                                              ▼
       🎓 Faculty Mentorship  (Academic Observations)           🩺 Priority Counsellor Flag
               │                                                              │
               └───────────────► 🛡️ Integrated Intervention Hub ◄─────────────┘
```

</div>

---

## 📑 Master Table of Contents

1. [Executive Summary & Product Vision](#1-executive-summary--product-vision)
   - [1.1 The Academic Stress Epidemic](#11-the-academic-stress-epidemic)
   - [1.2 MindGarden Paradigm Shift](#12-mindgarden-paradigm-shift)
   - [1.3 The Stakeholder Triad](#13-the-stakeholder-triad)
   - [1.4 Key Differentiating Features](#14-key-differentiating-features)
2. [End-to-End System Architecture](#2-end-to-end-system-architecture)
   - [2.1 High-Level Architecture Diagram](#21-high-level-architecture-diagram)
   - [2.2 Architectural Layers & Component Separation](#22-architectural-layers--component-separation)
   - [2.3 Data Pipeline & Inference Request Lifecycle](#23-data-pipeline--inference-request-lifecycle)
   - [2.4 Cross-Cutting Concerns & Security Boundaries](#24-cross-cutting-concerns--security-boundaries)
3. [Stakeholder Portals & User Journey Mapping](#3-stakeholder-portals--user-journey-mapping)
   - [3.1 Student Experience & Daily Tracking Journey](#31-student-experience--daily-tracking-journey)
   - [3.2 Faculty Experience & Academic Observational Logging](#32-faculty-experience--academic-observational-logging)
   - [3.3 Counsellor Control Center & Priority Clinical Intervention](#33-counsellor-control-center--priority-clinical-intervention)
4. [Machine Learning & Predictive Modeling Deep Dive](#4-machine-learning--predictive-modeling-deep-dive)
   - [4.1 Problem Formulation & Classification Objective](#41-problem-formulation--classification-objective)
   - [4.2 The 18-Feature Psychological & Academic Vector](#42-the-18-feature-psychological--academic-vector)
   - [4.3 Dataset Characteristics (`CEP_Train_Data.csv`)](#43-dataset-characteristics-cep_train_datacsv)
   - [4.4 Data Preprocessing Pipeline (`ColumnTransformer`)](#44-data-preprocessing-pipeline-columntransformer)
   - [4.5 Class Imbalance Mitigation via Sample Weighting](#45-class-imbalance-mitigation-via-sample-weighting)
   - [4.6 XGBoost Mathematical Foundation & Objective Formulation](#46-xgboost-mathematical-foundation--objective-formulation)
   - [4.7 Hyperparameter Optimization & Model Regularization](#47-hyperparameter-optimization--model-regularization)
   - [4.8 Inference Runtime Engine (`ml/ml_handler.py`)](#48-inference-runtime-engine-mlml_handlerpy)
   - [4.9 Training Execution & Pipeline Serialization (`ml/train_and_save_model.py`)](#49-training-execution--pipeline-serialization-mltrain_and_save_modelpy)
5. [Database Architecture & Schema Specification](#5-database-architecture--schema-specification)
   - [5.1 Entity Relationship Diagram (ERD)](#51-entity-relationship-diagram-erd)
   - [5.2 Data Dictionary & Table Schemas](#52-data-dictionary--table-schemas)
   - [5.3 Relational Constraints & Foreign Key Policies](#53-relational-constraints--foreign-key-policies)
   - [5.4 Database Seeding & First-Run Initialization](#54-database-seeding--first-run-initialization)
6. [Backend Engineering & Flask Server Implementation](#6-backend-engineering--flask-server-implementation)
   - [6.1 Application Entrypoint & Bootstrap (`app.py`)](#61-application-entrypoint--bootstrap-apppy)
   - [6.2 Complete HTTP Route Catalog](#62-complete-http-route-catalog)
   - [6.3 Session Security & Authentication Workflows](#63-session-security--authentication-workflows)
   - [6.4 Role-Based Access Control (RBAC) Dispatcher](#64-role-based-access-control-rbac-dispatcher)
   - [6.5 Asynchronous AJAX Route Handlers](#65-asynchronous-ajax-route-handlers)
   - [6.6 Server-Side Validation & Security Policies](#66-server-side-validation--security-policies)
7. [Frontend Architecture & "Ditto" Design System](#7-frontend-architecture--ditto-design-system)
   - [7.1 Philosophy of the Sunlit Wildflower Atelier ("Ditto")](#71-philosophy-of-the-sunlit-wildflower-atelier-ditto)
   - [7.2 CSS Custom Properties & Design Token Dictionary](#72-css-custom-properties--design-token-dictionary)
   - [7.3 Typographic System & Visual Hierarchy](#73-typographic-system--visual-hierarchy)
   - [7.4 Tactile UI Components & Micro-Interactions](#74-tactile-ui-components--micro-interactions)
   - [7.5 Client-Side Subsystems & JavaScript Engines (`static/script.js`)](#75-client-side-subsystems--javascript-engines-staticscriptjs)
   - [7.6 Interactive Visualizations with Chart.js](#76-interactive-visualizations-with-chartjs)
8. [Comprehensive REST API Reference](#8-comprehensive-rest-api-reference)
   - [8.1 Authentication Endpoints](#81-authentication-endpoints)
   - [8.2 Student Action Endpoints](#82-student-action-endpoints)
   - [8.3 Faculty Action Endpoints](#83-faculty-action-endpoints)
   - [8.4 Counsellor Clinical Endpoints](#84-counsellor-clinical-endpoints)
   - [8.5 Bi-Directional Messaging & Chat Endpoints](#85-bi-directional-messaging--chat-endpoints)
9. [Complete File & Directory Manifest](#9-complete-file--directory-manifest)
   - [9.1 Repository Tree Structure](#91-repository-tree-structure)
   - [9.2 Detailed Module-by-Module Breakdown](#92-detailed-module-by-module-breakdown)
10. [Installation, Setup & Local Environment Configuration](#10-installation-setup--local-environment-configuration)
    - [10.1 Hardware & Software Prerequisites](#101-hardware--software-prerequisites)
    - [10.2 Step-by-Step Installation Walkthrough](#102-step-by-step-installation-walkthrough)
    - [10.3 Virtual Environment Configuration](#103-virtual-environment-configuration)
    - [10.4 Python Package Dependency Installation](#104-python-package-dependency-installation)
    - [10.5 Database Generation & Seed Credentials](#105-database-generation--seed-credentials)
    - [10.6 Execution of the Local Development Server](#106-execution-of-the-local-development-server)
11. [Model Training & Machine Learning Operations Guide](#11-model-training--machine-learning-operations-guide)
    - [11.1 Preparing the Training Corpus (`ml/CEP_Train_Data.csv`)](#111-preparing-the-training-corpus-mlcep_train_datacsv)
    - [11.2 Executing the Training Script](#112-executing-the-training-script)
    - [11.3 Inspecting Pipeline Weights & Artifacts](#113-inspecting-pipeline-weights--artifacts)
    - [11.4 Research & Experimentation via Jupyter (`ml/CEP_Code.ipynb`)](#114-research--experimentation-via-jupyter-mlcep_codeipynb)
12. [Quality Assurance, Testing & Verification Suite](#12-quality-assurance-testing--verification-suite)
    - [12.1 Automated Integration Verification (`tests/verify_app_integration.py`)](#121-automated-integration-verification-testsverify_app_integrationpy)
    - [12.2 Integration Test Assertions & Test Criteria](#122-integration-test-assertions--test-criteria)
    - [12.3 Role-by-Role Manual Verification Playbook](#123-role-by-role-manual-verification-playbook)
    - [12.4 Edge Cases, Boundary Tests, and Error Trapping](#124-edge-cases-boundary-tests-and-error-trapping)
13. [Security, Privacy, and Ethical AI Considerations](#13-security-privacy-and-ethical-ai-considerations)
    - [13.1 Strict Separation of Powers & FERPA/HIPAA Principles](#131-strict-separation-of-powers--ferpahipaa-principles)
    - [13.2 Data Protection, Passwords, and Session Cryptography](#132-data-protection-passwords-and-session-cryptography)
    - [13.3 Client-Side XSS Mitigation & DOM Sanitization](#133-client-side-xss-mitigation--dom-sanitization)
    - [13.4 Ethical AI Principles & Clinical Human-in-the-Loop Safeguards](#134-ethical-ai-principles--clinical-human-in-the-loop-safeguards)
14. [Production Deployment & Scalability Architecture](#14-production-deployment--scalability-architecture)
    - [14.1 WSGI Production Web Servers (Gunicorn / Waitress)](#141-wsgi-production-web-servers-gunicorn--waitress)
    - [14.2 Reverse Proxy Configuration with Nginx](#142-reverse-proxy-configuration-with-nginx)
    - [14.3 Transitioning from SQLite to PostgreSQL](#143-transitioning-from-sqlite-to-postgresql)
    - [14.4 Asynchronous Worker Infrastructure (Celery & Redis)](#144-asynchronous-worker-infrastructure-celery--redis)
    - [14.5 Containerization with Docker & Docker Compose](#145-containerization-with-docker--docker-compose)
15. [Troubleshooting & Frequently Asked Questions (FAQ)](#15-troubleshooting--frequently-asked-questions-faq)
    - [15.1 Diagnostic Checklist](#151-diagnostic-checklist)
    - [15.2 Common Issues & Resolutions](#152-common-issues--resolutions)
    - [15.3 Comprehensive Developer & User FAQ](#153-comprehensive-developer--user-faq)
16. [Appendix: References, Citations, & Acknowledgments](#16-appendix-references-citations--acknowledgments)

---

## 1. Executive Summary & Product Vision

### 1.1 The Academic Stress Epidemic
Over the past decade, psychological distress among university students has reached unprecedented levels globally. Rigorous academic expectations, high-stakes examination cycles, social isolation, financial insecurity, and hyper-connected digital screen exposure combine to create an environment where anxiety, depressive symptoms, and academic burnout flourish. 

Traditional campus mental health infrastructures suffer from severe structural shortcomings:
* **Passive Engagement Models:** Universities typically rely on students recognizing their own deteriorating psychological state, overcoming substantial social stigma, and voluntarily seeking help at a physical counselling center.
* **Delayed Interventions:** By the time a student reaches clinical support services, they are frequently in acute crisis—experiencing severe depressive episodes, academic failure, or imminent dropout risk.
* **Siloed Context:** Academic performance and psychological wellbeing are treated as completely disconnected domains. Faculty members observe attendance drops, late submissions, and disengagement in lecture halls, yet have no secure, privacy-compliant channel to flag concerns to clinical professionals without violating student privacy.
* **Intimidating Clinical Software:** Existing health management systems are sterile, intimidating, and clinical in design, driving away digital-native students who crave warmth, empathy, and intuitive mobile interfaces.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TRADITIONAL CAMPUS INFRASTRUCTURE                      │
│                                                                             │
│  [Student Suffering] ──(Silence)──> [Crisis Point] ──> [Emergency Center]   │
│           ▲                                                    ▲            │
│           │                                                    │            │
│  [Faculty Notices Drops] ──(No Channel)────────────────────────┘            │
└─────────────────────────────────────────────────────────────────────────────┘

                                      VS

┌─────────────────────────────────────────────────────────────────────────────┐
│                         MINDGARDEN INTEGRATED ECOSYSTEM                     │
│                                                                             │
│  [Daily Habits] ──> [AI Predictor] ──> [Risk Trend] ──> [Flagged Queue]    │
│           │                                                    │            │
│           ▼                                                    ▼            │
│  [Faculty Ratings] ───────(Privacy Shield)─────────────► [Dr. Counsellor]   │
│                                                                │            │
│  [Student Portal] ◄───────(Instant Video / Chat)───────────────┘            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 MindGarden Paradigm Shift
MindGarden re-engineers collegiate psychological support from a **reactive crisis response** into a **proactive, machine-learning-assisted prevention ecosystem**. 

Rather than waiting for catastrophic student collapse, MindGarden monitors micro-indicators of wellbeing through low-friction daily check-ins (sleep hours, study load, exam pressure, subjective stress, and mood). These daily observations are fed into an optimized gradient-boosted decision tree classifier (`XGBoost`), which dynamically evaluates the student's risk level (`Low`, `Medium`, or `High`).

When a student registers sustained high-risk classifications (defined algorithmically as **3 or more consecutive high-risk days**), MindGarden’s automated triage system escalates the student into an **AI Priority Flagged Queue** in the campus counsellor's control center, enabling immediate, preventative clinical outreach before a crisis materializes.

### 1.3 The Stakeholder Triad
MindGarden is built around three distinct collegiate stakeholders, orchestrating a coordinated safety net around every student while preserving strict role-based data boundaries:

| Stakeholder | Primary Goals | Key Capabilities | Information Privacy Boundary |
|---|---|---|---|
| **Student** | Self-monitoring, emotional grounding, barrier-free access to support. | Onboarding psychological baseline survey; daily tactile habit check-ins; dynamic AI risk assessment; inspirational affirmations; 1-click consultation scheduling with automatic meeting link generation; confidential real-time counsellor chat. | Full access to personal trends, history, and chat. Cannot view faculty private notes or other students' records. |
| **Faculty Member** | Academic mentorship, identifying disengaged learners, tracking course participation. | Course roster directory; academic engagement evaluations (timely assignment submissions, classroom participation level, qualitative observational remarks). | **Strictly prohibited** from viewing student psychological scores, baseline anxiety/depression levels, clinical notes, or predicted risk categories. |
| **Campus Counsellor** | Clinical triage, preventative intervention, evidence-backed therapy tracking. | AI Priority Flagged Queue for sustained high-risk streaks; 360° comprehensive student drilldown modal (baseline psychometrics + faculty academic remarks + 5-day habit trends + calculated sleep averages); appointment manager; clinical session outcome reporting (*Significant, Moderate, No Change, Deterioration*); live multi-student messenger. | Complete access to aggregated psychological, behavioral, and academic engagement data for clinical intervention. |

### 1.4 Key Differentiating Features
* **Gradient-Boosted Triage Engine:** Employs an 18-feature machine learning model trained on extensive student wellness profiles, eliminating subjective human bias in early risk detection.
* **AI Early Warning Sustained Streak Detection:** Does not overreact to a single bad day. Instead, it tracks consecutive high-risk evaluations ($\ge 3$ consecutive logs) to accurately differentiate between temporary exam stress and dangerous chronic deterioration.
* **Warm "Ditto" Design Language:** Replaces clinical sterility with organic, garden-themed aesthetics (warm cream canvases, soft meadow green surfaces, vibrant yellow accents, and tactile 3D interactive controls), dramatically increasing student engagement and adherence.
* **Architectural Privacy Shield:** Implements strict Role-Based Access Control (RBAC) at both the routing layer and template level, ensuring academic and psychological data remain strictly partitioned according to ethical guidelines.
* **Zero-Dependency Core Execution:** Operates cleanly on a lightweight, self-contained Python Flask and SQLite foundation with minimal server overhead, making it immediately deployable across collegiate networks.

---

## 2. End-to-End System Architecture

### 2.1 High-Level Architecture Diagram
The following Mermaid architecture diagram illustrates the end-to-end topology of MindGarden, tracing user interactions through the presentation, routing, application, inference, and persistence tiers:

```mermaid
graph TB
    subgraph ClientTier ["CLIENT PRESENTATION TIER (Browser / Responsive UI)"]
        direction TB
        S_VIEW["Student Dashboard<br/>(student_dashboard.html)"]
        F_VIEW["Faculty Dashboard<br/>(faculty_dashboard.html)"]
        C_VIEW["Counsellor Dashboard<br/>(counsellor_dashboard.html)"]
        AUTH_VIEW["Authentication Portal<br/>(login.html)"]
        
        CSS_ENGINE["Ditto Design System<br/>(static/style.css)"]
        JS_ENGINE["Client Interactivity & AJAX<br/>(static/script.js)"]
        CHART_ENGINE["Visual Analytics Engine<br/>(Chart.js CDN)"]
        
        S_VIEW --- CSS_ENGINE
        F_VIEW --- CSS_ENGINE
        C_VIEW --- CSS_ENGINE
        AUTH_VIEW --- CSS_ENGINE
        
        S_VIEW --- JS_ENGINE
        C_VIEW --- JS_ENGINE
        S_VIEW --- CHART_ENGINE
    end

    subgraph GatewayTier ["GATEWAY & DISPATCHING LAYER"]
        FLASK_APP["Flask Core Web Server<br/>(app.py)"]
        AUTH_MGR["Session & Auth Manager<br/>(Werkzeug Security)"]
        RBAC_MGR["Role-Based Route Dispatcher<br/>(Index Router)"]
        
        FLASK_APP --- AUTH_MGR
        FLASK_APP --- RBAC_MGR
    end

    subgraph ServiceTier ["BUSINESS LOGIC & API ENDPOINTS"]
        STUDENT_SVC["Student Service<br/>(/student/checkin, /student/book)"]
        FACULTY_SVC["Faculty Service<br/>(/faculty/rate)"]
        CLINICAL_SVC["Counsellor Service<br/>(/counsellor/report, /counsellor/details)"]
        CHAT_SVC["Chat Service<br/>(/chat/send, /chat/history)"]
    end

    subgraph MachineLearningTier ["PREDICTIVE INFERENCE ENGINE"]
        ML_SINGLETON["MLPredictor Singleton<br/>(ml/ml_handler.py)"]
        PREPROCESSOR["ColumnTransformer<br/>(OneHotEncoder + Passthrough)"]
        XGB_CLASSIFIER["XGBClassifier Model<br/>(student_risk_model.pkl)"]
        LABEL_DEC["LabelEncoder Inverse<br/>(0->High, 1->Low, 2->Medium)"]
        
        ML_SINGLETON --> PREPROCESSOR
        PREPROCESSOR --> XGB_CLASSIFIER
        XGB_CLASSIFIER --> LABEL_DEC
    end

    subgraph PersistenceTier ["PERSISTENCE & STORAGE LAYER"]
        SQLALCHEMY["Flask-SQLAlchemy ORM"]
        SQLITE_DB[("mindgarden.db<br/>(SQLite Database)")]
        
        SQLALCHEMY --- SQLITE_DB
    end

    %% Client to Gateway
    S_VIEW -->|HTTP POST / AJAX| FLASK_APP
    F_VIEW -->|HTTP POST| FLASK_APP
    C_VIEW -->|HTTP GET / POST / AJAX| FLASK_APP
    AUTH_VIEW -->|HTTP POST Credentials| FLASK_APP

    %% Gateway to Services
    RBAC_MGR --> STUDENT_SVC
    RBAC_MGR --> FACULTY_SVC
    RBAC_MGR --> CLINICAL_SVC
    RBAC_MGR --> CHAT_SVC

    %% Services to ML
    STUDENT_SVC -->|18-Feature Vector| ML_SINGLETON
    LABEL_DEC -->|Predicted Risk: Low/Medium/High| STUDENT_SVC

    %% Services to Database
    AUTH_MGR --> SQLALCHEMY
    STUDENT_SVC --> SQLALCHEMY
    FACULTY_SVC --> SQLALCHEMY
    CLINICAL_SVC --> SQLALCHEMY
    CHAT_SVC --> SQLALCHEMY
```

### 2.2 Architectural Layers & Component Separation
MindGarden enforces strict separation of concerns across four primary software layers:

#### 1. Presentation Layer (`templates/`, `static/`)
* Built using semantic HTML5, CSS3 Custom Properties (Vanilla CSS), and Vanilla JavaScript (ES6+).
* Enforces accessibility standards (WCAG-compliant contrast ratios, ARIA labeling, keyboard navigation for modals and sliders).
* Avoids heavyweight client frameworks (such as React or Angular) to eliminate build-step complexity, ensure blazing-fast initial load times, and guarantee cross-platform device compatibility.
* Utilizes asynchronous `fetch()` calls for dynamic interactions (daily check-in submission, polling chat updates, student profile drilldowns) without requiring disruptive full-page refreshes.

#### 2. Application & Routing Layer (`app.py`)
* Implemented on Flask 3.1.3, providing lightweight, flexible WSGI routing.
* Manages user session state via encrypted client-side cookies signed by a server-side `app.secret_key`.
* Enforces authentication guards across all protected endpoints, inspecting `session["user_id"]` and verifying `session["role"]`.
* Handles input sanitization, form encoding, collegiate `.edu` email domain enforcement, and database transaction commits/rollbacks.

#### 3. Inference Subsystem (`ml/`)
* Decoupled from the core web server through an encapsulation layer (`MLPredictor` in `ml/ml_handler.py`).
* Operates as a singleton loaded into server memory during process startup, preventing redundant disk I/O during request processing.
* Features a fallback safety architecture: if model weights are missing or inputs fail schema checks, the system logs the issue and returns a safe fallback assessment (`Low`) to prevent system crashes.

#### 4. Persistence Layer (`instance/mindgarden.db`)
* Managed through SQLAlchemy ORM (via `Flask-SQLAlchemy 3.1.1`).
* Leverages SQLite for zero-configuration, ACID-compliant relational storage.
* Implements cascading referential integrity, foreign key associations, and unique constraints across 8 normalized tables.

### 2.3 Data Pipeline & Inference Request Lifecycle
To understand how data flows through MindGarden during runtime, consider the complete lifecycle of a **Student Daily Check-in**:

```
[1. Student Inputs Sliders]
   (Sleep=5.5 hrs, Study=6.0 hrs, Exam Pressure=8/10, Stress=8/10, Mood=3/10)
         │
         ▼
[2. Client Interactivity (static/script.js)]
   Captures form submit event -> Prevents default refresh ->
   Dispatches async HTTP POST payload to /student/checkin via Fetch API
         │
         ▼
[3. Route Dispatcher & Session Guard (app.py)]
   Authenticates session["user_id"] -> Validates role == "student" ->
   Verifies student has not already submitted a check-in for today's date
         │
         ▼
[4. Profile Parameter Merging (app.py)]
   Fetches StudentProfile from SQLite (Age, Gender, Academic Year, Social Support,
   Screen Time, Baseline Anxiety, Baseline Depression, Burnout Score, etc.) ->
   Merges daily metrics with baseline metrics into an 18-Feature Vector
         │
         ▼
[5. Machine Learning Predictor (ml/ml_handler.py)]
   Converts 18-Feature dictionary into a 1-row Pandas DataFrame ->
   Reorders columns to match exact training signature ->
   Passes DataFrame to Scikit-Learn Pipeline:
     a) OneHotEncoder transforms nominal 'gender' feature
     b) Passthrough retains 17 numerical variables
     c) XGBClassifier calculates class probability distribution (multi:softprob)
     d) LabelEncoder inversely decodes numeric class index to string ("High")
         │
         ▼
[6. Database Persistence (app.py)]
   Instantiates DailyCheckin model with predicted_risk="High" ->
   Persists record to mindgarden.db via db.session.commit()
         │
         ▼
[7. Dynamic Client Re-rendering (student_dashboard.html)]
   Server returns JSON response ->
   JavaScript animates check-in card into completed state ->
   Prepends new row to history table ->
   Dynamically appends new datapoint to Chart.js trendline canvas
         │
         ▼
[8. Counsellor Early Warning Triage (counsellor_dashboard.html)]
   Upon counsellor login, system queries DailyCheckin records ->
   Detects if consecutive high-risk days >= 3 ->
   Elevates student to the AI Priority Flagged Queue
```

### 2.4 Cross-Cutting Concerns & Security Boundaries
* **Strict Role-Based Information Siloing:** The application maintains an absolute firewall between academic feedback and clinical records. Faculty accounts have zero access to psychological scores or risk levels; students have zero access to faculty private notes; counsellors have full clinical visibility to facilitate intervention.
* **Defensive Input Validation:** String lengths, numeric boundaries (e.g., slider values strictly clamped between min and max), email domain patterns, and cryptographic password checks are enforced at both frontend and backend boundaries.
* **XSS Defense & Sanitization:** All dynamic DOM insertions in client-side scripts utilize a dedicated string escape helper (`window.escapeHtml`) to neutralize potential Cross-Site Scripting (XSS) vectors.

---

## 3. Stakeholder Portals & User Journey Mapping

MindGarden provides tailored user interfaces designed around the specific operational responsibilities of each stakeholder.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           MINDGARDEN PORTAL OVERVIEW                        │
├──────────────────────┬──────────────────────┬───────────────────────────────┤
│    STUDENT PORTAL    │    FACULTY PORTAL    │       COUNSELLOR PORTAL       │
├──────────────────────┼──────────────────────┼───────────────────────────────┤
│ • Baseline Survey    │ • Student Directory  │ • AI Priority Flagged Queue   │
│ • Daily Habit Sliders│ • On-Time Submissions│ • 360° Drilldown Profile      │
│ • Real-time AI Risk  │ • Class Participation│ • Consultation Scheduler      │
│ • Thought of the Day │ • Observational Notes│ • Clinical Progress Reports   │
│ • Instant Booking    │ • Strict Privacy     │ • Multi-Student Live Messenger│
│ • Counsellor Chat    │   Firewall           │ • Risk Analytics Dashboard    │
└──────────────────────┴──────────────────────┴───────────────────────────────┘
```

### 3.1 Student Experience & Daily Tracking Journey

#### Step 1: Authentication & Onboarding Baseline Assessment
Upon first creating an account and logging in, students without a registered profile are automatically redirected to the **Onboarding Baseline Survey** (`/onboarding`). 

Students complete a 14-parameter intake survey capturing:
* Demographics: Age, Gender identity, Academic collegiate year (Freshman through Senior).
* Academic standing: Self-reported cumulative academic performance percentage (30% to 100%).
* Daily lifestyle baselines: Physical activity hours, perceived social support rating (0–10), average daily screen time, recreational internet hours.
* Environmental stressors: Financial strain index (0–10), family academic expectations pressure (0–10).
* Baseline clinical indicators: Baseline anxiety score (0–10), depression score (0–10), burnout score (0–10), and overall self-rated mental health index (0–10).

Submitting this survey persists their `StudentProfile` record and unlocks their active student dashboard.

#### Step 2: The Student Dashboard & Daily Habit Tracking
The active student dashboard (`templates/student_dashboard.html`) is designed to feel like a warm, supportive personal haven:
* **Thought of the Day:** Every morning, the application dynamically selects an inspiring, psychologically grounded mental health quote from the database, reinforcing growth mindset habits.
* **Tactile Daily Check-In Form:** Students record their current daily metrics using interactive range sliders:
  1. *Sleep Hours Last Night* (2.0 to 12.0 hours, in 0.5-hour increments)
  2. *Study Hours Today* (0.0 to 15.0 hours, in 0.5-hour increments)
  3. *Exam / Academic Pressure* (0 to 10 scale)
  4. *Current Stress Level* (0 to 10 scale)
  5. *Overall Mood Score* (1 to 10 scale)
* **Immediate AI Feedback:** Clicking "Submit Daily Log" dispatches an AJAX request to the backend. The embedded XGBoost model immediately calculates their current risk category (`Low`, `Medium`, or `High`), updating the dashboard in real time with an animated confirmation message.
* **Duplicate Submission Prevention:** Students can submit exactly one check-in per calendar day, preventing skewed data clustering and redundant records.

#### Step 3: Interactive Visual Analytics & Historical Log
* Below the check-in form, an interactive **Chart.js** line graph visualizes the student's 7-day wellness trendlines, plotting nightly sleep duration, daily study hours, and overall mood trajectory simultaneously.
* An adjacent table displays recent check-in dates alongside their corresponding AI risk classification badge.

#### Step 4: Virtual Consultation Scheduling
* When students feel overwhelmed, they can click "Book Call" to launch a scheduling modal.
* Selecting a counsellor, target date, and time slot immediately reserves a session and generates an instant mock Google Meet link (`https://meet.google.com/mock-garden-{student_id}-{counsellor_id}`), allowing immediate access to remote support.

#### Step 5: Confidential Counsellor Messenger
* The dashboard features an integrated, real-time messaging panel.
* Students can choose any campus counsellor from a dropdown selector and send private, end-to-end synchronized messages with automatic 4.5-second polling and non-destructive scroll management.

#### Step 6: Dynamic Profile Management
* If a student's life circumstances shift (e.g., changes in financial stability, family pressure, or baseline health), they can update their baseline parameters at any time via the "Update Profile" card.

---

### 3.2 Faculty Experience & Academic Observational Logging

The Faculty Portal (`templates/faculty_dashboard.html`) empowers professors and teaching assistants to act as observant mentors without turning them into amateur therapists or compromising student privacy.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       FACULTY OBSERVATION WORKFLOW                          │
│                                                                             │
│  [Class Roster] ──> [Select Student] ──> [Record Academic Observations]     │
│                                                    │                        │
│                                                    ├─ Timely Submissions    │
│                                                    ├─ Class Participation   │
│                                                    └─ Behavioral Notes      │
│                                                                             │
│  [Save Record] ──> Stored in DB ──> Counsellor Views in 360° Modal         │
│                                                                             │
│  * NOTE: Faculty CANNOT view student psychological scores or AI risk!       │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Step 1: Active Student Directory
* Upon login, faculty members are presented with an enrolled student directory listing all registered students in their department, showing name, email, and academic year.

#### Step 2: Academic Engagement Logging
Faculty can click "Rate" or "Edit" next to any student to open the dedicated evaluation drawer. Faculty assess students on three observable academic dimensions:
1. **Timely Assignment Submissions:** Categorized as *Yes (Always/Mostly on Time)* or *No (Frequently Late/Missing)*.
2. **Classroom Participation Level:** Evaluated as *High (Very Active, Asks Questions)*, *Medium (Moderately Active)*, or *Low (Quiet, Disengaged)*.
3. **Qualitative Observational Notes:** Free-text area to record concrete, behavioral remarks (e.g., *"Alex missed three consecutive Monday morning lectures and appeared visibly exhausted during lab work today."*).

#### Step 3: Weekly Engagement Summary Table
* The portal displays a consolidated weekly summary table showing the last rating date, submission consistency, and participation status for all students.

#### Step 4: Strict Privacy Boundary
* **Compliance & FERPA/HIPAA Principles:** Faculty members **never** see psychological test scores, baseline depression ratings, daily check-in histories, or predicted risk classifications. This intentional barrier protects students from academic bias while ensuring faculty observations reach clinical professionals.

---

### 3.3 Counsellor Control Center & Priority Clinical Intervention

The Counsellor Portal (`templates/counsellor_dashboard.html`) serves as an AI-augmented clinical command center, organizing campus-wide student wellness data into actionable triage workflows.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     COUNSELLOR CLINICAL CONTROL CENTER                      │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ 🚨 AI PRIORITY FLAGGED QUEUE (Streak >= 3 Days High-Risk)             │  │
│  │  • Student Name     • Streak Days   • Faculty Engagement   • Action   │  │
│  │  • Alex Mercer      • 4 Days High   • Sub: No | Part: Low  • Profile  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                      │                                      │
│                                      ▼ [Click Profile]                      │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ 🔍 360° STUDENT DRILLDOWN MODAL                                       │  │
│  │  • Baseline Psychometrics (Anxiety, Depression, Burnout, Sleep Avg)   │  │
│  │  • Faculty Qualitative Observational Remarks                          │  │
│  │  • 5-Day Daily Habit Progression & AI Risk Trendlines                 │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                      │                                      │
│                                      ▼ [Take Action]                        │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ 🤝 CLINICAL INTERVENTION & PROGRESS TRACKING                          │  │
│  │  • Launch Video Call (Google Meet)                                    │  │
│  │  • Initiate Live Split-Pane Messenger Chat                            │  │
│  │  • Log Session Notes & Improvement Level (Significant/Moderate/...)   │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Step 1: AI Priority Flagged Queue (Early Warning Sustained Alert)
* At the top of the counsellor dashboard sits the **AI Priority Flagged Queue**.
* The server automatically queries daily logs and identifies students who have recorded a **High Risk prediction for 3 or more consecutive check-ins**.
* Students with the longest active high-risk streaks are prioritized at the top of the queue, highlighting individuals experiencing chronic, unmitigated distress.
* The queue displays the student's name, streak duration (e.g., *4 Days*), latest academic engagement rating from faculty, and quick-action buttons.

#### Step 2: 360° Comprehensive Student Drilldown Modal
Clicking "Profile" on any student dynamically fetches their entire holistic health record via an asynchronous JSON endpoint (`/counsellor/student/details/<student_id>`), rendering an in-depth clinical summary modal:
* **Baseline Psychological Profile:** Displays initial survey metrics (Anxiety score, Depression score, Burnout index, Self-rated Mental Health Index, Financial stress, Family expectations, Physical activity hours).
* **Computed Average Sleep:** Dynamically calculates and displays the student's exact average nightly sleep over their recent check-ins (e.g., *5.2 hrs/night (avg)*).
* **Faculty Engagement Insights:** Displays the most recent faculty evaluation, including timely submission status, participation level, and the faculty member's exact observational notes.
* **5-Day Check-in History Table:** Tabulates recent daily logs, displaying exact sleep hours, study load, academic pressure, mood score, and individual predicted risk statuses.

#### Step 3: Consultation Management & Clinical Progress Tracking
* Counsellors view all scheduled appointments booked by students.
* Clicking "Join Call" launches the virtual meeting link.
* Following a session, counsellors click "Log Notes" to open a clinical reporting modal where they record diagnostic notes and evaluate the student's clinical improvement across four standardized recovery tiers:
  * **Significant Improvement**
  * **Moderate Improvement**
  * **No Change**
  * **Deterioration**
* Submitting this report automatically updates the session status to **Completed** and archives the clinical notes.

#### Step 4: Split-Pane Direct Student Messenger
* A dedicated multi-student chat messenger enables direct, real-time communication with any student.
* Counsellors can browse student contacts in a sidebar list, view instant conversation histories, and send guidance messages directly to the student's portal.

---

## 4. Machine Learning & Predictive Modeling Deep Dive

### 4.1 Problem Formulation & Classification Objective
MindGarden frames mental health risk prediction as a **supervised multi-class classification problem**. Given a unified feature vector $\mathbf{x} \in \mathbb{R}^{18}$ representing a student's demographic, academic, behavioral, and psychological state, the model estimates the conditional probability distribution over three discrete risk tiers:

$$\mathcal{Y} = \{\text{Low}, \text{Medium}, \text{High}\}$$

The classification decision rule assigns the student to the class maximizing the posterior probability:

$$\hat{y} = \arg\max_{k \in \{0, 1, 2\}} P(Y = k \mid \mathbf{x})$$

Where:
* $k = 0 \implies \text{High Risk}$ (Urgent clinical concern, severe distress markers)
* $k = 1 \implies \text{Low Risk}$ (Stable psychological equilibrium, healthy coping mechanisms)
* $k = 2 \implies \text{Medium Risk}$ (Elevated stress or academic strain requiring monitoring)

### 4.2 The 18-Feature Psychological & Academic Vector
The feature vector integrates both longitudinal baseline indicators (from the student's onboarding survey) and dynamic daily lifestyle variables (from daily check-ins):

| # | Feature Name | Data Type | Source | Normal Range | Behavioral & Clinical Significance |
|---|---|---|---|---|---|
| 1 | `age` | Numerical (Integer) | Baseline Survey | 15 – 50 | Captures age-related developmental maturity and life stage expectations. |
| 2 | `gender` | Categorical (Nominal) | Baseline Survey | Female, Male, Other | Encoded via One-Hot Encoding to account for demographic variations in reported distress. |
| 3 | `academic_year` | Numerical (Integer) | Baseline Survey | 1 – 4 | Differentiates between freshman transition shock and senior graduation anxiety. |
| 4 | `study_hours_per_day` | Numerical (Float) | Daily Check-in | 0.0 – 15.0 hrs | Quantifies daily academic workload and cognitive effort. |
| 5 | `exam_pressure` | Numerical (Float) | Daily Check-in | 0.0 – 10.0 | Measures acute evaluation anxiety and upcoming academic deadlines. |
| 6 | `academic_performance`| Numerical (Float) | Baseline Survey | 30.0 – 100.0% | Self-reported cumulative academic performance percentage. |
| 7 | `stress_level` | Numerical (Float) | Daily Check-in | 0.0 – 10.0 | Subjective self-perceived psychological tension on the day of check-in. |
| 8 | `anxiety_score` | Numerical (Float) | Baseline Survey | 0.0 – 10.0 | Standardized baseline measure of generalized anxiety traits. |
| 9 | `depression_score` | Numerical (Float) | Baseline Survey | 0.0 – 10.0 | Standardized baseline assessment of depressive symptomatology and anhedonia. |
| 10| `sleep_hours` | Numerical (Float) | Daily Check-in | 2.0 – 12.0 hrs | Circadian rhythm integrity and biological recovery duration. |
| 11| `physical_activity` | Numerical (Float) | Baseline Survey | 0.0 – 10.0 hrs | Daily exercise, known to strongly correlate with neurochemical regulation. |
| 12| `social_support` | Numerical (Float) | Baseline Survey | 0.0 – 10.0 | Self-rated strength of peer, family, and institutional safety networks. |
| 13| `screen_time` | Numerical (Float) | Baseline Survey | 0.0 – 24.0 hrs | Total daily electronic device exposure. |
| 14| `internet_usage` | Numerical (Float) | Baseline Survey | 0.0 – 24.0 hrs | Recreational web and social media consumption duration. |
| 15| `financial_stress` | Numerical (Float) | Baseline Survey | 0.0 – 10.0 | Perceived economic hardship, tuition worries, and living expense strain. |
| 16| `family_expectation`| Numerical (Float) | Baseline Survey | 0.0 – 10.0 | External parental and familial achievement pressure. |
| 17| `burnout_score` | Numerical (Float) | Baseline Survey | 0.0 – 10.0 | Emotional exhaustion and depersonalization related to prolonged studies. |
| 18| `mental_health_index`| Numerical (Float) | Baseline Survey | 0.0 – 10.0 | Composite self-rated mental wellness and resilience index. |

### 4.3 Dataset Characteristics (`CEP_Train_Data.csv`)
* **Volume:** The model training corpus (`ml/CEP_Train_Data.csv`) contains extensive student wellness records (~294 MB), providing a rich sample distribution across diverse demographics and academic disciplines.
* **Leakage Prevention:** Features that directly correlate with future administrative outcomes rather than mental health state (specifically `dropout_risk` and `dropout_labels`) are programmatically dropped during training to prevent target leakage:
  ```python
  features_to_drop = ["risk_level", "dropout_risk", "dropout_labels"]
  X = df.drop(columns=[col for col in features_to_drop if col in df.columns], errors="ignore")
  y = df["risk_level"]
  ```

### 4.4 Data Preprocessing Pipeline (`ColumnTransformer`)
Data preprocessing is encapsulated inside a Scikit-Learn `ColumnTransformer` to guarantee identical transformations during both offline model training and real-time production inference:

```python
nominal_cat = ["gender"]
num_cols = X_train.select_dtypes(include="number").columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ("nominal", OneHotEncoder(handle_unknown="ignore", sparse_output=False), nominal_cat),
        ("numerical", "passthrough", num_cols)
    ],
    remainder="passthrough"
)
```

1. **Nominal Feature Encoding:** The `gender` feature is transformed via `OneHotEncoder(handle_unknown='ignore', sparse_output=False)`. If an unseen gender category appears during inference, the transformer outputs zeros rather than raising an exception.
2. **Numerical Passthrough:** The remaining 17 numerical features pass directly through without alteration, preserving their raw interpretability and native scale for tree-based partitioning.
3. **Target Variable Encoding:** The target labels (`High`, `Low`, `Medium`) are transformed into discrete integer indices via `LabelEncoder`:
   * `Class 0` $\rightarrow$ `High`
   * `Class 1` $\rightarrow$ `Low`
   * `Class 2` $\rightarrow$ `Medium`

### 4.5 Class Imbalance Mitigation via Sample Weighting
In student health datasets, severe risk instances are naturally less frequent than low-to-medium stress cases. To prevent the classifier from biasing predictions toward the majority class (which could cause dangerous false-negative classifications of high-risk students), MindGarden applies automated sample weighting during training:

$$w_i = \frac{N}{K \cdot n_{y_i}}$$

Where:
* $N$ is the total number of training samples.
* $K$ is the total number of classes ($K = 3$).
* $n_{y_i}$ is the count of samples in class $y_i$.

In the training pipeline (`ml/train_and_save_model.py`), this is computed using Scikit-Learn's utility:
```python
sample_weights = compute_sample_weight(class_weight="balanced", y=y_train)
pipe.fit(X_train, y_train, clf_model__sample_weight=sample_weights)
```

### 4.6 XGBoost Mathematical Foundation & Objective Formulation
MindGarden utilizes **eXtreme Gradient Boosting (XGBoost)**, an optimized distributed gradient boosting library implementing tree ensembles under a second-order Taylor expansion framework.

#### Objective Function
At boosting step $t$, the objective function to minimize across all $N$ instances and $M$ additive trees is:

$$\mathcal{L}^{(t)} = \sum_{i=1}^N l\left(y_i, \hat{y}_i^{(t-1)} + f_t(\mathbf{x}_i)\right) + \sum_{k=1}^t \Omega(f_k)$$

Where $l$ represents the multi-class log loss (cross-entropy), and $\Omega(f)$ is the model complexity regularization term penalizing tree leaves and weights:

$$\Omega(f_t) = \gamma T + \frac{1}{2} \lambda \sum_{j=1}^T w_j^2$$

Here:
* $T$ is the number of terminal leaves in decision tree $f_t$.
* $w_j$ represents the output weight assigned to leaf $j$.
* $\gamma$ is the minimum loss reduction required to make a split.
* $\lambda$ is the $L_2$ leaf weight regularization penalty.

#### Second-Order Taylor Approximation
XGBoost optimizes the objective using a second-order Taylor expansion:

$$\mathcal{L}^{(t)} \approx \sum_{i=1}^N \left[ l(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(\mathbf{x}_i) + \frac{1}{2} h_i f_t^2(\mathbf{x}_i) \right] + \Omega(f_t)$$

Where the first-order gradient $g_i$ and second-order Hessian $h_i$ are defined as:

$$g_i = \partial_{\hat{y}^{(t-1)}} l(y_i, \hat{y}^{(t-1)})$$
$$h_i = \partial_{\hat{y}^{(t-1)}}^2 l(y_i, \hat{y}^{(t-1)})$$

#### Multi-Class Softmax Formulation (`multi:softprob`)
For our 3-class classification problem, the probability that sample $i$ belongs to class $k \in \{0, 1, 2\}$ is computed via the Softmax activation over ensemble margin scores $z_k(\mathbf{x}_i)$:

$$P(Y = k \mid \mathbf{x}_i) = \frac{e^{z_k(\mathbf{x}_i)}}{\sum_{j=0}^2 e^{z_j(\mathbf{x}_i)}}$$

The training objective minimizes the multi-class cross-entropy loss:

$$\mathcal{L}_{multi} = - \sum_{i=1}^N \sum_{k=0}^2 y_{i, k} \log P(Y = k \mid \mathbf{x}_i)$$

Where $y_{i, k}$ is a binary indicator denoting whether class $k$ is the true label for student $i$.

### 4.7 Hyperparameter Optimization & Model Regularization
The `XGBClassifier` in `ml/train_and_save_model.py` is configured with regularized hyperparameters selected to balance classification precision, recall across minority classes, and rapid inference latency:

```python
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
```

| Hyperparameter | Value | Architectural Justification |
|---|---|---|
| `n_estimators` | `100` | Limits total ensemble trees to prevent overfitting while capturing non-linear interactions. |
| `max_depth` | `5` | Restricts tree depth to 5 levels ($2^5 = 32$ max leaves), preventing the model from memorizing individual student profiles. |
| `subsample` | `0.8` | Randomly samples 80% of training instances per tree, adding stochastic bagging variance reduction. |
| `colsample_bytree` | `0.8` | Subsamples 80% of feature columns at each split, preventing single dominant predictors (e.g., `anxiety_score`) from overpowering subtle interactions. |
| `learning_rate` ($\eta$) | `0.05` | Shrinks tree weight updates by 0.05, enforcing conservative gradient step sizes. |
| `objective` | `multi:softprob`| Computes multi-class class probabilities across all 3 risk tiers. |
| `eval_metric` | `mlogloss` | Optimizes multi-class cross-entropy log loss. |
| `n_jobs` | `-1` | Parallelizes tree construction across all available CPU cores. |

### 4.8 Inference Runtime Engine (`ml/ml_handler.py`)
The runtime inference service is encapsulated in `ml/ml_handler.py` as an `MLPredictor` singleton:

```python
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
```

#### Key Implementation Mechanisms:
1. **Singleton Lifecycle:** When `app.py` boots, it executes `from ml.ml_handler import predictor`. The class loads `student_risk_model.pkl` once into memory, caching the Scikit-Learn `Pipeline`, the `LabelEncoder`, and the training `feature_names` list.
2. **Dynamic Column Alignment:** Real-time user input is converted into a single-row Pandas DataFrame and strictly re-indexed against `self.feature_names`:
   ```python
   input_df = pd.DataFrame([student_data])
   input_df = input_df[self.feature_names]
   ```
   This guarantees that feature order remains invariant regardless of how dictionary keys were constructed in the HTTP route handler.
3. **Safe Exception Trapping:** If the pickle file is missing or prediction fails due to malformed inputs, the system logs an error message and returns `"Low"` as a safe default rather than terminating the Flask worker process.

### 4.9 Training Execution & Pipeline Serialization (`ml/train_and_save_model.py`)
The standalone script `ml/train_and_save_model.py` trains and exports the final model pipeline:
1. Loads `ml/CEP_Train_Data.csv`.
2. Drops leakage columns (`dropout_risk`, `dropout_labels`).
3. Fits the target `LabelEncoder`.
4. Performs a stratified 80/20 train/test split (`stratify=y_encoded`).
5. Fits the preprocessing and XGBoost pipeline using balanced sample weights.
6. Evaluates and logs training and testing accuracy.
7. Serializes the pipeline, label encoder, and feature list together into `ml/student_risk_model.pkl` via `joblib.dump()`:
   ```python
   save_data = {
       "pipeline": pipe,
       "label_encoder": le,
       "features": X.columns.tolist()
   }
   joblib.dump(save_data, model_filename)
   ```

---

## 5. Database Architecture & Schema Specification

MindGarden utilizes SQLite managed through the Flask-SQLAlchemy ORM. The relational model is fully normalized across 8 entities.

### 5.1 Entity Relationship Diagram (ERD)

```mermaid
erDiagram
    User ||--o| StudentProfile : "has profile (1:1)"
    User ||--o{ DailyCheckin : "submits logs (1:N)"
    User ||--o{ FacultyRating : "rates / is rated (1:N)"
    User ||--o{ SessionBooking : "student / counsellor participant (1:N)"
    User ||--o{ ChatMessage : "sender / receiver (1:N)"
    SessionBooking ||--o| CounsellorReport : "generates post-session (1:1)"
    Quote ||--|| User : "viewed by (N:M)"

    User {
        int id PK "Auto Increment"
        string email UK "Unique, .edu enforced"
        string password_hash "PBKDF2-SHA256"
        string name "Full Name"
        string role "'student' | 'faculty' | 'counsellor'"
    }

    StudentProfile {
        int id PK "Auto Increment"
        int user_id FK "References users.id"
        int age "15 to 50"
        string gender "Female | Male | Other"
        int academic_year "1 to 4"
        float academic_performance "30.0 to 100.0%"
        float physical_activity "Hours/day"
        float social_support "0.0 to 10.0"
        float screen_time "Hours/day"
        float internet_usage "Hours/day"
        float financial_stress "0.0 to 10.0"
        float family_expectation "0.0 to 10.0"
        float anxiety_score "0.0 to 10.0"
        float depression_score "0.0 to 10.0"
        float burnout_score "0.0 to 10.0"
        float mental_health_index "0.0 to 10.0"
    }

    DailyCheckin {
        int id PK "Auto Increment"
        int user_id FK "References users.id"
        string date "YYYY-MM-DD"
        float sleep_hours "Nightly sleep (hrs)"
        float study_hours "Daily study (hrs)"
        float exam_pressure "0.0 to 10.0"
        float stress_level "0.0 to 10.0"
        float mood_score "1.0 to 10.0"
        string predicted_risk "'Low' | 'Medium' | 'High'"
    }

    FacultyRating {
        int id PK "Auto Increment"
        int faculty_id FK "References users.id"
        int student_id FK "References users.id"
        string date "YYYY-MM-DD"
        string timely_submission "'Yes' | 'No'"
        string classroom_participation "'High' | 'Medium' | 'Low'"
        text notes "Observational feedback"
    }

    SessionBooking {
        int id PK "Auto Increment"
        int student_id FK "References users.id"
        int counsellor_id FK "References users.id"
        string date "YYYY-MM-DD"
        string time "HH:MM"
        string status "'Pending' | 'Scheduled' | 'Completed'"
        string meet_link "Google Meet URL"
    }

    CounsellorReport {
        int id PK "Auto Increment"
        int session_id FK "References session_bookings.id"
        text notes "Clinical diagnostic notes"
        string improvement_level "'Significant' | 'Moderate' | 'No Change' | 'Deterioration'"
    }

    ChatMessage {
        int id PK "Auto Increment"
        int sender_id FK "References users.id"
        int receiver_id FK "References users.id"
        text message_text "Sanitized message body"
        datetime timestamp "UTC Timestamp"
    }

    Quote {
        int id PK "Auto Increment"
        string text "Affirmation statement"
        string author "Quote attribution"
    }
```

### 5.2 Data Dictionary & Table Schemas

#### 1. Table: `users`
Stores user identities, credentials, and access roles across the platform.

| Column Name | SQL Type | Constraints | Default | Description |
|---|---|---|---|---|
| `id` | `INTEGER` | Primary Key, Auto Increment | *None* | Unique surrogate user identifier. |
| `email` | `VARCHAR(120)` | Unique, Not Null | *None* | Collegiate email address ending in `.edu`. |
| `password_hash` | `VARCHAR(128)`| Not Null | *None* | Cryptographic hash generated via Werkzeug PBKDF2-SHA256. |
| `name` | `VARCHAR(100)`| Not Null | *None* | Full legal or preferred name of the user. |
| `role` | `VARCHAR(20)` | Not Null | *None* | Authorization role: `'student'`, `'faculty'`, or `'counsellor'`. |

#### 2. Table: `student_profiles`
Stores 14 baseline physiological, psychological, and lifestyle attributes collected during onboarding.

| Column Name | SQL Type | Constraints | Default | Description |
|---|---|---|---|---|
| `id` | `INTEGER` | Primary Key, Auto Increment | *None* | Profile primary key. |
| `user_id` | `INTEGER` | Foreign Key (`users.id`), Not Null | *None* | User ID of the associated student. |
| `age` | `INTEGER` | Not Null | `22` | Age in years (validated 15–50). |
| `gender` | `VARCHAR(20)` | Not Null | `'Female'`| Gender identity (`'Female'`, `'Male'`, `'Other'`). |
| `academic_year` | `INTEGER` | Not Null | `1` | Collegiate year (`1`=Freshman, `2`=Sophomore, etc.). |
| `academic_performance`| `FLOAT` | Not Null | `70.0` | Self-reported cumulative GPA or percentage (30–100). |
| `physical_activity` | `FLOAT` | Not Null | `3.0` | Average daily physical exercise hours. |
| `social_support` | `FLOAT` | Not Null | `5.0` | Perceived social support strength (0–10). |
| `screen_time` | `FLOAT` | Not Null | `5.0` | Average total daily screen exposure hours. |
| `internet_usage` | `FLOAT` | Not Null | `5.0` | Recreational internet and social media usage hours. |
| `financial_stress` | `FLOAT` | Not Null | `5.0` | Subjective financial strain index (0–10). |
| `family_expectation`| `FLOAT` | Not Null | `5.0` | Perceived familial achievement pressure (0–10). |
| `anxiety_score` | `FLOAT` | Not Null | `3.0` | Standardized baseline anxiety metric (0–10). |
| `depression_score` | `FLOAT` | Not Null | `1.0` | Standardized baseline depression metric (0–10). |
| `burnout_score` | `FLOAT` | Not Null | `2.0` | Standardized academic burnout score (0–10). |
| `mental_health_index`| `FLOAT` | Not Null | `7.0` | Self-rated baseline wellness resilience (0–10). |

#### 3. Table: `daily_checkins`
Stores daily self-reported habit check-ins and the corresponding XGBoost-predicted risk level.

| Column Name | SQL Type | Constraints | Default | Description |
|---|---|---|---|---|
| `id` | `INTEGER` | Primary Key, Auto Increment | *None* | Check-in primary key. |
| `user_id` | `INTEGER` | Foreign Key (`users.id`), Not Null | *None* | ID of the student submitting the log. |
| `date` | `VARCHAR(10)` | Not Null | *None* | Calendar date of check-in (`YYYY-MM-DD`). |
| `sleep_hours` | `FLOAT` | Not Null | `7.0` | Sleep hours logged for the previous night. |
| `study_hours` | `FLOAT` | Not Null | `4.0` | Study hours logged for the day. |
| `exam_pressure` | `FLOAT` | Not Null | `5.0` | Academic examination pressure rating (0–10). |
| `stress_level` | `FLOAT` | Not Null | `4.0` | Subjective stress level rating (0–10). |
| `mood_score` | `FLOAT` | Not Null | `7.0` | Overall subjective mood rating (1–10). |
| `predicted_risk` | `VARCHAR(20)` | Not Null | *None* | Model classification output: `'Low'`, `'Medium'`, or `'High'`. |

#### 4. Table: `faculty_ratings`
Contains academic engagement assessments and behavioral remarks logged by faculty members.

| Column Name | SQL Type | Constraints | Default | Description |
|---|---|---|---|---|
| `id` | `INTEGER` | Primary Key, Auto Increment | *None* | Rating primary key. |
| `faculty_id` | `INTEGER` | Foreign Key (`users.id`), Not Null | *None* | ID of the faculty member logging the evaluation. |
| `student_id` | `INTEGER` | Foreign Key (`users.id`), Not Null | *None* | ID of the student being evaluated. |
| `date` | `VARCHAR(10)` | Not Null | *None* | Date of evaluation entry (`YYYY-MM-DD`). |
| `timely_submission`| `VARCHAR(10)` | Not Null | `'Yes'` | Assignment punctuality (`'Yes'` or `'No'`). |
| `classroom_participation`| `VARCHAR(10)`| Not Null | `'Medium'`| Engagement level (`'High'`, `'Medium'`, or `'Low'`). |
| `notes` | `TEXT` | Nullable | `NULL` | Qualitative observational feedback notes. |

#### 5. Table: `session_bookings`
Tracks scheduled consultation appointments between students and campus counsellors.

| Column Name | SQL Type | Constraints | Default | Description |
|---|---|---|---|---|
| `id` | `INTEGER` | Primary Key, Auto Increment | *None* | Booking primary key. |
| `student_id` | `INTEGER` | Foreign Key (`users.id`), Not Null | *None* | ID of the student attending the consultation. |
| `counsellor_id` | `INTEGER` | Foreign Key (`users.id`), Not Null | *None* | ID of the assigned campus counsellor. |
| `date` | `VARCHAR(10)` | Not Null | *None* | Appointment date (`YYYY-MM-DD`). |
| `time` | `VARCHAR(5)` | Not Null | *None* | Appointment time in 24-hour format (`HH:MM`). |
| `status` | `VARCHAR(20)` | Not Null | `'Pending'`| Session state: `'Pending'`, `'Scheduled'`, `'Completed'`. |
| `meet_link` | `VARCHAR(200)`| Nullable | `NULL` | Generated virtual meeting room URL. |

#### 6. Table: `counsellor_reports`
Archives clinical outcomes, recovery progress ratings, and session notes logged by counsellors following a consultation.

| Column Name | SQL Type | Constraints | Default | Description |
|---|---|---|---|---|
| `id` | `INTEGER` | Primary Key, Auto Increment | *None* | Report primary key. |
| `session_id` | `INTEGER` | Foreign Key (`session_bookings.id`), Not Null | *None* | Associated consultation booking ID. |
| `notes` | `TEXT` | Not Null | *None* | Clinical observations and intervention strategy notes. |
| `improvement_level`| `VARCHAR(50)`| Not Null | *None* | Outcome tier: `'Significant'`, `'Moderate'`, `'No Change'`, or `'Deterioration'`. |

#### 7. Table: `chat_messages`
Stores bi-directional text messages exchanged between students and counsellors.

| Column Name | SQL Type | Constraints | Default | Description |
|---|---|---|---|---|
| `id` | `INTEGER` | Primary Key, Auto Increment | *None* | Message primary key. |
| `sender_id` | `INTEGER` | Foreign Key (`users.id`), Not Null | *None* | ID of the user sending the message. |
| `receiver_id` | `INTEGER` | Foreign Key (`users.id`), Not Null | *None* | ID of the intended recipient. |
| `message_text` | `TEXT` | Not Null | *None* | Body content of the chat message. |
| `timestamp` | `DATETIME` | Not Null | `datetime.utcnow` | UTC creation timestamp. |

#### 8. Table: `quotes`
Stores positive affirmations and mental health quotations displayed on student dashboards.

| Column Name | SQL Type | Constraints | Default | Description |
|---|---|---|---|---|
| `id` | `INTEGER` | Primary Key, Auto Increment | *None* | Quote primary key. |
| `text` | `VARCHAR(300)`| Not Null | *None* | The motivational statement text. |
| `author` | `VARCHAR(100)`| Not Null | *None* | Attributed author or source name. |

### 5.3 Relational Constraints & Foreign Key Policies
* **Cascading Integrity:** Foreign keys link `student_profiles`, `daily_checkins`, `faculty_ratings`, `session_bookings`, and `chat_messages` directly to `users.id`.
* **Unique Constraints:** The `users.email` column carries an explicit `unique=True` index to prevent duplicate accounts.
* **Referential Association:** `counsellor_reports.session_id` creates a 1-to-1 relationship with `session_bookings.id`, ensuring every clinical report corresponds to a valid scheduled appointment.

### 5.4 Database Seeding & First-Run Initialization
During application startup (`app.py`), the function `seed_db()` executes inside an `app.app_context()` block:

```python
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_db()
    app.run(debug=True, port=5000)
```

1. **Table Creation:** `db.create_all()` inspects the local directory for `instance/mindgarden.db` and generates any missing database tables.
2. **Idempotency Guard:** `seed_db()` begins by executing `if Quote.query.first(): return`, ensuring seed records are inserted only on initial startup and preventing duplicate entries on subsequent server restarts.
3. **Affirmations Seeding:** Seeds 10 clinically curated, non-toxic motivational quotes into the `quotes` table.
4. **Seed Users:** Automatically provisions three default test accounts:
   * **Student:** `student@college.edu` (`student123`)
   * **Faculty:** `faculty@college.edu` (`faculty123`)
   * **Counsellor:** `counsellor@college.edu` (`counsellor123`)

---

## 6. Backend Engineering & Flask Server Implementation

### 6.1 Application Entrypoint & Bootstrap (`app.py`)
`app.py` serves as the centralized backend orchestrator, configuring Flask, initializing extensions, defining models, and mounting route handlers.

```python
# Initialization snippet from app.py
app = Flask(__name__)
app.secret_key = "mindgarden_secret_session_key"

# Database Configuration (SQLite local database)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mindgarden.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
```

### 6.2 Complete HTTP Route Catalog

| HTTP Method | Route URL | Endpoint Function | Allowed Roles | Request Type | Description / Response |
|---|---|---|---|---|---|
| `GET` | `/` | `index()` | Public / Any | Query | Root dispatcher. Redirects unauthenticated users to `/login`, students to `/student/dashboard` (or `/onboarding`), faculty to `/faculty/dashboard`, and counsellors to `/counsellor/dashboard`. |
| `GET`, `POST` | `/login` | `login()` | Public | Form / HTML | Authenticates user credentials against PBKDF2 password hashes. Sets session variables on success. |
| `POST` | `/signup` | `signup()` | Public | Form / HTML | Registers new user accounts. Enforces collegiate `.edu` email domain format, minimum password length (6 chars), and role assignment. |
| `GET` | `/logout` | `logout()` | Any Authenticated | Query | Clears the active session via `session.clear()` and redirects to `/login`. |
| `GET`, `POST` | `/onboarding` | `onboarding()` | `student` | Form / HTML | Renders and processes the 14-parameter initial intake assessment for first-time students. |
| `GET` | `/student/dashboard` | `student_dashboard()`| `student` | Query / HTML | Renders the primary student interface, daily sliders, quotes, check-in history, and appointments. |
| `POST` | `/student/profile/update` | `update_profile()` | `student` | Form / Redirect| Updates baseline profile parameters stored in `StudentProfile`. |
| `POST` | `/student/checkin` | `student_checkin()` | `student` | Form / JSON | **AJAX Endpoint.** Merges daily metrics with baseline profile, invokes XGBoost classifier, persists log, and returns predicted risk JSON. |
| `POST` | `/student/book` | `book_session()` | `student` | Form / Redirect| Schedules a consultation session with a counsellor and generates a mock Google Meet URL. |
| `GET` | `/faculty/dashboard` | `faculty_dashboard()`| `faculty` | Query / HTML | Renders student roster and academic engagement summary for faculty members. |
| `POST` | `/faculty/rate/<int:student_id>` | `faculty_rate()` | `faculty` | Form / Redirect| Records assignment punctuality, participation level, and observational notes for a student. |
| `GET` | `/counsellor/dashboard` | `counsellor_dashboard()`| `counsellor`| Query / HTML | Evaluates consecutive high-risk streaks, displays the AI Priority Queue, student directory, schedule, and chat. |
| `POST` | `/counsellor/report/<int:session_id>`| `submit_counsellor_report()`| `counsellor`| Form / Redirect| Records clinical consultation outcomes, improvement ratings, and marks the session as completed. |
| `GET` | `/counsellor/student/details/<int:student_id>`| `get_student_details()`| `counsellor`| Query / JSON | **AJAX Endpoint.** Returns complete 360° student summary (baseline profile, faculty rating, 5-day logs, computed sleep average). |
| `POST` | `/chat/send` | `send_message()` | Any Authenticated | JSON / JSON | **AJAX Endpoint.** Validates receiver ID and message body, persists record in `ChatMessage`, and returns status. |
| `GET` | `/chat/history/<int:other_user_id>` | `get_chat_history()` | Any Authenticated | Query / JSON | **AJAX Endpoint.** Fetches bi-directional conversation history sorted chronologically by timestamp. |

### 6.3 Session Security & Authentication Workflows
* **Cryptographic Passwords:** User passwords are never stored in plaintext. Passwords are salted and hashed using Werkzeug's `generate_password_hash()` utilizing PBKDF2-SHA256 with 260,000 iterations.
* **Authentication Validation:** Inbound login credentials are verified against stored hashes using `check_password_hash(user.password_hash, password)`.
* **Collegiate Email Domain Enforcement:** To preserve collegiate integrity, the `/signup` route enforces a strict validation rule requiring all user email addresses to end with `.edu`:
  ```python
  if not email.endswith(".edu"):
      return render_template("login.html", error="College registration requires a valid college email ending with .edu.", tab="signup")
  ```
* **Session State Management:** On successful authentication, the server populates client-side encrypted session cookies:
  ```python
  session["user_id"] = user.id
  session["user_name"] = user.name
  session["role"] = user.role
  ```

### 6.4 Role-Based Access Control (RBAC) Dispatcher
The application enforces RBAC both at the root URL router (`/`) and inside individual route controllers:
```python
def get_current_user():
    if "user_id" in session:
        return db.session.get(User, session["user_id"])
    return None

@app.route("/")
def index():
    user = get_current_user()
    if not user:
        return redirect(url_for("login"))
    
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
```

### 6.5 Asynchronous AJAX Route Handlers
MindGarden utilizes JSON-driven AJAX endpoints for dynamic, single-page-application-like interactions:
* `/student/checkin`: Accepts form-encoded daily metrics via `FormData`, executes prediction, and returns structured JSON:
  ```json
  {
    "status": "success",
    "predicted_risk": "High",
    "log": {
      "date": "2026-09-14",
      "sleep_hours": 5.0,
      "study_hours": 7.0,
      "exam_pressure": 8.0,
      "stress_level": 9.0,
      "mood_score": 3.0,
      "predicted_risk": "High"
    }
  }
  ```
* `/chat/send`: Ingests JSON bodies (`{"receiver_id": 3, "message": "Hello"}`) and returns message metadata with formatted time strings (`HH:MM`).
* `/counsellor/student/details/<student_id>`: Compiles profile records, faculty remarks, and historical logs into a unified JSON object, calculating average sleep duration on the fly.

### 6.6 Server-Side Validation & Security Policies
* **Duplicate Log Interception:** The daily check-in handler verifies that no `DailyCheckin` record exists for the active `user_id` and current calendar date string (`YYYY-MM-DD`), preventing redundant database writes.
* **Onboarding Integrity Enforcement:** If a student attempts to access `/student/dashboard` or submit a daily check-in without completing their intake assessment, the server catches the missing profile and redirects them to `/onboarding`.

---

## 7. Frontend Architecture & "Ditto" Design System

### 7.1 Philosophy of the Sunlit Wildflower Atelier ("Ditto")
Most healthcare software suffers from a "hospital corridor" visual identity—stark white backgrounds, cold corporate blues, sharp corners, and clinical terminology. This aesthetic creates emotional distance and discourages vulnerable students from engaging.

MindGarden implements the **Ditto Design System** (also termed the *Sunlit Wildflower Atelier*), guided by four core aesthetic principles:
1. **Warmth & Biophilia:** A soft, natural color palette anchored by warm cream canvas (`#f8faf5`), pale meadow surfaces (`#edf2e8`), and deep ink typography (`#0f172a`).
2. **Tactile Geometry:** Heavy pill-shaped buttons and inputs with smooth border radii (up to `1440px`), paired with generous 20px card curvatures that feel soft, friendly, and approachable.
3. **Micro-Interactions & Depth:** Interactive 3D button press effects (`.btn-3d`), dynamic gradient slider track fills, and gentle modal fade-ins that provide tactile sensory feedback.
4. **Accessible Visual Hierarchy:** High-contrast, WCAG-compliant status badges for priority states (`Low`, `Medium`, `High`) that remain readable across all lighting conditions.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       DITTO DESIGN COLOR LANGUAGE                           │
├───────────────────┬─────────────────────────────────────────────────────────┤
│ Canvas / Ground   │ #f8faf5 (Warm eggshell cream, replaces sterile white)  │
│ Surface / Cards   │ #edf2e8 (Soft botanical meadow green)                   │
│ Action Accent     │ #f59e0b (Sunlit amber / warm yellow)                    │
│ Growth Accent     │ #15803d (Vibrant forest moss green)                     │
│ Text / Borders    │ #0f172a (Deep indigo ink, replaces harsh pure black)    │
│ High Risk Alert   │ #dc2626 (Clear, WCAG-compliant crimson alert)          │
└───────────────────┴─────────────────────────────────────────────────────────┘
```

### 7.2 CSS Custom Properties & Design Token Dictionary
All aesthetic variables are declared in `static/style.css` under the `:root` pseudo-class:

```css
:root {
  /* Brand Palette Tokens */
  --color-deep-ink: #0f172a;
  --color-hi-yellow: #f59e0b;
  --color-hi-yellow-hover: #d97706;
  --color-moss-green: #15803d;
  --color-moss-light: rgba(22, 163, 74, 0.12);
  --color-fuchsia: #c026d3;
  --color-slate: #64748b;
  --color-canvas: #f8faf5;
  --color-soft-meadow: #edf2e8;
  --color-charcoal: #1e293b;
  --color-onyx: #0f172a;
  --color-paper: #ffffff;
  --color-border-subtle: rgba(15, 23, 42, 0.08);
  --color-border-medium: rgba(15, 23, 42, 0.16);

  /* Priority Status Colors (WCAG Compliant) */
  --color-low-risk: #16a34a;
  --color-low-risk-bg: rgba(22, 163, 74, 0.12);
  --color-medium-risk: #d97706;
  --color-medium-risk-bg: rgba(217, 119, 6, 0.12);
  --color-high-risk: #dc2626;
  --color-high-risk-bg: rgba(220, 38, 38, 0.12);

  /* Typography Font Families */
  --font-display: 'Hedvig Letters Serif', Georgia, Cambria, serif;
  --font-ui: 'Inter', system-ui, -apple-system, sans-serif;

  /* Typography Scale */
  --text-caption: 11px;
  --text-body-sm: 13px;
  --text-body: 15px;
  --text-subheading: 17px;
  --text-heading-sm: 20px;
  --text-heading: 28px;
  --text-heading-lg: 38px;
  --text-display: 48px;

  /* Spacing Scale */
  --spacing-8: 8px;
  --spacing-12: 12px;
  --spacing-16: 16px;
  --spacing-20: 20px;
  --spacing-24: 24px;
  --spacing-32: 32px;
  --spacing-48: 48px;
  --spacing-64: 64px;

  /* Border Radii */
  --radius-cards: 20px;
  --radius-buttons: 1440px;
  --radius-inputs: 12px;
  --radius-table-btn: 10px;

  /* Animation Durations */
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --ease-press: cubic-bezier(0.4, 0, 0.2, 1);
}
```

### 7.3 Typographic System & Visual Hierarchy
MindGarden establishes visual hierarchy by pairing an editorial serif with a clean, functional sans-serif:
* **Display & Heading Font (`--font-display`):** *Hedvig Letters Serif* provides an organic, literary aesthetic for page headings, hero banners, and section titles, conveying warmth and thoughtful reflection.
* **Interface & Body Font (`--font-ui`):** *Inter* provides legibility for data tables, form labels, chat bubbles, and interactive controls across all screen resolutions.

### 7.4 Tactile UI Components & Micro-Interactions

#### 1. Tactile 3D Buttons (`.btn-3d`)
Buttons implement physical depth through contrasting bottom box-shadows and tactile click translations:
```css
.btn-3d {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-ui);
  font-weight: 700;
  border-radius: var(--radius-buttons);
  cursor: pointer;
  border: 1.5px solid var(--color-deep-ink);
  box-shadow: 0 4px 0 var(--color-deep-ink);
  transition: all var(--duration-fast) var(--ease-press);
}

.btn-3d:active {
  transform: translateY(3px);
  box-shadow: 0 1px 0 var(--color-deep-ink);
}
```

#### 2. Tactile Range Sliders (`.slider-input`)
Standard browser range inputs are replaced with pill-shaped custom thumbs and dynamic CSS linear-gradient fill tracks:
```css
.slider-input {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 8px;
  border-radius: 999px;
  outline: none;
  border: 1px solid var(--color-border-medium);
}

.slider-input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--color-hi-yellow);
  border: 2px solid var(--color-deep-ink);
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(15, 23, 42, 0.2);
}
```

#### 3. Status Priority Badges (`.badge-priority`)
Categorical risk scores are communicated using high-visibility badges:
```css
.badge-priority {
  display: inline-flex;
  align-items: center;
  padding: 4px 12px;
  border-radius: 999px;
  font-weight: 700;
  font-size: 11px;
  text-transform: uppercase;
  border: 1px solid currentColor;
}
.badge-low { color: var(--color-low-risk); background: var(--color-low-risk-bg); }
.badge-medium { color: var(--color-medium-risk); background: var(--color-medium-risk-bg); }
.badge-high { color: var(--color-high-risk); background: var(--color-high-risk-bg); }
```

### 7.5 Client-Side Subsystems & JavaScript Engines (`static/script.js`)

`static/script.js` powers the interactive client-side behaviors across all three stakeholder portals:

#### 1. Safe HTML Sanitizer
To eliminate Stored Cross-Site Scripting (XSS) risks when injecting server strings into the DOM, `script.js` defines a global HTML escape helper:
```javascript
window.escapeHtml = function(str) {
    if (!str && str !== 0) return "";
    return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
};
```

#### 2. Toast Notification Engine
A toast notification system renders non-blocking alert banners that animate into view and automatically dismiss after 4 seconds:
```javascript
window.showToast("Daily log recorded! AI Risk: Low", "success");
```

#### 3. Dynamic Slider Track Fill Synchronization
As users slide range controls, an `input` event listener recalculates percentage offsets and dynamically updates the input background gradient to visually track completion:
```javascript
const pct = ((parseFloat(val) - min) / (maxVal - min)) * 100;
slider.style.background = `linear-gradient(to right, #15803d 0%, #15803d ${pct}%, #e2e8f0 ${pct}%, #e2e8f0 100%)`;
```

#### 4. Non-Destructive Polling Chat Engine
The live messaging subsystem polls the server for updates every 4.5 seconds. Crucially, the polling loop calculates scroll offsets to avoid interrupting users:
```javascript
const isNearBottom = chatHistory.scrollHeight - chatHistory.scrollTop - chatHistory.clientHeight < 70;
// Re-render only if partner switched or new messages arrived
if (isPartnerSwitched || messages.length !== lastRenderedMessageCount) {
    // Re-render chat messages...
    if (forceScroll || isPartnerSwitched || isNearBottom) {
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }
}
```

#### 5. Universal Modal Controller
A modal controller listens for open events, backdrop clicks, close button taps, and keyboard `Escape` presses, ensuring accessible modal dialog management across all portals.

#### 6. Mobile Drawer Navigation
On compact screens ($\le 768\text{px}$), the persistent desktop sidebar transforms into a collapsible slide-out drawer toggled by a hamburger button (`#hamburger-btn`) with an accompanying darkened backdrop.

### 7.6 Interactive Visualizations with Chart.js
On `templates/student_dashboard.html`, Chart.js visualizes longitudinal wellness trends over the student's recent daily check-ins. The multi-axis line chart tracks:
* **Sleep Duration (hrs):** Displayed in vibrant moss green (`#59e25d`) with soft area fill.
* **Study Time (hrs):** Plotted in bright amber yellow (`#ffe228`).
* **Mood Score (/10):** Rendered as a distinct indigo dashed line (`#130e30`).

When an AJAX check-in completes successfully, the chart dynamically pushes the new data point to its datasets and calls `healthChart.update()`, reflecting the new check-in without a page refresh.

---

## 8. Comprehensive REST API Reference

MindGarden features a structured RESTful interface for its client-side AJAX interactions.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           MINDGARDEN API MAP                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ • POST /student/checkin               -> Submit Daily Habits & Predict Risk │
│ • POST /student/book                  -> Schedule Consultation & Meet Link  │
│ • POST /faculty/rate/<id>             -> Log Academic Engagement Feedback   │
│ • POST /counsellor/report/<id>        -> Submit Clinical Consultation Notes │
│ • GET  /counsellor/student/details/<id> -> Fetch Complete 360° Profile JSON │
│ • POST /chat/send                     -> Dispatch Private Message           │
│ • GET  /chat/history/<id>             -> Retrieve Bi-directional Chat Stream│
└─────────────────────────────────────────────────────────────────────────────┘
```

### 8.1 Authentication Endpoints

#### `POST /login`
Authenticates user credentials and establishes an active HTTP session.
* **Headers:** `Content-Type: application/x-www-form-urlencoded`
* **Request Body:**
  ```urlencoded
  email=student%40college.edu&password=student123&role=student
  ```
* **Responses:**
  * `302 Found`: Redirects to `/` (which dispatches to the role-specific dashboard).
  * `200 OK`: Renders `login.html` with an error alert banner on invalid credentials.

#### `POST /signup`
Provisions a new user account with collegiate email domain validation.
* **Headers:** `Content-Type: application/x-www-form-urlencoded`
* **Request Body:**
  ```urlencoded
  name=Alex+Mercer&email=alex%40college.edu&role=student&password=secret123&confirm_password=secret123
  ```
* **Responses:**
  * `302 Found`: Redirects to `/` on successful user creation.
  * `200 OK`: Renders `login.html` with validation error messages if validation fails.

---

### 8.2 Student Action Endpoints

#### `POST /student/checkin`
Submits daily habit metrics, triggers real-time XGBoost inference, and persists the daily log.
* **Headers:** `Content-Type: application/x-www-form-urlencoded` (or `multipart/form-data`)
* **Request Body:**
  ```urlencoded
  sleep_hours=6.5&study_hours=5.0&exam_pressure=7.0&stress_level=6.0&mood_score=5.0
  ```
* **Response (Success - 200 OK):**
  ```json
  {
    "status": "success",
    "predicted_risk": "Medium",
    "log": {
      "date": "2026-09-14",
      "sleep_hours": 6.5,
      "study_hours": 5.0,
      "exam_pressure": 7.0,
      "stress_level": 6.0,
      "mood_score": 5.0,
      "predicted_risk": "Medium"
    }
  }
  ```
* **Response (Duplicate Check-in - 200 OK):**
  ```json
  {
    "status": "error",
    "message": "Already checked in today!"
  }
  ```
* **Response (Unauthorized - 401 Unauthorized):**
  ```json
  {
    "status": "error",
    "message": "Unauthorized"
  }
  ```

#### `POST /student/book`
Schedules a virtual appointment with a campus counsellor.
* **Headers:** `Content-Type: application/x-www-form-urlencoded`
* **Request Body:**
  ```urlencoded
  counsellor_id=3&date=2026-09-18&time=14%3A30
  ```
* **Response:** `302 Found` (Redirects to `/student/dashboard` with a success toast flash).

---

### 8.3 Faculty Action Endpoints

#### `POST /faculty/rate/<int:student_id>`
Records academic engagement observations and feedback for an enrolled student.
* **URL Parameter:** `student_id` (Integer user ID of the target student)
* **Headers:** `Content-Type: application/x-www-form-urlencoded`
* **Request Body:**
  ```urlencoded
  timely_submission=No&classroom_participation=Low&notes=Student+appeared+exhausted+and+did+not+submit+Assignment+2.
  ```
* **Response:** `302 Found` (Redirects to `/faculty/dashboard` with a confirmation flash).

---

### 8.4 Counsellor Clinical Endpoints

#### `GET /counsellor/student/details/<int:student_id>`
Fetches a student's complete holistic profile for display in the counsellor's drilldown modal.
* **URL Parameter:** `student_id` (Integer user ID of the student)
* **Response (Success - 200 OK):**
  ```json
  {
    "status": "success",
    "student": {
      "id": 1,
      "name": "Alex Mercer",
      "email": "student@college.edu"
    },
    "profile": {
      "age": 21,
      "gender": "Female",
      "academic_year": 2,
      "academic_performance": 74.5,
      "physical_activity": 2.5,
      "social_support": 4.0,
      "screen_time": 7.0,
      "internet_usage": 6.0,
      "financial_stress": 7.0,
      "family_expectation": 8.0,
      "anxiety_score": 7.5,
      "depression_score": 6.0,
      "burnout_score": 7.0,
      "mental_health_index": 4.0
    },
    "rating": {
      "timely_submission": "No",
      "classroom_participation": "Low",
      "notes": "Student missed lecture on Monday and appeared exhausted.",
      "date": "2026-09-12"
    },
    "checkins": [
      {
        "date": "2026-09-14",
        "sleep_hours": 4.5,
        "study_hours": 8.0,
        "exam_pressure": 9.0,
        "stress_level": 9.0,
        "mood_score": 2.0,
        "predicted_risk": "High"
      },
      {
        "date": "2026-09-13",
        "sleep_hours": 5.0,
        "study_hours": 7.5,
        "exam_pressure": 8.5,
        "stress_level": 8.5,
        "mood_score": 3.0,
        "predicted_risk": "High"
      }
    ],
    "avg_sleep": 4.8
  }
  ```

#### `POST /counsellor/report/<int:session_id>`
Archives post-session clinical notes and sets student recovery improvement tracking.
* **URL Parameter:** `session_id` (Integer booking ID)
* **Headers:** `Content-Type: application/x-www-form-urlencoded`
* **Request Body:**
  ```urlencoded
  notes=Completed+CBT+de-escalation+session.+Identified+midterm+exam+stressor.&improvement_level=Moderate
  ```
* **Response:** `302 Found` (Redirects to `/counsellor/dashboard` with a success flash).

---

### 8.5 Bi-Directional Messaging & Chat Endpoints

#### `POST /chat/send`
Transmits a direct message between a student and a counsellor.
* **Headers:** `Content-Type: application/json`
* **Request Body:**
  ```json
  {
    "receiver_id": 3,
    "message": "Hello Dr. Jenkins, I'm feeling overwhelmed about the upcoming exams."
  }
  ```
* **Response (Success - 200 OK):**
  ```json
  {
    "status": "success",
    "message": {
      "id": 42,
      "text": "Hello Dr. Jenkins, I'm feeling overwhelmed about the upcoming exams.",
      "sent": true,
      "time": "14:22"
    }
  }
  ```

#### `GET /chat/history/<int:other_user_id>`
Retrieves the complete bi-directional conversation history with a specific contact.
* **URL Parameter:** `other_user_id` (ID of the contact)
* **Response (200 OK):**
  ```json
  [
    {
      "id": 40,
      "text": "Welcome to MindGarden, Alex. How can I help you today?",
      "sent": false,
      "time": "09:15"
    },
    {
      "id": 41,
      "text": "Thank you Dr. Jenkins. I've been having trouble sleeping.",
      "sent": true,
      "time": "09:18"
    }
  ]
  ```

---

## 9. Complete File & Directory Manifest

### 9.1 Repository Tree Structure

```
c:\Users\yashg\OneDrive\Desktop\CEP_Project\
├── .git/                                 # Git version control metadata
├── .gitignore                            # Excluded patterns (virtualenvs, large CSVs, DBs)
├── .venv/                                # Local Python 3 virtual environment
├── __pycache__/                          # Python runtime bytecode caches
│
├── app.py                                # Main Flask server, routes, DB schemas, auth logic
├── requirements.txt                      # Project dependency specification
├── README.md                             # Master project documentation
│
├── ml/                                   # Machine Learning Subsystem
│   ├── __init__.py                       # Package marker
│   ├── ml_handler.py                     # ML runtime bridge: model loading & inference wrapper
│   ├── student_risk_model.pkl            # Serialized trained Scikit-learn / XGBoost pipeline
│   ├── train_and_save_model.py           # Standalone training script to build student_risk_model.pkl
│   ├── CEP_Train_Data.csv                # Dataset used for training student risk model (~294MB)
│   └── CEP_Code.ipynb                    # Jupyter research notebook (EDA & experimentation)
│
├── templates/                            # Jinja2 template views
│   ├── layout.html                       # Base layout, navbar, SEO meta, sidebar container
│   ├── login.html                        # Authentication view (Login / Signup with .edu filter)
│   ├── student_dashboard.html            # Student onboarding, daily check-in, bookings, and chat
│   ├── faculty_dashboard.html            # Faculty student directory and academic rating forms
│   └── counsellor_dashboard.html         # Priority flagged queue, drilldown modal, session reports
│
├── static/                               # Static frontend assets
│   ├── script.js                         # Dynamic interactions, AJAX checkins, and chat polling
│   └── style.css                         # Ditto design system stylesheet (variables, components)
│
├── instance/                             # Flask application instance folder
│   └── mindgarden.db                     # Active SQLite database file
│
├── tests/                                # Testing & Verification
│   └── verify_app_integration.py         # Integration test suite validating DB, ML, and endpoints
│
└── docs/                                 # Documentation & Backups
    ├── PROJECT_DOCUMENTATION.md          # Architecture documentation
    └── instance.zip                      # Compressed backup of the database instance
```

### 9.2 Detailed Module-by-Module Breakdown

#### 1. Core Application Controller: `app.py`
* **Role:** Serves as the central backend backbone of the entire platform.
* **Dependencies:** `Flask`, `Flask-SQLAlchemy`, `werkzeug.security`, `datetime`, `ml.ml_handler.predictor`.
* **Key Components:**
  * Declares 8 SQLAlchemy database models (`User`, `StudentProfile`, `DailyCheckin`, `FacultyRating`, `SessionBooking`, `CounsellorReport`, `ChatMessage`, `Quote`).
  * Implements session authentication and `.edu` domain verification.
  * Encapsulates all route handlers for student check-ins, faculty evaluations, counsellor clinical reports, and direct messaging APIs.
  * Implements `seed_db()` to automatically provision default database records and test accounts on first run.

#### 2. Machine Learning Inference Bridge: `ml/ml_handler.py`
* **Role:** Serves as the production inference wrapper between the Flask server and the serialized XGBoost model.
* **Dependencies:** `os`, `joblib`, `pandas`.
* **Key Components:**
  * Defines the `MLPredictor` class.
  * Automatically locates and deserializes `ml/student_risk_model.pkl` on application boot.
  * Exposes `predict(student_data)`, which validates input dictionaries, constructs 1-row DataFrames, aligns columns, invokes the pipeline, and decodes the predicted risk label.
  * Instantiates the singleton `predictor` imported across the application.

#### 3. Model Training Pipeline: `ml/train_and_save_model.py`
* **Role:** Standalone script executed to train, evaluate, and export the mental health classification pipeline.
* **Dependencies:** `pandas`, `numpy`, `sklearn`, `xgboost`, `joblib`.
* **Key Components:**
  * Ingests `ml/CEP_Train_Data.csv`.
  * Drops leakage features (`dropout_risk`, `dropout_labels`).
  * Encodes categorical `gender` using `OneHotEncoder` and passes through numerical attributes via `ColumnTransformer`.
  * Computes balanced sample weights to mitigate class imbalances.
  * Fits the `XGBClassifier` over 100 boosting rounds.
  * Outputs training and testing accuracy scores and exports `ml/student_risk_model.pkl`.

#### 4. Master Layout Template: `templates/layout.html`
* **Role:** Provides the global HTML shell, responsive sidebar navigation, brand SVG icons, and common CSS/JS includes.
* **Key Components:**
  * Declares SEO meta tags, SVG favicon data URIs, Chart.js CDN scripts, and Font Awesome icon sheets.
  * Renders role-aware sidebar navigation links adapted to the active user's permissions.
  * Implements the flash notification toast container and mobile drawer navigation triggers.

#### 5. Authentication View: `templates/login.html`
* **Role:** Renders the sliding dual-tab login and registration card.
* **Key Components:**
  * Features smooth CSS sliding transitions between the "Login" and "Sign Up" panels.
  * Includes role selection dropdowns, password visibility toggles, and collegiate `.edu` email pattern validation.
  * Includes 1-click demo filler buttons for fast testing access across Student, Faculty, and Counsellor accounts.

#### 6. Student Interface: `templates/student_dashboard.html`
* **Role:** Renders both the first-time onboarding survey and the active student wellness dashboard.
* **Key Components:**
  * 14-parameter onboarding baseline intake form.
  * Tactile daily check-in slider form with asynchronous AJAX submission.
  * Responsive Chart.js time-series trendline visualization for sleep, study, and mood.
  * Appointment booking modal with mock Google Meet link generator.
  * Embedded counsellor chat box with dropdown selection.
  * Profile baseline parameter update form.

#### 7. Faculty Portal View: `templates/faculty_dashboard.html`
* **Role:** Provides course roster management and academic engagement evaluation forms for faculty mentors.
* **Key Components:**
  * Enrolled student directory table with instant "Rate" modal triggers.
  * Academic logging form (timely submissions, classroom participation, qualitative notes).
  * Weekly academic summary table with complete separation from psychological scores.

#### 8. Counsellor Clinical View: `templates/counsellor_dashboard.html`
* **Role:** Provides the clinical control center for campus counsellors.
* **Key Components:**
  * AI Priority Flagged Queue highlighting students with $\ge 3$ consecutive high-risk days.
  * Monitored student directory with priority risk status badges.
  * Asynchronous 360° student drilldown modal displaying psychometrics, faculty remarks, and 5-day check-in logs.
  * Consultation schedule manager and post-session clinical notes submission modal.
  * Split-pane multi-student messaging interface.

#### 9. Ditto Stylesheet: `static/style.css`
* **Role:** Implements the complete Sunlit Wildflower / Ditto design system.
* **Key Components:**
  * Complete `:root` CSS custom property tokens for color, typography, spacing, and border radii.
  * Tactile 3D button animations (`.btn-3d`), custom range slider thumb styling, and responsive glassmorphism card containers.
  * Priority risk status badges, chat bubbles, responsive data tables, and modal overlay animations.

#### 10. Frontend Script Engine: `static/script.js`
* **Role:** Encapsulates all client-side JavaScript behaviors.
* **Key Components:**
  * Dynamic slider value updates and track fill gradient synchronization.
  * Non-destructive polling chat engine with smart-scroll preservation.
  * Universal modal controller handling backdrop clicks and `Escape` key dismissals.
  * Mobile drawer navigation controls.
  * Demo credentials auto-fill and password visibility toggling.
  * XSS prevention via global `window.escapeHtml` string sanitizer.

#### 11. Integration Verification Suite: `tests/verify_app_integration.py`
* **Role:** Automated integration test suite validating end-to-end system health.
* **Key Components:**
  * Verifies model binary existence (`ml/student_risk_model.pkl`).
  * Asserts clean imports of Flask routes and SQLAlchemy models.
  * Confirms runtime loading of the `MLPredictor` singleton.
  * Executes test predictions across simulated low-risk and high-risk student profiles.
  * Validates SQLite database generation and seed record counts.

---

## 10. Installation, Setup & Local Environment Configuration

### 10.1 Hardware & Software Prerequisites
* **Operating System:** Windows 10/11, macOS (10.15+), or Linux (Ubuntu 20.04+, Debian 11+, Fedora 36+).
* **Python Runtime:** Python **3.8+** (Python 3.10 or 3.11 recommended).
* **RAM:** Minimum 4 GB RAM (8 GB+ recommended if retraining the XGBoost model on `CEP_Train_Data.csv`).
* **Disk Space:** 1 GB free disk space (or 2 GB if storing the full raw training dataset).

### 10.2 Step-by-Step Installation Walkthrough

#### 1. Clone the Repository
Clone the project repository to your local workstation:
```bash
git clone https://github.com/YashGadkar/CEP_Project_Prototype.git
cd CEP_Project_Prototype
```

### 10.3 Virtual Environment Configuration
It is strongly recommended to use an isolated Python virtual environment to prevent package version conflicts:

* **On Windows (PowerShell / Command Prompt):**
  ```powershell
  python -m venv .venv
  .venv\Scripts\activate
  ```

* **On macOS / Linux (Bash / Zsh):**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

*(Verify your environment is active: your terminal prompt should display `(.venv)`.)*

### 10.4 Python Package Dependency Installation
Install all required pinned dependencies using `pip`:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### Core Package Breakdown:
* `Flask==3.1.3`: Core WSGI web application framework.
* `Flask-SQLAlchemy==3.1.1`: SQLAlchemy database ORM integration.
* `xgboost==3.4.1`: Gradient boosting model engine.
* `scikit-learn==1.9.0`: Preprocessing transformers, pipelines, and evaluation metrics.
* `pandas==3.0.5`: Tabular data processing.
* `numpy==2.5.2`: Numerical array operations.
* `joblib==1.5.3`: Model pipeline serialization and deserialization.
* `Werkzeug==3.1.8`: Cryptographic password hashing and WSGI utilities.

### 10.5 Database Generation & Seed Credentials
MindGarden automates database generation. You do not need to run manual SQL migration scripts. When `app.py` is started for the first time, it automatically creates `instance/mindgarden.db` and provisions default seed accounts:

| Stakeholder Role | Pre-Seeded Email | Default Password | Initial State / Description |
|---|---|---|---|
| **Student** | `student@college.edu` | `student123` | Provisioned as "Alex Mercer". Ready for baseline survey onboarding. |
| **Faculty Member** | `faculty@college.edu` | `faculty123` | Provisioned as "Prof. Vance". Active access to student roster. |
| **Campus Counsellor**| `counsellor@college.edu` | `counsellor123` | Provisioned as "Dr. Sarah Jenkins". Active access to AI Priority Queue. |

*(Note: In accordance with collegiate security rules, all self-registration signups require an email ending in `.edu`.)*

### 10.6 Execution of the Local Development Server
Launch the Flask development server:
```bash
python app.py
```

The terminal will confirm that the database has seeded and display the active server address:
```
Seeding SQLite database with default data...
Database seeding completed.
ML model loaded successfully.
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

You can click any of the **1-Click Demo Account Buttons** on the login card to immediately explore any stakeholder experience.

---

## 11. Model Training & Machine Learning Operations Guide

The repository includes a pre-trained model file (`ml/student_risk_model.pkl`). However, if you wish to retrain the model on updated student wellness records, follow the steps below.

### 11.1 Preparing the Training Corpus (`ml/CEP_Train_Data.csv`)
1. Place your training dataset named `CEP_Train_Data.csv` inside the `ml/` directory.
2. Ensure the CSV contains the target column `risk_level` with categories `Low`, `Medium`, and `High`.
3. *(Note: Because `CEP_Train_Data.csv` is ~294 MB in size, it is excluded from Git tracking via `.gitignore` to prevent repository bloat.)*

### 11.2 Executing the Training Script
Run the standalone training pipeline:
```bash
python ml/train_and_save_model.py
```

#### Expected Execution Output:
```
--- Loading dataset ---
Dataset shape: (100000, 21)

--- Encoding target variable ---
Class 0 -> High
Class 1 -> Low
Class 2 -> Medium

--- Splitting data ---
Nominal features: ['gender']
Numerical features (17): ['age', 'academic_year', 'study_hours_per_day', 'exam_pressure', 'academic_performance', 'stress_level', 'anxiety_score', 'depression_score', 'sleep_hours', 'physical_activity', 'social_support', 'screen_time', 'internet_usage', 'financial_stress', 'family_expectation', 'burnout_score', 'mental_health_index']

--- Computing sample weights for class balance ---

--- Initializing and training XGBoost Classifier ---
Fitting model...
Model fit complete!
Train Accuracy: 0.8942
Test Accuracy: 0.8816

--- Saving model to ml/student_risk_model.pkl ---
Model saved successfully!
```

### 11.3 Inspecting Pipeline Weights & Artifacts
The training script produces `ml/student_risk_model.pkl`, which packages three essential components:
1. `pipeline`: The complete Scikit-Learn `Pipeline` object containing the fitted `ColumnTransformer` (`OneHotEncoder` + passthrough) and trained `XGBClassifier`.
2. `label_encoder`: The fitted `LabelEncoder` instance mapping classes `[0, 1, 2]` back to `['High', 'Low', 'Medium']`.
3. `features`: An ordered list of feature column names matching the training dataset, used during inference to align input columns.

### 11.4 Research & Experimentation via Jupyter (`ml/CEP_Code.ipynb`)
For data science research, feature importance extraction, and exploratory data analysis (EDA), open the included research notebook:
```bash
jupyter notebook ml/CEP_Code.ipynb
```
The notebook contains feature correlation heatmaps, class distribution visualizations, ROC-AUC curve comparisons, and SHAP (SHapley Additive exPlanations) value analyses detailing how features like sleep deprivation and exam pressure drive high-risk predictions.

---

## 12. Quality Assurance, Testing & Verification Suite

### 12.1 Automated Integration Verification (`tests/verify_app_integration.py`)
MindGarden includes a comprehensive automated integration verification suite in `tests/verify_app_integration.py`. This script tests the integrity of the database, model file, web framework imports, and inference pipeline in a single command.

Run the test suite from the project root:
```bash
python tests/verify_app_integration.py
```

### 12.2 Integration Test Assertions & Test Criteria
The verification script performs 5 sequential validation checks:

```
[Test 1: Model Binary Check]
   Verifies ml/student_risk_model.pkl exists on disk.
   Assertion: os.path.exists(model_path) == True
         │
         ▼
[Test 2: Server Imports & Model Definitions Check]
   Verifies clean import of app, db, and all 8 SQLAlchemy models.
   Assertion: User, StudentProfile, DailyCheckin, FacultyRating, SessionBooking, Quote imported without syntax or namespace errors.
         │
         ▼
[Test 3: ML Predictor Runtime Check]
   Verifies that ml.ml_handler.predictor has initialized and deserialized the Scikit-learn Pipeline.
   Assertion: predictor.pipeline is not None
         │
         ▼
[Test 4: Real-Time Inference Assertion Check]
   Dispatches two synthetic 18-feature student profiles (one healthy baseline, one severe distress profile) to predictor.predict().
   Assertion: Both predictions return valid strings in ['Low', 'Medium', 'High'].
         │
         ▼
[Test 5: Database Creation & Seed Verification Check]
   Initializes the database context, runs db.create_all() and seed_db().
   Assertion: User.query.count() >= 3 and Quote.query.count() >= 10.
```

When all checks succeed, the script outputs:
```
=== MindGarden App Integration Verification ===
SUCCESS: Trained XGBoost model file found.
SUCCESS: Flask server and SQLAlchemy models imported successfully.
SUCCESS: ML Predictor successfully loaded XGBoost pipeline.
SUCCESS: Low risk prediction output: Low
SUCCESS: High risk prediction output: High
SUCCESS: SQLite Database tables verified.
         Seed counts -> Users: 3, Quotes: 10

ALL INTEGRATION VERIFICATION TESTS PASSED SUCCESSFULLY!
```

### 12.3 Role-by-Role Manual Verification Playbook

#### Scenario A: The Student Wellness Workflow
1. Navigate to `http://127.0.0.1:5000/login`.
2. Click the **🌱 Alex** demo filler button to load `student@college.edu` and log in.
3. If logging in for the first time, verify that you are redirected to `/onboarding`. Complete the 14-parameter survey and submit.
4. On the student dashboard, observe the "Thought of the Day" quote banner.
5. Move the daily habit sliders:
   * Set *Sleep Hours* to `4.0 hrs`
   * Set *Study Hours* to `9.0 hrs`
   * Set *Exam Pressure* to `9 / 10`
   * Set *Stress Level* to `8 / 10`
   * Set *Mood Score* to `3 / 10`
6. Click "Submit Daily Log". Verify that:
   * The button transitions to "Analyzing with AI...".
   * The card smoothly animates into a "Check-in successful!" confirmation card.
   * A new row appears at the top of the Check-in History table displaying the predicted risk badge.
   * The Chart.js trendline canvas dynamically appends the new data points.
7. Click "Book Call" in the Consultations card. Select a date and time, and click "Confirm Appointment". Verify that a new scheduled card appears with a clickable "Join Call" link.
8. Type a message in the chat panel and click "Send". Confirm that the message renders locally immediately and persists across refreshes.

#### Scenario B: The Faculty Mentorship Workflow
1. Log out, return to `/login`, and click **📚 Vance** to sign in as `faculty@college.edu`.
2. On the Faculty Dashboard, locate "Alex Mercer" in the student roster.
3. Click "Rate". Observe that the rating card smoothly scrolls into view with the student's name pre-populated.
4. Select *Timely Submissions: No*, *Participation: Low*, and enter an observational note: *"Alex appeared exhausted in class today and missed the assignment deadline."*
5. Click "Submit Engagement Record". Verify that the weekly summary table immediately updates with the new academic record.
6. Verify that **no psychological test scores, depression ratings, or AI risk predictions** are visible on this portal.

#### Scenario C: The Counsellor Clinical Workflow
1. Log out, return to `/login`, and click **🩺 Sarah** to sign in as `counsellor@college.edu`.
2. On the Counsellor Dashboard, inspect the **AI Priority Flagged Queue**. Verify that students with 3 or more consecutive high-risk days appear at the top of the queue with active streak counters.
3. Click "Profile" on any student in the queue.
4. Confirm that the **360° Student Drilldown Modal** opens and correctly displays:
   * The student's baseline psychometric scores.
   * The computed average nightly sleep (e.g., `4.8 hrs/night (avg)`).
   * The faculty engagement rating and observational remarks logged by Prof. Vance.
   * The recent 5-day daily check-in progression table.
5. Close the modal, open the Messenger, select the student, and verify that conversation messages sync in real time.
6. Under "Consultations Schedule", locate the appointment scheduled by the student, click "Log Notes", select *Improvement: Moderate*, enter clinical remarks, and submit. Verify that the session status transitions to **Completed**.

### 12.4 Edge Cases, Boundary Tests, and Error Trapping
* **Duplicate Daily Check-ins:** If a student attempts to submit a second daily check-in on the same date, the server returns an error message: `"Already checked in today!"`. The client catches this and displays an informative toast notification.
* **Unauthenticated Endpoint Access:** Directly requesting protected URLs (such as `/student/dashboard` or `/counsellor/dashboard`) without an active session immediately redirects the user to `/login`.
* **Cross-Role Unauthorized Navigation:** If an authenticated student attempts to browse to `/counsellor/dashboard`, the route handler intercepts the mismatched role and redirects them to their appropriate dashboard.
* **Missing Model Artifact Fallback:** If `ml/student_risk_model.pkl` is accidentally deleted, `ml_handler.py` catches the missing file, logs a warning, and returns `"Low"` as a safe default, preventing server crashes.
* **Invalid Form Inputs:** If non-numeric strings are submitted for slider values, Flask catches the type-conversion error and handles it gracefully.

---

## 13. Security, Privacy, and Ethical AI Considerations

### 13.1 Strict Separation of Powers & FERPA/HIPAA Principles
Educational mental health platforms operate at the intersection of student privacy standards (such as **FERPA** in the United States) and clinical health data protections (such as **HIPAA** principles):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ROLE-BASED DATA FIREWALL                              │
├──────────────────────────────────────┬──────────────────────────────────────┤
│               FACULTY                │              COUNSELLOR              │
│       (Academic Context Only)        │       (Clinical Context Only)        │
├──────────────────────────────────────┼──────────────────────────────────────┤
│  ✅ Class Attendance                 │  ✅ All Faculty Academic Notes       │
│  ✅ Assignment Submission Timeliness │  ✅ Baseline Psychological Surveys   │
│  ✅ Classroom Participation Level    │  ✅ Daily Habit Tracking (Sleep/Mood)│
│  ✅ Observational Academic Notes     │  ✅ XGBoost AI Risk Classifications  │
│  ❌ Baseline Depression/Anxiety Score│  ✅ Clinical Therapy Session Notes   │
│  ❌ Daily Sleep or Mood Records      │  ✅ Direct Confidential Messaging    │
│  ❌ Machine Learning Risk Category   │                                      │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

By enforcing these boundaries at the database and template levels, MindGarden protects students from unintended academic consequences (such as grading bias) while ensuring campus counsellors have access to the context needed to provide care.

### 13.2 Data Protection, Passwords, and Session Cryptography
* **Password Hashing:** Passwords are cryptographically salted and hashed using PBKDF2-SHA256 via Werkzeug. Plaintext passwords are never logged or stored.
* **Session Cookie Integrity:** Session cookies are signed using a server-side secret key (`app.secret_key`). In a production environment, this should be supplied via an environment variable with the `SESSION_COOKIE_SECURE=True` and `SESSION_COOKIE_HTTPONLY=True` flags enabled.
* **Email Validation:** Collegiate identity is verified at registration by requiring email addresses to end with `.edu`.

### 13.3 Client-Side XSS Mitigation & DOM Sanitization
When rendering dynamic user content in client-side scripts (such as chat messages, observational notes, and student names in modal dialogs), MindGarden routes all strings through a dedicated sanitization helper (`window.escapeHtml`):
```javascript
window.escapeHtml = function(str) {
    if (!str && str !== 0) return "";
    return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
};
```
This ensures that any malicious HTML tags or script injection attempts are neutralized before being inserted into the DOM.

### 13.4 Ethical AI Principles & Clinical Human-in-the-Loop Safeguards
1. **Decision-Support, Not Automated Diagnosis:** MindGarden's XGBoost classifier is explicitly designed as an **early-warning triage tool**, not a diagnostic medical device. It assists counsellors in prioritizing outreach; it never makes autonomous clinical diagnoses or prescribes medical treatments.
2. **Human-in-the-Loop Intervention:** The AI model cannot unilaterally alter a student's academic standing, notify family members, or take punitive actions. Every high-risk alert simply brings the student to the attention of a licensed campus counsellor, who evaluates the situation using professional clinical judgment.
3. **No Punitive Data Usage:** Mental health metrics collected in MindGarden are strictly siloed from academic transcripts, grade point averages, and disciplinary records.

---

## 14. Production Deployment & Scalability Architecture

While the built-in Flask development server is ideal for local testing, deploying MindGarden in an institutional production environment requires a robust production architecture:

```
[Web Traffic (HTTPS:443)] ──> [Nginx Reverse Proxy]
                                     │
                                     ├──> Static Asset Cache (/static/style.css, script.js)
                                     │
                                     └──> WSGI Application Server (Gunicorn / Waitress)
                                                 │
                                                 ├──> Flask Core Workers (app.py)
                                                 │           │
                                                 │           ▼
                                                 ├──> Persistent Database (PostgreSQL)
                                                 │
                                                 └──> ML Inference Singleton (In-Memory XGBoost)
```

### 14.1 WSGI Production Web Servers (Gunicorn / Waitress)
Flask's built-in development server is single-threaded by default and should not be used in production.

* **For Linux / macOS Deployments (Gunicorn):**
  Install Gunicorn:
  ```bash
  pip install gunicorn
  ```
  Launch Gunicorn with 4 pre-forked worker processes bound to an internal port:
  ```bash
  gunicorn --workers 4 --bind 127.0.0.1:8000 app:app
  ```

* **For Windows Server Deployments (Waitress):**
  Install Waitress:
  ```bash
  pip install waitress
  ```
  Run the server using Waitress:
  ```bash
  waitress-serve --port=8000 app:app
  ```

### 14.2 Reverse Proxy Configuration with Nginx
Nginx should sit in front of the WSGI server to handle SSL/TLS termination, request buffering, rate limiting, and high-performance static asset caching.

Example Nginx server configuration block (`/etc/nginx/sites-available/mindgarden`):
```nginx
server {
    listen 80;
    server_name mindgarden.university.edu;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name mindgarden.university.edu;

    ssl_certificate /etc/letsencrypt/live/mindgarden.university.edu/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/mindgarden.university.edu/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    # Serve static assets directly from disk
    location /static/ {
        alias /var/www/CEP_Project/static/;
        expires 30d;
        add_header Cache-Control "public, no-transform";
    }

    # Proxy application requests to Gunicorn
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_connect_timeout 60s;
        proxy_read_timeout 60s;
    }
}
```

### 14.3 Transitioning from SQLite to PostgreSQL
For enterprise deployments supporting thousands of concurrent students, migrate the persistence tier from SQLite to **PostgreSQL**:
1. Install the PostgreSQL database adapter:
   ```bash
   pip install psycopg2-binary
   ```
2. Update the database URI in `app.py` or set an environment variable:
   ```python
   import os
   app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
       "DATABASE_URL", 
       "postgresql://mindgarden_user:SecurePassword123@localhost:5432/mindgarden_prod"
   )
   ```
3. SQLAlchemy handles schema generation and queries across both SQLite and PostgreSQL without requiring application code changes.

### 14.4 Asynchronous Worker Infrastructure (Celery & Redis)
As campus enrollment scales, asynchronous background tasks (such as sending email notifications, generating clinical PDF summaries, and scheduling recurring analytics jobs) can be offloaded to **Celery** with a **Redis** message broker:
* **Background Email Dispatch:** Offload appointment confirmation emails to background workers.
* **WebSocket Chat Upgrade:** Upgrade the 4.5-second polling chat engine to persistent WebSockets via `Flask-SocketIO` and Redis Pub/Sub for instantaneous messaging.

### 14.5 Containerization with Docker & Docker Compose
To containerize the application for deployment via Docker or Kubernetes:

#### `Dockerfile`
```dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "app:app"]
```

#### `docker-compose.yml`
```yaml
version: '3.8'

services:
  web:
    build: .
    container_name: mindgarden_app
    restart: always
    ports:
      - "8000:8000"
    environment:
      - FLASK_ENV=production
      - SECRET_KEY=your_production_secret_key_here
      - DATABASE_URL=postgresql://mindgarden:gardenpass@db:5432/mindgardendb
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    container_name: mindgarden_db
    restart: always
    environment:
      POSTGRES_USER: mindgarden
      POSTGRES_PASSWORD: gardenpass
      POSTGRES_DB: mindgardendb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

---

## 15. Troubleshooting & Frequently Asked Questions (FAQ)

### 15.1 Diagnostic Checklist
If you encounter unexpected behavior during setup or runtime, follow this diagnostic checklist:
* [ ] Is the Python virtual environment active? (Check for `(.venv)` in your terminal prompt).
* [ ] Are all requirements installed? (Run `pip list` and verify `Flask`, `xgboost`, and `scikit-learn`).
* [ ] Does the trained model file exist at `ml/student_risk_model.pkl`?
* [ ] Did the automated integration verification pass? (Run `python tests/verify_app_integration.py`).
* [ ] Does your browser console show any JavaScript syntax or network errors?

---

### 15.2 Common Issues & Resolutions

#### Issue 1: `ModuleNotFoundError: No module named 'xgboost'` or `scikit-learn`
* **Root Cause:** Packages were installed in a different Python environment than the one currently executing `app.py`.
* **Resolution:** Ensure your virtual environment is active, then reinstall requirements:
  ```bash
  # Windows
  .venv\Scripts\activate
  pip install -r requirements.txt
  
  # Linux/macOS
  source .venv/bin/activate
  pip install -r requirements.txt
  ```

#### Issue 2: `Warning: Model file .../student_risk_model.pkl not found`
* **Root Cause:** The serialized machine learning pipeline has not been generated or was deleted.
* **Resolution:** Run the standalone training script to retrain and export the model:
  ```bash
  python ml/train_and_save_model.py
  ```

#### Issue 3: `sqlite3.OperationalError: database is locked`
* **Root Cause:** SQLite encountered concurrent write locks, often caused by having the database file open simultaneously in an external SQLite GUI browser.
* **Resolution:** Close any external SQLite viewers or database exploration tools. For concurrent production environments, migrate to PostgreSQL as outlined in [Section 14.3](#143-transitioning-from-sqlite-to-postgresql).

#### Issue 4: `College registration requires a valid college email ending with .edu`
* **Root Cause:** Self-registration requires a valid collegiate email domain.
* **Resolution:** Use an email address ending with `.edu` (e.g., `newstudent@university.edu`) when creating an account via the Sign Up tab.

#### Issue 5: Sliders Do Not Update Fill Progress Color
* **Root Cause:** Browser JavaScript execution was blocked, or older cached static assets are being served.
* **Resolution:** Hard refresh your browser (`Ctrl + F5` on Windows/Linux or `Cmd + Shift + R` on macOS) to clear cached versions of `static/script.js` and `static/style.css`.

---

### 15.3 Comprehensive Developer & User FAQ

#### Q1: Can MindGarden make medical or psychiatric diagnoses?
**No.** MindGarden is an educational early-warning triage tool. It evaluates lifestyle and academic indicators to predict relative psychological risk (`Low`, `Medium`, `High`), highlighting students who may benefit from support. All clinical evaluations, diagnoses, and care plans are made exclusively by licensed human campus counsellors.

#### Q2: What happens if a student has a single bad day? Will they be immediately flagged?
**No.** MindGarden’s triage algorithm requires a student to record **3 or more consecutive high-risk days** before escalating them into the counsellor's AI Priority Flagged Queue. This prevents false positives caused by temporary acute events (such as pulling an all-nighter before a midterm exam).

#### Q3: Can professors or teaching assistants see student risk scores?
**No.** The platform enforces a strict privacy firewall. Faculty members can only view course rosters, record assignment punctuality, rate classroom participation, and log academic observations. They have zero access to psychological survey scores, daily check-in logs, or AI risk predictions.

#### Q4: What machine learning algorithm powers MindGarden, and why was it chosen?
MindGarden uses **XGBoost (`XGBClassifier`)**. Gradient-boosted decision trees consistently outperform deep neural networks on tabular datasets with mixed numerical and categorical features. XGBoost handles non-linear relationships and feature interactions effectively while maintaining millisecond-level inference latency on modest server hardware.

#### Q5: How are Google Meet links generated for consultation bookings?
When a student schedules an appointment, the backend constructs a predictable, structured room link:
```
https://meet.google.com/mock-garden-{student_id}-{counsellor_id}
```
In a full production deployment, this can be integrated with the Google Calendar API or Zoom API via OAuth2 to generate verified video conference rooms automatically.

#### Q6: How does the system handle missing or incomplete baseline profiles?
If a student logs in without completing their baseline assessment, the application's routing dispatcher catches the missing profile and redirects them to `/onboarding`. Similarly, the daily check-in API requires a completed profile before running inference.

#### Q7: Can the platform run entirely offline in a closed campus intranet?
**Yes.** MindGarden has zero mandatory external cloud dependencies. The Flask web server, SQLite database, and XGBoost inference pipeline execute completely locally. To run without an internet connection, you can download the local font files and Chart.js library to the `static/` directory.

---

## 16. Appendix: References, Citations, & Acknowledgments

### 16.1 Academic Literature & Clinical Context
1. **American College Health Association (ACHA-NCHA III):** *National College Health Assessment Reference Group Executive Summary.* Research on the prevalence of anxiety, depression, and academic impairment in undergraduate populations.
2. **Chen, T., & Guestrin, C. (2016):** *XGBoost: A Scalable Tree Boosting System.* Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.
3. **Pedregosa et al. (2011):** *Scikit-learn: Machine Learning in Python.* Journal of Machine Learning Research, 12, 2825–2830.
4. **World Health Organization (WHO):** *Mental Health and Digital Interventions for Young Adults: Guidelines and Ethical Frameworks.*

### 16.2 Core Technologies & Open Source Acknowledgments
MindGarden is built with gratitude on the open-source software ecosystem:
* **[Python](https://www.python.org/):** The core programming language powering our backend and ML pipelines.
* **[Flask](https://flask.palletsprojects.com/):** The lightweight WSGI web framework by the Pallets Projects.
* **[XGBoost](https://xgboost.readthedocs.io/):** Scalable, portable, and distributed gradient boosting library.
* **[Scikit-Learn](https://scikit-learn.org/):** Machine learning tools for data analysis and pipeline preprocessing.
* **[SQLAlchemy](https://www.sqlalchemy.org/):** The Python SQL toolkit and Object Relational Mapper.
* **[Chart.js](https://www.chartjs.org/):** Simple, flexible JavaScript charting for client-side visualizations.
* **[Google Fonts](https://fonts.google.com/):** For typography (*Hedvig Letters Serif* and *Inter*).
* **[Font Awesome](https://fontawesome.com/):** Vector icon assets.

---

<div align="center">

### 🌱 MindGarden — Nurturing Student Wellness, One Day at a Time.
*Developed for Campus Communities, Faculty Mentors, and Mental Health Professionals.*

<br/>

[⬆ Back to Top](#-mindgarden-student-mental-health-prediction--support-platform)

</div>
