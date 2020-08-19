import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os.path

titles = []
year = []

def title_list():
    for x in range(12,21):
        url = "http://asianwiki.com/Category:20"+ str(x) + "_South_Korean_Drama_Series"
        page = requests.get(url)
        soup = bs(page.content, 'lxml')
        tables = soup.find('table',{'class':'wikitable'})
        links = tables.findAll('a')

        for link in links:
            titles.append(link.get('title'))
            year.append("20"+str(x))

def main():
    title_list()
    d1 = {'title': titles, 'year': year}
    df = pd.DataFrame(d1)

    df.drop_duplicates(subset="title",keep="first",inplace=True)
    if os.path.isfile("~/Documents/dramaList.csv"):
        df.to_csv("newDramaList.csv")
    else:
        df.to_csv("dramaList.csv")
    print(len(titles))


if __name__ == "__main__":
    main()
