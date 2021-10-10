from logging import root
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    first = "this is my first condition"
    return render_template("index.html", message=first)

@app.route("/tariq")
def mylist():
    names = ["mike", "james", "bilbao", "luca"]
    return render_template("body.html", object=names)





if __name__== "__main__":
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=80)