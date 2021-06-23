#comment added

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/")
def index2():
    return "Hello, Ayaz!"


if __name__ == "__main__":
    app.run()

