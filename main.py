from bs4 import BeautifulSoup
import pandas as pd
import requests


html_text = requests.get('https://stats.gfl.info/gfl/2022/confldrs.htm').text
soup = BeautifulSoup(html_text, 'lxml')

stats_html_tags = soup.find_all('th', style="text-align:left;")
stats_html_data = soup.find_all('td', style="text-align:left;")

for tags in stats_html_tags:
    for data in stats_html_data:
        #print(tags.text)
        #print(data.text)
        pass

df = pd.DataFrame(
    stats_html_data,
    columns=[
        "Rank",
        "Grade",
        "Username",
        "Uploads",
        "Followers",
        "Following",
        "Likes",
        "Interactions",
    ],
)
print(df)