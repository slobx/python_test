from flask import Flask,render_template, request, jsonify
from models import *

app = Flask(__name__)

@app.route("/")
def index():
    page = """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Comments</title>
    </head>

    <body>
        <h1>Welcome!</h1>
    </body>

    </html>
    """

    return page

@app.route("/comments")
def comments():

    comments = {}
    for k in COMMENTS:
        comments[k.text] = k.date
    return render_template('table.html', comments = comments)

@app.route("/api/v1.0/comments",methods=['GET'])
def api_comments():    

    return jsonify(comments =[e.serialize() for e in COMMENTS])

