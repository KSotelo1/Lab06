# Collaborators: Mia Doan (2483330) and Kaira Sotelo (6293070)
 
# imports
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 

### PART 3 ###
# loading dataset 
df = pd.read_csv("wdi_wide.csv")
print(df)

#Q3
info = df.info()
print(" The size of the dataset and its data types")
print(info)
#We can subtract the non-null count from the total number of rows to find the empty values for each category 
# Physicians = 217 - 207 = 10 empty values 
# Population = 217 - 217 = 0 empty values 

#Q4:
# nunique function 
nunique = df.nunique()
print(" The number of unique values")
print(nunique)

#Q5:
describe = df.describe()
print(" The mathematical values")
print(describe)
#The describe function gives us many values such as the count, mean, standard deviation, minimum, maximum and the quartile values for both the GNI and the High Income Economy

#Q6: 
#Creation of new column
df["GNI_per_capita"] = df["GNI"] / df["Population"]   
print("GNI_per_capita")
# rounding to nearest cent
df["GNI_per_capita"] = df["GNI_per_capita"].round(2)
print(df[["GNI", "Population", "GNI_per_capita"]])

#Q7: 
# a) 
countries_per_region = df["Region"].value_counts()
print(countries_per_region)

# b) 
high_income_economies = df["High Income Economy"].value_counts()
print(high_income_economies)

#Q8: 
region_of_high_income = pd.crosstab( df["Region"], df["High Income Economy"])
print(region_of_high_income)

#Q9
filtered_data = pd.crosstab(df["Country Name"], [df["Life expectancy, female"] > 80])
print(filtered_data)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


### PART 4 ###

#Q1: 
    
# female 
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, female"])
plt.title("GNI per capita vs Life expectancy of females")
plt.show()

# male 
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, male"])
plt.title("GNI per capita vs Life expectancy of males")
plt.show()
# There is an association. The higher the GNI, the higher the life expectancy"


#Q2:     
# female 
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, female"], hue = "Region")
plt.title("Relationship between GNI per capita and the life expectancy of females")
plt.show()
# male 
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, male"], hue = "Region")
plt.title("Relationship between GNI per capita and the life expectancy of males")
plt.show()  
# Yes, certain regions have lower GNIs which lead to lower life expectancies. for example, Africa's male life expectancy is much lower than Europe's, the same can be said about their GNIs

#Q3: 
# female 
sns.lineplot(data=df,  x = df['GNI_per_capita'], y = df["Life expectancy, female"], hue = "Region", errorbar = "sd" )
plt.title("Relationship between GNI per capital and life expectancy for females")
plt.show()
# male
sns.lineplot(data=df,  x = df['GNI_per_capita'], y = df["Life expectancy, male"], hue = "Region", errorbar = "sd" )
plt.title("Relationship between GNI per capital and life expectancy for males")
plt.show()

#Q4
sns.lmplot(data=df,  x = df['GNI_per_capita'], y = df["Life expectancy, female"], hue = "Region")
plt.title("Linear relationship between GNI per capital and life expectancy for females")
plt.show()

#Q5: 
# female 
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, female"], hue = "Region")
plt.title("Relationship between GNI per capita and the life expectancy of females")
plt.show()
# male 
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, male"], hue = "Region")
plt.title("Relationship between GNI per capita and the life expectancy of males")
plt.show()  




