# MindGarden Project Governance Rules

- Architecture: Flask 3.1.3, SQLAlchemy ORM, SQLite, XGBoost, Scikit-Learn.
- Privacy Firewall: Faculty accounts must NEVER have access to student mental health metrics, depression/anxiety scores, daily check-in logs, or AI risk predictions.
- Security Standards: Enforce PBKDF2-SHA256 password hashing and require all registration emails to end with `.edu`.
- UI Design: Adhere to the Ditto Design System (warm cream canvas `#f8faf5`, meadow green surfaces, tactile 3D buttons, WCAG-compliant status badges).
- Execution Protocol: Always write defensive code with try/except blocks. Never remove existing models or routes without explicit instruction.