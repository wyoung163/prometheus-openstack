import requests
import json
from requests.auth import HTTPBasicAuth

url = "https://devstack.zendesk.com/api/v2/tickets"

payload = json.loads("""{
  "ticket": {
    "comment": {
      "body": "{}"
    },
    "priority": "{}",
    "subject": "{}"
  }
}""")
headers = {
	"Content-Type": "application/json",
}
email_address = 'your_email_address'
api_token = 'your_api_token'
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

