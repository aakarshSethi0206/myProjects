from bs4 import BeautifulSoup
import requests
import csv

def scrapeQuotes():
    pageToScrape = requests.get("https://quotes.toscrape.com/")
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    authors = soup.findAll('small', attrs= {'class':'author'})
    quotes = soup.findAll('span', attrs= {'class':'text'})
    
    with open("quotes.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Author", "Quote"])  

        for author, quote in zip(authors, quotes):
            writer.writerow([author.text, quote.text])

scrapeQuotes()