import requests, json
from pprint import pprint

class QuranAPI:

    global url

    url = 'https://api.quran.com/api/v4/'

    def __init__(self) -> None:
        print('[utils.quran_api-staging]: erm.. what da flip? no API connection yet.')
        print('[utils.quran_api-staging]: ok we got a connection now to api/v4')
        print('[utils.quran_api-staging]: silly v2 | API call sent!')
        print('[utils.quran_api-staging]: happy mode :p | API call was Ok (status good)')
        print('[utils.quran_api-staging]: closing api portal, awaiting a invoke')
        self.url = url

    def GetChaptersInfo(id):
        success = None
        try:
           response = requests.get(f"{url}chapters/{id}/info")
           response1 = requests.get(f"{url}chapters/{id}")
           success = True
        except requests.HTTPError:
            print("error")
            success = False
        
        if success == True:
           data = response.text
           data1 = response1.text

           return json.loads(data), json.loads(data1), success
        
    def getChapterVerseLeagcy(page): # Muhammed Asad - Translation (Network Protocol External V2) - LEAGCY
        success = None
        try:
            response = requests.get(f'http://api.alquran.cloud/v1/page/{str(page)}/en.asad')
            success = True
        except requests.HTTPError:
            print("error")
            success = False

        if success == True:
            return json.loads(response.text), success
        
    def getChapterVerseByPage(page): # Quran.com API 
        success = None
        try:
            response = requests.get(f"https://api.quran.com/api/v4/verses/by_page/{page}?language=en&words=true&page=1&per_page=1")
            success = True
        except requests.HTTPError:
            print('error')
            success = False
        
        if success == True:
            return json.loads(response.text), success

QuranAPI()