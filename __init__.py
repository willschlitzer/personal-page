from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "<h1>Will Schlitzer</h1><p>An attempt at a personal page to learn Flask and web app development.</p>"


if __name__ == "__main__":
    app.run(debug=True)
