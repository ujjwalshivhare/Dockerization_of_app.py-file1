from flask import flask
app=Flask(__name__)
@app.route("/info")
def lw():
    return"welcome to lw..."
app.run(host='0.0.0.0')
