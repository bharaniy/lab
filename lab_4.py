import requests
url=requests.get("https://catalog.umkc.edu/course-offerings/graduate/comp-sci/").text
from bs4 import BeautifulSoup
soup: BeautifulSoup=BeautifulSoup(url,'html.parser')
print("\nTitle of web page:",soup.title.string)
text = soup.find_all(text=True)
resultsblock=soup.findAll('div',{'class':'courseblock'})
for div in resultsblock:
 titles=div.find('span',{'class':'title'}).text
 print(titles)
 overview=div.find('p',{'class':'courseblockdesc'}).text
 print(overview)