#!business scraper 2"
#scrape business listing from new haven commerce website
#https://www.gnhcc.com/list

from bs4 import BeautifulSoup
import csv
import requests
import re

def main():
    url=f'https://www.gnhcc.com/list'
    data=getData(url)
    #print(f"Data: {data}")
    bus_link=scrape_categorylink(data)
    #print(f"{bus_link} bus link")
    scrape_bus(bus_link)

def getData(url):
    page=requests.get(url)
    #print(f"get data called")
    return BeautifulSoup(page.text,"html.parser")

def scrape_categorylink(data):
    #returns links for categories
    links=[]
    for d in data.find('div',class_="row gz-cards gz-directory-cards gz-no-cards").find_all("a"):
        lcl_link=d.get("href")
        links.append(lcl_link)
        #print(f"{lcl_link}")   
    return links

def scrape_bus(bus_link):
    business_data=[]
    count=1
    #get category name
    #input(bus_link)
    for bus in bus_link:    
        #bus link is category link, scrape page for each link/category 
        #print(f"bus {bus}")
        new_page=requests.get(bus)
        full_page=BeautifulSoup(new_page.text,"html.parser")
        
        #get category title
        lcl_cat=full_page.find("div",class_="flex-grow-1 gz-pagetitle").find('h1')
        category=str(lcl_cat).strip('<h1>').strip('</').strip("'")
        #input(print(f"category: {category}"))

            
        #get business card links from category page
        for i in full_page.find_all('div', class_="gz-list-card-wrapper col-sm-6 col-md-4 col-lg-3"):
            #business_card=str(i.find_('a')).split("=")[2].split(" ")[0].strip('"')
            #input(f"_________________\n{lcl_cardlink}\n________________")
            input(f"business card: {i} bus card")
            




     


if __name__=="__main__":
    main()