import requests

APP_ID = 'b5db85a0'
APP_KEY = 'd8d73229c36b6cdf5cb8ca55fa31d7bf'

GENDER = 'female'
WEIGHT_KG = 55
HEIGHT_CM = 165
AGE = 25
exercise_input = input("What exercise did you do today? ")

end_point = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}
parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=end_point, headers=headers, json=parameters)
result = response.json()
print(result)