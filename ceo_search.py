import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_chief_executive_officers"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

# Creating list with all tables
tables = soup.find_all('table')

#  Looking for the table with the classes 'wikitable' and 'sortable'
table = soup.find('table', class_='wikitable sortable')

# Defining of the dataframe
df = pd.DataFrame(columns=['Company', 'Executive'])

# Collecting Ddata
for row in table.tbody.find_all('tr'):
    # Find all data for each column
    columns = row.find_all('td')
    
    if(columns != []):
        company = columns[0].text.strip()
        executive = columns[1].text.strip()

        df = pd.concat([df, pd.DataFrame([{'Company': company,  'Executive': executive}])], ignore_index=True)

df.head()

df_pandas = pd.read_html(url, attrs = {'class': 'wikitable sortable'},  flavor='bs4', thousands ='.')

company_name = input("Company Name: ").title()

print(df.loc[df['Company'] == company_name].values[0][1])