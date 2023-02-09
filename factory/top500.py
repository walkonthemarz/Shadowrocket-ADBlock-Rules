# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import threading
import time
import sys
import requests
import os
import shutil
import zipfile
import csv

THREAD_LIMIT = 1024

url = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
temp_dir = 'temp/'
domains = []

domains_proxy = []
domains_direct = []


# Get top sites from URL
class GetSites():
    def __init__(self):
        self.run()

    def run(self):
        global url,temp_dir,domains

        r = requests.get(url)

        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)

        zip_filename = 'top1m.zip'

        with open(temp_dir + zip_filename, "wb") as f:
            f.write(r.content)

        zip_ref = zipfile.ZipFile(temp_dir + zip_filename, 'r')
        zip_ref.extractall(temp_dir)
        zip_ref.close()

        csv_file = temp_dir + os.path.splitext(url.split('/')[-1])[0]

        i = 0
        for row in csv.reader(open(csv_file, 'r'), delimiter = ',', quoting=csv.QUOTE_MINIMAL):
            domains.append(row[1])
            i+=1
            if i >= 10000:
                break

requests_header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Cache-Control': 'max-age=0',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,pt;q=0.6',
    'Connection': 'keep-alive'
}


# thread to visit websites
class DomainScaner(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while len(domains) > 0:
            domain = domains.pop(0)

            if domain.endswith('.cn'):
                continue
            if 'google' in domain:
                continue

            is_proxy = False

            try:
                requests.get('http://www.' + domain, timeout=10, headers=requests_header)
            except BaseException:
                try:
                    requests.get('http://' + domain, timeout=10, headers=requests_header)
                except BaseException:
                    is_proxy = True

            if is_proxy:
                domains_proxy.append(domain)
            else:
                domains_direct.append(domain)

            print('[Doamins Remain: %d]\tProxy %s：%s' % (len(domains), is_proxy, domain) )

        global scaner_thread_num
        scaner_thread_num -= 1


print('top10000 Script Starting...\n\n')

GetSites()

# Start Thread
scaner_thread_num = 0
for i in range(THREAD_LIMIT):
    DomainScaner().start()
    scaner_thread_num += 1

# wait thread done
while scaner_thread_num:
    pass

# write files
file_proxy = open('resultant/top500_proxy.list', 'w', encoding='utf-8')
file_direct = open('resultant/top500_direct.list', 'w', encoding='utf-8')

now_time = time.strftime("%Y-%m-%d %H:%M:%S")
file_proxy.write('# top10000 proxy list update time: ' + now_time + '\n')
file_direct.write('# top10000 direct list update time: ' + now_time + '\n')

domains_direct = list( set(domains_direct) )
domains_proxy  = list( set(domains_proxy) )
domains_direct.sort()
domains_proxy.sort()

for domain in domains_direct:
    file_direct.write(domain+'\n')
for domain in domains_proxy:
    file_proxy.write(domain+'\n')

shutil.rmtree(temp_dir)

