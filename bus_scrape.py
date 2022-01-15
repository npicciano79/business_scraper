#scrape business listing from new haven commerce website
#https://www.gnhcc.com/list
# & C:/Users/npicc/Documents/python/python.exe c:/Users/npicc/Documents/Coding/projects/business_scraper/bus_scrape.py

from bs4 import BeautifulSoup
import csv
import requests
import re


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
        full_page=getData(bus)
  
        #new_page=requests.get(bus)
        #full_page=BeautifulSoup(new_page.text,"html.parser")
        #input(f"{full_page}:  full page  {bus} bus")

        #get category title
        lcl_cat=full_page.find("div",class_="flex-grow-1 gz-pagetitle").find('h1')
        category=str(lcl_cat).strip('<h1>').strip('</').strip("'")
        #input(print(f"category: {category}"))


        #get business card links from category page
        for i in full_page.find_all('div', class_="card-header"):
            lcl_cardlink=str(i.find('a')).split("=")[2].split(" ")[0].strip('"')
            #input(f"_________________\n{lcl_cardlink}\n  {category}________________") 
     
            c_page=requests.get(lcl_cardlink)
            card_page=BeautifulSoup(c_page.text,"html.parser")
            #input(f"{card_page}  \n{lcl_cardlink}")

            #find business name
            try:
                lcl_name=card_page.find('div',class_="d-flex gz-details-head").text
                lcl_name=lcl_name.replace('\n'," ").strip("'")
                #input(f"{card_page} \n {lcl_name} lcl_name")
            except Exception as e:
                input(f"error: {e}")


            #find full address
            
            address_check=True
            try:
                lcl_address_full=card_page.find('li',class_="list-group-item gz-card-address").text.splitlines()
                #input(lcl_address_full)
            except Exception as e:
                address_check=False
            
            #split full_address to street, city zip
            if address_check==True:
                for i,val in enumerate(lcl_address_full):
                    if i==3:
                        lcl_street=val
                    if i==4:
                        lcl_city=val
                    if i==6:
                        lcl_zip=val
                
            else:
                lcl_zip=lcl_city=lcl_street=None
            #print(f"name: {lcl_cardlink} street: {lcl_street} city {lcl_city}  zip {lcl_zip}")

            #add try/except for phone and fax
            try:
                lcl_phone=card_page.find('li',class_="list-group-item gz-card-phone").text
                lcl_phone=lcl_phone.replace('\n'," ")
                #print(lcl_phone)
            except Exception as e:
                #input(f"Phone number not found, error: {e}")
                lcl_phone=None

            try:
                lcl_fax=card_page.find('li',class_='list-group-item gz-card-fax').text
                lcl_fax=lcl_fax.replace("\n"," ")
                #input(f"fax: {lcl_fax}")
            except Exception as e:
                #input(f"fax number not found, error: {e}")
                lcl_fax=None


            try: 
                lcl_web=card_page.find('li',class_="list-group-item gz-card-website").find('a')
                lcl_web=lcl_web.split('=')
                input(f"website: {lcl_web}")
            except Exception as e:
                input(f"web not found, error: {e}")
                lcl_web=None
"""
            try:
                lcl_about=card_page.find('div',class_="row gz-details-about").text
                lcl_about-lcl_about.replace("\n"," ")
                #input(lcl_about)
            except Exception as e:
                #input(f"about not found, error: {e}")
                lcl_about=None

            try:
                lcl_contact=card_page.find('div',class_="gz-member-repname").text
                lcl_contact=lcl_contact.replace('\n'," ")
                #input(lcl_contact)
            except Exception as e:
                #input(f"contact not found, error: {e}")
                lcl_contact=None   

            lcl_businessData=[count,category,lcl_name,lcl_street,lcl_city,lcl_zip,lcl_phone,lcl_fax,lcl_web,lcl_about,lcl_contact]
            business_data.append(lcl_businessData)
            count+=1
            print(f"business data: {business_data}")
                

                
"""              
                








def main():
    url=f'https://www.gnhcc.com/list'
    data=getData(url)
    #print(f"Data: {data}")
    bus_link=scrape_categorylink(data)
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



        find address
        lcl_address=card_page.find('span',class_="gz-street-address").text
        input(print(lcl_address))

        #find city
        lcl_city=card_page.find('span',class_="gz-address-city").text
        input(print(lcl_city))

        #find zipcode
        lcl_zip=card_page.find_next('span', class_="gz-address-city")
        input(print(lcl_zip))

        #for item in card_page.find_all('li',class_="list-group-item"):
            #address_data=item.find_next('span').text
            #input(print(address_data))
"""