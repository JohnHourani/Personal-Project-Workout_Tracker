import requests
from datetime import datetime
import os


#  Environment Variables
APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

#  Global Variables
AGE = 23
GENDER = "male"
WEIGHT_KG = 77
HEIGHT_CM = 176

DATE = str(datetime.now().strftime("%x"))
TIME = str(datetime.now().strftime("%X"))

#  Nutritionix natural language API

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}
parameters = {
    "query": input("Tell me what exercise you did today:"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)

#  Creating list of dictionaries of the new exercises added
new_exercises = []
for exercises in response.json()["exercises"]:
    name = (exercises["name"])
    duration = (exercises["duration_min"])
    cals = (exercises["nf_calories"])
    new_data = {"date": DATE, "time": TIME, "exercise": name, "duration": duration, "calories": cals}
    new_exercises.append(new_data)

    
#  Usinging Sheety API to connect to a premade Google sheets template. 
#  See Readme file for steps in setting up sheet template
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

#  Creating new row in spreadsheet for each workout entered
for workout in new_exercises:
    new_workout = {"workout":
                   workout
                   }
    request = requests.post(url=SHEET_ENDPOINT, json=new_workout, headers=headers)







