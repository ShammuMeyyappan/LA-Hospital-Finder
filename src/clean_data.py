import bs4
import requests
import csv

"""
Loops through each website and selects for only the text within lists between two specified keywords which it then outputs to a CSV.
"""

url = "https://www.dignityhealth.org/dhmf/about/dhmn/inland-empire/services"
response = requests.get(url)
parser = bs4.BeautifulSoup(response.text, 'html.parser')
#CALI HOSP MED CENTER -Dignity Health

data = []
for ul in parser.find_all('ul'):
    for li in ul.find_all('li'):
        text = li.get_text(strip=True)
        data.append(text)


keep = [
    "Anthem Blue Cross",
    "Blue Shield",
    "Cigna",
    "HealthNet",
    "Inland Empire Health Plan",
    "United Health Care"
]


filtered = [
    line for line in data
    if any(k.lower() in line.lower() for k in keep)
]
for line in filtered: 
    print(line)
output = r"data/processed/CSV/dignity - Sheet1.csv"
with open(output, 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    for line in filtered:
        writer.writerow([line])

url = "https://www.keckmedicine.org/insurance/"
response = requests.get(url)
parser = bs4.BeautifulSoup(response.text, 'html.parser')

lines = []

for ul in parser.find_all('ul'):
    for li in ul.find_all('li'):
        text = li.get_text(strip=True)
        lines.append(text)

keyword = "Aetna"

idx_start = next(i for i, line1 in enumerate(lines) if keyword in line1)
result = lines[idx_start:]     

target = "USC Health Plans"

idx_end = next(i for i, line1 in enumerate(result) if target in line1)
result = result[:idx_end + 1]   

for line1 in result:
    print(line1)

output1 = r"data/processed/CSV/keck - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line1 in result:
        writer.writerow([line1])

url = "https://www.uclahealth.org/patient-resources/health-insurance-accepted-ucla-health#government-insurance"
response = requests.get(url)
parser = bs4.BeautifulSoup(response.text, 'html.parser')

lines = []

for ul in parser.find_all('ul'):
    for li in ul.find_all('li'):
        text = li.get_text(strip=True)
        lines.append(text)

keyword = "Aetna"

idx_start = next(i for i, line in enumerate(lines) if keyword in line)
result = lines[idx_start:]      

target = "U.S. Behavioral Health Plan, California"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line)

output1 = r"data/processed/CSV/ucla - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)

    for line in result:
        writer.writerow([line])

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
keyword = "Aetna"

idx_start = next(i for i, line in enumerate(lines) if keyword in line)
result = lines[idx_start:]      

target = "USA Network"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line)

output1 = r"data/processed/CSV/lalach - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)

    for line in result:
        writer.writerow([line])

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
keyword = "Aetna"

idx_start = next(i for i, line in enumerate(lines) if keyword in line)
result = lines[idx_start:]      

target = "USA Network"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line)

output1 = r"data/processed/CSV/ssh-hollywood - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in result:
        writer.writerow([line])

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
keyword = "America’s Choice Provider Network (ACPN)"

idx_start = next(i for i, line in enumerate(lines) if keyword in line)
result = lines[idx_start:]      

target = "Well Care"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line)

output1 = r"data/processed/CSV/ladowntownmc - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)

    for line in result:
        writer.writerow([line])

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
keyword = "Los Angeles County"

idx_start = next(i for i, line in enumerate(lines) if keyword in line)
result = lines[idx_start:]      

target = "Health Net Federal Services (TRICARE)"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line)

output1 = r"data/processed/CSV/mlkch - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)

    for line in result:
        writer.writerow([line])

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

item = "Emergency"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "Maternity"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line)
output1 = r"data/processed/CSV/MLKCH_Service - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in result:
        writer.writerow([line])

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
item = "1680 E 120th StreetLos Angeles, CA 90059"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "1680 E 120th StreetLos Angeles, CA 90059"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line)

csv_file_path = r"data/processed/CSV/MLKCH_Service - Sheet1.csv"
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    data1 = list(reader)
if len(data1) > 0:
    data1[0].append('Address')

    for i in range(1, len(data)):
        if i-1 < len(result):  
            data1[i].append(result[i-1])
else:
    print("Warning: CSV file is empty")
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data1)

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

item = "Cardiopulmonary"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "Speech Therapy"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line)
output1 = r"data/processed/CSV/ladowntownmc_Service - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in result:
        writer.writerow([line])

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

item = "1711 West Temple StreetLos Angeles, California 90026"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "1711 West Temple StreetLos Angeles, California 90026"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line)


csv_file_path = r"data/processed/CSV/ladowntownmc_Service - Sheet1.csv"
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    data1 = list(reader)
if len(data1) > 0:
    data1[0].append('Address')

    for i in range(1, len(data)):
        if i-1 < len(result):  
            data1[i].append(result[i-1])
