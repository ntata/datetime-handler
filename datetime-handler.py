import flask
from flask import jsonify
import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to my Date Time Handler!</h1>
<p>A prototype API for displaying current date/time in json (ISO) format</p>'''


# health check route
@app.route('/_health', methods=['GET'])
def health_check():
    return "200 OK"


# A route to return current date time in hh:mm:ss.microseconds format.
@app.route('/api/v1/timenow', methods=['GET'])
def api_all():
    return jsonify(datetime.datetime.now().isoformat())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
