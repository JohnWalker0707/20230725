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
url2=soup.find_all('a',class_='menu__item-link')[1]['href']

soup2=got(url2)
doc=soup2.find('a',class_='qa-list__title-link')
url3=doc['href']
print(url2+'  >>>  '+url3+'\n')
doc_text=got(url3).find('div',class_="leftside")

print('作者: '+doc_text.find('a',class_='qa-header__info-person').get_text(strip=True))
print('發文時間: '+doc_text.find('a',class_='qa-header__info-time').get_text(strip=True))
tag=''
for i in doc_text.find_all('a',class_='tag qa-header__tagList'):
    tag=tag+' '+i.get_text(strip=True)
print('文章標籤:'+tag)
print('瀏覽數: '+doc_text.find('span',class_='qa-header__info-view').get_text(strip=True).replace('瀏覽',""))
# print(doc_text.get_text(strip=True))



