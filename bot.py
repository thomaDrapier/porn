from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import csv
from io import StringIO



def print_delay(text, delay):

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay) 

def get_informations(parsed_html):
    csv_data = StringIO(parsed_html)
    fieldnames = ["ID", "Title", "Description", "Publish date, time", "Channel", "Website link", "Categories", "Models", "Duration", "Embed code", "Main thumbnail", "Preview URL"]
    reader = csv.DictReader(csv_data, delimiter='|', fieldnames=fieldnames)
    for row in reader:
        id = row['ID']
        title = row['Title']
        description = row['Description']
        publish_datetime = row['Publish date, time']
        channel = row['Channel']
        website_link = row['Website link']
        categories = row['Categories']
        models = row['Models']
        duration = row['Duration']
        embed_code = row['Embed code']
        main_thumbnail = row['Main thumbnail']
        preview_url = row['Preview URL']
        print_delay(f"ID: {id}", 0.005)
        print_delay(f"Title: {title}",0.005)
        print_delay(f"Description: {description}",0.005)
        print_delay(f"Publish date, time: {publish_datetime}",0.005)
        print_delay(f"Channel: {channel}",0.005)
        print_delay(f"Website link: {website_link}",0.005)
        print_delay(f"Categories: {categories}",0.005)
        print_delay(f"Models: {models}",0.005)
        print_delay(f"Duration: {duration}",0.005)
        print_delay(f"Embed code: {embed_code}",0.005)
        print_delay(f"Main thumbnail: {main_thumbnail}",0.005)
        print_delay(f"Preview URL: {preview_url}",0.005)
        print("-" * 50)

    csv_data.close()

def get():
    url = "https://hclips.com/admin/feeds/embed/?source=1229318837&feed_format=csv&screenshot_format=240x180&limit=1000&csv_separator=%7C"
    response = urlopen(url)
    if response.getcode() == 200:
        soup = BeautifulSoup(response.read(), 'html.parser')
        get_informations(soup.get_text())

    else:
        print("La requête GET a échoué.")







get()