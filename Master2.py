from unicodedata import name
import requests
import pandas as pd
import json
URL=""
response=requests.get("https://gbfs.urbansharing.com/oslobysykkel.no/gbfs.json").json()

url_list = []

data = response["data"]["nb"]["feeds"]
# print(json.dumps(data, indent=1))
for i in data:
    if "name" in i:
        url_list.append(i["url"])
url_dic={"URL": url_list}

url_dic2 = {}

for i in url_dic["URL"]:
    # url_dic2[str(i).split("/")[-1].replace(".json","")] = i
    str(i).split("/")[-1].replace(".json","") = i


def cb(input):
    requests.get(input).json()

#cb(system_information)
