a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]
print("Welcome to square calculation problems")
print("Please, enter your name")

x = True

while x is True:
    Var = input()
    print("Thank you", Var)
    print("so if you want to calculate the perimeter of the square, press p")
    print("and s in case you want to calculate surface")

    var2 = input()
    for i in a:
        if var2 == "p" or var2 == "P":
            print("Thank for chosing perimeter calculation")
            print("Now enter the side of your perimeter")
            var3 = int(input())
            print("now enter the width of your square")
            var4 = int(input())
            perimeter = var3*4
            print("the perimeter of your square is", perimeter)

        elif var2 == i:
            print("Thank you for chosing surface calculation")
            print("Please, enter the side of the square")
            side = int(input())
            surface = side**2
            print("The surface of your square is", surface)
            print("Thank you", Var,  "for using this calculation")

else:
    print("Man, follow the instruction very well")
    print("and restart again again by entering your name")