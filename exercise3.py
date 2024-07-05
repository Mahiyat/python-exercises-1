def compare_age(age1, age2):
    if age1 > age2:
        print("First brother is elder.")
    elif age2 > age1:
        print("Second brother is elder.")
    else:
        print("Both brothers are same aged.")


a = int(input("Enter the age of the first brother: "))
b = int(input("Enter the age of the second brother: "))
compare_age(a, b)
