from Search_Engines_Scraper.search_engines import Google
import time
import json
import numpy as np
import sys
filename = f'{time.strftime("%Y%m%d-%H%M%S")}'

file_path = sys.argv[1]

engine = Google()
with open('GH-Action/Lists/'+file_path) as f:
    websiteList = [line.strip() for line in f]
Links = {}
brokenWebsites = []
# for keyword corona

for website in websiteList:
    Links[website] = []
    try:
        results = engine.search("%22 corona %22 site:" + website + " &tbs=qdr:m", pages=2)
    except Exception as err:
        print(err) # add item to list of broken websites
        brokenWebsites.append(website)
        brokenWebsites.append("^ " + str(err))
    try:
        print(results.links())
        Links[website] = results.links()
    except Exception as err:
        print(err) # add item to list of broken websites
        brokenWebsites.append(website)
        brokenWebsites.append("^ " + str(err))
    time.sleep((30-5)*np.random.random()+5) #sleep from 5 to 30 seconds
    if(len(Links) % 10 == 0):
        engine = Google()



if len(Links) > 0:
    with open(rf'GH-Action/{file_path + "_" + filename+"_Links.json"}', "w") as fp:
        json.dump(Links, fp, indent = 4)

if len(brokenWebsites) > 0:
    with open(rf'{file_path + "_" + filename+"_BrokenLinks.json"}', "w") as f: 
        for website in brokenWebsites: 
            f.write("%s\n" % website)