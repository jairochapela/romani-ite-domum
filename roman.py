# def roman(n : int) -> str:
#     valores = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), 
#                (100, "C"), (90, "XC"),  (50, "L"), (40, "XL"), 
#                (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
#     texto = ""
#     for r,t in valores:
#         while (n >= r):
#             texto += t
#             n -= r
#     return texto


def roman2(n: int, valores = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),  (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]):
    if len(valores) > 0:
        r, t = valores[0]
        if n >= r:
            return t + roman2(n - r, valores)
        return roman2(n, valores[1:])
    return ""