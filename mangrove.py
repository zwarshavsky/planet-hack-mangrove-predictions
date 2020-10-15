import json
import requests

PLANET_API_KEY = '75c03d018975419abdf76b779154d5ae'

class MangrovePlanet():
    def __init__(self):
        self.planet_api_key = PLANET_API_KEY
        self.url = 'https://api.planet.com/data/v1'
    
    def send_planet_request(self, request_type, method, request=None):
        
        try:
            session = requests.session()
            session.auth = (PLANET_API_KEY, "")
            url = self.url + str(request_type)
            if request is None and method == "get":
                res = session.get(url)
                status_code = res.status_code
            elif request is not None and method == "post":
                res = session.post(url, json=request)
                status_code = res.status_code
        except Exception as ex:
            print(ex)
            print("Authorization Failed")
        return res, status_code
    
    def fetch_stats_data(self):

        try:
            item_types = ["PSScene3Band", "REOrthoTile"]
            date_filter = {"type": "DateRangeFilter", "field_name": "acquired", "config": {"gte": "2013-01-01T00:00:00.000Z"}}
            request = {"item_types" : item_types, "interval" : "year", "filter" : date_filter}
            res, status_code = self.send_planet_request(request_type="/stats", method="post", request=request)
        except Exception as ex:
            print(ex)
            print("Request failed")

        return res, status_code

if __name__ == "__main__":
    mangrove = MangrovePlanet()
    res, status_code = mangrove.fetch_data()
