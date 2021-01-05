import os
import pickle
import requests
from googlescript import Create_Service
dir_path = os.path.join(os.getcwd())

API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = dir_path + "\\" + "credentials.json"
print(CLIENT_SECRET_FILE)
SCOPES = ['https://www.googleapis.com/auth/photoslibrary',
          'https://www.googleapis.com/auth/photoslibrary.sharing']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

upload_url = 'https://photoslibrary.googleapis.com/v1/albums'
token = pickle.load(open('token_photoslibrary_v1.pickle', 'rb'))


headers = {
    'Authorization': 'Bearer ' + token.token,
    'Content-type': 'application/json',
}

request_body = {
  "album": {
    "title": "auto2"
  }
}
results = service.albums().create(body=request_body).execute()
print(results['id'])