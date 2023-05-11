import requests
import xml.etree.ElementTree as et
import aiohttp
import datetime 
import asyncio 
import create_table
import pandas as pd
def getdate(format,cur:datetime.date):
    delta=datetime.timedelta(1)
    yesterday=datetime.date.today()-delta
    dates=[]
    while cur <= yesterday:
        dates.append(cur.strftime(format))
        cur+=delta
    return dates


async def source1(dates):
    values=[]
    async with aiohttp.ClientSession() as session:
        for i in dates:
          async with session.get(f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={i}',verify=False) as response:
                result= await response.text()
                root=et.fromstring(result)
                for j in root.findall('Valute'):
                    if j.findtext('CharCode') =='USD':
                        values.append(float(j.findtext('Value').replace(',','.')))
    return values
async def source2(dates):
    values=[]
    async with aiohttp.ClientSession() as session:
        for i in dates:
          async with session.get(f'https://api.currencyapi.com/v3/historical?apikey=kYDvVe6IfM59XNuNHUDu5V9xa3FIPGCTlNq4Eary&currencies=RUB&date={i}') as response:
                result= await response.json()
                values.append(result['data']['RUB']['value'])
    return values


async def main():
    dates1=getdate('%d/%m/%Y',datetime.date(2023,2,10))
    dates2=getdate('%Y-%m-%d',datetime.date(2023,2,10))
    t1=asyncio.create_task(source1(dates1))
    t2=asyncio.create_task(source2(dates2))
    result1 = await t1
    result2=await t2
    df=create_table.create_data_frame(result1,result2,dates1)
    df.to_csv('currencyes.csv',index=False)
    


asyncio.get_event_loop().run_until_complete(main())

