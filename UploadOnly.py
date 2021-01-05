from bs4 import BeautifulSoup
from PIL import Image, ImageDraw
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
TacIm = Image.open('TAC.jpg')
Red = Image.new('RGBA', (30,30), (255,0,0))
Blue = Image.new('RGBA', (30,30), (0,0,255))
Green = Image.new('RGBA', (30,30), (0,255,0))
Pink = Image.new('RGBA', (30,30), (255,8,127))
mask = Image.new("L", (30,30), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, 30, 30), fill=255)
Coor = {'KVUO': (648,375), 'KPDX': (710,427), 'KSPB':(420,130), 'KHIO':(323,500), 'KTTD':(920,490)}
KVUO = (645,375)
i = ["KVUO", "KPDX", "KSPB", "KHIO", "KTTD"]
check = "m"
for i in i:
    airport = i
    url = "https://flightaware.com/resources/airport/%s/weather" % airport
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    curweather = list(soup.find(class_="smallrow1 hint").get_text())
    condense = ''.join(curweather)
    flightrules = condense[16:19].rstrip()
    mvfr = condense[16:20].rstrip()
    if check in condense:
        if mvfr == 'MVFR':
            TacIm.paste(Blue,Coor[i], mask=mask)
        elif mvfr == 'LIFR':
            TacIm.paste(Pink, Coor[i], mask=mask)
        elif flightrules == 'IFR':
            TacIm.paste(Red, Coor[i], mask=mask)
        elif flightrules == 'VFR':
            TacIm.paste(Green, Coor[i], mask=mask)
        print(i,'is',mvfr)
        TacIm.save('TACUpdate.jpg')
    else:
        if flightrules == 'VFR':
            TacIm.paste(Green, Coor[i], mask=mask)
        elif flightrules == 'IFR':
            TacIm.paste(Red, Coor[i], mask=mask)
        print(i,"is",flightrules)
        print(Coor[i])
        TacIm.save('TACUpdate.jpg')
print(CLIENT_SECRET_FILE)
dir_path = os.path.join(os.getcwd())
image_dir = os.chdir(os.path.dirname(os.path.abspath(__file__)))

upload_url = 'https://photoslibrary.googleapis.com/v1/uploads'
token = pickle.load(open('token_photoslibrary_v1.pickle', 'rb'))

headers = {
    'Authorization': 'Bearer ' + token.token,
    'Content-type': 'application/octet-stream',
    'X-Goog-Upload-Protocol': 'raw',
    'X-Goog-Upload-File-Name': "TACupdate.jpg"


}

filename = 'TACupdate.jpg'
albumid = 'AIJeZ-HdakZiXwq2i2jVhw8LR4nOwHXBgPsBqYXZBt6qE61ELSGUprUkO1BVg4RJdMnzuxMotFJT'
image_file = dir_path + "\\" + 'TACupdate.jpg'

img = open(image_file, 'rb').read()
response = requests.post(upload_url, data=img, headers=headers)

request_body = {
    'albumId': albumid,
    'newMediaItems':
        [
            {
                'description': filename,
                'simpleMediaItem':
                    {
                        'uploadToken': response.content.decode('utf-8')
                    }
            }
        ]
  }
upload_response = service.mediaItems().batchCreate(body=request_body).execute()
TacIm = Image.open('Seattle.png')
Coor = {'KSEA': (1000,5), 'KTIW': (710,277), 'KOLM':(355,750), 'KPLU':(1030,535), 'KSHN':(87,335)}
i = ["KSEA", "KTIW", "KOLM", "KPLU", "KSHN"]
check = "m"
for i in i:
    airport = i
    url = "https://flightaware.com/resources/airport/%s/weather" % airport
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    curweather = list(soup.find(class_="smallrow1 hint").get_text())
    condense = ''.join(curweather)
    flightrules = condense[16:19].rstrip()
    mvfr = condense[16:20].rstrip()
    if check in condense:
        if mvfr == 'MVFR':
            TacIm.paste(Blue,Coor[i], mask=mask)
        elif mvfr == 'LIFR':
            TacIm.paste(Pink, Coor[i], mask=mask)
        elif flightrules == 'IFR':
            TacIm.paste(Red, Coor[i], mask=mask)
        elif flightrules == 'VFR':
            TacIm.paste(Green, Coor[i], mask=mask)
        print(i,'is',mvfr)
        TacIm.save('seattleUpdate.png')
    else:
        if flightrules == 'VFR':
            TacIm.paste(Green, Coor[i], mask=mask)
        elif flightrules == 'IFR':
            TacIm.paste(Red, Coor[i], mask=mask)
        print(i,"is",flightrules)
        print(Coor[i])
        TacIm.save('seattleUpdate.png')

