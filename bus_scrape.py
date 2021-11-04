#scrape business listing from new haven commerce website
#https://www.gnhcc.com/list

from bs4 import BeautifulSoup
import csv
import requests
import re


def getData(url):
    page=requests.get(url)
    #print(f"get data called")
    return BeautifulSoup(page.text,"html.parser")

def scrape_link(data):
    #returns links for categories
    links=[]
    for d in data.find('div',class_="row gz-cards gz-directory-cards gz-no-cards").find_all("a"):
        lcl_link=d.get("href")
        links.append(lcl_link)
        #print(f"{lcl_link}")   
    return links

def scrape_bus(bus_link):
    #get category name
    for bus in bus_link:
        new_page=requests.get(bus)
        b_page=BeautifulSoup(new_page.text,"html.parser")
        
        








def main():
    url=f'https://www.gnhcc.com/list'
    data=getData(url)
    #print(f"Data: {data}")
    bus_link=scrape_link(data)
    #print(f"{bus_link} bus link")
    scrape_bus(bus_link)
     






if __name__=="__main__":
    main()




"""
def scrape(url):
    req=requests.get(url)
    soup=BeautifulSoup(req.content, 'html5lib')
    
    #find business categories
    links=soup.find('div',class_="row gz-cards gz-directory-cards gz-no-cards").find_all('a')
    
    for link in links:
        l_url=str(link).split("//",0)
        
        print(l_url)
"""