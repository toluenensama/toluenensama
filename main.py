import requests
import datetime as dt
from dotenv import find_dotenv,load_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
print(dotenv_path)
pixel_api = "https://pixe.la/v1/users"
today = dt.datetime.today()


USERNAME =os.getenv("USER_NAME")
TOKEN = os.getenv("TOKEN")
print(USERNAME,TOKEN)
today_date = today.strftime("%Y%m%d")
PARAMS = {"token": TOKEN, 
          "username": USERNAME, 
          "agreeTermsOfService":"yes", 
          "notMinor":"yes"}


headers ={
    "X-USER-TOKEN":TOKEN
}

graph_parameters = {
    "id": "graph1",
    "name": "Coding practice",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",

}

pixel_config = {
    "date" : today_date,
    "quantity" : str(input("How many hours did you code today? ")),
}

pixel = f"{pixel_api}/{USERNAME}/graphs/{graph_parameters['id']}"
update_pixel = f"{pixel_api}/{USERNAME}/graphs/{graph_parameters['id']}/{today_date}"

graph_pixel = f"{pixel_api}/{USERNAME}/graphs"

response = requests.post(url=pixel, json= pixel_config,headers=headers)
print(response.text)