dir_path = os.path.join(os.getcwd())

API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = dir_path + "\\" + "credentials.json"
print(CLIENT_SECRET_FILE)
SCOPES = ['https://www.googleapis.com/auth/photoslibrary',
          'https://www.googleapis.com/auth/photoslibrary.sharing']

upload_url = 'https://photoslibrary.googleapis.com/v1/uploads'
token = pickle.load(open('token_photoslibrary_v1.pickle', 'rb'))

headers = {
    'Authorization': 'Bearer ' + token.token,
    'Content-type': 'application/octet-stream',
    'X-Goog-Upload-Protocol': 'raw',
    'X-Goog-Upload-File-Name': "seattleupdate.png"


}

filename = 'seattleupdate.png'
albumid = 'AIJeZ-HdakZiXwq2i2jVhw8LR4nOwHXBgPsBqYXZBt6qE61ELSGUprUkO1BVg4RJdMnzuxMotFJT'
image_file = image_file = dir_path + "\\" + 'Seattleupdate.png'

img = open(image_file, 'rb').read()
response = requests.post(upload_url, data=img, headers=headers)

request_body = {
    'albumId': albumid,
    'newMediaItems':
        [
            {
                'description': filename,
                'simpleMediaItem':
                    {
                        'uploadToken': response.content.decode('utf-8')
                    }
            }
        ]
  }
upload_response = service.mediaItems().batchCreate(body=request_body).execute()
TacIm = Image.open('North.png')
Coor = {'KCLS': (1100,2), 'KKLS': (1200,820), 'KAST':(100,780)}
i = ["KCLS", "KKLS", "KAST"]
check = "m"
for i in i:
    airport = i
    url = "https://flightaware.com/resources/airport/%s/weather" % airport
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    curweather = list(soup.find(class_="smallrow1 hint").get_text())
    condense = ''.join(curweather)
    flightrules = condense[16:19].rstrip()
    mvfr = condense[16:20].rstrip()
    if check in condense:
        if mvfr == 'MVFR':
            TacIm.paste(Blue,Coor[i], mask=mask)
        elif mvfr == 'LIFR':
            TacIm.paste(Pink, Coor[i], mask=mask)
        elif flightrules == 'IFR':
            TacIm.paste(Red, Coor[i], mask=mask)
        elif flightrules == 'VFR':
            TacIm.paste(Green, Coor[i], mask=mask)
        print(i,'is',mvfr)
        TacIm.save('northUpdate.png')
    else:
        if flightrules == 'VFR':
            TacIm.paste(Green, Coor[i], mask=mask)
        elif flightrules == 'IFR':
            TacIm.paste(Red, Coor[i], mask=mask)
        print(i,"is",flightrules)
        print(Coor[i])
        TacIm.save('northUpdate.png')


dir_path = os.path.join(os.getcwd())


CLIENT_SECRET_FILE = dir_path + "\\" + "credentials.json"
print(CLIENT_SECRET_FILE)

upload_url = 'https://photoslibrary.googleapis.com/v1/uploads'
token = pickle.load(open('token_photoslibrary_v1.pickle', 'rb'))

headers = {
    'Authorization': 'Bearer ' + token.token,
    'Content-type': 'application/octet-stream',
    'X-Goog-Upload-Protocol': 'raw',
    'X-Goog-Upload-File-Name': "northupdate.png"


}

filename = 'northupdate.png'
albumid = 'AIJeZ-HdakZiXwq2i2jVhw8LR4nOwHXBgPsBqYXZBt6qE61ELSGUprUkO1BVg4RJdMnzuxMotFJT'
image_file = dir_path + "\\" + 'northupdate.png'

img = open(image_file, 'rb').read()
response = requests.post(upload_url, data=img, headers=headers)

request_body = {
    'albumId': albumid,
    'newMediaItems':
        [
            {
                'description': filename,
                'simpleMediaItem':
                    {
                        'uploadToken': response.content.decode('utf-8')
                    }
            }
        ]
  }
upload_response = service.mediaItems().batchCreate(body=request_body).execute()