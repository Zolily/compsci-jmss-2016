# write a program to read in 10 values from the keyboard and append them to a list.

stuff = []

for i in range(10):
	val = int(input("Please enter a value"))


	stuff.append(val)
while stuff < 100:
    print(stuff)



for i in range (10):
    print(stuff[0])

num = int(input("How many values are there?"))
for i in range(num):
    val = input("Please enter a value")

    stuff.append(val)
    print(i)

print(stuff)

total = 0

while total <= 100:
    num = input("please enter a number")
    total = total + int(num)
    print(total)
