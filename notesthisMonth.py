# -*- coding: utf-8 -*-
"""
https://www.decodingdevops.com/python-write-to-file-line-by-line/
write to the pokerstars notes.xml
use the above link as a tutorial

"""

import pandas as pd
import numpy as np

d="C:\\Users\\jonny\\Documents\\GitHub\\stars\\Stars\\"

f1="thisMonth.csv"

df=pd.read_csv(d+f1)

#clean the data
#####################################################
#                                                   #
#git rid of $ and convert to float                  #
#convert hands to int                               #
#replace '-' vpip with 0                            #
#replace '-' AF and AFq with 0                      #
#                                                   #
#####################################################

df['My C Won']=df['My C Won'].str.replace('$','')
df['My C Won']=df['My C Won'].astype(float)

#df['VPIP']=df['VPIP'].str.replace('-','0')
df['VPIP']=df['VPIP'].astype(float)

df['Hands']=df['Hands'].str.replace(',','')
df['Hands']=df['Hands'].astype(int)
df['BB/100']=df['BB/100'].str.replace(',','')
df['BB/100']=df['BB/100'].astype(float)

summary=df.describe()
print(summary.keys())
print(summary['My C Won'])
#players  played the most hands:
topTenPlayers=df[df['Hands']>30000]
topTenPlayers=topTenPlayers.sort_values('BB/100',axis=0,ascending=False)
print(topTenPlayers.describe())
print(topTenPlayers)

#write the clean data to a file
df.to_csv("cleanedPokerData2.csv")

dfWinners=df[df['BB/100']>3.9]
dfLosers=df[df['BB/100']<  -1.0]

dfWinners.to_csv("winners.csv")
dfLosers.to_csv("losers.csv")

#get the list of losers
winners=list(dfWinners.iloc[:,0])
losers=list(dfLosers.iloc[:,0])

#print a players stats
dfLosers[dfLosers['Player']=="ZZZPredator"]

#how many players have VPIP > 40
vp40=df[df["VPIP"]>40]
vp40=vp40[vp40["Hands"]>1500]
vp40.to_csv("vp40plus.csv")
#how many players have VPIP < 20
vp20=df[df["VPIP"]<20]
vp20=vp20[vp20["Hands"]>500]
vp20.to_csv("vp20minus.csv")

#worst players by BB/100 rate and 500 hands or more
negbbs=df[df['BB/100']<-1]
negbbs=negbbs[negbbs['Hands']>500]
negbbsNames=negbbs['Player']

#best players by BB/100 rate and 500 hands or more
posBBs=df[df['BB/100']> 6]
posBBs=posBBs[posBBs['Hands']>500]
posBBNames=posBBs['Player']


F=open("notes.cubicroot.xml","a")
index=1627255667
line=""
#write all the negative bb players to a file
#names only
for name in negbbsNames:
    line +="<note player=\"" + name + "\" label=\"0\" update=\"" + str(index) + "\"></note>\n"
          #\" label=\"0\" update=\"" + str(index) + \"""></note>\n")
    index +=1
F.writelines(line)

line=""
for name in posBBNames:
    line +="<note player=\"" + name + "\" label=\"6\" update=\"" + str(index) + "\"></note>\n"
          #\" label=\"0\" update=\"" + str(index) + \"""></note>\n")
    index +=1
line +="</notes>"
F.writelines(line)
F.close()








