from flask import Flask

app = Flask("FlaskScraper")


@app.route("/")  # '@' is Decorator
def home():
    return "Hello, flask"


@app.route("/contact")
def contact():
    return "Contact me!"


app.run(debug=True)
