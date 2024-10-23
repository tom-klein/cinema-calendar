import requests
import os
from bs4 import BeautifulSoup

r = requests.get("https://www.indiekino.de/kinoprogramm/en/berlin/")
file_path = "calendar.html"

with open(file_path, 'w') as calendar_file:
    calendar_file.write(r.text)

with open('calendar.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')


# Functionality: Boolean to filter cinemas. Then iterate through True cinemas.
# Structure is Date -> Cinema -> Film

