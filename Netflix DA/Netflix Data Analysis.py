#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


df1=pd.read_csv(r"D:\DA Project\Netflix.csv")


# In[87]:


df1


# In[4]:


# basic information about the data set


# In[5]:


df1.head()  #top 5 records of the dataset


# In[6]:


df1.tail()  #bottom 5 records of the dataset


# In[11]:


print(" no of rows:",df1.shape[0])


# In[12]:


print(" no of columns:",df1.shape[1])


# In[14]:


df1.size # total number of elements


# In[16]:


df1.columns


# In[18]:


df1.dtypes


# In[20]:


df1.info() # total information of the dataset


# #  Task 1 search for duplicates in the dataset, if yes remove them!

# In[23]:


df1.duplicated()


# In[24]:


df1[df1.duplicated()]


# In[26]:


df1.drop_duplicates(inplace = True) # removes duplicate records permanently


# In[28]:


df1.info()


# # Task - 2 Null values present in columns? present it with heat map

# # null values

# In[30]:


df1.isnull().sum()


# # seaborn library heat map

# In[75]:


import seaborn as sns


# In[36]:


sns.heatmap(df1.isnull())


# # Questions tab

# # 1) For 'House of Cards', what is the Show Id and Who is the Director of this show ?

# In[38]:


df1.columns


# In[45]:


df1[df1['Title'] == 'House of Cards'] [['Director','Show_Id','Title']]


# In[46]:


#Alternate way using isin


# In[48]:


df1[df1['Title'].isin(["House of Cards"])]


# In[49]:


#also by str contains


# In[52]:


df1[df1['Title'].str.contains("House of Cards")] [['Director','Show_Id','Title']]


# # Q. 2) In which year the highest number of the TV Shows & Movies were released ? Show with Bar Graph.

# In[110]:


df1.assign(New_Date=pd.to_datetime(df1['Release_Date']))


# In[54]:


df1.dtypes


# In[61]:


df1['New_Date'].dt.year.value_counts() # counts the occurences of all individual years in the New_Date Column


# In[62]:


df1['New_Date'].dt.year.value_counts().plot(kind='bar')


# # Q. 3) How many Movies & TV Shows are in the dataset ? Show with Bar Graph.

# In[84]:


df1.head()


# In[72]:


df1.groupby('Category').Category.count()


# In[74]:


# to show the count of unique values in the category column in the form of bar graph


# In[88]:


from sklearn.preprocessing import LabelEncoder

# Create a label encoder
label_encoder = LabelEncoder()

# Apply label encoding to the 'Category' column
df1['Category_encoded'] = label_encoder.fit_transform(df1['Category'])

# Now you can create a count plot using the encoded column
sns.countplot(data=df1, x='Category')


# # Q. 4) Show all the Movies that were released in year 2000.

# In[118]:


df1['New_Date'] = pd.to_datetime(df1['Release_Date'])


# In[119]:


df1


# In[120]:


df1['Year'] = df1['New_Date'].dt.year


# In[121]:


df1


# In[122]:


df1.columns


# In[126]:


df1[(df1['Category'].str.contains('movie', case=False)) & (df1['Year'] == 2020)]


# # Q. 5) Show only the Titles of all TV Shows that were released in France only.

# In[124]:


df1.columns 


# In[128]:


df1[(df1['Category'].str.contains('TV Show', case=False)) & (df1['Country'].str.contains('France',case=False))] #Filtering


# # Q. 6) Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?

# In[144]:


df1['Director'].value_counts().head(10)


# In[5]:


df1.columns


# # Q. 7) Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".

# In[8]:


df1[(df1['Category'] == "Movie") & (df1['Type'] == "Comedies") | (df1['Country'] == "United Kingdom")]


# In[9]:


df1.info(memory_usage="deep")


# In[ ]:




