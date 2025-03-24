# file converter, could fix if result is not desired later https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv
import pandas as pd
import requests
import base64
import json


def jsonToCSV(json_file_name, output_csv="csvfile.csv"):
    with open(json_file_name, encoding='utf-8') as inputfile:
        df = pd.read_json(inputfile)

    df.to_csv(output_csv, encoding='utf-8', index=False)


# https://stackoverflow.com/questions/19697846/how-to-convert-csv-file-to-multiline-json
def csvToJson(csv_file_name, output_csv="jsonfile.json"):
    csv_file = pd.DataFrame(pd.read_csv(csv_file_name, sep=",", header=0, index_col=False))
    csv_file.to_json(output_csv)





# setting up api call, need access token first
# these are normally valid for 1 hr so u guys can make ur own app and just paste these info here to generate more token
client_id = 'eae2627823e2419890fa69ae50deec74'  # this is jackson's info plz dont do bad thing
client_secret = '8f884de0f9d04452a3116fcdbceb8074'

url = "https://api.spotify.com/v1/"


# kinda mimiced this
# https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow
def get_api_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

    url_token = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {auth_base64}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(url_token, headers=headers, data=data)

    if response.status_code == 200:
        token_info = response.json()
        access_token = token_info['access_token']
        print(f"Access Token: {access_token}")
        return access_token
    else:
        print("lol smt went wrong")
        return None


    # test_token = get_api_token() #run this every 1 hr to get ur token lol

# token = "BQDwvqfuTrtCVgWH7BmIqdvCLB5PKt6vEGCIaTnAHJU4L_KAdgEqlwiRJpbDUmPTeQp6Jfj6p5oOrVmJ3L1figg6DUXqIU7cDAZi1Jz7Pu_nH9FL6D0FWZsoSESzbdUmRHs_1W9tlEA"


def getSongInfo(merged_csv, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    df = pd.read_csv(merged_csv)
    templist = []

    for index, row in df.iterrows():
        song_name = row['Song']
        query = song_name.replace(" ", "%20")

        search_url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
        response = requests.get(search_url, headers=headers)

        if response.status_code == 200:
            result = response.json()
            items = result['tracks']['items']

            if items:
                track = items[0]
                info = {
                    'Song': song_name,
                    'Duration_ms': track['duration_ms'],
                    'Explicit': track['explicit'],
                    'Popularity': track['popularity']
                }
                templist.append(info)
            else:
                print(f"No search results for: {song_name}")
                # error handle just add none if we can't find
                info = {
                    'Song': song_name,
                    'Duration_ms': None,
                    'Explicit': None,
                    'Popularity': None
                }
                templist.append(info)
        else: #handles api erorr
            print(f"api didn't work for dis {song_name} - status code is {response.status_code}")
            continue
    print(templist)
    tempdf = pd.DataFrame(templist)

    merged_df = pd.merge(df, tempdf, on='Song', how="left")

    merged_df.to_csv("Api_kaggle_final.csv", index=False, encoding='utf-8')


# getSongInfo("hot100_grammys_merged.csv", "BQDfwVpWF3dMZmCx_YOGD9imbhTI5syNYI2hQnFpnRd8QTQPjlFidYzkZAiWHe_M9S7SOsDFh28AoPwXGv1z2CqucFahP2mXkuWKcln41MC6zOck8pv9rl1bd7YJY9TW86k17lJmirw")

def add_column_and_value(csv, column_name, artist, value):
    df = pd.read_csv(csv)
    if column_name not in df.columns:
        df[column_name] = None  # Add column with empty values
    # Update value for the given track_id
    if artist in df['Artist'].values:
        df.loc[df['Artist'] == artist, column_name] = value
        print(f"Updated '{column_name}' for artist {artist} with value '{value}'")
    else:
        print(f"{artist} not found.")
    df.to_csv("updated_modify.csv", index=False)

def update_column_value(csv, column_name, artist, new_value):
    df = pd.read_csv(csv)
    if column_name in df.columns:
        if artist in df['Artist'].values:
            df.loc[df['Artist'] == artist, column_name] = new_value
            print(f"Modified '{column_name}' for artist {artist} to '{new_value}'")
        else:
            print(f"{artist} does not exist.")
    else:
        print(f"Column '{column_name}' does not exist.")
    df.to_csv("updated_modify.csv", index=False)

add_column_and_value('Api_kaggle_final.csv','handsomeness', 'Kendrick Lamar', 10)
update_column_value('updated_modify.csv', 'handsomeness', 'Eminem', 8)
