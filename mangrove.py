import json
import os
import requests

PLANET_API_KEY = ''

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
    
    def fetch_stats_data_by_date(self, filter, date):

        try:
            item_types = ["PSScene3Band", "REOrthoTile"]
            date_filter = {"type": "DateRangeFilter", "field_name": "acquired", "config": {"{filter}".format(filter=filter): "{date}".format(date=date)}}
            request = {"item_types" : item_types, "interval" : "year", "filter" : date_filter}
            res, status_code = self.send_planet_request(request_type="/stats", method="post", request=request)
        except Exception as ex:
            print(ex)
            print("Request failed")

        return res, status_code
    
    def fetch_analytic_sr_data(self, file_name, greater_than_date, less_than_date):
        # cloud cover percentage: 0-2% cloud cover; 
        # 1 unique tile ID per month
        # 2016
        # testing
        #os.system("touch test.txt")
        path = "/Users/sgadepalli/Google\ Drive\ \(mangroveplanet\@gmail.com\)/"
        # os.system("mv test.txt {path}".format(path=path))
        command = "planet -k {API_KEY} data download --item-type 'PSScene4Band' --asset-type 'analytic_sr' --date acquired gt '{greater_than_date}' --date acquired lt '{less_than_date}' --range cloud_cover lt '0.2' --geom '{file_name}' --dest '{PATH}'".format(API_KEY=PLANET_API_KEY, greater_than_date=greater_than_date, less_than_date=less_than_date, file_name=file_name, PATH=path)
        os.system(command)

if __name__ == "__main__":
    mangrove = MangrovePlanet()
    mangrove.fetch_analytic_sr_data(greater_than_date="2020-10-01", less_than_date="2020-10-15", file_name="test_geometry.geojson")
    
