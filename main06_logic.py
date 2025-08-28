# logical operators
# or, and, not

temp = 25
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is canceled!")
elif temp > 20 and temp < 35 and not is_raining:
    print("The conditions are perfect!")

# ternary - ne toks elegantiskas kaip kitose kalbose

num = -5
user_role = "admin"

print("Positive" if num > 0 else "Negative")
print("Even" if not num % 2 else "Odd")
print("Full Access" if user_role == "admin" else "Limited Access")