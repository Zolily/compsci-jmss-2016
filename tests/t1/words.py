# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically
wordlist = []





FinalWord = True
while FinalWord:
    response = input("Please Enter a word")
    if "quit" in response.lower():
        FinalWord = False
        print(wordlist)

    else:
        wordlist = wordlist, response








