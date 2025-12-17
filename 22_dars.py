# def kopaytma(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma = kopaytma * son
#     return kopaytma
#
#
# print(
#     kopaytma(
#         3,
#         4,
#         5,
#         6,
#         7,
#         8,
#     )
# )
import importlib

mod = importlib.import_module("21_dars")

baholar = mod.baholar()
baholar


def chaqirish(ism, familya, **qoshimcha):
    qoshimcha["ism"] = ism
    qoshimcha["familya"] = familya
    return qoshimcha


print(chaqirish("husan", "muhammadiyev", yosh=23, tjoy="qashqadaryo"))
