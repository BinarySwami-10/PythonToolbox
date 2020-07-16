from mymodules import * 
url='https://www.bseindia.com/corporates/shpdrPercnt.aspx?scripcd=532488&qtrid=105.00&CompName=DIVI%27S%20LABORATORIES%20LTD.&QtrName=March%202020&Type=TM'
page=open_page(url)
tables=get_tags(page,'table')
table=tables[3] 
organisedData=extractData(table)
df = pd.DataFrame(organisedData[1:],columns=organisedData[0]) #dataframe building
df.to_csv(r'BSE_Link4.csv',index=False)	;print(df)

# NOTES
#LINE NO 1:	cleaning of code into one dependency called 
# 			mymodules which is present adjacent to this file.

#LINE NO 5:	this is the required table as there are 3 levels of 
# 			unnecessary nesting. we can try through 
# 			api url also for better data. and if the data is huge.



