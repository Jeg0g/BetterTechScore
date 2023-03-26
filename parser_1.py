import json
import requests
import glob
import os
from bs4 import BeautifulSoup

def parseURL(URL):
    page = requests.get(URL+"full-scores/")

    soup = BeautifulSoup(page.content, "html.parser")

    images = soup.select('.burgee-cell')
    imageurls=[]
    for img in images:
        imgg=img.find('img')
        if imgg is not None:
            imageurls.append("https://scores.hssailing.org"+imgg['src'])
        else:
            imageurls.append('staticFiles/noimg.png')

    divaS = soup.find_all("tr",class_="divA")
    names=[]
    links=[]
    for a in divaS:
        aa=a.find("a")
        names.append(aa.text)
        links.append(aa['href'])

    ascores=[]
    for i,tr in enumerate(divaS):
        td = tr.find_all("td", class_="right")
        ascores.append([])
        for j in td:
            ascores[i].append(j.text)               
    mascots=[]
    bscores=[]
    divbS = soup.find_all("tr",class_="divB")
    for i,tr in enumerate(divbS):
        mascotTD=tr.find_all("td")
        mascots.append(mascotTD[2].text)
        td = tr.find_all("td", class_="right")
        bscores.append([])
        for j in td:
            bscores[i].append(j.text)

    for i,l in enumerate(links):
        links[i]=l+mascots[i]

    namemasts=[]
    for n,m in zip(names,mascots):
        namemasts.append(n+m)

    atot=[ascores[i][-1] for i in range(len(ascores))]
    btot=[bscores[i][-1] for i in range(len(bscores))]
    for i,scores in enumerate(ascores):
        ascores[i]=str(scores[:len(scores)-1]).replace("'","").replace(" ","")
    for i,scores in enumerate(bscores):
        bscores[i]=str(scores[:len(scores)-1]).replace("'","").replace(" ","")
    namesstr=str(namemasts).replace("'","").replace('"',"").replace(" ","")
    
    sailorsPage=requests.get(URL+"sailors/")
    soup2 = BeautifulSoup(sailorsPage.content, "html.parser")

    schoolnames=soup2.find_all("td",class_="schoolname")
    newnames=[]
    newlinks=[]
    for i in schoolnames:
        newnames.append(i.text)
        newlinks.append(i.find('a')['href'])
    teamnames=soup2.find_all("td",class_="teamname")
    newteams=[]
    for i in teamnames:
        newteams.append(i.text)

    for i,l in enumerate(newlinks):
        newlinks[i]=l+newteams[i]

    # newnamemasts=[]
    # for n,m in zip(newnames,newteams):
    #     newnamemasts.append((n+m).replace("'","").replace('"',"").replace(" ",""))
    rankcells=soup2.find_all("td",class_="rank-cell")

    files={"names":namesstr}
    json_object=json.dumps(files, indent=4)

    dir = 'staticFiles/data'
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)
    with open("staticFiles/data/files.json",'w') as outfile:
        outfile.write(json_object)

    
    # alphalinks=links.copy()
    # links.sort()
    # corresIndex=[]
    # for n in newlinks:
    #     corresIndex.append(alphalinks.index(n))

    # #FUCKING SHEBOYGAN

    for i,name in enumerate(names):
        d={
            "rank":f"{i+1}",
            "name":f"{name}",
            "imgpath":imageurls[i],
            "ascores":ascores[i],
            "bscores":bscores[i],
            "totscore":f"{int(atot[i])+int(btot[i])}",
            "atot":f"{atot[i]}",
            "btot":f"{btot[i]}",
            "arank":rankcells[2*newlinks.index(links[i])].text,
            "brank":rankcells[2*newlinks.index(links[i])+1].text,
            "mascot":mascots[i]
            }
        json_object=json.dumps(d, indent=4)
        namestr=namemasts[i].replace("'","").replace('"',"").replace(" ","")
        with open(f'staticFiles/data/{namestr}.json','w') as outfile:
            outfile.write(json_object)

    
parseURL("https://scores.hssailing.org/s23/missa-ice-breaker-chicago-yacht-club/")