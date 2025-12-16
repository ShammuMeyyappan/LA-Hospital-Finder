import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
Outputs the number of services and insurers per hospital.
"""

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