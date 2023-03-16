import json
import requests
from bs4 import BeautifulSoup

URL = "https://scores.hssailing.org/f22/central-great-lakes-acc-qualifier/full-scores/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

divaS = soup.find_all("tr",class_="divA")
names=[]
for a in divaS:
    names.append(a.find("a").text)
ascores=[]
for i,tr in enumerate(divaS):
    td = tr.find_all("td", class_="right")
    ascores.append([])
    for j in td:
        ascores[i].append(j.text)



bscores=[]
divbS = soup.find_all("tr",class_="divB")
for i,tr in enumerate(divbS):
    td = tr.find_all("td", class_="right")
    bscores.append([])
    for j in td:
        bscores[i].append(j.text)


atot=[ascores[i][-1] for i in range(len(ascores))]
btot=[bscores[i][-1] for i in range(len(bscores))]
ascores=ascores[:len(ascores)-1]
bscores=bscores[:len(bscores)-1]

ascores = str(ascores).replace("'","")
bscores = str(bscores).replace("'","")

print(ascores)
print(bscores)
print(atot)
print(btot)

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