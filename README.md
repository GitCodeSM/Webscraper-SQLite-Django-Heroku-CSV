# Webscraper-SQLite-Django-Heroku-CSV

Assignment Goal: Learned BeautifulSoup bs4, webscraping, html, csv, csv to SQLite database, build and push django project on cloud (chose heroku).

main branch: - A django project with one app,  to create a web scraper to read articles off theverge.com using Python.
             - The script will perform the following:
             - Read the headline, get the link of the article, the author, and the date of each of the articles found on "theverge.com".
             - Store above data in a CSV file titled `ddmmyyy_verge.csv`, with the following header `id, URL, headline, author, date`.
             - Create an SQLite database using sqlite command: sqlite> ddmmyyy_verge.csv newfilename to store the above data with id as the primary key.
             - Run this script on a cloud service (Used Heroku and Gunicorn).
             - add testcases.

To do list: - Save the articles (and de-duplicate them) daily on the server in a SQL Database.

project name: scraperproject
appname: scraperapp
scraper module: VergeScraper_module.py
testcases: test.py in app
