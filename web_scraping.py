'''web scraping is the another way to collect the data using the requests and bs4'''
import requests
url="https://www.scrapethissite.com/pages/simple/"
res=requests.get(url)
res

res.status_code#200 will be the answer
res.text
res.contect
''' saving the data that we scraped form the given link into the HTML file'''
"step1-- first we will create the a folder withw a sutable name for example if our folder name is scaped"
"""now we are ready to done the other work"""
with open ('scraped/mango.html','w',encoding="utf-8") as f:
    f.write(res.text)




# USING THE BEAUTIFULSOUP {bs4}
from bs4 import BeautifulSoup

with open("scraped_data/data1.html", "r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "lxml")

soup.find('h3')
# .find() is use to get all the data come under the TAG you mention in it



all_h3 = soup.find_all("h3")
# find_all() is the function that will return the first matching values the the TAG
all_countries = []

for h3 in all_h3:
    name = h3.get_text(strip=True)
    # get_text will return the text collected from the HTML file

all_h3 = soup.find_all("h3")

all_countries = []
population = h3.find_next("div").select("span.country-population")[0].get_text(strip=True)
    # print(h3.find_next("div").select_one("span.country-population").get_text(strip=True))

all_countries.append([name, population])

    

import pandas as pd

df = pd.DataFrame(all_countries, columns=["Name", "Population"])

df.to_csv("cleaned_data/data.csv", index=False)