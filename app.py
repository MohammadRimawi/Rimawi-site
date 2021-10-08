from flask import Flask,flash, render_template, request, session, jsonify,url_for,redirect,make_response
from flask_assets import Environment, Bundle

app = Flask(__name__)


@app.route('/')
def index():

    return render_template("home.html")



if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)


    