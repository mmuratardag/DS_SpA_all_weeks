"""

Interaction Terms

combine features to get new ones

1. Execute the code 
   (in Jupyter, split it into multiple cells)

2. Understand what is happening
   QUESTIONS:
   - If you multiply two columns that are 0 or 1,
     what logical operation is this?
   - Why do interaction terms make the model better?
   - Does it make sense to combine every feature with every other?

3. Apply the procedure to the Titanic data
   (if you have time, combine multiple features)

4. Explain to the rest of the group what you did
"""

import pandas as pd


df = pd.read_csv('penguins_simple.csv', sep=';')


# male and adelie
male = (df['Sex'] == 'MALE').astype(int)
ade = (df['Species'] == 'Adelie').astype(int)

df['male_ade'] = male * ade


# culmen area
df['culmen_area'] = df['Culmen Length (mm)'] * df['Culmen Depth (mm)']

print(df.head())
