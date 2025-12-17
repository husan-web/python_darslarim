# buyurtma = []
# while True:
#     a = input(
#         "Savatchaga nimalarni qo'shasiz? (dasturni to'xtatish uchun exit deb yozing): "
#     )
#     if a == "exit":
#         break
#     buyurtma.append(a)
#     b = input("Yana savatga nimadir qo'shasizmi?(ha/yo'q) ")
#     if b != "ha":
#         break
# # print(buyurtma)
#
#
# e_bozor = {}
# n = 1
# while True:
#     c = input(
#         f"{n}chi mahsulotni kiriting (dasturni to'xtatish uchun exit deb yozing): "
#     )
#     if c == "exit":
#         break
#     d = float(input("Uning narhini kiriting(faqat son kiriting): "))
#     e_bozor[c] = d
#     n += 1
# # print(e_bozor)
#
#
# for n in buyurtma:
#
#     if n in e_bozor:
#         print(f"{n} bor narxi - {e_bozor[n]}")
#     else:
#         print(f"Bizda {n} yo'q")
