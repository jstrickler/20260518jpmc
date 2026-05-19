from datetime import datetime
import time
import requests

URL = 'http://httpbin.org/post'
CONNECTION_TIMEOUT = 10

response = requests.post(  # POST data to server
    URL,
    data={'date': datetime.now(),
        'label': 'testing POST',
    },
    # json="json doc string",
    cookies={'python': 'testing'},
    headers={'X-Python': 'Guido van Rossum'},
    timeout=(CONNECTION_TIMEOUT), 
)
if response.status_code in (requests.codes.OK, requests.codes.created):
    if 'json' in response.headers['content-type'].lower()
        print(response.status_code)
        print(response.text)
    else:
        print("did not get JSON back")
