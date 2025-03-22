import math
print("Select your shit:  ")
print("1. ADD")
print("2. SUB")
print("3. DIV")
print("4. MUL")
print("5. POW")
print("6. SQR")

operation = input()

if operation == "1":
    num1 = input("1st number pleaseeeee: ")
    num2 = input("2nd number pleaseeeee: ")
    print("Your value: " + str(int(num1) + int(num2)) + ". Voila you've done math")
elif operation == "2":
    num1 = input("1st number pleaseeeee: ")
    num2 = input("2nd number pleaseeeee: ")
    print("Your value: " + str(int(num1) - int(num2)) + ". Voila you've done math")
elif operation == "3":
    num1 = input("1st number pleaseeeee: ")
    num2 = input("2nd number pleaseeeee: ")
    print("Your value: " + str(int(num1) / int(num2)) + ". Voila you've done math")
elif operation == "4":
    num1 = input("1st number pleaseeeee: ")
    num2 = input("2nd number pleaseeeee: ")
    print("Your value: " + str(int(num1) * int(num2)) + ". Voila you've done math")
elif operation == "5":
    num = float(input("1st number only pleaseeeee: "))
    print("Your value: %f" %(math.pow(num, 2)) + ". Voila you've done math")
elif operation == "6":
    num = float(input("1st number only pleaseeeee: "))
    print("Your value: %.10f" %(math.sqrt(num)) + ". Voila you've done math")
else:
    print("Bro get your senses together")
