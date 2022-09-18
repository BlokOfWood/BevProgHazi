def main():
    print("Adjon meg egy számot és egy mértékegységet (cm/inch):")
    givenAmount = float(input())
    measurementUnit = input()

    if measurementUnit.lower() == "cm":
        print(round(givenAmount / 2.54, 2), "inches")
    elif measurementUnit.lower() == "inch":
        print(round(givenAmount * 2.54, 2), "cm")
    else:
        print("Not correct unit!")


if __name__ == '__main__':
    main()
