import requests
import json 
baseURL = 'https://api.sofascore.com/api/v1/event/{}/lineups'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.sofascore.com/',
    'Origin': 'https://www.sofascore.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'If-None-Match': 'W/cf252765ae',
}


#slug = 'liverpool-brighton-and-hove-albion'
with open("lib/link_gen_helper.txt", "r") as inp:
    for line in inp.readlines():
        line = line.strip().split(",")  # Remove leading/trailing whitespace
        id = line[0]
        link = baseURL.replace("{}",id)
        matchData = requests.get(link,headers=headers)
        data  = matchData.json()
        with open("lib/{}.txt".format(line[1]),"w") as file:
            json.dump(data,file,indent = 4)
    print("successfully written the data")
