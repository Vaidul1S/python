# Module - failas, kuris import'inamas su kodu

#print(help("modules"))                          # visi imanomi modules

import math

print(math.pi)

from modules import example

result = example.pie
print(result)

print(example.square(5))
print(example.cube(5))
print(example.circumference(5))
print(example.area(5))