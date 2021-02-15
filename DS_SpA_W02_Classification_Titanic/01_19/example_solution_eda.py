"""
Exploratory data analysis of the titanic data. Challenge of the
"What is Machine Learning?" chapter.
"""
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12,6)

# %%
## Step 1: Read the file train.csv into Python and print a few rows.

df = pd.read_csv('../datasets/train.csv')
df.head()


# %%
## Step 2: Calculate the number of surviving/non-surviving passengers and display it as a bar plot.

## Solution 1
surviving = df['Survived'][df['Survived']==1].count()
non_surviving = df['Survived'][df['Survived']==0].count()

surviving
non_surviving

surviving/(non_surviving+surviving)

## Solution 2
df.groupby('Survived').size().plot(kind='bar')


# %%
## Step 3: Calculate the proportion of surviving 1st class passengers with regards to the total number of 1st class passengers.

## Solution 1
surviving_1 = df['Survived'][(df['Survived']==1) & (df['Pclass']==1)].count()
surviving_1

class_1 = df['Survived'][df['Pclass']==1].count()
class_1

surviving_1/class_1

## Solution 2
# Filter for Pclass == 1, look at column Survived and calculate the mean
df[df['Pclass']==1]['Survived'].mean()


# %%
# Step 4: Create a bar plot with separate bars for male/female passengers and 1st/2nd/3rd class passengers.

df.groupby(['Survived', 'Sex']).size().unstack().plot.bar()
plt.title('Nr. of Passengers who Died/Survived by their Sex')
plt.ylabel('Nr. of Passengers')


df.groupby(['Survived', 'Sex']).size().unstack(0).plot.bar()
plt.title('Nr. of Passengers who Died/Survived by their Sex')
plt.ylabel('Nr. of Passengers')


df.groupby(['Survived', 'Pclass']).size().unstack().plot.bar()
plt.title('Nr. of Passengers who Died/Survived by their Passenger Class')
plt.ylabel('Nr. of Passengers')


df.groupby(['Survived', 'Pclass']).size().unstack(0).plot.bar()
plt.title('Nr. of Passengers who Died/Survived by their Passenger Class')
plt.ylabel('Nr. of Passengers')


df.groupby(['Survived', 'Sex', 'Pclass']).size().unstack(0).plot.bar()
plt.title('Nr. of Passengers who Died/Survived by their Passenger Class')
plt.ylabel('Nr. of Passengers')


# %%

## Step 5: Create a histogram showing the age distribution of passengers. Compare surviving/non-surviving passengers.

df.groupby('Survived')['Age'].hist(alpha=0.5, bins=50)
plt.xticks(list(range(0, 85, 5)))


# %%
## Step 6: Calculate the average age for survived and drowned passengers separately.

df.groupby('Survived')['Age'].mean()


# %%
## Step 7: Replace missing age values by the mean age

df['Age'].fillna(df['Age'].mean(), inplace=True)
df.isna().any()


# %%
## Step 8: Create a table counting the number of surviving/dead passengers separately for 1st/2nd/3rd class and male/female.
df.groupby(['Survived', 'Pclass', 'Sex']).size()
