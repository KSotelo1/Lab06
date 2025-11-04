# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 08:45:41 2025

@author: 2483330
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("songs_normalize.csv")
df = pd.read_csv("songs_normalize.csv")



#Part 2 
#Q1

print("missing values this dataset has", data.isnull().sum)
#Since all values are false, there are no empty values for each variable

#Q2 
duplicates = data.duplicated().sum()

print("How many duplicate values this dataset has", duplicates)
if duplicates > 0 :
    data = data.drop_duplicates()
    print("Removed duplicates")
else: print ("There are no duplicates found")
#There are 59 duplicates values 

#Q3
#rows, columns = data shape

print("data({data.shape[0]} rows x {data.shape[1]} columns")


#Q4 
print("The number of uniques values for each column is", data.nunique())

#Q5

print("The number of songs this dataset has per year")   
print(data["year"].value_counts().sort_index())

#Q6
#The top 5 most danceable
print("The 5 most danceable songs are")
print(data.sort_values (by="danceability", ascending=False).head(5))
print(["artist", "song", "danceability"])

     
                              
#The top 5 least danceable                                                                                
print("The least 5 danceable songs are")          
print(data.sort_values  (by="danceability", ascending=True).head(5))                                                                   
print(["artist", "song", "danceability"])

#Q7
filtered_data = data[data['year']>= 2010] & (data["year"] <=2019) & (data["popularity"] > 80)
print(filtered_data) 

#Q8
print("toop 50 artists")
print(data["artist"].value_counts().head,(50))
#Part 3
#Q1
sns.displot(df, x="year")                                                                               