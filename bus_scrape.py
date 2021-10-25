#scrape business listing from new haven commerce website
#https://www.gnhcc.com/list

from bs4 import BeautifulSoup
import csv
import requests


url="https://www.gnhcc.com/list"

def scrape(url):
    req=requests.get(url)
    soup=BeautifulSoup(req.content, 'html5lib')
    
    #find business categories

    cat=soup.find('div',class_="row gz-cards gz-directory-cards gz-no-cards")
    print(f"cat--- {cat} ---cat")
    #test=soup.find("div",class_="row gz-directory-cards gz-no-cards")
    #print(f"test: {test}")






if __name__=="__main__":
    scrape(url)