# we are using 3 main source of data
#grammys2025 csv
#originalhot100 csv
#spotify api

'''cleaning was done in Cleaning.py, you can take a look at that file for the result of hot100_grammys_merged.csv'''
from API import jsonToCSV, csvToJson, get_api_token, getSongInfo, add_column_and_value, update_column_value, delete_column

#SQL database stuff is in project_dss.ipynb
#figures helps with our report


#all the values is merged into api_kaggle_final.csv

# get songs that matches grammys and hot100 songs and add their info, then combine it into a file.
getSongInfo("hot100_grammys_merged.csv", get_api_token())

#user can choose to delete or add column or modify colum
# it takes in file, column name, key (just matches the song title), and then change value or input a value
add_column_and_value('Api_kaggle_final.csv','handsomeness', 'Kendrick Lamar', 10) # output into updated_modify_after_added.csv
update_column_value('updated_modify_after_added.csv', 'handsomeness', 'Eminem', 8) # modify_update_value.csv
# this one just finds what column you want to delete
delete_column('modify_update_value.csv', 'handsomeness') # modify_delete.csv"

#user can choose if they wanna convert their file
#input is file to change, and file output, there is a default
csvToJson("modify_delete.csv", "outputjson_after_conversion.json")
jsonToCSV("outputjson_after_conversion.json", "json_but_back_to_csv")