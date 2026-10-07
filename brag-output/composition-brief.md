# Hyperframes Composition Brief: MindGarden

## Objective
Create a short, polished, human-centered introduction launch video for MindGarden, a Community Engineering Project (CEP) for campus mental health vulnerability prediction and early intervention.

## Output
- Composition directory: `brag-output/composition/`
- Rendered video: `brag-output/brag.mp4`
- Format: landscape — 1920x1080
- Duration: 20 seconds (600 frames at 30 fps)

## Source Material
- Project root: `c:/MindGarden`
- Primary files read: `README.md`, `static/style.css`, `templates/student_dashboard.html`, `templates/counsellor_dashboard.html`, `app.py`
- Product name: MindGarden
- Tagline / strongest claim: "An Intelligent, Multi-Stakeholder Intervention Ecosystem Powered by XGBoost, Flask, and the Ditto Design System"
- Key UI or visual moments to recreate:
  - The Sunlit Wildflower Atelier ("Ditto") design aesthetics: rounded cards, pill buttons, warm meadow canvas.
  - Student Daily Check-in with tactile habit & pressure sliders.
  - XGBoost Multi-Class Risk Inference badge & 18-Feature Vector.
  - Campus Counsellor Clinical Priority Queue alert card.
- Copy that must appear verbatim:
  - "Campus mental health shouldn't wait for a crisis."
  - "MindGarden 🌱 — Proactive Student Wellness & Vulnerability Prediction"
  - "18-Feature Psychological Vector · XGBoost Inference"
  - "Priority Clinical Triage Queue"
  - "Early prediction. Empathetic intervention. Zero stigma."
  - "Community Engineering Project (CEP)"

## Creative Direction
- Tone preset: polished
- Creative direction: "An inspiring, human-centered Community Engineering Project introduction video showcasing proactive campus mental health support."
- Interpretation: Thoughtful, elegant, warm, and confident. High visual polish, authentic UI representations, and respectful dignity for collegiate mental wellness.
- Angle: Traditional university mental health is passive and siloed, intervening only when students reach acute crisis. MindGarden unites students, faculty mentors, and campus counsellors through XGBoost predictive early detection.
- Hook: "Campus mental health shouldn't wait for a crisis." (First 2.5s)
- Outro / punchline: "Early prediction. Empathetic intervention. Zero stigma." (Final 4s)
- Avoid:
  - Generic SaaS buzzwords ("streamline your workflow", "boost your productivity")
  - Abstract filler graphics
  - Chaotic strobe effects or aggressive alarms

## Visual Identity
- Background: #f8faf5 (Soft Canvas / Warm Meadow)
- Card Paper: #ffffff (with border: 1.5px solid rgba(15, 23, 42, 0.08), border-radius: 20px, box-shadow: 0 10px 30px rgba(15, 23, 42, 0.04))
- Text / Deep Ink: #0f172a
- Slate Muted: #64748b
- Brand Primary: #f59e0b (Sunlit Amber) and #15803d (Moss Green)
- Risk Accents: Low (#16a34a), Medium (#d97706), High (#dc2626)
- Display font: 'Hedvig Letters Serif', Georgia, serif
- Body font: 'Inter', system-ui, -apple-system, sans-serif

## Storyboard Summary
1. **Scene 1 — The Problem & The Awakening (0.0s – 4.5s):**
   Dark contemplative opening transitioning into sunlit warmth. "Campus mental health shouldn't wait for a crisis." → MindGarden mark emerges.
2. **Scene 2 — The Ditto Student Experience (4.5s – 9.5s):**
   Daily Check-in card with interactive sliders (Sleep: 7.5 hrs, Social Support, Academic Load) and dynamic Mental Health Index counter.
3. **Scene 3 — XGBoost Inference & Counsellor Triage (9.5s – 15.0s):**
   18-feature psychological vector flows into XGBoost classification. The Counsellor Priority Queue activates with real-time early risk notification.
4. **Scene 4 — The Triad & Project Close (15.0s – 20.0s):**
   The unified triad (Students · Faculty · Counsellors). "Early prediction. Empathetic intervention. Zero stigma." Grand MindGarden emblem with CEP attribution.

## Audio
- Audio role: Warm community/collegiate bed with subtle, authentic UI accents
- Music: `assets/music/happy-beats-business-moves-vol-12-by-ende-dot-app.mp3`
- Music treatment: Starts at t=0s, volume 0.32, smooth rhythmic progression, subtle fade out over the last 1.2s.
- Music cue guidance: Preset cues at 8.74s, 13.11s, 17.47s; beat locks on major card appearances and status reveals.
- SFX files:
  - `assets/sfx/interface/drop_001.ogg` at ~2.5s (MindGarden card entrance)
  - `assets/sfx/interface/click_002.ogg` at ~6.2s (Slider settle)
  - `assets/sfx/impact/impactBell_heavy_000.ogg` at ~11.8s (Clinical priority queue alert)
  - `assets/sfx/interface/bong_001.ogg` at ~16.5s (Brand outro resolve)

## Hyperframes Instructions
- Composition structure: Single index.html using native Hyperframes data attributes (`data-start`, `data-duration`, `data-track-index`, `data-volume`).
- Ensure high WCAG contrast on all text elements.
- Ensure all text has sufficient settled reading time.
- All styles, layout, and motion should reflect the authentic MindGarden Ditto Design System tokens.
- Run `hyperframes check` before rendering.
