# indexing
# [start : end : step]

credit_card = "1234-5678-9012-3456"

print(credit_card[4])                   # 5 narys, nes nuo 0
print(credit_card[0:4])                 # pirmi 4 skaiciai
print(credit_card[5:9])                 # antri 4 skaiciai
print(credit_card[5:])                  # nuo 6 simbolio iki galo
print(credit_card[-5])                  # nuo galo 5 ir skaiciuojam nuo 1!
print(credit_card[::3])                 # imam kas 3 simboli

print(f"xxxx-xxxx-xxxx-{credit_card[-4:]}")

#format specifiers {value: flags}
# : - formatavimas

price1 = 3.14159
price2 = -5.99
price3 = 16.4

print(f"Price 1 is $ {price1:.2f}")                 # .2 - du skaiciai, f - float, po kablelio
print(f"Price 2 is $ {price2:10}")                  # skaicius susideda is 10 simboliu
print(f"Price 3 is $ {price3:010}")                 # skaicius susideda is 10 simboliu ir priekije darasomi 0
print(f"Price 3 is $ {price3:+}")                   # + prides priekije +
print(f"Price 3 is $ {price3:+,.3f}")               # +16.400