from flask import Flask,flash, render_template, request, session, jsonify,url_for,redirect,make_response
from flask_assets import Environment, Bundle
from flask_scss import Scss


app = Flask(__name__)
Scss(app)



bundles = {
    "flex.css": Bundle('css/flex.css', output = "gen/flex.css"),
    "general.css": Bundle('assets/scss/general.scss', filters='pyscss', output='gen/general.css')
}

assets = Environment(app)
assets.register(bundles)



@app.route('/')
def index():

    return render_template("home.html")



if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)


    