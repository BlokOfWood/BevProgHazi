def main():
    print("Adja meg a háromszög három oldalát cm-ben:")
    sideA = int(input("a oldal (cm): "))
    sideB = int(input("b oldal (cm): "))
    sideC = int(input("c oldal (cm): "))

    isCorrectTriangle = (
            (sideA + sideB) >= sideC and
            (sideB + sideC) >= sideA and
            (sideA + sideC) >= sideB)
    print(isCorrectTriangle)

    print(f"A {sideA}, {sideB} és {sideC} oldalú háromszög {'' if isCorrectTriangle else 'NEM '}szerkeszthető.");


if __name__ == '__main__':
    main()
