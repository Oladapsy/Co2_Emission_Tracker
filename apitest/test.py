#!/usr/bin/python3
""" python to test the co2 api"""
import requests
import json


url = "https://daily-atmosphere-carbon-dioxide-concentration.p.rapidapi.com/api/co2-api"

print("url passed")
headers = {
        "x-rapidapi-host" : "daily-atmosphere-carbon-dioxide-concentration.p.rapidapi.com",
        "x-rapidapi-key" : "62f0ec2bfdmshdb1f8417ca787b3p179058jsn54953359a295"
        }
print("header passed")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print("failed to get response")
