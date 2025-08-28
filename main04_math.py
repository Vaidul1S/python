import math
# Aretmetics

friends = 0

friends = friends + 5               # 5
friends -= 2                        # 3
friends *= 4                        # 12
friends /= 2                        # 6
friends = friends ** 2              # **+ 36
friends = friends % 5               # modulus, remainder 1

print(f"Friends: {friends}")

x = 3.14
y = -4
z = 5
t = 16

result = round(x)                   # apvalinimas
result = abs(y)                     # modulis (teigiamas)
result = pow(x, z)                  # laipsniu 3.14^5

print(result)

print(math.pi)
print(math.e)
print(math.sqrt(t))                 # saknis
print(math.ceil(x))                 # round i virsu
print(math.floor(x))                # round i apacia

# Skaiciuojam apskritimo ilgi

radius = float(input("Enter radius of the circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference of the circle is {round(circumference, 2)} cm.")

# Skaiciuojam apskritimo plota

radius = float(input("Enter radius of the circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is {round(area, 2)} cm2.")

# HIPOPOTAMUS!!!

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Hypotenuse of the triangle is {c} cm.")


