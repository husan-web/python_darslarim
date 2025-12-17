# def yosh_hisobla(ism, yosh):
#     print(f"{ism} {2025-yosh} yoshda.")
# yosh_hisobla("Husan", 2002)


# def son_darajalari(son):
#     print(f"{son}ning kvadrati {son**2}ga teng. " f"{son}ning kubi {son**3}ga teng")
# son_darajalari(3)


# def juft_toq(son):
#     if son % 2:
#         print("Toq son")
#     else:
#         print("Juft son")
#
#
# juft_toq(15)


# def taqqoslash(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
#
#
# taqqoslash(13, 12)


# def taqqoslash(x, y=2):
#     if x > y:
#         print(f"{x}>{y}")
#     elif x < y:
#         print(f"{x}<{y}")
#     else:
#         print(f"{x}={y}")
#
#
# taqqoslash(44, 66)


# def daraja(x, y=2):
#     print(f"{x} ning {y} darajasi {x**y} ga teng")
#
#
# daraja(4)
# daraja(5)
# daraja(3 * 2)


def qoldiqsiz(x):
    for n in range(2, 11):
        if not x % n:
            print(f"{x} {n}ga qoldiqsiz bo'linadi.")


qoldiqsiz(10)
qoldiqsiz(13.2)
