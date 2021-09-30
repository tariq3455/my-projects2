from flask import Flask 

app = Flask(__name__)

@app.route("/")
def stevie():
    return "Hi tariq, we'll handle your problem in the break time"

@app.route('/second')
def second():
    return 'lay lay lom!'

@app.route('/third/subthird')
def third():
    return 'hacı noluyor burada yawww'

@app.route('/forth/<string:id>')
def forth(id):
    return f"id number of this is {id}"



if __name__=="__main__":
    app.run(debug=True)
    