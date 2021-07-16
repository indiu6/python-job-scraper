from flask import Flask, render_template

app = Flask("FlaskScraper")


@app.route("/")  # '@' is Decorator
def home():
    return render_template("basic_html.html")


@app.route("/<username>")
def say_name(username):
    return f"Your name is {username}"


@app.route("/contact")
def contact():
    return "Contact me at hewas6@gmail.com"


app.run(debug=True)
