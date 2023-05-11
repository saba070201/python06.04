import requests
import bs4
response=requests.get('https://mfd.ru/currency/?currency=USD')
soup=bs4.BeautifulSoup(response.text,'html.parser')
data=soup.find('table',{'class':'mfd-table mfd-currency-table'})
data1=data.find_all('tr')
print(data)