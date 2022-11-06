import string

if __name__ == '__main__':
    userInput = input("Please input a word, that you want to know about whether it's a palindrome: ").replace(' ', '') 
    for char in string.punctuation:
        userInput = userInput.replace(char, '')

    multiCharacterLetters = ['cs', 'dz', 'dzs', 'gy', 'ly', 'sz', 'ty', 'zs']
    reversed = userInput[::-1]
    
    for letter in multiCharacterLetters:
        reversed = reversed.replace(letter[::-1], letter)

    if userInput.lower() == reversed.lower():
        print("The word is a palindrome.")
    else:
        print("The word isn't a palindrome.")