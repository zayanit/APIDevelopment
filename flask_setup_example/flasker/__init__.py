from flask import Flask, jsonify
from models import setup_db, Plant
from flask_cors import CORS

def create_app(test_config=None):
  # Create and configure the app
  app = Flask(__name__)
  setup_db(app)
  # CORS(app, resources={r"*/api/*" : {origins: '*'}})
  CORS(app)

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authoraization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

  # a simple page that says hello
  @app.route('/')
  # @cross_origin
  def hello():
    return jsonify({'message': 'Hello world!'})

  @app.route('/smiley')
  def smiley():
    return ':)'

  return app