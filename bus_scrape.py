#scrape business listing from new haven commerce website
#https://www.gnhcc.com/list

from bs4 import BeautifulSoup
import csv
import requests
import re


url="https://www.gnhcc.com/list"

def scrape(url):
    req=requests.get(url)
    soup=BeautifulSoup(req.content, 'html5lib')
    
    #find business categories
    links=soup.find('div',class_="row gz-cards gz-directory-cards gz-no-cards").find_all('a')
    
    for link in links:
        l_url=str(link).split("//",0)
        
        print(l_url)
        
     






if __name__=="__main__":
    scrape(url)