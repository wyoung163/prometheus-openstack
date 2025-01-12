from http import HTTPStatus
from flask import Flask, jsonify, redirect, render_template, request, url_for

import requests
import json
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route("/alerts", methods=['POST'])
def post():
    params = request.get_json()
    subject = params["alerts"][0]["labels"]["alertname"]
    body = params["alerts"][0]["labels"]

    url = "https://devstack.zendesk.com/api/v2/tickets"

    #payload = json.loads("""{
    payload = {
      "ticket": {
        "comment": {
          "body": "{}".format(body)
        },
        "priority": "High",
        "subject": "{}".format(subject)
      }
    }

    #}""".format(body, subject))
    headers = {
    	"Content-Type": "application/json",
    }
    email_address = 'chaerikim@devstack.co.kr'
    api_token = 'aUB3kjFKF0nPzsXZjFSviwGKzkO9Leq59f7B4q2F'
    # Use basic authentication
    auth = HTTPBasicAuth(f'{email_address}/token', api_token)
    
    response = requests.request(
    	"POST",
    	url,
    	auth=auth,
    	headers=headers,
    	json=payload
    )
    
    print(response.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5055, debug=True)
