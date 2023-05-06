from bs4 import BeautifulSoup
import requests 
import re 

def getData(url):
    page=requests.get(url)
    #print(f"get data called")
    return BeautifulSoup(page.text,"html.parser")