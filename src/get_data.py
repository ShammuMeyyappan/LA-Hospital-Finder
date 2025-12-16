#!/usr/bin/env python
# coding: utf-8

# In[3]:


import bs4
import requests
import csv
url = "https://www.dignityhealth.org/dhmf/about/dhmn/inland-empire/services"
response = requests.get(url)
parser = bs4.BeautifulSoup(response.text, 'html.parser')
#CALI HOSP MED CENTER -Dignity Health

data = []
for ul in parser.find_all('ul'):
    for li in ul.find_all('li'):
        text = li.get_text(strip=True)
        data.append(text)

output = r"dignity - Sheet1.csv"
with open(output, 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    for line in data:
        writer.writerow(line)
        print(line)


# In[6]:


import bs4
import requests
import csv
url = "https://www.keckmedicine.org/insurance/"
response = requests.get(url)
parser = bs4.BeautifulSoup(response.text, 'html.parser')

lines = []

for ul in parser.find_all('ul'):
    for li in ul.find_all('li'):
        text = li.get_text(strip=True)
        lines.append(text)

output1 = r"keck - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line1 in lines:
        writer.writerow(line1)
        print(line1)


# In[7]:


import bs4
import requests

url = "https://www.uclahealth.org/patient-resources/health-insurance-accepted-ucla-health#government-insurance"
response = requests.get(url)
parser = bs4.BeautifulSoup(response.text, 'html.parser')

lines = []

for ul in parser.find_all('ul'):
    for li in ul.find_all('li'):
        text = li.get_text(strip=True)
        lines.append(text)

output1 = r"ucla - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)

    for line in lines:
        writer.writerow([line])
        print(line)


# In[9]:


import bs4
import requests
import csv
url = "https://www.lach-la.com/patients-and-visitors/accepted-insurance/"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 
lines = []
#print(html)
for entry in parser.find_all('ul'):
    #print(entry)
    for entry2 in entry.find_all('li'): 
        abc = entry2.get_text()
        lines.append(abc)

output1 = r"lalach - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)

    for line in lines:
        writer.writerow([line])
        print(line)


# In[10]:


import bs4
import requests
import csv
url = "https://www.sch-hollywood.com/patients--visitors/accepted-insurance/"
response = requests.get(url)
html = response.text
parser = bs4.BeautifulSoup(html, 'html.parser') 
lines = []
#print(html)
for entry in parser.find_all('ul'):
    #print(entry)
    for entry2 in entry.find_all('li'): 
        abc = entry2.get_text()
        lines.append(abc)

output1 = r"ssh-hollywood - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in lines:
        writer.writerow([line])
        print(line)


# In[11]:


import bs4
import requests
import csv
url = "https://ladowntownmc.com/#contracted-health-plans"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 
lines = []
#print(html)
for entry in parser.find_all('ul'):
    #print(entry)
    for entry2 in entry.find_all('li'): 
        abc = entry2.get_text()
        lines.append(abc)


output1 = r"ladowntownmc - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)

    for line in lines:
        writer.writerow([line])
        print(line)


# In[12]:


import bs4
import requests
import csv
url = "https://www.mlkch.org/health-insurance"
response = requests.get(url)
html = response.text

parser = bs4.BeautifulSoup(html, 'html.parser') 
lines = []
for entry in parser.find_all('ul'):
    #print(entry)
    for entry2 in entry.find_all('li'): 
        abc = entry2.get_text()
        lines.append(abc)

output1 = r"mlkch - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)

    for line in lines:
        writer.writerow([line])
        print(line)


# In[14]:


import bs4
import requests
import csv
url = "https://www.mlkch.org/our-services"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 

data = []
for entry in parser.find_all('h3', class_="paragraph-header"):
    #print(entry)
    for entry2 in entry.find_all('strong'): 
        abc = entry2.get_text(strip=True)
        #print(abc)
        data.append(abc)

output1 = r"MLKCH_Service - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in data:
        writer.writerow([line])
        print(line)


# In[17]:


import pandas as pd
import requests
import csv


url = "https://www.mlkch.org/contact-and-directions"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 

data = []
for entry in parser.find_all('p'):
    #print(entry)
    for entry2 in entry.find_all('strong'):
        abc = entry2.get_text(strip=True)
        #print(abc)
        data.append(abc)
output1 = r"ladowntownmc_Service - Sheet1.csv"
with open(output1, 'w', newline='') as file:
    writer = csv.writer(file)
    for line in data:
        writer.writerows([line])
        print(line)


# In[18]:


import bs4
import requests
import csv
url = "https://ladowntownmc.com/"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 

data = []
for entry in parser.find_all("div", class_="et_pb_blurb_description"):
    #print(entry)
    abc = entry.get_text(strip=True)
    #print(abc)
    data.append(abc)


output1 = r"ladowntownmc_Service - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in data:
        writer.writerow([line])
        print(line)


# In[19]:


import bs4
import requests
import csv
url = "https://ladowntownmc.com/"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 

data = []
for entry in parser.find_all("div", class_="et_pb_blurb_description"):
    #print(entry)
    abc = entry.get_text(strip=True)
    #print(abc)
    data.append(abc)




csv_file_path = r"ladowntownmc_Service - Sheet1.csv"
with open(csv_file_path, 'w', newline='') as file:

    writer = csv.writer(file)
    for line in data:
        writer.writerows(data)
        print(line)


# In[20]:


import bs4
import requests
import csv
url = "https://www.sch-hollywood.com/services/"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 

data = []
for entry in parser.find_all('h3'):
    #print(entry)
    abc = entry.get_text(strip=True)
    #print(abc)
    data.append(abc)


output1 = r"sch-hollywood_Service - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in data:
        writer.writerow([line])
        print(line)


# In[21]:


import bs4
import requests
import csv
url = "https://www.sch-hollywood.com/services/"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 

data = []
for entry in parser.find_all('p'):
        abc = entry.get_text(strip=True)
        #print(abc)
        data.append(abc)

csv_file_path = r"sch-hollywood_Service - Sheet1.csv"

with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    for line in data:
        writer.writerows(line)
        print(line)


# In[22]:


import bs4
import requests
import csv
url = "https://www.lach-la.com/programs-and-services/"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 

data = []
for entry in parser.find_all('ul'):
    for entry2 in entry.find_all('li'): 
        abc = entry2.get_text(strip=True)
        data.append(abc)


output1 = r"lach-la_Service - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in data:
        writer.writerow([line])
        print(line)


# In[23]:


import bs4
import requests
import csv
url = "https://www.lach-la.com/programs-and-services/"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 

data = []
for entry in parser.find_all('ul'):
    for entry2 in entry.find_all('li'):
        abc = entry.get_text(strip=True)
        #print(abc)
        data.append(abc)
csv_file_path = r"lach-la_Service - Sheet1.csv"
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    for line in data:
        writer.writerows(data)
        print(line)


# In[24]:


import bs4
import requests
import csv
url = "https://www.uclahealth.org/medical-services"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 

data = []
for entry in parser.find_all('a', class_='md:inline-block mr-3 mb-3 button button--pill'):
    #print(entry)
    for entry2 in entry.find_all('span', class_="line-clamp-1 leading-5"): #loop over find li
        abc = entry2.get_text(strip=True)
        #print(abc)
        data.append(abc)


output1 = r"ucla_Service - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in data:
        writer.writerow([line])
        print(line)


# In[26]:


import py4j
import bs4
import requests
import csv
url = "https://www.uclahealth.org/hospitals/reagan"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') #xml

data = []
for entry in parser.find_all('p'):
    #print(entry)
    abc = entry.get_text(strip=True)
    print(abc)
    data.append(abc)

csv_file_path = r"ucla_Service - Sheet1.csv"
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    for line in data:
        writer.writerows(data)
        print(line)


# In[28]:


import bs4
import requests
import csv
url = "https://www.sch-hollywood.com/services/"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') #xml

data = []
for entry in parser.find_all('li', class_="footer-block footer-block-last"):
    #print(entry)
    for entry2 in entry.find_all("div"):
        abc = entry2.get_text(strip=True)
        #print(abc)
        data.append(abc)

csv_file_path = r"sch-hollywood_Service - Sheet1.csv"
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    for line in data:
        writer.writerows(data)
        print(line)


# In[30]:


import bs4
import requests
import csv
url = "https://www.keckmedicine.org/conditions-and-treatments/"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') #xml

data = []
for entry in parser.find_all('a', class_="title"):
        abc = entry.get_text(strip=True)
        #print(abc)
        data.append(abc)

output1 = r"service_keck - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in data:
        writer.writerow([line])
        print(line)


# In[32]:


import bs4
import requests
import csv
url = "https://www.keckmedicine.org/locations/1500-san-pablo-st-los-angeles/"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 

data = []
for entry in parser.find('a', href="https://www.google.com/maps/place/1500+San+Pablo+Street+Los+Angeles%2C+CA+90033 "): 
    print(entry)
    abc = entry.get_text(strip=True)
    print(abc)
    data.append(abc)  

with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    for line in data:
        writer.writerows(data)
        print(line)


# In[33]:


import bs4
import requests
import csv
url = "https://www.keckmedicine.org/locations/1441-eastlake-ave-los-angeles/"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 

data = []
for entry in parser.find('a', href="https://www.google.com/maps/place/1441+Eastlake+Ave+Los+Angeles%2C+CA+90033 "): 
    print(entry)
    abc = entry.get_text(strip=True)
    print(abc)
    data.append(abc)  

csv_file_path = r"service_keck - Sheet1.csv"

with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    for line in data:
        writer.writerows(data)
        print(line)




# In[34]:


import bs4
import requests
import csv
url = "https://www.dignityhealth.org/socal/locations/californiahospital/services"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') 

data = []
for entry in parser.find_all('a', class_="cmp-list__item-link cmp-list__item-title"):
        abc = entry.get_text(strip=True)
        print(abc)
        data.append(abc)


output1 = r"dignity_Service - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in data:
        writer.writerow([line])
        print(line)


# In[3]:


import bs4
import requests
import csv
url = "https://www.dignityhealth.org/socal/contact-us"
response = requests.get(url)
html = response.text
#print(html)
parser = bs4.BeautifulSoup(html, 'html.parser') #xml

data = []
for entry in parser.find_all('span', class_='small-txt'):
        abc = entry.get_text(strip=True)
        print(abc)
        data.append(abc)

csv_file_path = r"dignity_Service - Sheet1.csv"

with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    for line in data:
        writer.writerows(data)
        print(line)


# In[ ]:




