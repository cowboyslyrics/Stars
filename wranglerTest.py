# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 02:25:17 2022
Clean the pokertaker report "tobecleaned.csv"
write the cleaned data to "cleanedpokerdata.csv"
@author: machineLearner
"""
import pandas as pd
import wrangler

d="g:\\code\\cowboyslyrics\\Stars\\"

fname="tobecleaned.csv"
d+=fname
df=pd.read_csv(fname,sep=",")
output="cleanedpokerdata.csv"
players=wrangler.cleanMe(fname, output)

