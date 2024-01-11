import requests
import json 
import datetime
from urllib.parse import quote

baseURL = 'https://api.sofascore.com/api/v1/sport/football/scheduled-events/'
currDate = datetime.datetime.now()
formattedDate = str(currDate).split()[0]

encodedDate = quote(formattedDate)
completeURL = baseURL + encodedDate

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

response = requests.get(completeURL, headers=headers)
print(response.status_code)
data = response.json()
events = data.get("events", [])
with open("lib/link_gen_helper.txt", "w") as output_file:
    for event in events:
        # Extract id, slug, and customId
        event_id = event.get("id", "")
        event_slug = event.get("slug", "")
        custom_id = event.get("customId", "")

        # Write id, slug, and customId to the output file
        output_file.write(str(event_id) +"," + str(event_slug)+"," + str(custom_id) +"\n")

print("Data has been written to link_gen_helper.txt")