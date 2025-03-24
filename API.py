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


# test_token = get_api_token() #run this every 1 hr to get ur token lol

token = "BQDwvqfuTrtCVgWH7BmIqdvCLB5PKt6vEGCIaTnAHJU4L_KAdgEqlwiRJpbDUmPTeQp6Jfj6p5oOrVmJ3L1figg6DUXqIU7cDAZi1Jz7Pu_nH9FL6D0FWZsoSESzbdUmRHs_1W9tlEA"


def getSongInfo(merged_csv, token):
    url = "https://api.spotify.com/v1/search"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    df = pd.read_csv(merged_csv)

    for index, row in df.iterrows():
        song_name = row['Song']
        query = song_name.replace(" ", "%20")

        search_url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
        response = requests.get(search_url, headers=headers)

        if response.status_code == 200:
            print(response.json())

getSongInfo("hot100_grammys_merged.csv", token)
