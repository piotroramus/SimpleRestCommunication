from flask import Flask

app = Flask(__name__)


@app.route("/hello", methods=['GET'])
def api_temperature():
    return "Hello from server"


if __name__ == '__main__':
    app.run(debug=False)
