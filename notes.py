# -*- coding: utf-8 -*-
"""
https://www.decodingdevops.com/python-write-to-file-line-by-line/
write to the pokerstars notes.xml
use the above link as a tutorial

"""

import pandas as pd

d="C:\\Users\\jonny\\Documents\\GitHub\\stars\\Stars\\"

f1="allplayers.csv"

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

df['VPIP']=df['VPIP'].str.replace('-','0')
df['VPIP']=df['VPIP'].astype(float)

df['Hands']=df['Hands'].str.replace(',','')
df['Hands']=df['Hands'].astype(int)
df['Total AF']=df['Total AF'].str.replace('-','0')
df['Total AF']=df['Total AF'].astype(float)
df['Total AFq']=df['Total AFq'].str.replace('-','0')
df['Total AFq']=df['Total AFq'].astype(float)
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
df.to_csv("cleanedPokerData.csv")

dfWinners=df[df['My C Won']>25]
dfLosers=df[df['My C Won']< -25]

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


F=open("Losernotes.txt","a")
index=1627255667
line=""
for name in losers:
    line +="<note player=\"" + name + "\" label=\"0\" update=\"" + str(index) + "\"></note>\n"
          #\" label=\"0\" update=\"" + str(index) + \"""></note>\n")
    index +=1
F.writelines(line)
F.close()

F=open("Winnernotes.txt","a")
line=""
for name in winners:
    line +="<note player=\"" + name + "\" label=\"6\" update=\"" + str(index) + "\"></note>\n"
          #\" label=\"0\" update=\"" + str(index) + \"""></note>\n")
    index +=1
F.writelines(line)
F.close()









'''
index=1627255667
donors= "<note player=\"Artishell\" label=\"0\" update=\"" + str(index) + "\"><\\note>\n"
player = "Artishell"

F = open("note.xml","a")

for line in range(5):
    F.writelines(donors)
    index  +=1
    donors= "<note player=\"Artishell\" label=\"0\" update=\"" + str(index) + "\"></note>\n"
    

F.close()

'''