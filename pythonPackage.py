import requests

r =requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson =r.json()

gu =rjson['RealtimeCityAir']['row']

for i in gu:
    name =i['MSRSTE_NM']
    idex =i['IDEX_MVL']

    if idex <60:
        print(name, idex)
