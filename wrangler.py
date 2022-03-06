# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import csv
d="g:\\code\\cowboyslyrics\\Stars\\"

fname="losers.csv"
d+=fname
df=pd.read_csv(fname,sep=",")

#clean the data
#####################################################
#                                                   #
#git rid of $ and convert to float                  #
#convert hands to int                               #
#                                                   #
#####################################################
def cleanMe(f,output):
    df=pd.read_csv(fname)
    df['My C Won']=df['My C Won'].str.replace('$','')
    df['My C Won']=df['My C Won'].astype(float)
    df['VPIP']=df['VPIP'].astype(float)
    df['Hands']=df['Hands'].str.replace(',','')
    df['Hands']=df['Hands'].astype(int)
    df['BB/100']=df['BB/100'].astype(float)
    
    
    #write the clean data to a file
    df.to_csv(output)
    return df

pokerDf=cleanMe(fname,"output.csv")

#print a players stats
def stats(pName):
    s=pokerDf[pokerDf['Player']==pName]
    print(s)
    return s
    

#print a list of players stats

players=['cubicroot','striko1144','Sposito1973','kingspawnn']
pstats={'Name':[],'Won':[],'Hands':[],'VPIP':[],'BB/100':[]}
losers=[]
for player in players:
    df2=stats(player)
    pstats['Name'].append(df2.iloc[0][0])
    pstats['Won'].append(df2.iloc[0][1])
    pstats['Hands'].append(df2.iloc[0][2])
    pstats['VPIP'].append(df2.iloc[0][3])
    pstats['BB/100'].append(df2.iloc[0][4])

for x in range(4):
    print(pstats['Name'][x],pstats['Won'][x],pstats['Hands'][x],pstats['VPIP'][x],pstats['BB/100'][x])


#write the stats dict to a file
a_file = open("sample.csv", "w")

writer = csv.writer(a_file)
for key, value in pstats.items():
    writer.writerow([key, value])

a_file.close()
    

