# Music Data ETL Processor

Project by Jackson Le, Joanne Lee, Kenny Nguyen.

---

## Project Overview

This project processes, cleans, enriches, and merges Grammy nominees/winners, Billboard Hot 100 songs, and Spotify metadata to analyze songs with both commercial and critical success.

---

## Important Files

- `Cleaning.py`: Cleans both Kaggle datasets.
- `Hot100andGrammysMerging.py`: Merges both Kaggle datasets.
- `Main.py`: Enriches dataset, allows modifications.
- `API.py`: Handles Spotify API calls & column functions.
- `project_dss.ipynb`: Contains SQLite database setup & data analysis & visualizations.
- `hot100_grammys_merged.csv`: Cleaned and merged dataset containing the two from Kaggle.
- `api_kaggle_final.csv`: Final dataset containing all three sources.

---

## How to Use

1. **Data Wrangling:**  
   Run `Cleaning.py` to clean both the Grammy & Hot100 datasets. Then run `Hot100andGrammysMerging.py`, this will output `hot100_grammys_merged.csv`.

2. **Enrichment:**  
   Run `main.py` to enrich the merged dataset with Spotify API song data, apply any column modifications, and handle CSV/JSON conversions. The final output is `api_kaggle_final.csv`.

3. **Database Insertion & Analysis:**  
   Open `project_dss.ipynb` to load the cleaned datasets into an SQLite database and perform further analysis and visualization.

---

## ETL Processor (main.py) Explanation

The `main.py` file serves as the core of the ETL processor. Here's how to use it:

1. **Spotify API Integration:**  
   Running `main.py` will fetch audio features from Spotify based on the songs in `hot100_grammys_merged.csv`.

2. **Data Modification:**  
   You can also modify the dataset by adding new columns and values, updating existing values or deleting columns.

3. **Format Conversion:**  
   You can also convert the dataset between CSV and JSON, depending on your desired format.

4. **Final Output:**  
   The final dataset is then saved as `Api_kaggle_final.csv`, ready for analysis or to be inserted into a database.

--- 

## Jupyter Notebook Explanation
The `project_dss.ipynb` contains the SQLite database of the final dataset.

1. **Creating Table & Reading CSV:**
   The SQLite Database has a table called Songs that holds information such as song (name), artist, peak position, week in charts, category,    winner, duration in milliseconds, explicit, and popularity. The data that is inserted into this database is the final dataset `Api_kaggle_final.csv`.
   
2. **Summary Ingested Data:**
   You can get the summary of the ingested data which gives you the number of records and columns.
   
3. **Summary Transformed Data:**
   You can get the summary of the transformed data by removing duplicates and getting the number of records and columns after deduplication.
---

## Conclusions from Data Visualization and Analysis
The `project_dss.ipynb` file serves as the SQLite database and visualization:

1. **Basic Analysis:**  
   You can see the first 5 rows of the dataset, we can see that the first 5 rows were mostly not Grammy winners. You can see the number of songs by category and here we can see that most of the songs were Record of the Year. You can see the average popularity by category. Here we can see that Best Pop Duo/Group Performance was the most popular.

2. **Number of Charting Songs in each Grammy Category:**  
   You can see that most of the charting songs were in the Record of the Year category. 

3. **Average Weeks on Charts: Grammy Winners vs Non-Winners:**  
   You can see that there is not much discrepency between the Grammy Winners and Non-Winners on the average weeks their songs were on charts.

4. **Weeks on Chart Distribution (Grammy Winners vs. Non-Winners):**  
   You can see that Grammy Non-Winners had roughly 2 songs that had ~27 weeks on chart which was the highest. Overall, Grammy Non-Winners had more songs on charts than Grammy Winners.

5. **Conclusion:**
   With the initial data exploration and analysis we’ve performed, there is no immediate strong relationship between the critical success       and commercial success as seen in the average weeks on charts graph where Grammy Winners and Non-Winners are approximately equal.            However, Grammy-Winning songs have a more distinct separation of distribution in the number of weeks they charted with many being less       than 5 or greater than 15. On the other hand, Grammy Non-Winners have more distribution throughout all the weeks.
   Realistically, the Grammy categories that would directly relate to the Hot 100 charts would be genres that have been historically popular    such as rap, pop, and country. 
