try:
    
    number = float(input("Please enter a number: 25").strip())

    
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
