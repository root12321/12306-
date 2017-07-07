import urllib.request
import re
import ssl
import json
from cons import station_names
ssl._create_default_https_context=ssl._create_unverified_context
city={}
for i in station_names.split('@'):
    if i :
        city[i.split('|')[1]]=i.split('|')[2]
#print(city)
#print(city['马鞍山东'])
#print(city['南京南'])
t=input('请输入你的出发时间（例如：2017-07-08）：')
from_station=city[input('请输入你的出发地：')]
to_station=city[input('请输入你的目的地：')]
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(t,from_station,to_station)
def getlist():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    urllib.request.Request(url,headers=headers)
    req=urllib.request.urlopen(url)
    html=req.read().decode('utf-8-sig')
    dict=json.loads(html)#把字符串类型的json数据转换为dict
    return dict['data']['result']
#软卧=23，硬卧=28 车次=3 出发时间=8 到达时间=9 历时=10
#n=0
for i in getlist():
    #for y in i.split('|'):
     #   print(n,y)
     #   n=n+1
    trn=i.split('|')
    if trn[23]!='无'or trn[23]!='--':
        print('当前有票\n车次：%s\n出发时间：%s\n到达时间：%s\n历时：%s'%(trn[3],trn[8],trn[9],trn[10]))
    else:
        print('无票，请继续检查')
        continue

