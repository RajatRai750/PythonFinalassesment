import requests
import csv
from bs4 import BeautifulSoup as bs

url = requests.get("https://reqres.in/api/users?page=1")
soup = bs(url.content, 'html.parser')

filename = "Datapage.csv"
csv_writer = csv.writer(open(filename, 'w'))


for tr in soup.find_all("tr"):
    data = []
    # for headers ( entered only once - the first time - )
    for th in tr.find_all("th"):
        data.append(th.text)
    if data:
        print("Inserting headers : {}".format(','.join(data)))
        csv_writer.writerow(data)
        continue

    for td in tr.find_all("td"):
        if td.a:
            data.append(td.a.text.strip())
        else:
            data.append(td.text.strip())
    if data:
        print("Inserting data: {}".format(','.join(data)))
        csv_writer.writerow(data)