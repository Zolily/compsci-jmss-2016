# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read
sum = []
sum = int()


NotDoneNumber = True
while NotDoneNumber:
    response = input("Please type a number")
    if "-1" in response:
        print(sum)
        NotDoneNumber = False

    else:
        sum = int(response) + sum