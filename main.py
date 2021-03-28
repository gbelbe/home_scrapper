#beautiful soup html parser library
from bs4 import BeautifulSoup

#requests import curl type library
import requests

#convert scraped date text to proper date format
from datetime import datetime

#retrieve the url from the web address
website = requests.get('http://www.kerentree-immobilier.fr/recherche,basic.htm?idp=568148&idtt=2&idtypebien=2')

#check if status is ok http200
print(website)

soup = BeautifulSoup(website.content, 'html.parser')
#print(soup.prettify())

#print(soup.find_all(name="div" ))


#all_div_tags = soup.find_all(name = "div", class_ ="span12 padding-10 transition-bg recherche-annonces box-shadow")

div_tag = soup.find_all(name="div", class_="span12 padding-10 transition-bg recherche-annonces box-shadow")


#print(div_tag)

####WIP
#desc = div_tag.find(name = "span")
#print(span.get)

annonces = []

for tag in div_tag:

    print("_______________________")

    MAJ = tag.find("p", class_="margin-top-10 height-50").find_all(text=True, recursive=False)
    #print(MAJ)

    #retrieve the date, 2nd element of the text list received from MAJ
    majdate = datetime.strptime(MAJ[1].strip().split()[2], '%d/%m/%Y')
    print(majdate)
    annonces.append(majdate)



    lien = tag.find(name= "a")
    print(lien.get("href"))
    print(lien.get("title"))
    #break

print(annonces)

#retrieve index position of the most recent item in the list annonces
#max gives the most recent date when list elements are datetime
print(annonces.index(max(annonces)))

#for tag in all_div_tags:
 #   print(tag.getText)

