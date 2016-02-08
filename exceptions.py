my_list = [1,2,3,5]

#try:
x = my_list[5]
#except IndexError:
#    print("Out of Range")
notNum = True
while notNum:
    try:
        x = input ("Please enter a whole number")

        x = int(x)
        notNum = False
    except ValueError:
        print("Hey! I asked you for a number!! Not a ",x)

Print ("x is", x)

total = x/0