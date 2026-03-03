extendList = []
concatList = []


appendValues = [0, 10, 32, 55, 80, 100]

''' Adding the values using extend() function '''
extendList.extend(appendValues)
print(extendList)

''' Adding the values using concatenation '''
concatList += appendValues
print(concatList)


extendList.remove("Apples")