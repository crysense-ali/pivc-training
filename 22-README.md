# PIVC Training: Pediatric IV Cannulation Training and Self-Assessment (student prototype)
Flask + SQLite, Arabic/English (RTL), mobile first. Demo data only.
Run: pip install -r requirements.txt && python app.py  (http://localhost:5000). No accounts: progress is stored in the browser (localStorage).
Deploy: Dockerfile included (port from $PORT). Set SECRET_KEY. Free hosts may reset the SQLite file.
Features: 8 learning modules with quizzes, step simulator (choose next step, critical-step warnings), ordering puzzle,
self-assessment competency checklist (competent = all critical steps + 80% of steps), personal progress page,
nursing process page (NANDA-style labels, references only), sources page.
Limits: content is a summary of the listed sources and must be reviewed by the supervisor; it does not replace supervised practice.
