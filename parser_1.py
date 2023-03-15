import json

testdict={
    "rank":"5",
    "name":"schoolschool",
    "imgpath":"./images/jones.png",
    "ascores":"['12','34','15']",
    "bscores":"['124','324','145']",
    "totscore":"534",
    "atot":"56",
    "btot":"67"
    }
json_object=json.dumps(testdict, indent=4)

with open("./data/testdict.json",'w') as outfile:
    outfile.write(json_object)