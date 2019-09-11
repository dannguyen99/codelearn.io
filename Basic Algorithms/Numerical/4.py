def maxFraction(numerators, denominators):
    index = 0
    for i in range(len(numerators)):
        if i == 0:
            largest = numerators[i]/denominators[i]
        elif largest < numerators[i]/denominators[i]:
            largest = numerators[i]/denominators[i]
            index = i
    return index

print(maxFraction([1, 2, 3, 10], [1, 3, 4, 11]))
