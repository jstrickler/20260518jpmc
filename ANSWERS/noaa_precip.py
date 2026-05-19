from pprint import pprint
import requests
BASE_URL = 'https://www.ncei.noaa.gov/cdo-web/api/v2/datasets'
TOKEN = 'RZvAuJvzafAimtwbJFmORyXQbOpEoVId'

session = requests.Session()
session.headers.update(
    {
        'token': TOKEN, 
        'UserAgent': "cja-tech.com,jstrickler@gmail.com", 
        'Accept': "application/GeoJSON"
    }
)
response = session.get(
    BASE_URL,
    params={
        'datasetid': 'GSOM',
    },
    timeout=10,

)
if response.ok:
    pprint(response.json())
else:
    print(response.text)
    print(response.status_code)