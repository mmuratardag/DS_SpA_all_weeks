#
# Solution
#
import pandas as pd

fn = '/home/kristian/Desktop/data/gapminder/gapminder_total_fertility.csv'

# 1. Read a data file
df = pd.read_csv(fn, index_col=0)

# 2. Inspect the size of a DataFrame
df.shape

# 3. Convert column labels to integers
df.set_axis(df.columns.astype(int), axis=1, inplace=True)

# 4. Remove rows with missing values
df.dropna(inplace=True)

# 5. Inspect a single value
df.loc['Germany', '2000']

# 6. Calculate the mean of a column
df['2000'].mean()

# 7. Find values in given range
df[df[2000].between(6.0, 6.5)][2000]

# 8. Mean fertility over time
df.mean().plot()

# 9. Three countries over time
df.loc[['Germany', 'Sweden', 'Kenya']].transpose().plot()

# 10. Countries with most frequent initials
df.reset_index()['Total fertility rate'].str[0].value_counts().head(5).plot.bar()
