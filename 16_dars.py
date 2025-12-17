# buxoriy = {
#     "ism": "Imom al-Buhoriy",
#     "tyil": 810,
#     "vyil": 870,
#     "tjoy": "Buxoro",
#     "asar": "Al Jome as-Sahih",
# }
# alisher = {
#     "ism": "Mir Alisher Navoiy",
#     "tyil": 1441,
#     "vyil": 1501,
#     "tjoy": "Hirot",
#     "asar": "Xamsa",
# }
# qodiriy = {
#     "ism": "Abdulla Qodiriy",
#     "tyil": 1894,
#     "vyil": 1938,
#     "tjoy": "Toshkent",
#     "asar": "Mehrobdan chayon",
# }
# shaxslar = [buxoriy, alisher, qodiriy]
# for shaxs in shaxslar:
#     ism = shaxs["ism"]
#     tyil = shaxs["tyil"]
#     tjoy = shaxs["tjoy"]
#     vyil = shaxs["vyil"]
#     asar = shaxs["asar"]
#     print(
#         f"{ism} {tyil}-yilda {tjoy}da tavallud topgan."
#         f" {vyil-tyil} yil umr ko'rgan. Mashxur asarlaridan biri {asar}."
#     )

# dostlar = []
# kinolar = []
# for i in range(3):
#     ism = input(f"{i+1} dostingizni ismi nima?: ")
#     dostlar.append(ism)
#     kino = input(f"{dostlar[i]} ning yoqtirgan kinosi:")
#     kinolar.append(kino)
#
# for i in range(3):
#     print(f"{dostlar[i]} ning yoqqtirgan kinosi: {kinolar[i]} ")

# for i in range(3):
#     ism = input(f"{i+1} dostingiz : ")
#     kino = input(f"{ism} ning yoqtrgan kinosi : ")
#     print(f"{ism} ning yoqtrgan kinosi : {kino}")

# davlatlar = {}
# for i in range(5):
#     davlat = input(f"{i+1}chi davlat nomini kiriting:")
#     davlatlar.append(davlat)
#     aholi = input(f"{davlat(i)} aholi sonini kiriting:")


malibus = []
for malibu in range(10):
    new_car = {
        "model": "malibu",
        "rang": None,
        "yil": 2020,
        "narh": "",
        "km": "",
        "karobka": "avto",
    }
    malibus.append(new_car)
# rangi
for malibu in malibus[:3]:
    malibu["rang"] = "qizil"
for malibu in malibus[3:6]:
    malibu["rang"] = "qora"
for malibu in malibus[6:]:
    malibu["rang"] = "oq"


for malibu in malibus[:5]:
    malibu["narh"] = 35000
for malibu in malibus[5:]:
    malibu["narh"] = 40000
for malibu in malibus:
    if malibu["narh"] == 35000:
        malibu["karobka"] = "mexanika"
    elif malibu["narh"] == 40000:
        malibu["karobka"] = "avtomat"
    # probeg
for malibu in malibus[7]:
    malibus[7]["km"] = 2000
    malibus[7]["narh"] = 37000

print(malibus)
