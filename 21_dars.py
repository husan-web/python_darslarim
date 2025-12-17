# def matn(bosh_harf_katta):
#     for i in range(len(bosh_harf_katta)):
#         bosh_harf_katta[i] = bosh_harf_katta[i].title()
#
#
# talabalar = ["ali", "vali", "hasan", "husan", "olim"]
# talabalar1 = talabalar.copy()
# talabalar2 = talabalar[:]
# matn(talabalar)
# print(talabalar)
# print(talabalar1)
# print(talabalar2)


def bahola(ismlar):
    for i in range(len(ismlar)):
        baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar


talabalar = ["ali", "vali", "hasan", "husan", "olim"]
talabalar1 = talabalar.copy()
baholar = bahola(talabalar1)
print(baholar)
