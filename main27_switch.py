# Switch - Match-case statement

def day_of_the_week1(day):
    if day == 1:
        return "It's Monday!"
    elif day == 2:
        return "It's Tuesday!"
    elif day == 3:
        return "It's Wednesday!"
    elif day == 4:
        return "It's Thursday!"
    elif day == 5:
        return "It's Friday!"
    elif day == 6:
        return "It's Saturday!"
    elif day == 7:
        return "It's Sunday!"
    else:
        return "Not a valid day!"

print(day_of_the_week1(5))

def day_of_the_week2(day):
    match day:
        case 1:
            return "It's Monday!"
        case 2:
            return "It's Tuesday!"
        case 3:
            return "It's Wednesday!"
        case 4:
            return "It's Thursday!"
        case 5:
            return "It's Friday!"
        case 6:
            return "It's Saturday!"
        case 7:
            return "It's Sunday!"
        case _:                                                                     # case _ - default, gen Z kalba 100%
            return "Not a valid day!"
        
print(day_of_the_week2(5))

def is_weekend(day):
    match day:
        case "Monaday" | "Tuesday" | "Wednesday" | "Thursday":
            return False
        case "Sunday" | "Saturday":
            return True
        case "Friday":
            return "Yeah nah yeah, kind of :)"
        case _:
            return "Invalid day!"
        
print(is_weekend("Friday"))