import json
# import requests
# from bs4 import BeautifulSoup

# URL = "https://scores.hssailing.org/f22/central-great-lakes-acc-qualifier/full-scores/"
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")

# print(soup.find_all("div",class_="divA"))

files={"names":"[BonesBollegeBep, Latin]"}

json_object=json.dumps(files, indent=4)

with open("./data/files.json",'w') as outfile:
    outfile.write(json_object)

BonesBollegeBep={
    "rank":"1",
    "name":"Bones Bollege BeP",
    "imgpath":"./images/jones.png",
    "ascores":"[12,OCS,15,6,2,3,34]",
    "bscores":"[124,324,145,3,5,7,54,3,2,34]",
    "totscore":"534",
    "atot":"575",
    "btot":"67"
    }
json_object=json.dumps(BonesBollegeBep, indent=4)

with open("./data/BonesBollegeBep.json",'w') as outfile:
    outfile.write(json_object)

Latin={
    "rank":"2",
    "name":"Latin",
    "imgpath":"./images/latin.png",
    "ascores":"[12,RDG,15,6,2,3,34]",
    "bscores":"[124,7,54,3,2,34]",
    "totscore":"23",
    "atot":"7",
    "btot":"6"
    }
json_object=json.dumps(Latin, indent=4)

with open("./data/Latin.json",'w') as outfile:
    outfile.write(json_object)