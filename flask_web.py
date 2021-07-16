from flask import Flask, render_template, request

app = Flask("FlaskScraper")


@app.route("/")  # '@' is Decorator
def home():
    return render_template("basic_html.html")


@app.route("/<username>")
def say_name(username):
    return f"Your name is {username}"


@app.route("/report")
def report():
    word = request.args.get("word")
    return render_template("report.html", searchingBy=word)


app.run(debug=True)
