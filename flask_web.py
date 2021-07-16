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
        from_db = db.get(word)

        if from_db:
            jobs = from_db
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")

    return render_template("report.html", searchingBy=word, resultsNumber=len(jobs))


app.run(debug=True)
