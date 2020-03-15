import os
import pandas as pd
path = 'F:\PRICE REFRESH\Blocked'
# path =input("Enter the path=")

for file in os.listdir(path):
    if file.endswith('.xlsx'):
        file_name = os.path.join(path,file)
        print(file_name)

        df = pd.read_excel(file_name,sep="\t")
        temp_df = df[['noon_sku','comp_link']]
        df['Competitor_URL'] = "M2|"+temp_df['noon_sku']+"|"+temp_df['comp_link']
        df['Length'] = df['Competitor_URL'].str.len()
        if 'egy' in temp_df['comp_link']:
            df['comp_name'] = df['comp_name'] == 'souq_egy'

        temp_df =df.reindex(columns=['noon_sku','comp_link','Competitor_URL','Length','comp_name'])
        df1 = temp_df.sort_values(by='Length',ascending=False)
        # block_path =
        if not os.path.exists(os.path.join(path,'Block')):
            os.mkdir(os.path.join(path,'Block'))

        # df1.to_excel(os.path.join(path,'Block','Block.xlsx'), index=False)

        # print(temp_df)
        print(df1)


