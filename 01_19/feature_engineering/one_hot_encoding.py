"""

One-Hot Encoding

converts a categorical column to numerical columns

1. Execute the code 
   (in Jupyter, split it into multiple cells)

2. Understand what is happening

   QUESTION: Why do we convert to multiple columns?

3. Apply the procedure to the Titanic data

4. Explain to the rest of the group what you did

"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('penguins_simple.csv', sep=';')


# transform a categorical column
ohc = OneHotEncoder(sparse=False, handle_unknown='ignore')
cols = df[['Species']]
ohc.fit(cols)            # learn the classes
t = ohc.transform(cols)  # result is a numpy array
print(t.shape)
print()

# format output as a DataFame
species = pd.DataFrame(t, columns=ohc.categories_)
print(species.head())
print()


# BONUS: include a second column
cols = df[['Sex']]

ohc2 = OneHotEncoder(sparse=False, handle_unknown='ignore')
ohc2.fit(cols)
t = ohc2.transform(cols)
sex = pd.DataFrame(t, columns=ohc2.categories_)

# merge both DataFrames
df2 = pd.concat([species, sex], axis=1)
print(df2.head())
