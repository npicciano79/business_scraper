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
        full_page=BeautifulSoup(new_page.text,"html.parser")
        #input(print(b_page))
        
        #get category title
        lcl_cat=full_page.find("div",class_="flex-grow-1 gz-pagetitle").find('h1')
        category=str(lcl_cat).strip('<h1>').strip('</')
        input(print(category))

        #get card link 
        card_link=full_page.find('div',class_='card-header').find('a')
        card_link=str(card_link).split('=')[2].split(" ")[0].strip('"')
        input(print(card_link))
        
        c_page=requests.get(card_link)
        card_page=BeautifulSoup(c_page.text,"html.parser")
        input(print(card_page))

        #find business name
        lcl_name=card_page.find('div',class_="d-flex gz-details-head").text
        input(print(lcl_name))

        #find address
        lcl_address=card_page.find('span',class_="gz-street-address").text
        input(print(lcl_address))

        #find city
        #lcl_city=card_page.find('span',class_="gz-address-city").text
        #input(print(lcl_city))

        #find zipcode
        #lcl_zip=card_page.find_next(lcl_city)
        #input(print(lcl_zip))

        for item in card_page.find_all('li',class_="list-group-item"):
            address_data=item.find_next('span').text
            input(print(address_data))








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




"""


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
        lcl_zip=b_page.find("div",itemprop="citystatezip")
        lcl_zip=str(lcl_zip).split('<span>',3)[2].split('<')[0]
        input(print(f"zip: {lcl_zip}"))

        #get phone
        lcl_phone=b_page.find('li', class_="list-group-item gz-card-phone").text
        input(print(f"phone {lcl_phone}"))



"""