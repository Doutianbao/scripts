import subprocess
import sys

# Check if the required libraries are installed
try:
    import bs4
    import lxml
except ImportError:
    # Install the required libraries using pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4", "lxml"])

import requests
from bs4 import BeautifulSoup

# Get the URL to scrape from user input
url = input("Enter the URL to scrape: ")

# Create a session object
session = requests.Session()

# Make a request to the URL and get the response
response = session.get(url)

# Create a BeautifulSoup object from the response
soup = BeautifulSoup(response.content, "lxml")

# Find all the div elements with the class="table" or "xtable" using CSS selectors
tables = soup.select("div.html-table_show")

# Update the href attribute of all a elements within the tables to include the URL
for table in tables:
    for a in table.select("a"):
        a["href"] = f"{url}{a['href']}"

# Save the tables as an HTML file using a generator expression
with open("tables.html", "w") as f:
    f.write("".join(table.prettify() for table in tables))
