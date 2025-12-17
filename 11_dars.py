# taom = ["manti", "osh", "kabob"]
# "osh" in taom


# yosh = int(input("yoshingizni kiriting "))
# if yosh <= 4:
#     price = "tekin"
# elif 4 < yosh <= 12:
#     price = "5000 so'm"
# else:
#     price = "10000 so'm"
# print(f"Sizga kirish {price}.")


# a = int(input("Juft son kiriting:"))
# if a % 2:
#     print("Juft son kiriting")
# else:
#     print("Rahmat")


# a = int(input("1chi sonni kiriting: "))
# b = int(input("2chi sonni kiriting: "))
# if 4 >= a or a >= 60:
#     print("Sizga tekin.")
# elif 18 < a <= 4:
#     print("Sizdan 10000 so'm.")
# elif 18 <= a < 60:
#     print("Sizdan 20000 so'm.")
# else:
#     print("Sizga tekin.")


# if a > b:
#     print(f"{a} soni {b}dan katta")
# elif a < b:
#     print(f"{a} soni {b}dan kichik")
# else:
#     print(f"{a} va {b} teng sonlar")


# mahsulotlar = [
#     "mashina",
#     "uy",
#     "yer",
#     "ishxona",
#     "shaxar",
#     "davlatlar",
#     "son",
#     "harflar",
#     "ovqat",
#     "kiyim",
# ]
# savat = []
# for i in range(5):
#     a = input("Savatchaga 5ta mahsulot kiriting: ")
#     if a.lower() in mahsulotlar:
#         savat.append(a)
#         print(f"{a.title()} savatingizga qo'shildi")
#     else:
#         print(f"{a.title()} do'konimizda yo'q.")
# print(f"Sizning savatingiz {savat}")


# mahsulotlar = [
#     "mashina",
#     "uy",
#     "yer",
#     "ishxona",
#     "shaxar",
#     "davlatlar",
#     "son",
#     "harflar",
#     "ovqat",
#     "kiyim",
# ]
# bor_mahsulotlar = []
# mavjud_emas = []
# for i in range(5):
#     a = input("Savatchaga 5ta mahsulot kiriting: ")
#     if a.lower() in mahsulotlar:
#         bor_mahsulotlar.append(a)
#         print(f"{a.title()} savatingizga qo'shildi")
#     elif a.lower() not in mahsulotlar:
#         mavjud_emas.append(a)
#         print(f"{a.title()} dokonimizda mavjud emas")
# print(f"Sizning so'ragan bizda mavjud mahsulot {bor_mahsulotlar}")
# print(f"Siz so'ragan bizda mavjud emas mahsulotlar {mavjud_emas}")


foydalanuvchilar = ["husan", "hasan", "behruz", "muxtor", "qilichbek"]
a = input("yangi login kiriting: ")
if a in foydalanuvchilar:
    print("bu login band qilingan")
elif a not in foydalanuvchilar:
    foydalanuvchilar.append(a)
    print(f"xush kelibsiz, {a}")
print(foydalanuvchilar)


a = int(input("Butun son kiriting: "))
for i in range(1, 11):
    if a % i == 0:
        print(f"{a} soni {i}ga qoldiqsiz bo'linadi.")
