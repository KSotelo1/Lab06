#### Collaborators: Mia Doan (2483330) and Kaira Sotelo (6293070) ####
 
##### PART 3 #####

#Q2:
# MODULES
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 

# DATASET 
df = pd.read_csv("wdi_wide.csv")
# PRINT
print(df)


#Q3:
# INFO FCT
info = df.info()
# PRINT
print(" The size of the dataset and its data types")
print(info)
# We can subtract the non-null count from the total number of rows to find the empty values for each category 
# Physicians = 217 - 207 = 10 empty values 
# Population = 217 - 217 = 0 empty values 


#Q4:
# NUNIQUE FCT
nunique = df.nunique()
# PRINT
print(" The number of unique values")
print(nunique)


#Q5:
# DESCRIBE FCT
describe = df.describe()
# PRINT
print(" The mathematical values")
print(describe)
# The describe function gives us the count, mean, standard deviation, minimum, maximum and the quartile values for both the GNI and the High Income Economy


#Q6: 
# CREATION NEW COLUMN
df["GNI_per_capita"] = df["GNI"] / df["Population"]   
# PRINT
print("GNI_per_capita")

# ROUNDING TO NEAREST CENT 
# nearest cent = 2 numbers after decimal
df["GNI_per_capita"] = df["GNI_per_capita"].round(2)
# PRINT
print(df[["GNI", "Population", "GNI_per_capita"]])


#Q7: 
# a) COUNTRIES PER REGION
countries_per_region = df["Region"].value_counts()
# PRINT
print("Here are the number of countries in each region:")
print(countries_per_region)

# b) NUMBER OF HIGH INCOME ECONOMIES 
high_income_economies = df["High Income Economy"].value_counts()
# PRINT
print("There are ", high_income_economies, "high income economies.")


#Q8: 
# INTERSECTION BETWEEN REGION & HIGH INCOME ECONOMY
region_of_high_income = pd.crosstab( df["Region"], df["High Income Economy"])
# PRINT
print("The regions of high income are: ", region_of_high_income)


#Q9
# FILTER
high_life_exp_female = df[df["Life expectancy, female"] > 80 ]

# NUM OF COUNTRIES THAT FOLLOW FILTER
number_countries = high_life_exp_female["Country Name"].nunique 

# LIST OF COUNTRIES
countries_name = high_life_exp_female["Country Name"].unique
# PRINT 
print("There are ", number_countries, "countries where women are expected to live longer than 80 years.")
print("Here is a list of those countries:", countries_name)



##### PART 4 #####

#Q1: 
    
# GNI PER CAPITA VS LIFE EXPETANCY: FEMALE
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, female"])
plt.title("GNI per capita vs Life expectancy of females")
plt.show()

# GNI PER CAPITA VS LIFE EXPETANCY: MALE
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, male"])
plt.title("GNI per capita vs Life expectancy of males")
plt.show()
# There is an association. The higher the GNI, the higher the life expectancy since people are more likely to have better, more well-funded life conditions


#Q2:     
    
# GNI PER CAPITA VS LIFE EXPETANCY: FEMALE, BASED ON REGION
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, female"], hue = "Region")
plt.title("Relationship between GNI per capita and the life expectancy of females")
plt.show()

# GNI PER CAPITA VS LIFE EXPETANCY: MALE, BASED ON REGION
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, male"], hue = "Region")
plt.title("Relationship between GNI per capita and the life expectancy of males")
plt.show()  
# Yes, certain regions have lower GNIs which lead to lower life expectancies. For example, Africa's male life expectancy is much lower than Europe's, the same can be said about their GNIs


#Q3: 
    
# female life expectancy vs GNI per capita linear plot
sns.lineplot(data=df,  x = df['GNI_per_capita'], y = df["Life expectancy, female"], hue = "Region", ci = "sd" )
plt.title("Relationship between GNI per capita and life expectancy for females")
plt.show()

# male life expectancy vs GNI per capita linear plot
sns.lineplot(data=df,  x = df['GNI_per_capita'], y = df["Life expectancy, male"], hue = "Region", ci = "sd" )
plt.title("Relationship between GNI per capita and life expectancy for males")
plt.show()


#Q4

# GNI PER CAPITA VS LIFE EXPETANCY: FEMALE, BASED ON REGION -> LINEAR
sns.lmplot(data=df,  x = df['GNI_per_capita'], y = df["Life expectancy, female"], hue = "Region")
plt.title("Linear relationship between GNI per capita and life expectancy for females")
plt.show()

