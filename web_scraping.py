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