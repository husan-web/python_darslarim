# a = "Yoqtirgan kitobingizni kiriting"
# a += "(dasturni yakunlash uchun Break deb yozing):"
# Kitoblar = []
# while True:
#     kitob = input(a)
#     Kitoblar.append(kitob)
#     if kitob == "Break".lower():
#         break
# print(f"{Kitoblar} sizning yoqtirgan kitoblaringiz.")
# print("Rahmat.")

# a = "Yoshingizni kiriting"
# a += " (dasturni to'xtatish uchun exit deb yozing)."
# while True:
#     qiymat = input(a)
#     if qiymat == "exit" or qiymat == "quit":
#         break
#     yosh = int(qiymat)
#     if yosh < 7:
#         narh = 2000
#     elif 7 <= yosh < 18:
#         narh = 3000
#     elif 18 <= yosh < 65:
#         narh = 10000
#     else:
#         narh = 0
#     if narh == 0:
#         print("Sizga tekin")
#     else:
#         print(f"Sizga kirish {narh} so'm")


# savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True:
#     qiymat = input(savol)
#     if qiymat == exit:
#         break
#     elif float(qiymat) < 0:
#         continue
#     else:
#         ildiz = float(qiymat) ** (0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
