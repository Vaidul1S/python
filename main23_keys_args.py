# Keyword

def hello(greeting, title, firstname, lastname):
    print(f"{greeting} {title} {firstname} {lastname}")

hello(firstname="Hello", title="Mr.", lastname="Spongebob", greeting="Squarepants")

# exercise

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone = get_phone(country=370, area=123, first=666, last=12345)

print(phone)

print(1,2,3,4,5, sep="-")                                   # end and sep is buildin keywords

# *args - arguments
# **kwargs = key arguments

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(2,2,5,4,6,6,6,6,6,56,6))

def display_name(*args):
    for arg in args:
        print(arg, end = " ")

display_name("Dr.", "Ella", "Meovv", "Gross")

print()

def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

address(street="fake avn.",
        apt="25",
        city="fake City", 
        country="fake Country", 
        zip="123456")

# exercise

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    if "pobox" in kwargs:
        print(f"{kwargs.get('pobox')}")
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
        print(f"{kwargs.get('city')} {kwargs.get('country')} {kwargs.get('zip')}")
    else:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
        print(f"{kwargs.get('city')} {kwargs.get('country')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepant", "IV",                      # argumentu tvarka butina!!!
                street="Pineapple st.",
                apt="5",
                city="Bikini Bottom", 
                country="Under the Sea", 
                zip="123456",
                pobox="PO box 5005")