import bs4
from selenium import webdriver

url = "http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;szzf;pn10000;ddesc;qsd20200108;qed20210108;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb"

brower = webdriver.Chrome("./chromedriver")
brower.get(url)

soup = bs4.BeautifulSoup(brower.page_source, "lxml")

with open("fund.xml","a") as output_handler:
    output_handler.writelines(soup.prettify())

