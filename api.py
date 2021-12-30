from bs4 import BeautifulSoup
import requests
 
username = "kothawleprem"
 
github_html = requests.get(f'https://github.com/{username}').text
soup = BeautifulSoup(github_html, "html.parser")
print(soup)