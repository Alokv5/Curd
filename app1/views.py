from django.shortcuts import render
from Covid_API.settings import COVID_19_FILE
import json


def showIndex(request):
    dict_data=json.loads(open(COVID_19_FILE).read())
    state_code=[x for x in dict_data]
    return render(request, "index.html",{"state_code":state_code})


def open_district(request):
    state_codes=request.GET.get("state_codes")
    dict_data = json.loads(open(COVID_19_FILE).read())
    for x in dict_data[state_codes]:

     return render(request,"district.html",{"state_codes":state_codes,"data":dict_data[state_codes]})