import pandas as pd

input_file = 'originalHot100.csv'
df = pd.read_csv(input_file)

print("Initial Data Overview:")
print(df.info())
print("\nFirst few rows:")
print(df.head())

# convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# only include the range of Sept 2023 til Aug 2024 [grammy eligibility window]
start_date = pd.to_datetime('2023-09-01')
end_date = pd.to_datetime('2024-08-31')

# remove all other rows
df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# drop irrelevant columns
df = df.drop(columns=['Image URL', 'Last Week', 'Rank'])

print("Post Cleaning Overview:")
print(df.info())
print("\nFirst few rows:")
print(df.head())

# export the df to a new csv file
df.to_csv('hot100.csv', index=False)

grammys_df = pd.read_csv('originalGrammys2025.csv')

# drop "Entry_ID" and "Category_ID"
grammys_df = grammys_df.drop(columns=['Entry_ID', 'Category_ID'])

# rename "Work" to "Song"
grammys_df = grammys_df.rename(columns={'Work': 'Song'})

# drop rows that aren't songs or albums
grammys_df = grammys_df.dropna(subset=['Song'])
grammys_df = grammys_df[grammys_df['Song'].str.strip() != '']

# drop rows that aren't songs
keywords = ['Song', 'Record', 'Performance', 'Recording']
grammys_df = grammys_df[grammys_df['Category'].str.contains('|'.join(keywords), case=False, na=False)]

print("\nGrammys Data Overview:")
print(grammys_df.info())
print("\nFirst few rows:")
print(grammys_df.head())

grammys_df.to_csv('grammys2025.csv', index=False)
