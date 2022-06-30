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
headings = []
# i think a 2d array might work here to sort the text into lists determined by stat catagory
for tags in stats_html_tags:
    if tags.text in headings:
        pass
    else:
        headings.append(tags.text)
        data1 = tags.text
        data2 = []
        for data in stats_html_data:

            # this line is currently broken
            x = soup.find_all('td', style="text-align:left;", text=True).text
            if x in data2:
                pass
            else:
                data2.append(x)
        print(data2)
        #print(tags.text)
        #print(data.text)
"""
df = pd.DataFrame(
    data in stats_html_data,
    columns=headings,
)
print(df)
"""



# this is an example of a dataframe that I would like to use to structure the data (not working)

"""
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
"""