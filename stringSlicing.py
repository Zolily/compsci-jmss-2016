#1height = 10
#
# def triangle(height,c1,c2):
#     for i in range(height):
#         spaces = height - i - 1
#         xs = 2 * i + 1
#         print(c1 * spaces + c2 * xs + c1 * spaces)
#
#
# h  = int(input("How many lines?"))
# a = input("first character?")
# b = input("second character?")
# triangle(h,a,b)
# triangle(h+1,a,b)
# triangle(6,a,b)


# task 2

def printItem(l):
    for i in range(len(l)):
        print (i,l[i])

words = ["fish", "sun", "cat", "book"]
printItem(words)
    #define your own length function that takes a list as a parameter and returns the length of that list, without using the "len" function

def length(l):
    count = 0
    for item in l:
        count = count +1
    return count

print(length([0,1,4,5,6]))
print(length(words))

# write a function that returns the sume of all the numbers in a list

def sumList(l):
    l = [0]
    total = l
    for item in l:
        total = total + item
    return item

print (sumList([2,3,4]))
