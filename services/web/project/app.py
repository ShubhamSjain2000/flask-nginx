from flask import Flask, jsonify
from project.scripts.test_script import test_function

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify(hello="world")

@app.route("/testscript")
def testscript():
    result = test_function()
    return jsonify(script=result)