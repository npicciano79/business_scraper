#main scraper driver function 
import getData
import categoryLinks
import scrapeData
import createCSV
import clearCSV





def main():
    url=f'https://www.gnhcc.com/list'
    data=getData.getData(url)
    print(f"Data: {data}")
    bus_link=categoryLinks.scrape_categorylink(data)
    print(f"{bus_link} bus link")
    business_data,category_len=scrapeData.scrape_business_data(bus_link)
    #space=padding(category_len)
    createCSV.createCSV(business_data)
    cleanCSV.createCleanCSV()
    
    
    






if __name__=="__main__":
    main()
