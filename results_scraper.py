import requests
from bs4 import BeautifulSoup

# URL
race_result_url = "https://ebet.tab.co.nz/results/NSWC-reslt03271700.html"

# Query the website and retrive the page variable
r = requests.get(race_result_url)
print('Status code: ' + str(r.status_code))

# Create soup from result content
content = r.content
soup = BeautifulSoup(content, 'html5lib')

# Get the event name
event_element = soup.find('div', class_='infoPanelBar navbar').find('strong')
event_name = event_element.contents[0].strip()

print('Event name: ' + event_name)

# Take the race containers from the soup
# - This collection of elements contains info
#   about the races at this event.
race_containers = soup.find_all('div', class_='content')

for race_container in race_containers:
    print('found one')
