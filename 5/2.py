if __name__ == '__main__':
    userInput = input("Please input a word, that you want to know about whether it's a palindrome: ").replace(' ', '')
    if userInput == userInput[::-1]:
        print("The word is a palindrome.")
    else:
        print("The word isn't a palindrome.")