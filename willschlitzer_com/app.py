import flask

app = flask.Flask(__name__)

def main():
    app.run(debug=True)

@app.route("/", methods=["GET"])
def home():
    return "<h1>Will Schlitzer's Page</h1><p>This page is being built to learn Flask.</p>"

@app.route("/about", methods=["GET"])
def about():
    return "<h1>About Schlitz</h1><p>I'm making a website.</p>"


if __name__ == "__main__":
    main()
