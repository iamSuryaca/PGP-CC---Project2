from flask import Flask ,url_for, request,jsonify
import json
import requests
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World !"

@app.route("/process-invoice", methods = ['POST'])
def processInvoice():
    return " JSON Message: " + json.dumps(request.json)

@app.route("/sns-subscribe", methods=['GET','POST','PUT'])
def handle_requests():
    global messages
    request_content = json.loads(request.get_data())
    sys.stdout.write(str(request_content))

    if request.method == 'POST':
        sys.stdout.write("Message Recieved")
        request_content = json.loads(request.get_data())
        sys.stdout.write(str(request_content))

    return "OK"

if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port=80,
        debug=True
    )
