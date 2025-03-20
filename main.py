# getting data




#setting up api call, need access token first
import requests
import base64

#these are normally valid for 1 hr so u guys can make ur own app and just paste these info here to generate more token
client_id = 'eae2627823e2419890fa69ae50deec74' #this is jackson's info plz dont do bad thing
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

token = "BQBJ4ejUWPTP4iJDpbALxoiivXil99DVmSUWdwmM9MeJbHN91G4FPfcjT6kK67Fe3nS_t7RFn9gaUnbYYu87USG05VGF802loSJgvXKBfv787Q5dS03j6ybvB5-_dV1S1FuMJEemyxs"


