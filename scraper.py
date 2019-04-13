# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import os
os.environ['SCRAPERWIKI_DATABASE_NAME'] = 'sqlite:///data.sqlite'
import scraperwiki
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

req = requests.get('https://osam.com/Commentary')
soup = BeautifulSoup(req.content, 'html.parser')
table = soup.select('a[href$=\".pdf\"]')

data = [{"turl":"https://osam.com" + x['href']} for x in table]
scraperwiki.sqlite.save(unique_keys=['turl'], data=data)

import  datetime
import math
import re
dta = [datetime.datetime.now() + datetime.timedelta(days=x) for x in range(-10,0)]
dta = [x.weekday() for x in dta if x.weekday()<5]
dta = [ "http://www.qhdb.com.cn/Newspaper/PageNavigate.aspx?nid=" + str(math.floor(x /7) * 5 + x % 7 + 2413) for x in dta]
for dtb in dta[0:1]:
  # print(dtb)
  req = requests.get(dtb)
  soup = BeautifulSoup(req.content, 'html.parser')
  table = soup.select('.p_b_list2')
  # print(table)

  table = soup.find_all("span", class_="float")
  dtta = [  x.text for x in table]
  dttb = ["http://www.qhdb.com.cn/Newspaper/"+re.sub("PageNavigate", "CheckLogin", x.a["href"]) for x in table]
  dttc = [re.compile(r"^(?!.*郑州|大连|上海).*(理论|研究|观点|国际|聚集|分析|宏观|焦点|关注).*$").match(x.strip()) != None for x in dtta]
  hkt = pytz.timezone('Asia/Hong_Kong')
  dt = datetime.datetime.now().replace(tzinfo=hkt).date()
  data = [{"turl":dttb[k],"date":dt,"pname":dtta[k],"web":"qhrb"} for k,v in enumerate(dttc)]
  scraperwiki.sqlite.save(unique_keys=['turl'], data=data)
  
dta=["http://www.bankofchina.com/fimarkets/summarize/index"+("" if dti ==0 else "_"+ str(dti)) +".html" for dti in range(2)]
for dtb in dta[0:1]:
  req = requests.get(dtb)
  soup = BeautifulSoup(req.content, 'html.parser')
  table = soup.select('.news a')
  # print(table)
  dtc = [ "http://www.bankofchina.com/fimarkets/summarize/"+ x["href"] for x in table]
  for dtd in dtc[0:1]:
    req2 = requests.get(dtd)
    soup2 = BeautifulSoup(req2.content, 'html.parser')
    table = soup2.select('a[href$=\".pdf\"]')
    data = [{"turl":x['href'],"date":dt,"pname":"bankofchina","web":"zgyh"} for x in table]
    # print(data)
    scraperwiki.sqlite.save(unique_keys=['turl'], data=data)