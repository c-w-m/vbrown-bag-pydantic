import flask
from models.people import Person


app = flask.Flask(__name__)

# @app.route("/")
@app.get("/")
def index():
    return "<h1>SUPER simple API site</h1>Try it: <a href='/api'>/api</a>"


# @app.route('/api', methods=["POST"])
@app.post('/api')
def api():
    data = flask.request.json or {}
    person = Person(**data)
    print(person)
    return person.address.json()


if __name__ == '__main__':
    app.run(debug=True)
