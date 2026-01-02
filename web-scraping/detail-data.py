import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from dotenv import load_dotenv
import time
import random
from urllib.parse import urljoin, urlparse, parse_qs	

# loading variables from .env file
load_dotenv() 

# accessing and printing value
os.getenv("MY_KEY")

# URLs
login_url = os.getenv('LOGIN_URL')
index_url = os.getenv('INDEX_URL')

# LAST YEARS
#past_years_url = os.getenv('PAST_YEARS_URL')

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

# Dates
start = "24.11.2025 00:00:00"
end = "30.12.2025 00:00:00"

date_data = {
		# 'SelectedYears': 2024,
		"dateBaslangic": start,
		"dateBitis": end
}

# RESPONSES
# Login Response
login_response = session.post(login_url, data=payload, headers=headers)

# Index Response
index_response = session.post(index_url, headers=headers, data=date_data)

# PastYears Response
# past_years_response = session.post(past_years_url, headers=headers, data=date_data)

# BeautifulSoup
soup = BeautifulSoup(index_response.text, "html.parser")

# Select the table you want:
table = soup.find_all("table")[0]

# Table column titles
table_titles = [th.text.strip() for th in table.find_all("th")]

# Taking table rows:
rows = table.find_all("tr")

# Detaylar linklerini değişkene atama

detay_url_listesi = []
for a_tag in table.find_all("a"):
		href = a_tag.get("href")
		detay_url_listesi.append(href) 



# URL Birleştirme (Relative URL leri tam URL ye çevirme)
base_url = os.getenv('BASE_URL')

full_url = []
for url in detay_url_listesi:
		urls = urljoin(base_url, url)
		full_url.append(urls)
		
# for döngüsü ile full_url içindeki tüm url lere request gönder 
tables_list = []
session.headers.update(headers)

for req in full_url:
		detay_response = session.get(req)
		
		time.sleep(random.uniform(1, 5))
		
		soup2 = BeautifulSoup(detay_response.text, "html.parser")
		table = soup2.find("table")
		if table is None:
			print(f"Tablo bulunamadı: ${req}")
			continue
		
		rows = []
		for tr in table.find_all("tr"):
				cols = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
				rows.append(cols)

		if len(rows) < 2:
			print(f"Boş tablo: {req}")
			continue
				
		header = rows[0]
		data = rows[1:]
	
		df = pd.DataFrame(data, columns=header)
		# Getting data out of URLs
		parsed_url = urlparse(req)
		url_params = parse_qs(parsed_url.query)
		
		# URL'den şube adı, tarih ve sıra no çekme
		sube_adi = url_params.get('sube', [''])[0]
		tarih = url_params.get('tarih', [''])[0]
		sira_no = url_params.get('sira_no', [''])[0]
		
		# URL den gelen bilgileri excel için hazırlama
		df['SubeAdi'] = sube_adi
		df['Tarih'] = tarih
		df['Sira_no'] = sira_no
		tables_list.append(df)


final_df = pd.concat(tables_list, ignore_index = True)
final_df.to_excel("detail_2025_8_8.xlsx", index = False)