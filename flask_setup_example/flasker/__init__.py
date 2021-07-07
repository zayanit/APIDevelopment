from flask import Flask, jsonify

def create_app(test_config=None):
  # Create and configure the app
  app = Flask(__name__)

  # a simple page that says hello
  @app.route('/')
  def hello():
    return jsonify({'message': 'Hello world!'})

  @app.route('/smiley')
  def smiley():
    return ':)'

  return app