from django.test import TestCase

# Create your tests here.
from VergeScraper_module import *
import bs4
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
import lxml
import re
import string
from csv import writer

url = "https://www.theverge.com/"

page = urlopen(url)
verge_html = page.read()
soup = bs4.BeautifulSoup(verge_html, "lxml")
print(soup)

mymodule = web_scraper("verge.com")
print(mymodule)

article_list = mymodule.create_verge_articles()
print(article_list)

author_list = mymodule.create_author_names()
print(author_list)

url_list = mymodule.create_url_links()
print(url_list)

id_list = mymodule.create_verge_ids(url_list)
print(id_list)

date_list = mymodule.create_article_dates(url_list)
print(date_list)

scraper_to_csv(id_list, url_list, article_list, author_list, date_list)
