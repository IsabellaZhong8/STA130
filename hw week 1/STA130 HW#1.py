#!/usr/bin/env python
# coding: utf-8

# Question 1:

# In[50]:


import pandas as pd 
url = "https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Diabetes%20Missing%20Data.csv"
df = pd.read_csv(url)
df.isna().sum()

print(df)


# Question 2:

# In[51]:


import pandas as pd 
url = "https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Diabetes%20Missing%20Data.csv"
df = pd.read_csv(url)
df.isna().sum()
rows, columns = df.shape

print(df)
print(f"Rows: {rows} Columns: {columns}")


# Observation: The indivdiaul pieces of data/records in the dataset, where each row respresents an observation i.e. each person in this dataframe has a row of information including BMI, glucose levels, age, etc. - record of this information PER person is an observation 
# 
# Variables: They are the indivdiaul variables/columns in the dataframe, such as the glucose, age, class, etc. 
# 
# Essentially, the rows are the observations, and the variables are the columns 

# Question 3:

# In[6]:


import pandas as pd 
url = "https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Diabetes%20Missing%20Data.csv"
df = pd.read_csv(url)
df.isna().sum()
rows, columns = df.shape

summary = df.describe()
print(f"Columns Summary: \n {summary}")


df.head() 
print(f"Rows: {rows} Columns: {columns}")


# Question 4: 

# In[12]:


import pandas as pd 
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv" 
df = pd.read_csv(url)

df.isna().sum()
rows, columns = df.shape


numeric_summary = df.describe()
non_numeric_summary = df.describe(include= 'object')
print(f"Numeric Columns Summary: \n {numeric_summary} \n")
print(f"Non-Numeric Columns Summary: \n {non_numeric_summary}")


df.head() 
print(f"Rows: {rows} Columns: {columns}")


# Question 5: 

# df.shape only reports the number of rows and columns in the form (rows, columns), indicating, in this examples, the amount of people (observations) and the amount of studied variables
# 
# Key characteristics for df.shape: 
#     - reports total number of columns regardless of their missing values and data types
#     - does not end with closed brackets/parantheses () -> this means it is a property instead of a method, returning a tuple value 
# 
# df.describe will provide statisitcs like count, mean, std, min, etc. for numerical columns/variables only: however, for non-numerical columns/variables, it will provide the count, frequency, etc. given that df.describe(include = "object") is executed. This generates a summary for object types (non-numeric). 
#  
# Key characteristics for df.describe: 
#     - analyzes numerical values by default, unless stated otherwise (inlcude = "object") 
#     - if a column contains only NaN, it may skip it entirely 
#     - ends with closed brackets()/parathanese -> is a method/function, where the paranthese allows us to take arguments, and indicates that it should run on its INTERNAL logic and return the result 
# 
# 
# The count row given by df.describe can indicate how many missing values/NaN exist in each column, as it only counts meaningfull values (actual data that is not missing) 
# 
# In relation to df.shape, we can use it to determine how many missing values there are using the difference. 
# 
# i.e. there are 891 rows, but there are 714 in the count row for age. This means that 187 missing values in the age column. 

# Question 6: 

# - count: number of NOT missing data (how many actual values are provided) in each column 
# - mean: arthimetric average for the non-missing values (so all the values summed up divided by the NUMBER of values) 
# - std (standard deviation): the amount of variation of values in the column -> a low value means that the values are close to the mean
# - min: the minimum value in the column 
# - max: the maximum value in the column
# - 25%: the value where 25% of the values in the column are under 
# - 50%: the value where 50% of the values in the column are under
# - 75%: the value where 75% of the values in the column are under 

# Question 7: 

# 1. If all information is required to be in the dataset, removing columns/rows that include missing data is more efficent since it removes ALL the columns. 
# 2. If you want to delete a specific column due to reasons that are not because it has missing values 
# 3. Becuase you should filter out which columns are not necessary first in order to make df.dropna more efficent and increase performance 
# 4. In the titantic csv, it includes the column 'survived' and 'alive', which is uncessary since we know that ALL the observations are based on people who survived (count is 891, and # of rows is 891) so we could use del df['survived'] and del df['alive'], and instead put it in the title of the dataset ex. Data on Titanic Survivors 
# 
# Before: there are 15 columns and 891 rows
# After: there are 13 columns and 891 rows 
# 

# Question 8: 

# 1. The df.groupby('col1') takes col1 and groups in into subgroups that have same values in column one. Then, it takes executes df.describe() method onto col2, and provides the statistics for each group 
# ex.            count        mean         std   min   25%   50%   75%   max
# class                                                                      
# First    216.000000  38.233443  14.805684  22.0  27.0  36.0  49.0  80.0
# Second   184.000000  29.877682  13.047279  14.0  23.0  28.0  35.0  70.0
# Third    491.000000  24.082020  14.253794   0.0  16.0  22.0  30.0  74.0
# 
# where it provides stats on age for each class 
# 
# 2. Because these are in groups of people, so the count is for the amount of people in each GROUP, also indicating that the sum of the count values in the column is equal to the total count before executing groupby
# purpose of count in groupby is just to show how many people are in each group 
# 
# 3. a. (see following code) 
# b. (seeing following code)
# c. (seeing following code)
# d. (seeing following code)
# e. (seeing following code)
# f. (seeing following code)
# g. (seeing following code)

