# template taken from https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

from flask import Flask, jsonify, request, render_template
import requests
import json
import os
import time
import sys
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import flask_restless

application = Flask(__name__)
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)

class models:
    class Series(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        author = db.Column(db.Text)
        title = db.Column(db.Text)
        link = db.Column(db.Text)
        summary = db.Column(db.Text)
        content = db.Column(db.Text)
        updated = db.Column(db.DateTime)
        trending = db.Column(db.Text)

        def __repr__(self):
            return "<Series {}>".format(self.id)

    class News(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        heading = db.Column(db.Text)
        subheading = db.Column(db.Text)
        body = db.Column(db.Text)
        author = db.Column(db.Text)
        date = db.Column(db.DateTime)

        def __repr__(self):
            return "<News {}>".format(self.id)

db.create_all()

def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


application.after_request(add_cors_headers)

manager = flask_restless.APIManager(application, flask_sqlalchemy_db=db)

def post_get_single(result, **kw):
    print("aoe")
    print(result)
    try:
        print(result['body'])
        result['body'] = result['body'][0-101]

def post_get_many(result, search_params, **kw):
    print("aoeu")
    for r in result:
        try:
            print(r['body'])
            r['body'] = r['body'][0-101]

manager.create_api(
    models.Series,
    methods=["GET", "POST", "PUT", "DELETE"],
    allow_delete_many=True,
    max_results_per_page=500,
    results_per_page=9,
    url_prefix="/",
)
manager.create_api(
    models.News,
    methods=["GET", "POST", "PUT", "DELETE"],
    allow_delete_many=True,
    max_results_per_page=500,
    results_per_page=9,
    url_prefix="/",
)

manager.create_api(
    models.News,
    methods=["GET"],
    allow_delete_many=True,
    max_results_per_page=500,
    results_per_page=9,
    url_prefix="/latest",
    postprocessors={
        "GET_MANY": [post_get_many],
        "GET_SINGLE": [post_get_single]
    }
)





@application.route('/')
def hello_world():
    return 'Endpoints:\n/api/series\n/api/news\n/latest/news'

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True

    port = int(os.environ.get("PORT", 5000))
    application.run(host="172.17.0.2", port=port)
