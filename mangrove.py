import json
import requests

PLANET_API_KEY = '75c03d018975419abdf76b779154d5ae'

class MangrovePlanet():
    def __init__(self):
        self.planet_api_key = PLANET_API_KEY
        self.url = 'https://api.planet.com/data/v1'
    
    def auth_obj(self):
        
        try:
            session = requests.session()
            session.auth = (PLANET_API_KEY, "")
            res = session.get(self.url)
            status_code = res.status_code
        except Exception as ex:
            print(ex)
            print("Authorization Failed")
        return res, status_code
    
    def fetch_data(self):
        res, status_code = self.auth_obj()
        return res, status_code

if __name__ == "__main__":
    mangrove = MangrovePlanet()
    res, status_code = mangrove.fetch_data()
