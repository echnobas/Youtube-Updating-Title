import requests, time
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

KEY = "API_KEY_HERE"
SECRET = 'secret.json'
scopes = ["https://www.googleapis.com/auth/youtube"]

flow = InstalledAppFlow.from_client_secrets_file(SECRET, scopes)
creds = flow.run_console()
youtube = build('youtube', 'v3', credentials=creds)

def getViewCount(id, API_KEY):
    r = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={id}&key={API_KEY}')
    res = r.json()['items'][0]['statistics']['viewCount']
    print(r.json())
    return res

def updateViewCount(v):
    data = {
          'id': '2ZKmKoC_fgk',
          'snippet': {
            'title': f'This video has {v} views',
            'categoryId': '22',
          }
        }
    req = youtube.videos().update(part="snippet", body=data)
    res = req.execute()
    print(res)
    
while True:
    views = getViewCount("2ZKmKoC_fgk", KEY)
    print(views)
    updateViewCount(views)
    time.sleep(30)
