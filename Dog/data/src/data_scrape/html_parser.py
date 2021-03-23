import bs4

save_path = "../../data/fund/fund_history_data/"

soup = bs4.BeautifulSoup(open("fund.xml","r"),"html.parser")

table = soup.find('table', id="dbtable")
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    final_cols = [ele.text.replace("\n",'').strip() for ele in cols]
    with open(save_path + final_cols[2] +".csv","a") as input_handler:
        input_handler.writelines(str(final_cols[4])+ ","+ str(final_cols[5])+ ","+ str(final_cols[6])+"\n")
