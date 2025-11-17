# Sorting in python we got two ways .sort() > methode and sorted() >> function


# ------  Lists -----------

items = ["phone","banana","apple","orange","watch",] # thats for strings
prices = [10,12,54,56,45,2,564,5,1,] # thats for numbers 

items.sort() 
prices.sort() 


# for reversing order we gonna use the reverse using the key word argument 

items.sort(reverse=True)
prices.sort(reverse=True)


# print (prices)
# print (items)

# -----  tuples --------

cars = ("ford","amg","bmw","gmc","toyota")

#cars.sort() if we use the sort methode we will get this error tuple' object has no attribute 'sort' 

cars = tuple(sorted(cars,reverse=True)) 

# print (cars)


#------ Dict -------

fruits = {"banana":105,
          "oranges":345,
          "apple":34,
          "cocunat":2344}

# fruits = dict(sorted(fruits.items())) # items() Return a set-like object providing a view on the dict's items.
fruits = dict(sorted(fruits.items(), key=lambda item: item[1] , reverse=True ))# item: what do we want to return 
print (fruits)