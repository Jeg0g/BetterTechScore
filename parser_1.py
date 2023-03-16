import json
import requests
from bs4 import BeautifulSoup

URL = "https://scores.hssailing.org/f22/kick-off-classic/full-scores/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

images = soup.select('.burgee-cell img') 
imageurls=[]
for img in images:
    imageurls.append("https://scores.hssailing.org"+img['src'])

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
for i,scores in enumerate(ascores):
    ascores[i]=str(scores[:len(scores)-1]).replace("'","").replace(" ","")
for i,scores in enumerate(bscores):
    bscores[i]=str(scores[:len(scores)-1]).replace("'","").replace(" ","")
namesstr=str(names).replace("'","").replace('"',"").replace(" ","")
files={"names":namesstr}
json_object=json.dumps(files, indent=4)

with open("./data/files.json",'w') as outfile:
    outfile.write(json_object)

for i,name in enumerate(names):
    d={
        "rank":f"{i+1}",
        "name":f"{name}",
        "imgpath":imageurls[i],
        "ascores":ascores[i],
        "bscores":bscores[i],
        "totscore":f"{int(atot[i])+int(btot[i])}",
        "atot":f"{atot[i]}",
        "btot":f"{btot[i]}"
        }
    json_object=json.dumps(d, indent=4)
    namestr=name.replace("'","").replace('"',"").replace(" ","")
    with open(f'./data/{namestr}.json','w') as outfile:
        outfile.write(json_object)
