import csv
# from pprint import pprint

with open("28-12526-27636 (1).csv", 'r+', encoding='utf-8') as file:
    data_province = []
    for row in csv.DictReader(file, delimiter=";"):
        data_province.append(dict(row))

top_data = []
for i in data_province:
    s = 0
    for j in range(2012, 2018):
        s += int(i[str(j)])
    top_data.append(dict(hudud=i["Hududlar"], soni=s))   # append -- dict(key = hudud, array = soni)
top_data.sort(key=lambda arr: int(arr['soni']), reverse=True)   # sort -- key= soni

print("2012-2017 - yillar oralig'idagi eng ko'p kasalxonalar qurulgan 3 ta viloyat: ")
top = top_data[1:4]
            # nega top_data ni top o'zgaruvchiga yuklashimdan maqsad:
            # top_data[:m] - bizga kerakli ixtiyoriy dastlabki m tasini olish imkonini beradi.
space_hudud = 0
space_son = 0
for i in top:
    if len(i['hudud']) > space_hudud:
        space_hudud = len(i['hudud'])

    if len(str(i['soni'])) > space_son:
        space_son = len(str(i['soni']))
t = 0 # consolda tartib raqamli chiqishi uchun
for i in top:
    t += 1
    if t > 9:
        print(f"\t{t}.", i['hudud'], " " *(space_hudud - 1 - len(i["hudud"])), " - ", i["soni"]," " *(space_son - len(str(i['soni']))), " ta")
    else:
        print(f"\t{t}.", i['hudud'], " " *(space_hudud - len(i["hudud"])), " - ", i["soni"], " " *(space_son - len(str(i['soni']))), " ta")


