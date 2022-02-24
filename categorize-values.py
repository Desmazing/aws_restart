# mixing data types is highly applicable in real life scenarios.
# banking details will consist of names, numbers, dates, images...

myMixedTypeList = [12, 34567898765, 2.345, False, "Desmond", 45, True, 6j]

# use a loop to identify all the different data types.
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item, type(item)))
