import csv
import os
import requests
from bs4 import BeautifulSoup

current_dir = os.path.dirname(__file__)
filename = os.path.join(current_dir, 'z-artist-names.csv')

# Collect first page of artists’ list
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Remove bottom links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

# Create a file to write to, add headers row
new_file = open(filename, 'w', encoding='utf-8')
f = csv.writer(new_file)
f.writerow(['Name', 'Link'])

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='BodyText')

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')

# Create for loop to print out all artists' names
for artist_name in artist_name_list_items:
    # Pull the contents from the tags
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')
    print("{0}: {1}".format(names, links))
    # Add each artist’s name and associated link to a row
    f.writerow([names, links])