# A. 

# In[1]:


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv" 
df = pd.read_csv(url)

df.isna().sum()
rows, columns = df.shape


numeric_summary = df.describe()
non_numeric_summary = df.describe(include= 'object')
print(f"Numeric Columns Summary: \n {numeric_summary} \n")
print(f"Non-Numeric Columns Summary: \n {non_numeric_summary}")


df.head() 
print(f"Rows: {rows} Columns: {columns}")


# B.

# In[3]:


import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanics.csv" 
df = pd.read_csv(url)

df.isna().sum()
rows, columns = df.shape


numeric_summary = df.describe()
non_numeric_summary = df.describe(include= 'object')
print(f"Numeric Columns Summary: \n {numeric_summary} \n")
print(f"Non-Numeric Columns Summary: \n {non_numeric_summary}")


df.head() 
print(f"Rows: {rows} Columns: {columns}")


# C. 

# In[4]:


import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv" 
df = pd.read_csv(url)

df.isna().sum()
rows, columns = df.shape


numeric_summary = df.describe()
non_numeric_summary = DF.describe(include= 'object')
print(f"Numeric Columns Summary: \n {numeric_summary} \n")
print(f"Non-Numeric Columns Summary: \n {non_numeric_summary}")


df.head() 
print(f"Rows: {rows} Columns: {columns}")


# D. 

# In[9]:


import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv" 
df = pd.read_csv(url

df.isna().sum()
rows, columns = df.shape


numeric_summary = df.describe()
non_numeric_summary = df.describe(include= 'object')
print(f"Numeric Columns Summary: \n {numeric_summary} \n")
print(f"Non-Numeric Columns Summary: \n {non_numeric_summary}")


df.head() 
print(f"Rows: {rows} Columns: {columns}")


# E. 

# In[10]:


import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv" 
df = pd.read_csv(url)

df.isna().sum()
rows, columns = df.shape


numeric_summary = df.describe()
non_numeric_summary = df.describe(include= 'object')
print(f"Numeric Columns Summary: \n {numeric_summary} \n")
print(f"Non-Numeric Columns Summary: \n {non_numeric_summary}")


df.group_by("col1")["col2"].describe()
                 
df.head() 
print(f"Rows: {rows} Columns: {columns}")


# F. 

# In[14]:


import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv" 
df = pd.read_csv(url)

df.isna().sum()
rows, columns = df.shape


numeric_summary = df.describe()
non_numeric_summary = df.describe(include= 'object')
print(f"Numeric Columns Summary: \n {numeric_summary} \n")
print(f"Non-Numeric Columns Summary: \n {non_numeric_summary}")


df.groupby("Sex")["age"].describe()
                 
df.head() 
print(f"Rows: {rows} Columns: {columns}")


# G. 

# In[15]:


import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv" 
df = pd.read_csv(url)

df.isna().sum()
rows, columns = df.shape


numeric_summary = df.describe()
non_numeric_summary = df.describe(include= 'object')
print(f"Numeric Columns Summary: \n {numeric_summary} \n")
print(f"Non-Numeric Columns Summary: \n {non_numeric_summary}")


df.groupby(sex)["age"].describe() 

df.head() 
print(f"Rows: {rows} Columns: {columns}")


# 3. a) I think Google is sufficent in providing insight on how to fix the problem as it is a common error, and using common sense, it is easy to understand what you need to do. 
# 
# 3. b) It is easier with ChatGPT as it targets exactly what the problem is in your OWN code, whereas Google Search is broader and requires you to rely on checking other people's errors and how they have fixed them (or input from others on how to fix them on others). This error is a lot more niche, because it is only because causing an error as the file name is wrong, which Google Search would not know. 
# 
# 3. c) ChatGPT is easier as it is a small syntax error SPECIFIC to my own code. Google would not know that this is the error, as variables can be named anything, and would need to see my entire code to determine what the entire problem is. However, Google search is based on key words to search, rather than actually analyzing the problem, so it would difficult to find resources from Google Search that would accomedate me to fix my error
# 
# 3. d) ChatGPT is easier as it takes the exact error and understands where we messed up on judging from our code 
# 
# 3. e) ChatGPT is easier (same reasoning as above)
# 
# 3. f) ChatGPT is easier (same reasoning as above)
# 
# 3. g) ChatGPT is easier (same reasoning as above)
# 
# 
# CONCLUSION: 
# 
# I think ChatGPT is easier for the nicher problems or ones that require to look at the entire code (i.e. wrong variable naming, syntax errors), as ChatGPT can actually thoroughly filter out what we have done correctly and what we have not. It can also easily identify what we need to fix just by seeing the error, as it stores what we have already written/asked for help in our code in its memory, and can also implement how to fix our errors by showing us actual code. In comparsion, I think Google is useful for extremely common errors or asking how to code something, like a importing pandas. However, ChatGPT can also do the same thing, so Google I think is good to rely on more complex problems and ChatGPT would not be able to give a correct answer to, where we can research on sites like StackOverflow, and gain insight on other people's methods of solving similar types of problems that we are encountering. 
# 

# 9. Somewhat 
