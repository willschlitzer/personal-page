import flask

app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "<h1>Will Schlitzer's Page</h1><p>An attempt at a personal page to learn Flask and web app development.</p>"

@app.route("/about", methods=["GET"])
def about():
    return "<h1>About Schlitz</h1><p>I'm making a website.</p>"


if __name__ == "__main__":
    app.run(debug=True)
