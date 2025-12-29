from bs4 import BeautifulSoup
import requests
import csv

url = 'https://quotes.toscrape.com/'

def scrapeQuotes(url):
    while url is not None:
        pageToScrape = requests.get(url)
        soup = BeautifulSoup(pageToScrape.text, "html.parser")
        authors = soup.findAll('small', attrs= {'class':'author'})
        quotes = soup.findAll('span', attrs= {'class':'text'})
            
            

        with open("quotes.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Author", "Quote"])  

            for author, quote in zip(authors, quotes):
                writer.writerow([author.text, quote.text])

        nextButton = soup.find("li", attrs= {'class':'next'})
        if nextButton:
            nextPage = nextButton.find("a")["href"]
            url = "https://quotes.toscrape.com" + nextPage
        else:
            url = None




scrapeQuotes(url)


