# WebScraper
This is a project based on Accessing Web Data using Python. This project is aimed at learning mere basics of web scraping using Beautiful Soup library in Python. This project aims at scraping the Hacker News website to get a list of links to the articles having a certain number of likes or points.

This code uses following Python libraries
1. Re - This library is used to handle pattern matching through regular expression
2. Requests - This module allows to communicate with HTTP server using Python
3. BeautifulSoup - This package is used to parse HTML and XML documents using Python
4. Pprint - This package allows to apply pretty printer on Data structures

Functions in the project:
1. sort_by_points() :- Returns the sorted list of links based on the number of points / votes.
2. get_links() :- Get the list of links in a particular page of Hacker News website whose number of votes is greater than 100
3. get_next_page() :- Scrape the data from all pages of Hacker News website till the last page
