# in roman the order is largest to smallest ex: VI = 6 IV = 4

# if the largest is in the left sum with the right 
# unless the hierarchy stop.

# ex: CIV = 104 and not 106 because I is smaller than V and 
# in that case you should rest the right number with the left one


def romanToInt(s: str) -> int:
    romanNumber = s.upper()
    arrayOfValuesInsideS = []
    number = []

    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    # this loads my array with the translated values from roman to int and in order
    for i in s:
        arrayOfValuesInsideS.append(values[i])

    for i in range(len(arrayOfValuesInsideS)):
        try:
            if arrayOfValuesInsideS[i] >= arrayOfValuesInsideS[i+1]:
                number.append(arrayOfValuesInsideS[i])
            elif arrayOfValuesInsideS[i] < arrayOfValuesInsideS[i+1]:
                arrayOfValuesInsideS[i+1] -= arrayOfValuesInsideS[i]

        except:
            number.append(arrayOfValuesInsideS[i])
            print(f'You reached the array limit, len(array) = {i+1}')

    return sum(number)

print(romanToInt('LVIII'))

