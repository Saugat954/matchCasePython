number= int(input("Enter any number between 1 and 3 "))
match number:
    case 1:
        print("number is One")
    case 2:
        print("number is Two")
    case 3:
        print("number is Three")
    case _:
        print("The number is not in between One and Three, Please enter a valid number")