else:
    print("Warning: CSV file is empty")
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data1)

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

item = "Cardiology"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "Vascular"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line) 
output1 = r"data/processed/CSV/sch-hollywood_Service - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in result:
        writer.writerow([line])

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
item = "6245 De Longpre AvenueLos Angeles, CA 90028"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "6245 De Longpre AvenueLos Angeles, CA 90028"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line) 

csv_file_path = r"data/processed/CSV/sch-hollywood_Service - Sheet1.csv"
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    data1 = list(reader)
if len(data1) > 0:
    data1[0].append('Address')

    for i in range(1, len(data)):
        if i-1 < len(result):  
            data1[i].append(result[i-1])
else:
    print("Warning: CSV file is empty")
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data1)

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

item = "Cardiology Services"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "Wound Care"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line) 
output1 = r"data/processed/CSV/lach-la_Service - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in result:
        writer.writerow([line])

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
item = "4081 E. Olympic Blvd.Los Angeles, CA 90023"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "4081 E. Olympic Blvd.Los Angeles, CA 90023"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line)
    result_str= ' '.join(result)
    result2=result_str.replace('AboutAbout UsContact UsAwardsPatients and VisitorsFind a DoctorAccepted InsurancePreparing for HospitalizationLocationsBellflowerNorwalkProspect MedicalContact UsHospital Address','')
    result3=result2.replace('Phone Directory(323) 267-0477Follow UsFacebookTwitterInstagram','')
    csv_file_path = r"data/processed/CSV/lach-la_Service - Sheet1.csv"
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    data1 = list(reader)
    data1[0].append('Address')
    data1[1].append(result3)
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data1)

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

item = "Adolescent Epilepsy Care"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "Women’s Cardiovascular Services"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line) 
output1 = r"data/processed/CSV/ucla_Service - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in result:
        writer.writerow([line])

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
item = "Address757 Westwood PlazaLos Angeles, California 90095"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "Address757 Westwood PlazaLos Angeles, California 90095"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line) 
csv_file_path = r"data/processed/CSV/ucla_Service - Sheet1.csv"
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    data1 = list(reader)
if len(data1) > 0:
    data1[0].append('Address')

    for i in range(1, len(data)):
        if i-1 < len(result):  
            data1[i].append(result[i-1])
else:
    print("Warning: CSV file is empty")
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data1)

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
item = "6245 De Longpre AvenueLos Angeles, CA 90028"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "6245 De Longpre AvenueLos Angeles, CA 90028"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line) 
csv_file_path = r"data/processed/CSV/sch-hollywood_Service - Sheet1.csv"
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    data1 = list(reader)
if len(data1) > 0:
    data1[0].append('Address')

    for i in range(1, len(data)):
        if i-1 < len(result):  
            data1[i].append(result[i-1])
else:
    print("Warning: CSV file is empty")
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data1)

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

item = "Ablation Surgery (Our expert surgeons offer the latest techniques in minimally invasive ablation surgery.)"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "Wound Healing Center and Hyperbaric Oxygen Center"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   
for line in result:
    print(line) 
output1 = r"data/processed/CSV/service_keck - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in result:
        writer.writerow([line])

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
item = "1500 San Pablo Street"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "Los Angeles, CA 90033"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line)
    summary = (result[0] + result[1])
    print(summary)
csv_file_path = r"data/processed/CSV/service_keck - Sheet1.csv"
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    data1 = list(reader)
    data1[0].append('Address')
    data1[i].append(summary)
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data1)

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
item = "1441 Eastlake Ave"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "Los Angeles, CA 90033"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    #print(line)
    summary = (result[0] + result[1])
    print(summary)
csv_file_path = r"data/processed/CSV/service_keck - Sheet1.csv"
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    data1 = list(reader)
    data1[0].append('Address1')
    data1[i].append(summary)

with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data1)

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

item = "Centro de Nacimiento"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "Womens health"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line) 
output1 = r"data/processed/CSV/dignity_Service - Sheet1.csv"
with open(output1, 'w', newline='', encoding='utf8') as j:
    writer = csv.writer(j)
    for line in result:
        writer.writerow([line])

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
item = "1401 S. Grand Ave. Los Angeles, CA, 90015"
idx_start = next(i for i, line in enumerate(data) if item in line)
result = data[idx_start:]     

target = "1401 S. Grand Ave. Los Angeles, CA, 90015"

idx_end = next(i for i, line in enumerate(result) if target in line)
result = result[:idx_end + 1]   

for line in result:
    print(line) 
csv_file_path = r"data/processed/CSV/dignity_Service - Sheet1.csv"
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    data1 = list(reader)
    data1[0].append('Address')
    data1[1].append(result)

with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data1)