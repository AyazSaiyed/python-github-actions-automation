from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "welcome to the demo of python github actions"

@app.route("/")
def index2():
    return "Hello, Ayaz!"


if __name__ == "__main__":
    app.run()

