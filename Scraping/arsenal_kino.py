import requests
import os
import json

""" Test script to check how to scrape the film material"""

r = requests.get("https://www.arsenal-berlin.de/api/v1/search/calendar/")

# Save the response data to a file
file_path = "calendar.json"
with open(file_path, 'w') as calendar_file:
    calendar_file.write(r.text)

# Load the JSON data from the file
with open(file_path, 'r') as f:
    data = json.load(f)

# Navigate through the nested JSON structure to get the 'documents' data
try:
    documents = data['content']['colPos'][0]['content']['data']['documents']
except KeyError as e:
    print(f"KeyError: {e}")
    documents = None

# If documents are found, process the movies
if documents:
    movies = []
    for result in documents['list']['results']:
        movie = {
            'id': result['id'],
            'date': result['dateText'],
            'title': result['title'],
            'subtitle': result['subtitle'],
            'director': result.get('director'),
            'country': result.get('country'),
            'year': result.get('year'),
            'film_format': result.get('filmFormat'),
            'playing_time': result.get('playingTime'),
            'location': result.get('location')
        }
        movies.append(movie)

    # Display the movies data
    for movie in movies:
        print(movie)
else:
    print("No documents found in the JSON response.")

