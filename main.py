from bs4 import BeautifulSoup
import urllib.request
import re
import requests
import pandas as pd

data = {
    'ilosc_przejazdow' : [],
    'data_przejazdu': []
}
df = pd.DataFrame(columns=['ilosc_przejazdow', 'data_przejazdu'])

html_page = requests.get("https://www.wroclaw.pl/open-data/dataset/wrmprzejazdy_data/resource_history/c737af89-bcf7-4f7d-8bbc-4a0946d7006e").text
soup = BeautifulSoup(html_page, 'html.parser')
list = soup.find_all(class_='heading')
list = list[1:]
name = list[0].contents
name = str(name)
name = name.split("_")[2]
list.reverse()
# list = list[:5] #test na malej ilosc elem
# quantity = []
for elem in list:

    name = elem.contents
    elem = str(elem)

    name = str(name)
    name = name.split("_")[2]

    link = elem.split(" ")
    link = link[2]
    link = link[5:]
    link = link[1:]
    link = link[:-1]
    # link = link.replace("\""," ")
    print(link)
    c=pd.read_csv(link)
    quantity = c.__len__()
    # df["ilosc_przejazdow"]=c.__len__()
    df = df.append({'ilosc_przejazdow':quantity,'data_przejazdu':name},ignore_index=True)
    # df = df.append({'data_przejazdu':name},ignore_index=True)

# df["ilosc_przejazdow"]=quantity
print(df)
# items = list.find_all('a')
# print(soup.prettify())
# for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
#     print(link.get('href'))
