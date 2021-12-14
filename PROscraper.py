from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

start_url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(start_url)

soup = bs(page.text,"html.parser")
star_table = soup.find("table")

temp_list = []
table_rows = star_ table[7].find_all('tr')
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td] 
    temp_list.append(row)

star_names = []
star_radiuses = []
star_masses = []
star_distance = []
for i in range(1, len(temp_list)):
    star_names.append(temp_list[i][0])
    star_radiuses.append(temp_list[i][9])
    star_masses.append(temp_list[i][8])
    star_distance.append(temp_list[i]5])