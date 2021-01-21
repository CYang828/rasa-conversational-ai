# -*- coding: utf-8 -*-
"""
    qweather.py
    ~~~~~~~~~
    使用和风天气数据查询天气
"""

import requests
import json

KEY = '882e721338b4441dbf1b7e514029aaa8'  # API key(私钥)
UID = ""  # 用户ID, @todo: 当前并没有使用这个值,签名验证方式将使用到这个值

# LOCATION = 'beijing'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等
API_loc_id = 'https://geoapi.qweather.com/v2/city/lookup?' # 城市id查询
API = 'https://devapi.qweather.com/v7/weather/3d?' # API URL，可替换为其他 URL
# UNIT = 'c'  # 单位
# LANGUAGE = 'zh-Hans'  # 查询结果的返回语言

def fetch_location_id(location):
    result = requests.get(API_loc_id, params={
        'key': KEY,
        'location': location,
    })
    return result.json()

def fetch_weather(location_id):
    result = requests.get(API, params={
        'key': KEY,
        'location': location_id,
    })
    return result.json()

def get_weather_by_day(location, day=1):
    location_id = fetch_location_id(location)["location"][0]["id"]
    result = fetch_weather(location_id)
    normal_result = {
        "location": location,
        "fxDate": result["daily"][day]["fxDate"],
        "tempMax": result["daily"][day]["tempMax"],
        "tempMin": result["daily"][day]["tempMin"],
        "textDay": result["daily"][day]["textDay"],
        "textNight": result["daily"][day]["textNight"],
        "humidity": result["daily"][day]["humidity"]
    }

    return normal_result

if __name__ == "__main__":
    print(get_weather_by_day('上海', 1))
    print(json.dumps(get_weather_by_day('上海', 1), ensure_ascii=False))