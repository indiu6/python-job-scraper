from scraper import get_jobs
from flask import Flask, render_template, request, redirect

app = Flask("FlaskScraper")

db = {}


@app.route("/")  # '@' is Decorator
def home():
    return render_template("home.html")


@app.route("/<username>")
def say_name(username):
    return f"Your name is {username}"


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        existing_jobs = db.get(word)

        if existing_jobs:
            jobs = existing_jobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")

    return render_template(
        "report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs
    )


@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        return f"Generate CSV for {word}"
    except:
        return redirect("/")


app.run(debug=True)
