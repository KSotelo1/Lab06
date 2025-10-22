# Collaborators: Mia Doan (2483330) and Kaira Sotelo (6293070)
 
# imports
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 

##### PART 3 #####
# loading dataset 
df = pd.read_csv("wdi_wide.csv")
print(df)

#Q3
# info function
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
# nunique function
describe = df.describe()
print(" The mathematical values")
print(describe)
#The describe function gives us many values such as the count, mean, standard deviation, minimum, maximum and the quartile values for both the GNI and the High Income Economy

#Q6: 
#Creation of new column
df["GNI_per_capita"] = df["GNI"] / df["Population"]   
print("GNI_per_capita")
# rounding to nearest cent (2 number after the decimal)
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
# Determining intersection between Region and High Income Economy
region_of_high_income = pd.crosstab( df["Region"], df["High Income Economy"])
print(region_of_high_income)

#Q9
# Creating filter
high_life_exp_female = df[df["Life expectancy, female"] > 80 ]
# Count number of countries that follow filter
number_countries = high_life_exp_female["Country Name"].nunique 
# List countries
countries_name = high_life_exp_female["Country Name"].unique
print("There are ", number_countries, "countries where women are expected to live longer than 80 years.")
print("Here is a list of those countries:", countries_name)




##### PART 4 #####

#Q1: 
    
# female life expectancyvs GNI per capita plot
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, female"])
plt.title("GNI per capita vs Life expectancy of females")
plt.show()

# male life exoectancy vs GNI per capita plot
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, male"])
plt.title("GNI per capita vs Life expectancy of males")
plt.show()
# There is an association. The higher the GNI, the higher the life expectancy since people are more likely to have better, more well-funded life conditions


#Q2:     
    
# female life expectancy vs GNI per capita based on region plot
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, female"], hue = "Region")
plt.title("Relationship between GNI per capita and the life expectancy of females")
plt.show()

# male life expectancy vs GNI per capita based on region plot
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, male"], hue = "Region")
plt.title("Relationship between GNI per capita and the life expectancy of males")
plt.show()  
# Yes, certain regions have lower GNIs which lead to lower life expectancies. for example, Africa's male life expectancy is much lower than Europe's, the same can be said about their GNIs


#Q3: 
    
# female life expectancy vs GNI per capita linear plot
sns.lineplot(data=df,  x = df['GNI_per_capita'], y = df["Life expectancy, female"], hue = "Region", errorbar = "sd" )
plt.title("Relationship between GNI per capita and life expectancy for females")
plt.show()

# male life expectancy vs GNI per capita linear plot
sns.lineplot(data=df,  x = df['GNI_per_capita'], y = df["Life expectancy, male"], hue = "Region", errorbar = "sd" )
plt.title("Relationship between GNI per capita and life expectancy for males")
plt.show()


#Q4

# female life expectancy vs GNI per capita based on region LINEAR plot
sns.lmplot(data=df,  x = df['GNI_per_capita'], y = df["Life expectancy, female"], hue = "Region")
plt.title("Linear relationship between GNI per capita and life expectancy for females")
plt.show()

# male life expectancy vs GNI per capita based on region LINEAR plot 
sns.lmplot(data = df, x = df["GNI_per_capita"], y = df["Life expectancy, female"], hue = "Region")
plt.title("Linear relationship between GNI per capita and life expectancy for males")
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


#Q6 

#a) Internet use vs emissions per capita
sns.lmplot(data = df, x = df["Internet use"], y = df["Greenhouse gas emissions"], hue = "Region")
plt.title("Linear relationship between internet usage and greenhouse gas emissions")
plt.show()
#

#b) countries with high emissions (>0.03)
# Creating filter
high_emissions = df[df["Greenhouse gas emissions"] > 0.03 ] 
# List countries
countries_name_emissions = high_emissions["Country Name"].unique
print("Here is a list of the countries that have high gas emissions:", countries_name_emissions)

#d) high income economies and high emissions
# Determining intersection between Region and High Income Economy
high_income_and_emissions = pd.crosstab( df["Greenhouse gas emissions"], df["High Income Economy"])
print(high_income_and_emissions)






