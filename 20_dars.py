# def mijoz_malumoti(ism, familiya, t_yil, t_joy, email="", tel_raqam=None):
#     print("\nQuyidagi malumotlarni to'ldiring")
#
#     mijoz = {
#         "ismi": ism,
#         "familiyasi": familiya,
#         "tug'ilgan yili": t_yil,
#         "yoshi": 2025 - t_yil,
#         "tug'ilgan joyi": t_joy,
#         "emaili": email,
#         "telefon raqami": tel_raqam,
#     }
#     return mijoz
#
# print("\nMijoz haqida malumot")
# mijozlar = []
# while True:
#     ism = input("Mijoz ismi: ")
#     familiya = input("Mijoz familiyasi: ")
#     t_yil = int(input("Tug'ilgan yili: "))
#     yosh = 2025 - t_yil
#     t_joy = input("Tug'ilgan joyi: ")
#     email = input("Emaili: ")
#     tel_raqam = input("Telefon raqami: ")
#     mijozlar.append(mijoz_malumoti(ism, familiya, t_yil, t_joy, email, tel_raqam))
#     javob = input("Davom etasizmi (ha/yo'q): ")
#     if javob != "ha":
#         break
#
# print(mijozlar)
# for mijoz in mijozlar:
#     print(
#         f"{mijoz['ismi'].title()} {mijoz['familiyasi'].title()}, "
#         f"{mijoz['yoshi']} yoshda, telefon raqami: {mijoz['telefon raqami']}, "
#         f"{mijoz['emaili']} va {mijoz['tug\'ilgan joyi'].title()}da tug'ilgan."
#     )


# def eng_kattasi(x, y, z):
#     max = x
#     if y > max:
#         max = y
#     if z > max:
#         max = z
#     return max
#
#
# print(eng_kattasi(44, y=555**2, z=9 * 9))


# def aylana(radius, PI=3.14):
#     aylana = {
#         "radiusi": radius,
#         "pi": PI,
#         "diametri": 2 * radius,
#         "aylana yuzi": PI * radius**2,
#         "perimatri": 2 * radius * PI,
#     }
#     return aylana
#
#
# print(aylana(10, PI=3.14))


# def tub_son(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#     return tub_sonlar
#
#
# tub_sonlar = tub_son(10, 20)
# print(tub_sonlar)


# r = int(input("Aylananing radiusini kiriting: "))
# PI = 3.14
# s = PI * r**2
# p = 2 * PI * r
# print(f"Aylananing yuzi {s}ga teng, aylananing perimetri {p}ga teng")


# def fibonachi(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar
#
#
# print(fibonachi(100))


# def royhat(matn):
#     for i in range(len(matn)):
#         matn[i] = matn[i].title()
#
#
# ismlar = ["ali", "vali"]
# royhat(ismlar)
# print(ismlar)


# def kopaytirish(son):
#     for i in range(len(son)):
#         son[i] = son[i] * 3
#
#
# raqamlar = [3, 4, 5, 6]
# kopaytirish(raqamlar)
# print(raqamlar)


# def kichraytirish(matn):
#     for i in range(len(matn)):
#         matn[i] = matn[i].lower()
#
#
# sozlar = ["SALom", "saliH", "big BUG"]
# kichraytirish(sozlar)
# print(sozlar)


# def minus_qosh(raqamalr):
#     for i in range(len(raqamalr)):
#         raqamalr[i] = f"-{raqamalr[i]}"
#
#
# raqamlar = [10, 50, 100, 150]
# minus_qosh(raqamlar)
# print(raqamlar)
# print(type(raqamlar[0]))


# def juft_qil(son):
#     for i in range(len(son)):
#         if son[i] % 2 != 0:
#             son[i] = f"toq"
#         # else:
#         #     son[i] = f"juft"
#
#
# son = [444, 123, 441, 22, 33453, 56786, 42334]
# juft_qil(son)
# print(son)


# def chegirma(son):
#     for i in range(len(son)):
#         son[i] = son[i] * 0.9
#
#
# son = [12000, 5000, 20000, 3000]
# chegirma(son)
# print(son)


# def empty_to_none(empty):
#     for i in range(len(empty)):
#         if empty[i] == "":
#             empty[i] = None
#
#
# matnlar = ["salom", "", "bugun", "", "python"]
# empty_to_none(matnlar)
# print(matnlar)

# talabalar = ["ali", "vali", "hasan", "husan"]
#
#
# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = int(input(f"{ism}ning bahosini kiriting: "))
#         baholar[ism] = baho
#     return baholar
#
#
# baholar = bahola(talabalar)
#
# print(baholar)
# print(talabalar)


talabalar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
fanlar = ["tarix", "matematika", "adabiyot"]


def bahola_fan(kundalik):
    ismlar = {}
    for i in kundalik:
        baho = {}
        for f in fanlar:
            baho[f] = int(input(f"{i}ning {f.title()} fanining bahosini kiriting: "))
        ismlar[i] = baho
    return ismlar


natija = bahola_fan(talabalar)
print(natija)
