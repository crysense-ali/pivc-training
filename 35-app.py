# -*- coding: utf-8 -*-
import os, json
from flask import Flask, send_from_directory, request, redirect, url_for, render_template, abort, make_response
from content import MODULES, STEPS, NANDA, REFERENCES, UI

HERE = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=HERE, static_folder=None)

@app.route("/static/<path:filename>", endpoint="static")
def static_files(filename):
    if filename not in ("store.js", "style.css"): abort(404)
    return send_from_directory(HERE, filename)

def lang():
    return "ar" if request.cookies.get("lang") == "ar" else "en"

@app.context_processor
def ctx():
    L = lang(); i = 0 if L == "en" else 1
    def t(k): return UI[k][i]
    return dict(t=t, L=L, dir="rtl" if L == "ar" else "ltr")

@app.after_request
def nocache(r):
    if r.mimetype == "text/html": r.headers["Cache-Control"] = "no-store"
    return r

@app.route("/lang")
def setlang():
    r = make_response(redirect(request.referrer or url_for("home")))
    r.set_cookie("lang", "en" if lang() == "ar" else "ar", max_age=31536000)
    return r

@app.route("/")
def home():
    return render_template("home.html", modules=MODULES)

@app.route("/modules")
def modules():
    return render_template("modules.html", modules=MODULES)

@app.route("/module/<mid>")
def module(mid):
    m = next((x for x in MODULES if x["id"] == mid), None) or abort(404)
    idx = MODULES.index(m)
    L = lang()
    quiz = [dict(a=q["a"]) for q in m["quiz"]]
    return render_template("module.html", m=m, quiz_json=json.dumps(quiz), nxt=MODULES[idx + 1] if idx + 1 < len(MODULES) else None)

@app.route("/simulator")
def simulator():
    i = 0 if lang() == "en" else 1
    steps = [dict(text=s[i], crit=s[2]) for s in STEPS]
    return render_template("simulator.html", steps_json=json.dumps(steps, ensure_ascii=False))

@app.route("/puzzle")
def puzzle():
    i = 0 if lang() == "en" else 1
    steps = [dict(id=k, text=s[i]) for k, s in enumerate(STEPS)]
    return render_template("puzzle.html", steps_json=json.dumps(steps, ensure_ascii=False))

@app.route("/checklist")
def checklist():
    return render_template("checklist.html", steps=STEPS, crit_json=json.dumps([1 if s[2] else 0 for s in STEPS]))

@app.route("/progress")
def progress():
    mods = [dict(id=m["id"], title=m["title"][lang()], total=len(m["quiz"])) for m in MODULES]
    return render_template("progress.html", mods_json=json.dumps(mods, ensure_ascii=False), n=len(STEPS))

@app.route("/nursing")
def nursing():
    return render_template("nursing.html", items=NANDA)

@app.route("/sources")
def sources():
    return render_template("sources.html", refs=REFERENCES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
