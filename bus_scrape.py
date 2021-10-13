#scrape business listing from new haven commerce website
#https://www.gnhcc.com/list

from bs4 import BeautifulSoup
import csv
import requests


url="https://www.gnhcc.com/list"

def scrape(url):
    req=requests.get(url)
    print(req)






if __name__=="__main__":
    scrape(url)