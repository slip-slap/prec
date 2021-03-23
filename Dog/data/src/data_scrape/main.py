import  bs4 as bs
import requests

psuedo_chrome = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language":
        "ja-JP,ja;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6,en;q=0.5",
"If-Modified-Since": "Wed, 12 Aug 2015 09:56:42 GMT",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "document",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }

url = "https://www.imdb.com/chart/top/"
url = "http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;szzf;pn10000;ddesc;qsd20200108;qed20210108;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb"

page=requests.get(url, headers=psuedo_chrome)
print(page.status_code)

soup = bs.BeautifulSoup(page.content)

print(soup.prettify())

with open("fund","a") as output_handler:
    output_handler.writelines(soup.prettify())

table = soup.find('table', id="dbtable")
table_body = table.find('tbody')
print(table_body)
rows = table_body.find_all('tr')
for row in rows:
    cols = rows.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    print(cols)



"""
movies = soup.find_all('td', class_="titleColumn")
for i in range(len(movies)):
    print(movies[i].get_text())
"""

