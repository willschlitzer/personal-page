import flask

app = flask.Flask(__name__)

def main():
    app.run(debug=True)

@app.route("/", methods=["GET"])
def home():
    return flask.render_template("home/home.html")

@app.route("/about", methods=["GET"])
def about():
    return "<h1>About Schlitz</h1><p>I'm making a website.</p>"


if __name__ == "__main__":
    main()
