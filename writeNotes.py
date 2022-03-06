# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 03:08:00 2022
provide two files:
    worst:players who have the highest vpip more than 500 hands and have lost more than $10
    best:players who have  more than 500 hands and have won more than $10
@author: machineLearner
"""


#open the pokerstars notes xml file
F=open("notes.cubicroot.xml","a",encoding="UTF-8")

#open a csv file containing the names of the worst players
FR1=open("worst.csv",encoding="UTF-8")
negbbsNames=[]
for n in FR1:
    n=FR1.readline()
    n=n.strip("\n")
    negbbsNames.append(n)
FR1.close()

#open a csv file containing the names of the worst players
FR2=open("best.csv",encoding="UTF-8")
pbbNames=[]
for n in FR2:
    n=FR2.readline()
    n=n.strip("\n")
    pbbNames.append(n)

FR2.close()

#create a string then append it to the 
#pokerstars players notes xml file
index=1627255667
line=""
#write all the negative bb players to a file
#names only
for name in negbbsNames:
    line +="<note player=\"" + name + "\" label=\"0\" update=\"" + str(index) + "\"></note>\n"
          #\" label=\"0\" update=\"" + str(index) + \"""></note>\n")
    index +=1

for name in pbbNames:
    line +="<note player=\"" + name + "\" label=\"7\" update=\"" + str(index) + "\"></note>\n"
          #\" label=\"0\" update=\"" + str(index) + \"""></note>\n")
    index +=1

line +="</notes>"
F.writelines(line)
F.close()
