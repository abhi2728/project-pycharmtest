from flask import Flask

app = Flask(__name__)


# @app.route('//myabhishektripathi.com/')
@app.route('/')
def hello():
    return 'Hello Abhishek'


if __name__ == "__main__":
    app.run(debug=True)
