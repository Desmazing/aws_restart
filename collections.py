# Let us introduce the list data type

myFruitList = ["Apple", "Banana", "Cherry"]
print(myFruitList)
print(type(myFruitList))


# Accessing list items through indexing
print(myFruitList[0]) # this will print Apple
print(myFruitList[1]) # this will print Banana
print(myFruitList[2]) # this will print Cherry

# The next step is to change values in a list
myFruitList[2] = "Orange" # replaces the Cherry with Orange
print(myFruitList)
print("\n")

# Let us introduce the tuple data type. How does it differ from a list?
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

print("\n")
# Let us introduce the tuple data type. How does it differ from a list?
myFavoriteFruitDictionay = {
    "Allan" : "apple",
    "Bill" : "banana",
    "Cindy" : "pineapple"
}

print(myFavoriteFruitDictionay)
print(type(myFavoriteFruitDictionay))

#dictionary values are accessed through the keys
print("Allan's favorite fruit is " + myFavoriteFruitDictionay["Allan"])
print("Bill's favorite fruit is " + myFavoriteFruitDictionay["Bill"])
print("Cindy's favorite fruit is " + myFavoriteFruitDictionay["Cindy"])
