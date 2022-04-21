

contore = 10

while contore >=0 :
    enter_num = [int(input("enter your number : "))]
    contore -= 1
    for n in enter_num:
        if n%2==0 or n%3==0:
            print("not first number")
        else:
            print("first number")

    if contore == 0 :
        asq = input("Are sure continue ? yes or no ")
        if asq == "yes":
            contore = 10
        else :
            asq = "no"
            print("bye >>><<<")
            break