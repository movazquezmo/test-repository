from typing import Literal
from bs4 import BeautifulSoup
import requests
import shutil

from urllib.parse import urlparse
from pathlib import Path


MAIN_LINK_1 = 'https://datos.cdmx.gob.mx/dataset/afluencia-diaria-de-metrobus-cdmx'
MAIN_LINK_2 = 'https://datos.cdmx.gob.mx/dataset/inmuebles-catalogados'

# Making a GET request
r = requests.get(MAIN_LINK_2)

soup = BeautifulSoup(r.text, 'html.parser')

# Find all hyperlinks present on webpage
links = soup.find_all('a')
# print(links)
i = 0


def download_data(link_path: str, i: int) -> Literal['Ok']:
    """Downloads data from the given link and saves it to a file.

    Args:
        link_path: The path to the link to download the data from.
        i: The file number.

    Returns:
        A literal string of "Ok".
    """
    download_link = link_path.get('href')
    print(download_link)
    parsed_url = urlparse(download_link)
    path = parsed_url.path
    file_name = Path(path).name
    
    print(f"Downloading file number {i+1}: {download_link}")
    
    # Get response object for link
    response = requests.get(download_link)

    # Write content in pdf file
    with open(f"{file_name}", 'wb') as csv:
        csv.write(response.content)

    print(f"File {i+1}: {file_name} downloaded")
    i += 1
    return "Ok"

# From all links check for pdf link and
# if present download file
for link in links:
    # Uncomment the following line to process 
    # an specific number of files
    if i == 3:
        break
    
    if ('.csv' in link.get('href', [])):
        result = download_data(link_path=link, i=i)
        if result == "Ok":
            print("CSV Downloaded")
        else:
            print("Error in CSV")

    if ('.json' in link.get('href', [])):
        download_data(link_path=link, i=i)
        if result == "Ok":
            print("JSON Downloaded")
        else:
            print("Error in CSV")