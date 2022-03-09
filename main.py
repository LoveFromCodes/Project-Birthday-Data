import os
import json
import time


# 读取文件并构建一维数组
folder_path = "/Users/hailing/Downloads/years/jsons/"
file_names = os.listdir(folder_path)
file_names.sort()

day_list = []
for file_name in file_names:
    file_path = folder_path + file_name
    with open(file_path,'r') as f:
        lines = f.readlines()
        file_json = json.loads( ''.join(lines) )

        for day in file_json:
            lunar_year_str = day['lunar']['year'] #己丑
            solor_year_str = str(day['gregorian']['year']) #1949
            year_str = solor_year_str + lunar_year_str #1949己丑
            month_str = day['lunar']['month'] #十一月
            date_str = day['lunar']['date'] #十二
            month_date_str = month_str + date_str #十一月十二
            solor_date = day['gregorian'] #{'year': 1949, 'month': 12, 'date': 31}

            d = {
                "lunar_year_str": lunar_year_str,
                "solor_year_str": solor_year_str,
                "year_str": year_str,
                "month_str": month_str,
                "date_str": date_str,
                "month_date_str": month_date_str,
                "solor_date": solor_date
            }
            day_list.append(d)


# 处理数组，构建目标数据结构
lunar_dict = dict()
year_list = []
year_to_month_dict = {}
year_month_to_date_dict = {}


lunar_dict_json_str = ""
year_key = "1900庚子"
lunar_dict[year_key] = {}
year_list.append(year_key)

month_dict = {}
for day in day_list:
    if day['month_date_str'] == "正月初一":
        lunar_dict[year_key] = month_dict

        year_list.append(year_key)
        year_to_month_dict[year_key] = []
        for month in month_dict:
            year_to_month_dict[year_key].append(month)
            
            year_plus_month_str = year_key+month
            year_month_to_date_dict[year_plus_month_str] = []
            for dddate in month_dict[month]:
                year_month_to_date_dict[year_plus_month_str].append(dddate)
        month_dict = {}

    month_key = day['month_str']
    date_key = day['date_str']
    solor_date = day['solor_date']
    
    if month_key not in month_dict:
        month_dict[month_key] = {}
    month_dict[month_key][date_key] = solor_date

    if day['month_date_str'] == "正月初十":
        year_key = day['year_str']
    
items = (
    ("lunar_dict", "/Users/hailing/Downloads/years/lunar_list.json"), 
    ("year_list", "/Users/hailing/Downloads/years/year_list.json"), 
    ("year_to_month_dict", "/Users/hailing/Downloads/years/year_to_month.json"), 
    ("year_month_to_date_dict", "/Users/hailing/Downloads/years/year_month_to_date_dict.json"), 
)
for var, path in items:
    var_json_str = json.dumps(var, ensure_ascii=False)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(var_json_str)