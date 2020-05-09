import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    return (
        "<h1>Will Schlitzer</h1><p>An attempt at a personal page to learn Flask adn web app development</p>"
    )

app.run()