# Import library
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from dotenv import load_dotenv
import random
import time

# loading variables from .env file
load_dotenv() 

# accessing and printing value
os.getenv("MY_KEY")

# URLs
login_url = os.getenv('LOGIN_URL')
index_url = os.getenv('INDEX_URL')

# LAST YEARS
# past_years_url = os.getenv('PAST_YEARS_URL')

# DETAIL 
# detail_url = os.getenv('DETAIL_URL')

# Login informations
user = os.getenv('USER')
password = os.getenv('PASSWORD')

payload = {
		'User': user,
		'Password': password
}

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,tr;q=0.8",
}

# Session
session = requests.Session()

time.sleep(random.uniform(10, 20))

# years = ['2019', '2020', '2021', '2022', '2023', '2024', '2025']

# Dates
start = "1.01.2025 00:00:00"
end = "31.12.2025 00:00:00"

date_data = {
    # SelectedYears for past years
    # 'SelectedYears': 2024,
		"dateBaslangic": start,
		"dateBitis": end
}

# RESPONSES
# Login Response
login_response = session.post(login_url, data=payload, headers=headers)

# Index Response
index_response = session.post(index_url, headers=headers)

# Past Years Response
# past_years_response = session.post(past_years_url, headers=headers, data=date_data)

# Detail
# detail_response = session.post(detail_url, headers=headers, data=date_data)

# BeautifulSoup
soup = BeautifulSoup(index_response.text, "html.parser")

# Past years
#soup = BeautifulSoup(past_years_response.text, "html.parser")

# Details
# soup = BeautifulSoup(detail_response.text, "html.parser")
 
# Select the first table on the page:
table = soup.find_all("table")[0]

# Table column titles
table_titles = [th.text.strip() for th in table.find_all("th")]

# Taking table rows:
rows = table.find_all("tr")

# Create an array and write the data into it
all_data = []
for tr in rows:
		cols = [c.get_text(strip=True) for c in tr.find_all("td")]
		if len(cols) > 0:
			all_data.append(cols)
		

# Print to Excel:
df = pd.DataFrame(all_data, columns=table_titles)
df.to_excel("data_2025.xlsx", index=False)