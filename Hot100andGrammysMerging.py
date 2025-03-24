import pandas as pd

hot100_df = pd.read_csv('hot100.csv')
grammys_df = pd.read_csv('grammys2025.csv')

merged_df = pd.merge(hot100_df[['Song', 'Artist', 'Peak Position', 'Weeks in Charts']],
                     grammys_df[['Song', 'Artist', 'Category', 'Winner']],
                     on=['Song', 'Artist'],
                     how='inner')

# Keep only the relevant columns
final_df = merged_df[['Song', 'Artist', 'Peak Position', 'Weeks in Charts', 'Category', 'Winner']]

# Export the merged data
final_df.to_csv('hot100_grammys_merged.csv', index=False)
print("\nMerged data exported to 'hot100_grammys_merged.csv'")