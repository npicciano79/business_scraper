import getData


def scrape_bus(bus_link):
    business_data=[]
    category_len=[]
    count=1
    #get category name
    #input(bus_link)
    catlen=namelen=streetlen=citylen=phonelen=faxlen=ziplen=weblen=aboutlen=contactlen=0
    for bus in bus_link:    
        #bus link is category link, scrape page for each link/category 
        #print(f"bus {bus}")
        full_page=getData.getData(bus)
  
        #new_page=requests.get(bus)
        #full_page=BeautifulSoup(new_page.text,"html.parser")
        #input(f"{full_page}:  full page  {bus} bus")

        #get category title
        
        lcl_cat=full_page.find("div",class_="flex-grow-1 gz-pagetitle").find('h1')
        category=str(lcl_cat).strip('<h1>').strip('</').strip("'").replace(","," ")
        catlen=max(catlen,len(category))

        print(f"category: {category} cat len{catlen}")


        #get business card links from category page
        for i in full_page.find_all('div', class_="card-header"):
            try:
                lcl_cardlink=str(i.find('a')).split("=")[2].split(" ")[0].strip('"')
                #input(f"_________________\n{lcl_cardlink}\n  {category}________________") 
     
                c_page=requests.get(lcl_cardlink)
                card_page=BeautifulSoup(c_page.text,"html.parser")
                #input(f"{card_page}  \n{lcl_cardlink}")
            except Exception as e:
                print(f"{e} No link available")
                continue


            #find business name
            try:
                lcl_name=card_page.find('div',class_="d-flex gz-details-head").text
                lcl_name=lcl_name.replace('\n'," ").strip("'")
                lcl_name=lcl_name.replace(' '' '," ")
                namelen=max(namelen,len(lcl_name))
                #input(f"{card_page} \n {lcl_name} lcl_name")
            except Exception as e:
                lcl_name=None
                #input(f"error: {e}")


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
                        streetlen=max(streetlen,len(lcl_street))
                    if i==4:
                        lcl_city=val
                        citylen=max(citylen,len(lcl_city))
                    if i==6:
                        lcl_zip=val
                        ziplen=max(ziplen,len(lcl_zip))
                
            else:
                lcl_zip=lcl_city=lcl_street=None
            #print(f"street: {lcl_street} city {lcl_city}  zip {lcl_zip}")

            #add try/except for phone and fax
            try:
                lcl_phone=card_page.find('li',class_="list-group-item gz-card-phone").text
                lcl_phone=lcl_phone.replace('\n'," ")
                phonelen=max(phonelen,len(lcl_phone))
                #print(lcl_phone)
            except Exception as e:
                #input(f"Phone number not found, error: {e}")
                lcl_phone=None

            try:
                lcl_fax=card_page.find('li',class_='list-group-item gz-card-fax').text
                lcl_fax=lcl_fax.replace("\n"," ")
                faxlen=max(faxlen,len(lcl_fax))
                #input(f"fax: {lcl_fax}")
            except Exception as e:
                #input(f"fax number not found, error: {e}")
                lcl_fax=None

            #try/except for website
            try: 
                lcl_web=card_page.find('li',class_="list-group-item gz-card-website").find('a')
                lcl_web=str(lcl_web).split('=')[2].split(" ")[0]
                lcl_web=lcl_web.replace('"'," ")
                weblen=max(weblen,len(lcl_web))
                #input(f"website: {lcl_web}")
            except Exception as e:
                #input(f"web not found, error: {e}")
                lcl_web=None
            #try/except for about/info
            try:
                lcl_about=card_page.find('div',class_="row gz-details-about").text
                lcl_about=lcl_about.replace("\n"," ")
                lcl_about=lcl_about.split("Us ")[1]
                aboutlen=max(aboutlen,len(lcl_about))
                #input(f"about: {lcl_about}")
            except Exception as e:
                #input(f"about not found, error: {e}")
                lcl_about=None
            #try/except for contact person
            try:
                lcl_contact=card_page.find('div',class_="gz-member-repname").text
                lcl_contact=lcl_contact.replace('\n'," ")
                contactlen=max(contactlen,len(lcl_contact))
                #input(f"contact: {lcl_contact}")
            except Exception as e:
                #input(f"contact not found, error: {e}")
                lcl_contact=None   


            #clean data


            lcl_businessData=[count,category,lcl_name,lcl_street,lcl_city,lcl_zip,lcl_phone,lcl_fax,lcl_web,lcl_about,lcl_contact]
            print(f"{count} business {lcl_name} category {category} appended")
            indexlen=4
            category_len=[indexlen,catlen,namelen,streetlen,citylen,ziplen,phonelen,faxlen,weblen,aboutlen,contactlen]
            business_data.append(lcl_businessData)
            count+=1
    
    print("business_data returned")
    return business_data,category_len
