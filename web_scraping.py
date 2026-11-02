'''web scraping is the another way to collect the data using the requests and bs4'''
import requests
url="https://www.scrapethissite.com/pages/simple/"
res=requests.get(url)
res

res.status_code#200 will be the answer
