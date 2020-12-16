import requests
import json
class Covid19Middleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("im constructor")
        response= requests.get("https://api.covid19india.org/v4/data.json")
        print(response.status_code)
        dict_data=json.loads(response.text)
        json.dump(dict_data,open("app1/raw/covid19.json" ,"w"))

        print("data written into file")




    def __call__(self,request, *args,**kwargs):
        response=self.get_response(request)
        print("i m call")
        return response

