import requests 
import pandas as pd
import openpyxl
from openpyxl import load_workbook

base_url = "https://api.hooktheory.com/v1/"
headers = {"Accept": "application/json", # Headers for Json formatting
        "Content-Type": "application/json",
        "Authorization": "Bearer 47b8ab479a54cf82dd65c3d27d6395db"}

credentials = {
    "username": "Kobbu",
	"password": "_WUym4nQn!CEu6V"
}

token = "47b8ab479a54cf82dd65c3d27d6395db" #Access token
cp = '1,5,4,b7,1'    #Child Parameter to choose which cord combination the song results will belong to
page = "1"        #Dictates the page of the results as there are only 20 results per page

def token_request():
    url = f"{base_url}users/auth"
    response = requests.post(url, json=credentials, headers=headers) #Send the credentials for authentication

    if response.status_code == 200:
        temp_token = response.json().get("activkey") #Requesting the activation key
        print(f"authentication successful! Token:{temp_token}")
        return(temp_token)
    else:
        print(f"Failed to authenticate:{response.status_code}")
    
#Gives back the songs with the specific chord progression given
def song_progressions(parameter,page):  #Gives back the songs with the specific chord progression given
    url = f"{base_url}trends/songs?cp={parameter}&page={page}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        songs = response.json()
        print(f"Songs retrieved successfully\n {songs}")
        return(songs)
    else:
        print(f"Failed to retrieve songs{response.status_code}")

#Convert the data from a dictionary to a panda dataframe to then convert it to an excel file.
def excel_file(dataframe):
    song_list = pd.DataFrame(dataframe)
    song_list.to_excel("Songs_list.xlsx",index=False)
    print("Your data was saved in an excel file successfully")

#Adds data to an already existing excel file in the same sheet.
def append_to_existing_file(dataframe,file_name,sheet_name):
    song_list = pd.DataFrame(dataframe)
    book = load_workbook(file_name)
    existing_data = pd.read_excel(file_name,sheet_name=sheet_name)
    combined_data = pd.concat([existing_data,song_list])
    with pd.ExcelWriter(file_name, engine="openpyxl",mode="a",if_sheet_exists="replace") as writer:
        combined_data.to_excel(writer, sheet_name = sheet_name, index = False)
    print("Data updated successfully!")

#Used it to find the child_path of some specific chords.
def next_chord(parameter):
    url = f"{base_url}trends/nodes?cp={parameter}"
    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        result = response.json()
        print(f"Results retrieved successfully {result}")
    else:
        print(f"Failed to retrieve results! {response.status_code}")


songs = song_progressions(cp,page)
append_to_existing_file(songs,"Songs_list.xlsx","Songs")
