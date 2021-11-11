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
        #bus link is category link, scrape page for each link/category 
        #input(print(bus)) 
        new_page=requests.get(bus)
        b_page=BeautifulSoup(new_page.text,"html.parser")
        #input(print(b_page))
        
        #get category title
        lcl_cat=b_page.find("div",class_="flex-grow-1 gz-pagetitle").find('h1')
        category=str(lcl_cat).strip('<h1>').strip('</')
        input(print(category))

        #get business name
        try:
            lcl_name=b_page.find('span',class_='gz-img-placeholder').text
            input(print(f"name: {lcl_name}"))
        except Exception as e:
            print("Name not found",e)

        #get business address
        lcl_address=b_page.find('span',class_='gz-street-address').text
        input(print(f"address: {lcl_address}"))

        #get city
        lcl_city=b_page.find("span",class_="gz-address-city").text
        input(print(f"city: {lcl_city}"))

        #get zip
        lcl_zip=b_page.find("div",itemprop="citystatezip")[2]
        #lcl_zip1=str(lcl_zip).strip('<span>').strip('</')
        input(print(f"zip: {lcl_zip}"))



        #lcl_cat=str(category)
        
        
        








def main():
    url=f'https://www.gnhcc.com/list'
    data=getData(url)
    #print(f"Data: {data}")
    bus_link=scrape_link(data)
    #print(f"{bus_link} bus link")
    scrape_bus(bus_link)
     






if __name__=="__main__":
    main()




