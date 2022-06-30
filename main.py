from bs4 import BeautifulSoup
import pandas as pd
import requests

# saves the data from the html as an object in python
html_text = requests.get('https://stats.gfl.info/gfl/2022/confldrs.htm').text
soup = BeautifulSoup(html_text, 'lxml')

# finds the data saved under table headers(th) and table data (td)
stats_html_tags = soup.find_all('th', style="text-align:left;")
stats_html_data = soup.find_all('td', style="text-align:left;")

#simple way of printing the text in the tables. Still very unstructured
for tags in stats_html_tags:
    for data in stats_html_data:
        #print(tags.text)
        #print(data.text)
        pass
# this is an example of a dataframe that I would like to use to structure the data
df = pd.DataFrame(
    stats_html_data,
    columns=[
        "SCORING OFFENSE",
        "Games",
        "Touchdowns",
        "Field Goals",
        "Extra points",
        "2-point conversions",
        "Defensive extra points",
        "Safeties",
        "Points",
        "Average points",
    ],
)
print(df)