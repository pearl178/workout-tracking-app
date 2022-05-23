import requests
import datetime as dt
import os

APP_ID # nutritionix api
APP_KEY # nutritionix api
SHEETY_END_POINT #sheeting api endpoint
AUTH #sheeting api authentication

GENDER 
WEIGHT_KG
HEIGHT_CM
AGE
exercise_input = input("What exercise did you do today? ")

app_end_point = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}
app_parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=app_end_point, headers=headers, json=app_parameters)
result = response.json()

headers = {'Authorization': AUTH}
for item in result['exercises']:
    sheety_parameters = {
        'workout': {
            'date': dt.datetime.now().strftime('%d/%m/%Y'),
            'time': dt.datetime.now().strftime('%X'),
            'exercise': item['name'].title(),
            'duration': item['duration_min'],
            'calories': item['nf_calories']
        }
    }

    fill_form = requests.post(url=SHEETY_END_POINT, headers=headers, json=sheety_parameters)
