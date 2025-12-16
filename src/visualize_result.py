import matplotlib.pyplot as plt
import pandas as pd
import csv
import geopandas as gpd
from matplotlib.patches import FancyArrow, Rectangle
from matplotlib.lines import Line2D
import numpy as np

with open(r"data/processed/CSV/mlkch - Sheet1.csv", 'r', encoding='utf-8') as f:
    res = sum(1 for line in f)
print(res)
with open(r"data/processed/CSV/ladowntownmc - Sheet1.csv", 'r', encoding='utf-8') as f:
    res1 = sum(1 for line in f)
print(res1)
with open(r"data/processed/CSV/ssh-hollywood - Sheet1.csv", 'r', encoding='utf-8') as f:
    res2 = sum(1 for line in f)
print(res2)
with open(r"data/processed/CSV/lalach - Sheet1.csv", 'r', encoding='utf-8') as f:
    res3 = sum(1 for line in f)
print(res3)
with open(r"data/processed/CSV/ucla - Sheet1.csv", 'r', encoding='utf-8') as f:
    res4 = sum(1 for line in f)
print(res4)
with open(r"data/processed/CSV/keck - Sheet1.csv", 'r', encoding='utf-8') as f:
    res5 = sum(1 for line in f)
print(res5)
with open(r"data/processed/CSV/dignity - Sheet1.csv", 'r', encoding='utf-8') as f:
    res6 = sum(1 for line in f)
print(res6)
items = ["MLKCH", "LADTMC", "Hollywood", "lachla", "UCLA", "Keck&Norris", "CHMC"]
values = [res, res1, res2, res3, res4, res5, res6]
plt.bar(items, values)
plt.xlabel('Hospitals')
plt.ylabel('Values')
plt.title('Insurances')
plt.show()

with open(r"data/processed/CSV/MLKCH_Service - Sheet1.csv", 'r', encoding='utf-8') as f:
    res = sum(1 for line in f)
print(res)
with open(r"data/processed/CSV/ladowntownmc_Service - Sheet1.csv", 'r', encoding='utf-8') as f:
    res1 = sum(1 for line in f)
print(res1)
with open(r"data/processed/CSV/sch-hollywood_Service - Sheet1.csv", 'r', encoding='utf-8') as f:
    res2 = sum(1 for line in f)
print(res2)
with open(r"data/processed/CSV/lach-la_Service - Sheet1.csv", 'r', encoding='utf-8') as f:
    res3 = sum(1 for line in f)
print(res3)
with open(r"data/processed/CSV/ucla_Service - Sheet1.csv", 'r', encoding='utf-8') as f:
    res4 = sum(1 for line in f)
print(res4)
with open(r"data/processed/CSV/service_keck - Sheet1.csv", 'r', encoding='utf-8') as f:
    res5 = sum(1 for line in f)
print(res5)
with open(r"data/processed/CSV/dignity_Service - Sheet1.csv", 'r', encoding='utf-8') as f:
    res6 = sum(1 for line in f)
print(res6)
items = ["MLKCH", "LADTMC", "Hollywood", "LAlach", "UCLA", "Keck&Norris", "CHMC"]
values = [res, res1, res2, res3, res4, res5, res6]
plt.bar(items, values)
plt.xlabel('Hospitals')
plt.ylabel('Count')
plt.title('Services')
plt.show()

