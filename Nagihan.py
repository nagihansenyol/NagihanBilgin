import json
dosya=open("myfile.json","r")
json_dosya=json.load(dosya)
print("ADINIZ:",json_dosya["ad"])
print("SOYADINIZ:",json_dosya["soyad"])
print("API_KEY:",json_dosya["access_token"])

