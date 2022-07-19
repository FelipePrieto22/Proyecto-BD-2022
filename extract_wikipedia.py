import json
from bs4 import BeautifulSoup
import requests

url = "https://es.wikipedia.org/wiki/Michelle_Bachelet"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
tbl = soup.find("table", {"class": "infobox biography vcard"})
# print("tbl: ", tbl)
list_of_table_rows = tbl.findAll('tr')
print("List:",list_of_table_rows)
info = {}
for tr in list_of_table_rows:
        list_of_info = tr.findAll('th').strings
        for th in list_of_info:
            # print(th)
            if isinstance(th, str):
                innerText += th.strip()
            elif th.name == 'br':
                innerText += '\n'
            info[th.text] = innerText
            
        """  td = tr.find("td")
        if th is not None:
            innerText = ''
            for elem in td.recursiveChildGenerator():
                if isinstance(elem, str):
                    innerText += elem.strip()
                elif elem.name == 'br':
                    innerText += '\n'
            info[th.text] = innerText """
