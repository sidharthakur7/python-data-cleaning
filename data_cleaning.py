#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

#Load Data
df= pd.read_csv("data.csv")


print("Origina Data:")
print(df)

#Remove rows with missing values 
df.dropna()

#Remove Duplicate roes to avoid repeated data
df=df.drop_duplicates()

#Stanardize column names (remove spaces and lowercase)
df.columns=df.columns.str.strip().str.lower()

#Save Cleaned Data
df.to_csv("cleaned_data.csv",index=False)

print("\nCleaned Data:")
print("\nShape Before Cleaning")
print("Shape After Cleaning",df.shape)
print(df)

print("\nData Cleaned Sucessfully!")


# In[ ]:




