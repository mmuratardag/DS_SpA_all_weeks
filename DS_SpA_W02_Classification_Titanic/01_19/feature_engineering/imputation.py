"""

Imputation

fill missing values

1. Execute the code 
   (in Jupyter, split it into multiple cells)

2. Understand what is happening
   QUESTION: What are pros/cons of the two approaches?

3. Apply the procedure to the Titanic data
   (the Age column in particular)

4. Explain to the rest of the group what you did
"""

import pandas as pd
import numpy as np

df = pd.read_csv('penguins_simple.csv', sep=';')
df = df[['Species', 'Culmen Depth (mm)']]

# introduce 150 artificial NaNs in random positions
# (don't do this for the Titanic data!)
ids = df.sample(150, random_state=42).index
df.loc[ids, 'Culmen Depth (mm)'] = np.NaN


# Approach 1. fill by median
median = df['Culmen Depth (mm)'].median()
print(median)
print()
df['fill_1'] = df['Culmen Depth (mm)'].fillna(median)


# Approach 2. fill by median for each species
print(df.groupby('Species')['Culmen Depth (mm)'].mean().round(1)) # for illustration only
print()

medians = df.groupby('Species')['Culmen Depth (mm)'].transform('median') # <-- 'mean', 'sum' or custom function work as well
df['fill_2'] = df['Culmen Depth (mm)'].fillna(medians) # <-- requires index to be the same
print(df)


