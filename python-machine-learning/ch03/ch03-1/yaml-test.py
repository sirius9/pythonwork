# -*- coding: utf-8 -*-
import yaml

#  yaml 정의
yam_str = """
Date : 2017-03-10
PriceList:
    -
        item_id : 1000
        name : Banana
        color : Yellow
        price : 800
    -
        item_id : 1001
        name: Orange
        color: orange
        price: 1400
    -
        item_id : 1002
        name : Apple
        color : red
        price : 2400
"""

# YAML 분석
data = yaml.load(yam_str)

# 이름 과 가격 출력
for item in data["PriceList"]:
    print(item["name"], item["price"])
