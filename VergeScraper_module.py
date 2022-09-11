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

class web_scraper:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"Contains methods to scrape id, url, article, author and date from {self.name}"

    def create_verge_articles(self):

        article = soup.find_all("a", attrs={"data-analytics-link": "article"})
        verge_articles = [headline.getText() for headline in article]
        return verge_articles

    def create_author_names(self):
        author_name = soup.find_all('a', attrs={"data-analytics-link": "author-name"})
        verge_authors = [name.getText() for name in author_name]
        return verge_authors

    def create_url_links(self):
        id_links = soup.find_all("a", attrs={"data-analytics-link":"article"})
        https_links = [tag["href"] for tag in id_links]
        return https_links

    def create_verge_ids(self, https_links):
        verge_ids = [link.split('/')[-2] for link in https_links]
        return verge_ids

    def create_article_dates(self, https_links):
        article_dates = []
        for link in https_links:
            str_part1 = "/".join(link.split('/')[:3])
            str_part2 = "/".join(link.split('/')[6:8])
            strnew1 = re.sub(str_part1, "", link)
            strnew01 = strnew1.split('/')
            if strnew01[1].isnumeric() == False and strnew01[-3] != '':
                strnew01.pop(1)
                strnew = '/'.join(strnew01)
                str_part2 = "/".join(link.split('/')[7:9])
                strnew2 = (re.sub('/'+str_part2, "", strnew)).lstrip('/')
            elif strnew01[-3] == '':
                strnew2 = '0'
            else:
                strnew2 = (re.sub('/'+str_part2, "", strnew1)).lstrip('/')
    
            article_dates.append(strnew2)
        return article_dates

def scraper_to_csv(verge_ids, https_links, verge_articles, verge_authors, article_dates):
    with open("Verge.csv", "w", encoding="utf-8", newline="") as f:
        thewriter = writer(f)
        header = ["verge_ids", "https_links", "verge_articles", "verge_authors", "article_dates"]
        thewriter.writerow(header)
        for item in zip(verge_ids, https_links, verge_articles, verge_authors, article_dates):
            thewriter.writerow(item)
