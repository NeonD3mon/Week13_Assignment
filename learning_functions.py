def findMaxInList(listOfNumbers):
    largestNumber = listOfNumbers[0]

    for num in listOfNumbers:
        if num > largestNumber:
            largestNumber = num

    return largestNumber



listOfNumbers = [1, 5, 3, 78, 224, 0]

print(findMaxInList(listOfNumbers))