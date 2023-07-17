# Usado com API

# importing the libraries
import requests
import json

# Link containing the api
api_link = "https://dicio-api-ten.vercel.app/v2/comer"

# requests
r = requests.get(api_link)

# Converting Request Data to Dictionary
dados = r.json()

print(dados)
