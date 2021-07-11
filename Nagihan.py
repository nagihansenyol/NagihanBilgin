import json
dosya=open("Nagihan.json","r")
json_dosya=json.load(dosya)
print("ADINIZ:",json_dosya["kimlik"]["ad"])
print("SOYADINIZ:",json_dosya["kimlik"]["soyad"])
print("KIMLIGINIZ:",json_dosya["kimlik"])
