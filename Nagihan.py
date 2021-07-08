import json
dosya=open("Nagihan.json","r")
json_dosya=json.load(dosya)
print("ADINIZ:",json_dosya["ad"])
print("SOYADINIZ:",json_dosya["soyad"])
print("API_KEY:",json_dosya["access_token"])
print("YASADIGINIZ SEHIR:",json_dosya["sehir"])
print("YASADIGINIZ ULKE:",json_dosya["ulke"])
