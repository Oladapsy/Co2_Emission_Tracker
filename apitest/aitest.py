#!/usr/bin/python3
""" python to test the co2 api"""
import requests
import json

# Define the specific date you want to filter
target_date = {
    "year": "2024",
    "month": "8",
    "day": "16"
}

url = "https://daily-atmosphere-carbon-dioxide-concentration.p.rapidapi.com/api/co2-api"

headers = {
    "x-rapidapi-host": "daily-atmosphere-carbon-dioxide-concentration.p.rapidapi.com",
    "x-rapidapi-key": "62f0ec2bfdmshdb1f8417ca787b3p179058jsn54953359a295"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Filter the data for the specific date
    filtered_data = [
        entry for entry in data['co2']
        if entry['year'] == target_date['year'] and
           entry['month'] == target_date['month'] and
           entry['day'] == target_date['day']
    ]
    
    if filtered_data:
        print(json.dumps(filtered_data, indent=4))
    else:
        print(f"No data found for the date: {target_date['year']}-{target_date['month']}-{target_date['day']}")
else:
    print("Failed to get response")
