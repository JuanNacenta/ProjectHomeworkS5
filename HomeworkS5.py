try:
    print("Hi, with this tool you can calculate your net salary.")
    gross = float(input("How much is your gross salary? "))
    children = int(input("How many children do you have? "))
except ValueError:
    print("The number was invalid ¯\_(ツ)_/¯")
    exit(1)
# We added another if when you have so many children that theoretically,
# you would get profit from the state thanks to tax deduction, but as we know thats not how it works
else:
    if gross < 0:
        print("You cannot have a negative salary, you are the employee, not the employer ¯\_(ツ)_/¯")
        exit(1)
    elif children < 0:
        print("You cannot have negative children ¯\_(ツ)_/¯")
        exit(1)
    elif gross < 1000:
        if children > 10:
            net= gross
            print("Your net income is", net)
        else:
            net = gross * (0.90 + children / 100)
            print("Your net income is", net)
    elif gross < 2000:
        if children > 12:
            net= gross
            print("Your net income is", net)
        else:
            net= gross*(0.88+children/100)
            print("Your net income is", net )
    elif gross < 4000:
        if children > 14:
            net=gross
            print("Your net income is", net )
        else:
            net = gross * (0.86 + children / 200)
            print("Your net income is", net)
    else:
        if children > 18:
            net = gross
            print("Your net income is", net)
        else:
            net= gross*(0.82+children/200)
            print("Your net income is", net )