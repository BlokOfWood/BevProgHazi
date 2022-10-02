def main():
    inputString = input("Adjon meg egy mondatot:")

    characterFrequency = {};
    for char in inputString:
        characterFrequency[char] = characterFrequency.get(char, 0) + 1

    print("Betűk gyakorisága: ", characterFrequency)
    print("Fordítva: ", inputString[::-1])

    wordList = inputString.split(' ')
    print("Listába rendezve szavanként: ", wordList)

if __name__ == '__main__':
    main()