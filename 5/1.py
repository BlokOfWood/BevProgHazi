import itertools

if __name__ == '__main__':
    multiTableSize = int(input('How large should the multiplication table be?'))

    layout = '{:>3}{:>6}' + ('{:>4}' * (multiTableSize - 1))
    multiNumbers = list(range(1,multiTableSize+1))

    print(layout.format('', *multiNumbers))
    print('  :------' + ('----'*(multiTableSize-1)))
    
    for num in multiNumbers:
        output = [str(num) + ':']
        for multiplier in multiNumbers:
            output.append(str(num * multiplier))
        print(layout.format(*output))
