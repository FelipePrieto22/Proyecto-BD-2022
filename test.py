from bs4 import BeautifulSoup
import urllib.request
# specify the url
urlpage =  'https://en.wikipedia.org/wiki/Star_Trek'
# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
# find results within table
table = soup.find('table', attrs={'class': 'infobox vevent'})
results = table.find_all('tr')
print(type(results))
print('Number of results', len(results))
print(results)