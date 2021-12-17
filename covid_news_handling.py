"""Module to access a news API"""
import json
import logging
import requests

logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
def news_API_request(covid_terms='Covid COVID-19 coronavrius'):

    """Function to access a news API and filter through headlines
       with specific query parameters and store them in a list"""

    # Takes arguement and splits string into list of single words
    logging.info('Search parameters getting split into single words')
    filters = covid_terms.split()

    # Opening JSON config file
    logging.info('config file opening')
    file = open('config.json', encoding="utf8")
    news_key = json.load(file)
    file.close()
    logging.info('config file closed')

    # following query parameters are used, qInTitle and apiKey.
    # API key is stored in seperate config file
    search_metric = {
      "qInTitle":(filters),
      "apiKey": (news_key.get('api_key'))
    }
    base_url = "https://newsapi.org/v2/everything?"

    res = requests.get(base_url, params=search_metric)
    open_news = res.json()

    global ARTICLE
    ARTICLE = open_news["articles"]

    # empty list containing relevant news headlines and URL's
    product = []

    for i in ARTICLE:
        product.append(i["title"])
        product.append(i["url"])
    return product
    logging.info('Returned relevant URLs and headlines')


def update_news(time):

    """Function to return relevant news articles and URL's
       and update a list"""

    # Calling news_API_request function to get recent news stories
    news_API_request()
