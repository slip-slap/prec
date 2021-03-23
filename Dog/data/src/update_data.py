import pandas as pd
import tushare as ts


pro = ts.pro_api("b33e62c478b891177c214181aa32ac19864e8ee97e0cc5793b19b7da")

keywords = 'ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,website,email,office,employees'

df = pro.stock_company(exchange='SSE', fields=keywords)
df.to_csv("SSE_listed_company_info.csv",index=False)
print(df)

