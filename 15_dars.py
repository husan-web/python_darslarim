# ozgaruvchilar = {
#     "string": "matn",
#     "int": "son",
#     "float": "o'nlik son",
#     "boolean": "true/false",
#     "if": "agar",
#     "range": "takrorlash",
#     "range": "takrorlash",
#     "float": "o'nlik son",
#     "boolean": "true/false",
#     "if": "agar",
# }
# print(ozgaruvchilar.items())
# for keys in ozgaruvchilar.items():
#     print(f"kalit {keys}")
# print(ozgaruvchilar.keys())
# print(sorted(ozgaruvchilar.items()))
# print(ozgaruvchilar.values())
# for keys, variable in ozgaruvchilar.items():
#     print(f"{keys.title()} ning qiymati {variable}")
# print(sorted(ozgaruvchilar))
# print(set(ozgaruvchilar.values()))


# poytaxtlar = {
#     "shvetsariya": "born",
#     "aqsh": "washington",
#     "germaniya": "berlin",
#     "ispaniya": "madrid",
#     "kanada": "ottava",
#     "saudiya arabiy": "riyod",
#     "koreya": "seul",
#     "o'zbekiston": "toshkent",
# }
# # print(sorted(poytaxtlar.items()))
# # print(sorted(poytaxtlar.values()))
# a = str(input("Istalgan davlatni kiriting: "))
# capital = poytaxtlar.get(a)
# if capital == None:
#     print("Bunday malumot bizda yo'q")
# else:
#     print(f"{a.upper()}ning poytaxti {capital.title()}")


# poytaxtlar = {
#     "shvetsariya": "born",
#     "aqsh": "washington",
#     "germaniya": "berlin",
#     "ispaniya": "madrid",
#     "kanada": "ottava",
#     "saudiya arabiy": "riyod",
#     "koreya": "seul",
#     "o'zbekiston": "toshkent",
# }
#
# a = input("Istalgan davlatni kiriting: ").lower()
#
# if a in poytaxtlar:
#     print(f"{a.title()}ning poytaxti {poytaxtlar[a].title()}")
# else:
#     print("Bunday davlat ma’lumoti topilmadi")


# restoran_menyusi = {
#     "osh": 27000,
#     "norin": 35000,
#     "shashlik": 12000,
#     "boyin gosht": 60000,
#     "lagmon": 28000,
#     "mastava": 23000,
#     "sezar salat": 35000,
#     "mujskoy kapriz": 39000,
#     "non": 5000,
#     "choy": 3000,
# }
#
# print("3 ta taom buyurtma bering.")
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())
#
# for buyurtma in buyurtmalar:
#     if buyurtma in restoran_menyusi:
#         print(f"{buyurtma.title()} {restoran_menyusi[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")


# restoran_menyusi = {
#     "osh": 27000,
#     "norin": 35000,
#     "shashlik": 12000,
#     "boyin gosht": 60000,
#     "lagmon": 28000,
#     "mastava": 23000,
#     "sezar salat": 35000,
#     "mujskoy kapriz": 39000,
#     "non": 5000,
#     "choy": 3000,
# }
#
# print("3 ta taom buyurtma bering:")
#
# for n in range(1, 4):
#     taom = input(f"{n}-taom: ").lower()
#     if taom in restoran_menyusi:
#         print(f"{taom.title()} — {restoran_menyusi[taom]:,} so'm")
#     else:
#         print(f"Kechirasiz, bizda {taom.title()} yo'q.")
