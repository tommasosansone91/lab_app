from flask import render_template
from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route("/")

def hello():
    return render_template('hello.html', message = "Hello World!")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
