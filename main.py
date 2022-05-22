import requests
import datetime as dt

APP_ID = 'b5db85a0'
APP_KEY = 'd8d73229c36b6cdf5cb8ca55fa31d7bf'

GENDER = 'female'
WEIGHT_KG = 55
HEIGHT_CM = 165
AGE = 25
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

sheety_end_point = 'https://api.sheety.co/f266fc6da30b4c5d27abf38dbec08fea/myWorkout/workouts'
headers = {'Authorization': 'Basic cGVhcmwxNzg6MTE3ODc4VGlhbg=='}
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

    fill_form = requests.post(url=sheety_end_point, headers=headers, json=sheety_parameters)
