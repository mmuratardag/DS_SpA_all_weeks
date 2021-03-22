
import pandas as pd
df = pd.read_csv('df.csv', na_values=[' '])
df['title_only'] = df['title'].replace('\(.*', '', regex = True)
new_df = df[['title_only']]
new_df.to_csv('movie_titles_df.csv', index=False)

