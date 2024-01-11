import requests
from bs4 import BeautifulSoup
import json

class NewsScraper:
    def __init__(self):
        self.news = {}  # Initialize an empty dictionary to store news data
        self.url = 'https://www.goal.com/en-in/news'  # URL of the webpage

    def scrape_news(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the script element containing the JSON data
            script_tag = soup.find('script', {'type': 'application/ld+json'})

            if script_tag:
                script_content = script_tag.string

                # Parse the JSON data from the script content
                data = json.loads(script_content)

                # Extract and store @id and headline in the dictionary
                for item in data['itemListElement']:
                    news_item = item['item']
                    news_id = news_item['@id']
                    headline = news_item['headline']
                    self.news[headline] = news_id

    def get_news(self):
        return self.news
