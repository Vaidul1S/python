# default arguments (in functions) - turi but gale, nes negali but def arg pries kintamuosius parametrus
def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0.05, 0.05))
print(net_price(500))

import time

def count(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(0.5)
    print("Done!!!")

count(10)