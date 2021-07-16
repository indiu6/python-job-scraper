from scraper import get_jobs
from flask import Flask, render_template, request, redirect

app = Flask("FlaskScraper")


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
        jobs = get_jobs(word)
        print(jobs)
    else:
        return redirect("/")

    return render_template("report.html", searchingBy=word)


app.run(debug=True)
