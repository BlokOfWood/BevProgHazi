import string

accented_letters = "á","é","í","ó","ö","ő","ú","ü","ű"

if __name__ == '__main__':
    input_file = open("hazi.txt", "r", encoding="utf-8")
    lines = input_file.readlines()
    input_file.close()
    
    for i in range(len(lines)):
        for c in string.punctuation:
            lines[i] = lines[i].replace(c, "")
        lines[i] = lines[i].replace(" ", "")
        for d in accented_letters:
            lines[i] = lines[i].replace(d, "")
            lines[i] = lines[i].replace(d.upper(), "")

    output_file = open("output.txt", "w")
    for i in range(len(lines)):
        if i % 3 == 0 and lines[i] != "\n":
            output_file.write(lines[i])
    output_file.close()