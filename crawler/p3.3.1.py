import requests as req
from bs4 import BeautifulSoup


url="https://ithelp.ithome.com.tw/"
head={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}

def got(url):

    respon=req.get(url,headers=head).text
    return BeautifulSoup(respon,'lxml')

soup=got(url)
url2=soup.find('a',class_='menu__item-link')['href']
soup2=got(url2)
doc=soup2.find('a',class_='qa-list__title-link')
print(doc['href'])
url3=doc['href']




