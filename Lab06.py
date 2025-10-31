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
print(" Number of unique values:")
print(nunique)


#Q5:
# DESCRIBE FCT
describe = df.describe()
# PRINT
print(" Mathematical values")
print(describe)
# The describe function gives us the count, mean, standard deviation, minimum, maximum and the quartile values for both the GNI and the High Income Economy


#Q6: 
# CREATION NEW COLUMN
df["GNI_per_capita"] = df["GNI"] / df["Population"]   
# PRINT
print("GNI_per_capita")
# ROUNDING TO NEAREST CENT = 2 numbers after decimal
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
print("Here are the high income economies:")
print(high_income_economies)


#Q8: 
# INTERSECTION BETWEEN REGION & HIGH INCOME ECONOMY
region_of_high_income = pd.crosstab( df["Region"], df["High Income Economy"])
# PRINT
print("Here are the regions of high income per continent: ")
print(region_of_high_income)


#Q9
# FILTER
high_life_exp_female = df[df["Life expectancy, female"] > 80 ]

# NUM OF COUNTRIES THAT FOLLOW FILTER
number_countries = high_life_exp_female["Country Name"].nunique 

# LIST OF COUNTRIES
countries_name = high_life_exp_female["Country Name"].unique
# PRINT 
print("Here are how many countries women are expected to live longer than 80 years.")
print(number_countries)
print("Here is a list of those countries:")
print(countries_name)



##### PART 4 #####
sns.set_theme(style ="darkgrid")

#Q1: 
# GNI PER CAPITA VS LIFE EXPETANCY: FEMALE
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, female"])
plt.title("GNI per capita vs Life expectancy of females")
plt.show()

# GNI PER CAPITA VS LIFE EXPETANCY: MALE
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, male"])
plt.title("GNI per capita vs Life expectancy of males")
plt.show()
# There is an association. The higher the GNI, the higher the life expectancy since people are more likely to have better, more well-funded life conditions. We can see a relationship between life expectancy and GNI for both genders 


#Q2:     
# GNI PER CAPITA VS LIFE EXPETANCY: FEMALE, BASED ON REGION
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, female"], hue = "Region")
plt.title("Relationship between GNI per capita and the life expectancy of females")
plt.show()

# GNI PER CAPITA VS LIFE EXPETANCY: MALE, BASED ON REGION
sns.relplot( data = df, x = df['GNI_per_capita'], y = df["Life expectancy, male"], hue = "Region")
plt.title("Relationship between GNI per capita and the life expectancy of males")
plt.show()  
# Yes, certain regions have lower GNIs which lead to lower life expectancies. For example, Africa's male life expectancy is much lower than Europe's and Africa's GNI is lower than Europe's. Therefore, we can say that the region does affect life expectancy and GNI, for both males and females. 


#Q3: 
# FEMALE LIFE EXPECTANCY VS GNI PER CAPITA LINEAR PLOT 
sns.relplot( data=df,  x = df['GNI_per_capita'], y = df["Life expectancy, female"], kind = "line",  hue = "Region", errorbar = "sd" ,)
plt.title("Relationship between GNI per capita and life expectancy for females")
plt.show()

# MALE LIFE EXPECTANCY VS GNI PER CAPITA LINEAR PLOT 
sns.relplot( data=df,  x = df['GNI_per_capita'], y = df["Life expectancy, male"], kind = "line",  hue = "Region", errorbar = "sd", )
plt.title("Relationship between GNI per capita and life expectancy for males")
plt.show()
#The standard deviations don't appear in the plot because we only have one value per row, therefore error bars aren't possible since we need more than one value to calculate the standard deviations. 


#Q4:
# GNI PER CAPITA VS LIFE EXPETANCY: FEMALE, BASED ON REGION -> LINEAR
sns.lmplot( data=df,  x = 'GNI_per_capita', y = "Life expectancy, female",hue = "Region")
plt.title("Linear relationship between GNI per capita and life expectancy for females")
plt.show()

# GNI PER CAPITA VS LIFE EXPETANCY: MALE, BASED ON REGION -> LINEAR 
sns.lmplot( data = df, x = "GNI_per_capita", y = "Life expectancy, female",  hue = "Region")
plt.title("Linear relationship between GNI per capita and life expectancy for males")
plt.show()


#Q5: 

# a) Physicians and life expectancy
# female
sns.relplot( data = df, x = df['Physicians'], y = df["Life expectancy, female"], hue = "Region", size = "Population", col = "Region")
plt.title("Relationship between the number of physicians and the life expectancy of females")
plt.show()
# male 
sns.relplot( data = df, x = df['Physicians'], y = df["Life expectancy, male"], hue = "Region", size = "Population", col = "Region")
plt.title("Relationship between the number of physicians and the life expectancy of males")
plt.show()
# The male and female plots have similar relationships between the number of physicians and the life expectancy, however some females life expectancies go beyond 85 years old while none of the male life expectancies do not exceed 85 years old.

