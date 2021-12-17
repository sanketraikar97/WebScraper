import pprint

import requests
from bs4 import BeautifulSoup

main_url = 'https://news.ycombinator.com/'
res = requests.get(main_url)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select(".titlelink")
subtext = soup.select(".subtext")


# print(links[0].contents[0])
# print(scores[0].contents[0])
# print(scores)

# Get the list of links sorted based on votes
def sort_by_points(data):
    return sorted(data,key = lambda k:k['votes'], reverse = True)

# Scrape the data from next page till last page
def get_next_page(nextsoup):
    for new in nextsoup.find_all('a', href = True):
        if 'news?p=' in new['href']:
            print("\033[1m"+new['href']+"\033[0m")
            nextpage = requests.get(main_url+new['href'])
            newsoup = BeautifulSoup(nextpage.text,'html.parser')
            next_link = newsoup.select('.titlelink')
            next_subtext = newsoup.select('.subtext')
            pprint.pprint(get_links(next_link,next_subtext))
            get_next_page(newsoup)
    return

# Get the data from the website
def get_links(links, subtext):
    data = []
    for idx, item in enumerate(links):
        link = links[idx].get('href', None)
        title = links[idx].getText()
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].contents[0].replace(' points',''))
            if points > 99:
                data.append({'title': title, 'link': link, 'votes':points})
    return sort_by_points(data)

# Print data from page 1
pprint.pprint(get_links(links,subtext))
# Call function to get data till last page
get_next_page(soup)

