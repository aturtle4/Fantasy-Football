import requests
from bs4 import BeautifulSoup
import json

class marketValue:
    def getMarketValue(x):
        url = "https://www.footballtransfers.com/en/search?search_value="
        urlLink = url + (x.replace(" ","-"))
        request = requests.get(urlLink)
        soup = BeautifulSoup(request.text, "html.parser")
        print(request.text)
        with open("out.txt",'w') as file:
            json.dump(request.json,file,indent=4)
        price_element = soup.find("span", {"class": "player-price"})
        xTV_element = soup.find("span", {"class": "player-tag"})

        if price_element is not None:
            price = price_element.text
        else:
            price = "Price not found"

        if xTV_element is not None:
            xTV = xTV_element.text
        else:
            xTV = "xTV not found"

        print(f"Player Price: {price}")
        print(f"Player xTV: {xTV}")


if __name__ == '__main__':
    marketValue.getMarketValue("Jude Bellingham")
