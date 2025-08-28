# dictionary - a collection of {key:value} panasiai kaip objektai

capitals = {"USA": "Washington D.C.",
            "China": "Beijing",
            "Lithuania": "Vilnius",
            "Germany": "Berlin"}

# print(dir(capitals))                                                  #pagalba
# print(help(capitals))

print(capitals.get("USA"))
print(capitals.get("Japan"))

capitals.update({"Japan": "Edu"})
capitals.update({"Japan": "Tokiyo"})

#capitals.popitem()                                                     # nutrina paskutini, clear() - istrina

print(capitals)
print(capitals.keys())                                                  # raktai
print(capitals.values())                                                # reiksmes
print(capitals.items())                                                 # poros