# b) Education and life expectancy 
# female 
sns.relplot( data = df, x = df['Tertiary education, female'], y = df["Life expectancy, female"], hue = "Region", size = "Population", col = "Region")
plt.title("Relationship between the tertiary education of females and the life expectancy of females")
plt.show()
# male 
sns.relplot( data = df, x = df['Tertiary education, male'], y = df["Life expectancy, male"], hue = "Region", size = "Population", col = "Region")
plt.title("Relationship between the tertiary education of males and the life expectancy of males")
plt.show()
#There is a relationship between the tertiary education depending on the region and the amount of people (males and females) that are educated, but there are no relationship between the males and females education as females have more tertiary education. In adition, it is clear that having access to tertiary education increases the life expectancy of both genders.

# c) Women in national parliament and life expectancy 
# female 
sns.relplot( data = df, x = df['Women in national parliament'], y = df["Life expectancy, female"], hue = "Region", size = "Population", col = "Region")
plt.title("Relationship between the number of women in the national parliament and the life expectancy of females")
plt.show()
# male 
sns.relplot( data = df, x = df['Women in national parliament'], y = df["Life expectancy, male"], hue = "Region", size = "Population", col = "Region")
plt.title("Relationship between the number of women in the national parliament and the life expectancy of males")
plt.show()
#There is a relationship between the number of females and the life expectancy. The higher the life expectancy. the more women are in the national parliament. The plot shows that some regions, such as Africa, have less people in the national parliament. On the other hand, other regions, such as Europe, have a greater population (both females and males) in the national parliament. This demonstrates that in both male life and female life expectancy the region someone is from has an influence on the number of poeple represented in the national parliament. Therefore, there are more people and they also have greater life expectancy.

# d) Population and life expectancy 
# female 
sns.relplot( data = df, x = df['Population'], y = df["Life expectancy, female"], hue = "Region", size = "Population", col = "Region")
plt.title("Relationship between the totol population and the life expectancy of females")
plt.show()
# male 
sns.relplot( data = df, x = df['Population'], y = df["Life expectancy, male"], hue = "Region", size = "Population", col = "Region")
plt.title("Relationship between the totol population and the life expectancy of males")
plt.show()
# There isnt a meaningful relationship between population and life expectancy, except for extreme values. However we can see that the life expectancies vary no matter which region or population. But there is more variation in regions like Africa and Asia and less in regions like Europe

# e) International tourism and life expectancy 
# female 
sns.relplot( data = df, x = df['International tourism'], y = df["Life expectancy, female"], hue = "Region", size = "Population", col = "Region")
plt.title("Relationship between the international tourism and the life expectancy of females")
plt.show()
# male 
sns.relplot( data = df, x = df['International tourism'], y = df["Life expectancy, male"], hue = "Region", size = "Population", col = "Region")
plt.title("Relationship between the international tourism and the life expectancy of males")
plt.show()
#There is a relationship between region and ine=ternational tourism. Since some regions like Asia and Europe have more toursim while other regions like Africa and Oceania have less tourism. However this doesn't affect the life expectancies of either males or females. 


#Q6:

# a) INTERNET USE VS EMISSIONS PER CAPITA 
# CREATION NEW COLUMN
df["Emissions per capita"] = df["Greenhouse gas emissions"] / df["Population"] 
# PLOT
sns.relplot(data = df, x = df["Internet use"], y = df["Emissions per capita"], hue = "Region")
plt.title("Relationship between internet usage and greenhouse gas emissions per capita")
plt.show()
# It looks like there is a relationship betweeen the internet usage and greenhouse gas emissions per capita as greater internet usage releases more emissions per capita.

# b) HIGH EMISSION COUNTRIES (>0.03)
# FILTER
high_emissions = df[df["Greenhouse gas emissions"] > 0.03 ] 
# COUNTRIES LIST
countries_name_emissions = high_emissions["Country Name"].unique
print("Here is a list of the countries that have high gas emissions:", countries_name_emissions)

# c) INTERNET USE VS EMISSIONS PER CAPITA, BASED ON REGION
# PLOT
sns.relplot(data = df, x = df["Internet use"], y = df["Emissions per capita"], col = "Region" , hue = "Region")
plt.title("Relationship between internet usage and greenhouse gas emissions per capita")
plt.show()
# By using the plot from Q6, a), and adding a column for each region, we can conclude that the variation of high emissions vs internet use depends on the region. In fact, Asia, America and Oceania have a higher variation, while Europe and Africa have more stable variation betwwen emissions vs internet use.  

# d) HIGH INCOME ECONOMIES VS HIGH GREENHOUSE GAS EMISSIONS
# No. not all high income economies have high greenhouse gas emissions