# GNI PER CAPITA VS LIFE EXPETANCY: MALE, BASED ON REGION -> LINEAR 
sns.lmplot(data = df, x = df["GNI_per_capita"], y = df["Life expectancy, female"], hue = "Region")
plt.title("Linear relationship between GNI per capita and life expectancy for males")
plt.show()


#Q5: 
# FEMALE RELATIONSHIP PLOTS
# a) Physicians and life expectancy
sns.relplot( data = df, x = df['Physicians'], y = df["Life expectancy, female"], hue = "Region")
plt.title("Relationship between the number of physicians and the life expectancy of females")
plt.show()
# b) Education and life expectancy 
sns.relplot( data = df, x = df['Tertiary education, female'], y = df["Life expectancy, female"], hue = "Region")
plt.title("Relationship between the tertiary education of females and the life expectancy of females")
plt.show()
# c) Women in national parliament and life expectancy 
sns.relplot( data = df, x = df['Women in national parliament'], y = df["Life expectancy, female"], hue = "Region")
plt.title("Relationship between the number of women in the national parliament and the life expectancy of females")
plt.show()
# d) Population and life expectancy 
sns.relplot( data = df, x = df['Population'], y = df["Life expectancy, female"], hue = "Region")
plt.title("Relationship between the totol population and the life expectancy of females")
plt.show()
# e) Intermediate region and life expectancy 
sns.relplot( data = df, x = df['Intermediate Region'], y = df["Life expectancy, female"], hue = "Region")
plt.title("Relationship between the intermediate region and the life expectancy of females")
plt.show()

# MALE RELATIONSHIP PLOTS
# a) Physicians and life expectancy
sns.relplot( data = df, x = df['Physicians'], y = df["Life expectancy, male"], hue = "Region")
plt.title("Relationship between the number of physicians and the life expectancy of males")
plt.show()
# b) Education and life expectancy 
sns.relplot( data = df, x = df['Tertiary education, male'], y = df["Life expectancy, male"], hue = "Region")
plt.title("Relationship between the tertiary education of males and the life expectancy of males")
plt.show()
# c) Women in national parliament and life expectancy 
sns.relplot( data = df, x = df['Women in national parliament'], y = df["Life expectancy, male"], hue = "Region")
plt.title("Relationship between the number of women in the national parliament and the life expectancy of males")
plt.show()
# d) Population and life expectancy 
sns.relplot( data = df, x = df['Population'], y = df["Life expectancy, male"], hue = "Region")
plt.title("Relationship between the totol population and the life expectancy of males")
plt.show()
# e) Intermediate region and life expectancy 
sns.relplot( data = df, x = df['Intermediate Region'], y = df["Life expectancy, male"], hue = "Region")
plt.title("Relationship between the intermediate region and the life expectancy of males")
plt.show()



#Q6:

# a) INTERNET USE VS EMISSIONS PER CAPITA 
# CREATION NEW COLUMN
df["Emissions_per_capita"] = df["Greenhouse gas emissions"] / df["Population"] 
# PLOT
sns.lmplot(data = df, x = df["Internet use"], y = df["Emissions_per_capita"], hue = "Region")
plt.title("Linear relationship between internet usage and greenhouse gas emissions per capita")
plt.show()
# There

# b) HIGH EMISSION COUNTRIES (>0.03)
# FILTER
high_emissions = df[df["Greenhouse gas emissions"] > 0.03 ] 
# COUNTRIES LIST
countries_name_emissions = high_emissions["Country Name"].unique
print("Here is a list of the countries that have high gas emissions:", countries_name_emissions)

# c) INTERNET USE VS EMISSIONS PER CAPITA, BASED ON REGION
sns.lmplot(data = df, x = df["Internet use"], y = df["Emissions_per_capita"], hue = "Region")
plt.title("Linear relationship between internet usage and greenhouse gas emissions per capita, based on region")
plt.show()
# There is alot/not much variaton of emissions per capita based on internet use, according to the region

#d)HIGH INCOME ECONOMIES VS HIGH GREENHOUSE GAS ECONOMIES
# INTERSECTION BETWEEN HIGH GAS EMISSIONS AND HIGH INCOME ECONOMIES
high_income_and_emissions = pd.crosstab( df["Greenhouse gas emissions"], df["High Income Economy"])
print(high_income_and_emissions)