list1 = []
with open(r"data/processed/CSV/mlkch - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list1.append(row)
list2 = []
with open(r"data/processed/CSV/ladowntownmc - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list2.append(row)
list3 = []
with open(r"data/processed/CSV/ssh-hollywood - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list3.append(row)
list4 = []
with open(r"data/processed/CSV/lalach - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list4.append(row)
list5 = []
with open(r"data/processed/CSV/ucla - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list5.append(row)
list6 = []
with open(r"data/processed/CSV/keck - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list6.append(row)
list7 = []
with open(r"data/processed/CSV/dignity - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list7.append(row)

all_lists = [list1, list2, list3, list4, list5, list6, list7]

def search_multiple_lists(search, lists_search):
    """
    Searches for matching hospitals through dataset based on user input.
    """
    found_list = []
    for i, lists in enumerate(lists_search):
        for row in lists:
            if any(search in col for col in row):
                found_list.append(f"{i+1}")
                break
    return found_list
user_input = input("Enter Insurance: ")

results = search_multiple_lists(user_input, all_lists)

if results:
    print("List of Hospitals: Martin Luther King Jr. Community Hospital (1), LA DownTown Medical Center (2), Southern California Hospital at Hollywood (3), Los Angeles Community Hospital(4), Ronald Reagan UCLA Medical Center (5), Keck Hospital of USC and USC KENNETH NORRIS JR. CANCER HOSPITAL(6), California Hospital Medical Center -Dignity Health (7)")   
    print(f"'{user_input}' was found in: {', '.join(results)}")
else:
    print(f"'{user_input}' was not found in any list")

list1 = []
with open(r"data/processed/CSV/MLKCH_Service - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list1.append(row)
list2 = []
with open(r"data/processed/CSV/ladowntownmc_Service - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list2.append(row)
list3 = []
with open(r"data/processed/CSV/sch-hollywood_Service - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list3.append(row)
list4 = []
with open(r"data/processed/CSV/lach-la_Service - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list4.append(row)
list5 = []
with open(r"data/processed/CSV/ucla_Service - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list5.append(row)
list6 = []
with open(r"data/processed/CSV/service_keck - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list6.append(row)
list7 = []
with open(r"data/processed/CSV/dignity_Service - Sheet1.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list7.append(row)

all_lists = [list1, list2, list3, list4, list5, list6, list7]

results = search_multiple_lists(user_input, all_lists)

if results:
    print("List of Hospitals: Martin Luther King Jr. Community Hospital (1), LA DownTown Medical Center (2), Southern California Hospital at Hollywood (3), Los Angeles Community Hospital(4), Ronald Reagan UCLA Medical Center (5), Keck Hospital of USC and USC KENNETH NORRIS JR. CANCER HOSPITAL(6), California Hospital Medical Center -Dignity Health (7)")   
    print(f"'{user_input}' was found in: {', '.join(results)}")
else:
    print(f"'{user_input}' was not found in any list")

with open(r"data/processed/CSV/mlkch - Sheet1.csv", 'r', encoding='utf-8') as f:
    res = sum(1 for line in f)
print(res)
with open(r"data/processed/CSV/ladowntownmc - Sheet1.csv", 'r', encoding='utf-8') as f:
    res1 = sum(1 for line in f)
print(res1)
with open(r"data/processed/CSV/ssh-hollywood - Sheet1.csv", 'r', encoding='utf-8') as f:
    res2 = sum(1 for line in f)
print(res2)
with open(r"data/processed/CSV/lalach - Sheet1.csv", 'r', encoding='utf-8') as f:
    res3 = sum(1 for line in f)
print(res3)
with open(r"data/processed/CSV/ucla - Sheet1.csv", 'r', encoding='utf-8') as f:
    res4 = sum(1 for line in f)
print(res4)
with open(r"data/processed/CSV/keck - Sheet1.csv", 'r', encoding='utf-8') as f:
    res5 = sum(1 for line in f)
print(res5)
with open(r"data/processed/CSV/dignity - Sheet1.csv", 'r', encoding='utf-8') as f:
    res6 = sum(1 for line in f)
print(res6, "Insurance")

values = pd.Series([res, res1, res2, res3, res4, res5, res6])

with open(r"data/processed/CSV/MLKCH_Service - Sheet1.csv", 'r', encoding='utf-8') as f:
    result = sum(1 for line in f)
print(result)
with open(r"data/processed/CSV/ladowntownmc_Service - Sheet1.csv", 'r', encoding='utf-8') as f:
    result1 = sum(1 for line in f)
print(result1)
with open(r"data/processed/CSV/sch-hollywood_Service - Sheet1.csv", 'r', encoding='utf-8') as f:
    result2 = sum(1 for line in f)
print(result2)
with open(r"data/processed/CSV/lach-la_Service - Sheet1.csv", 'r', encoding='utf-8') as f:
    result3 = sum(1 for line in f)
print(result3)
with open(r"data/processed/CSV/ucla_Service - Sheet1.csv", 'r', encoding='utf-8') as f:
    result4 = sum(1 for line in f)
print(result4)
with open(r"data/processed/CSV/keck_Service - Sheet1.csv", 'r', encoding='utf-8') as f:
    result5 = sum(1 for line in f)
print(result5)
with open(r"data/processed/CSV/dignity_Service - Sheet1.csv", 'r', encoding='utf-8') as f:
    result6 = sum(1 for line in f)
print(result6, "Services")
items = ["MLKCH", "LADTMC", "Hollywood", "lachla", "UCLA", "Keck&Norris", "CHMC"]
values1 = pd.Series([result, result1, result2, result3, result4, result5, result6])

correlation = values.corr(values1)
print(correlation)
fig, ax = plt.subplots()
ax.scatter(values, values1)
for i, txt in enumerate(items):
    ax.annotate(txt, (values[i], values1[i]))
plt.plot(np.unique(values), np.poly1d(np.polyfit(values, values1, 1))
         (np.unique(values)), color='red')
plt.title('Correlation Coefficient Analysis')
plt.xlabel('Insurances')
plt.ylabel('Services')

def scale_bar(ax, length, units='m', location=(0.1, 0.05)):

    """
    Defines the scale bar.
    """

    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()

    sbx = x0 + (x1 - x0) * location[0]
    sby = y0 + (y1 - y0) * location[1]


    bar_height = (y1 - y0) * 0.015

    ax.add_patch(Rectangle(
        (sbx, sby),
        length,
        bar_height,
        facecolor='black',
        edgecolor='black'
    ))

    ax.text(
        sbx + length,
        sby - bar_height * 0.5,
        f"{int(length)} {units}",
        ha="center", va="top", fontsize=10
    )

gdf2 = gpd.read_file(r"dignity_Service.shp")
gdf3 = gpd.read_file(r"Keck_Hospital.shp")
gdf4 = gpd.read_file(r"lachla_Service.shp")
gdf5 = gpd.read_file(r"ladowntownmc.shp")
gdf6 = gpd.read_file(r"MLKCH.shp")
gdf7 = gpd.read_file(r"schhollywood.shp")
gdf8 = gpd.read_file(r"ucla_service.shp")
gdf9 = gpd.read_file(r"USC_Norris_Hospital.shp")


gdf2 = gdf2.to_crs(3857)
gdf3 = gdf3.to_crs(3857)
gdf4 = gdf4.to_crs(3857)
gdf5 = gdf5.to_crs(3857)
gdf6 = gdf6.to_crs(3857)
gdf7 = gdf7.to_crs(3857)
gdf8 = gdf8.to_crs(3857)
gdf9 = gdf9.to_crs(3857)
fig, ax = plt.subplots(figsize=(20, 40))


gdf2.plot(ax=ax, color="lightgreen", markersize=200)
gdf3.plot(ax=ax, color="lightblue", markersize=200)
gdf4.plot(ax=ax, color="orange", markersize=200)
gdf5.plot(ax=ax, color="red", markersize=200)
gdf6.plot(ax=ax, color="purple", markersize=200)
gdf7.plot(ax=ax, color="blue", markersize=200)
gdf8.plot(ax=ax, color="black", markersize=200)
gdf9.plot(ax=ax, color="grey", markersize=200)

ax.add_patch(FancyArrow(
    0.95, 0.90, 0, 0.05,
    transform=ax.transAxes,
    width=0.01,
    head_width=0.05,
    color='black'
))
ax.text(
    0.99, 0.01,
    "Map created by Philippe Naviaux & Shammu Meyyappan",
    transform=ax.transAxes,
    ha='right',
    va='bottom',
    fontsize=10,
    color="black"
)

scale_bar(ax, length=1000, units="m", location=(0.1, 0.05))

# Legend
legend_elements = [
    Line2D([0], [0], marker='o', color='lightgreen', label='California Hospital Medical Center',
           markersize=8, linestyle=''),
    Line2D([1], [1], marker='o', color='lightblue', label='Keck Hospital of USC',
           markersize=8, linestyle=''),
    Line2D([2], [2], marker='o', color='orange', label='L.A. Downtown Medical Center',
           markersize=8, linestyle=''),
    Line2D([3], [3], marker='o', color='red', label='Los Angeles Community Hospital',
           markersize=8, linestyle=''),
    Line2D([4], [4], marker='o', color='purple', label='Martin Luther King Jr. Community Hospital',
           markersize=8, linestyle=''),
    Line2D([5], [5], marker='o', color='blue', label='Southern California Hospital at Hollywood',
           markersize=8, linestyle=''),
    Line2D([6], [6], marker='o', color='black', label='UCLA Medical Center',
           markersize=8, linestyle=''),
    Line2D([7], [7], marker='o', color='grey', label='USC Kenneth Norris Cancer Hospital',
           markersize=8, linestyle=''),
]

ax.legend(handles=legend_elements, loc='upper left')

ax.set_title("Hospitals", fontsize=16)
plt.tight_layout()
plt.show()