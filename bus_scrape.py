#scrape business listing from new haven commerce website
#https://www.gnhcc.com/list

from bs4 import BeautifulSoup
import csv
import requests


url="https://www.gnhcc.com/list"

def scrape(url):
    req=requests.get(url)
    soup=BeautifulSoup(req.content, 'html5')
    print(soup)






if __name__=="__main__":
    scrape(url)