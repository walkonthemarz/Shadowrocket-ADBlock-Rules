import zipfile
import requests
import os
import csv


url = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
r = requests.get(url)
temp_dir = 'temp/'

with open(temp_dir + "file.zip", "wb") as f:
    f.write(r.content)

zip_ref = zipfile.ZipFile(temp_dir + "file.zip", 'r')
zip_ref.extractall(temp_dir)
zip_ref.close()

csv_file = temp_dir + os.path.splitext(url.split('/')[-1])[0]

#print(csv.list_dialects())
i = 0
for row in csv.reader(open(csv_file, 'r'), delimiter = ',', quoting=csv.QUOTE_MINIMAL):
    domain = row[1]
    print(domain)
    i+=1
    if i > 1000:
        break
