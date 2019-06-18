import requests
from bs4 import BeautifulSoup

# Collect first page of artists’ list
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
# print(page.text)
# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)
# Pull all text from the BodyText div
artist_name_list = soup.find(class_="BodyText")
# print(artist_name_list)
# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')
# print(artist_name_list_items)
# Create for loop to print out all artists' names
for artist_name in artist_name_list_items:
    print(artist_name.prettify())