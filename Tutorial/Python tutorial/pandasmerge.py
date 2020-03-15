import pandas as pd

df1 = pd.read_excel("F:\PRICE REFRESH\Blocked\EGY_CATALOG_PRICING_20200105_0430.xlsx"
                    )
df2 = pd.read_excel("F:\PRICE REFRESH\Blocked\Block\Block.xlsx")
df3 =pd.merge(df2,df1,on=['noon_sku','comp_link'],how='left')

pd.set_option('display.max_columns',10)


print(df1.head())
df4 =df1["Reason_Code"]=="Blocked"
print(len(df4))

print("-----------------------------------------------------------------------------")
# print(df2.head())
print("-----------------------------------------------------------------------------")
# print(df3.head())
# df3.to_excel('pandas2.xlsx', index=False, freeze_panes=(1,0))
