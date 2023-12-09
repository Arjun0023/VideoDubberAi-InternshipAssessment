
import requests
from bs4 import BeautifulSoup

url = 'https://theresanaiforthat.com/saved/'
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

results = s.find(id='li_right')
job_title = results.find_all('h2', class_='ai_link new_tab')

for job in job_title:
    print(job.text)
