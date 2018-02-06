
#Strings in Python

Life = "For me is to innovate something very unique for the World!"

#len
print(Life.__len__())

#index
print(Life.index('e'))

#count
print(Life.count('i'))

#upper
print(Life.upper())

#lower
print(Life.lower())

#repetition
print(Life *2)

#concatenation
print(Life + ' Enjoy it everyday!')


#Lists in Python
#List always comes between["",""]
Home = ["TV","XBOX","Computer"]
print(Home)
Clothes = ["Shirts","Jeans","TShirts"]

#index
print(Home.index("TV"))

#repetition
sports = ['Tennis','Football','Cricket']
print(sports * 3)

#append
Home.append("Table")
print(Home)

#insert
Clothes.insert(2,"Trousers")
print(Clothes)

#extend
Home.extend(Clothes)
print(Home)

#remove
Clothes.remove("TShirts")
print(Clothes)

#reverse
Home.reverse()
print(Home)

'''Tuples in Python
Tuples are sequences like lists in python
Tuples can not be changed like Lists and always comes inside the parentheses'''

home = ('Computer','Tv','XBOX')
collection = ('Books','Games','Laptops')
print(collection)

#index
print(home.index('XBOX'))
print(home[0])

#slicing
print(home[0:2])

#concatenation
myThings = home + collection
print(myThings)

#repetition
print(collection * 2)

#count
print(myThings.count("Books"))

#len
print(myThings.__len__())

'''Sets in Python
it comes in {}
Sets are collections of unique items'''

numbers = {10,20,30,40,50,60,70}
print(numbers)

#discard
numbers.discard(10)
print(numbers)

#union
Numbers = {11,22,33,44,55}
print(numbers|Numbers)


'''Dictionaries in Python
We use dict when we have a large amount of data
Unordered collection of key-values pairs'''
User = {'Name':'Hamza','Age':32}
print(User['Age'])

#add
User['Gender'] = 'Male'
print(User)

#del by using .pop function
User.pop("Age")
print(User)

#we can clear the dict at any point in python
User.clear()

#replacement of value by using key in dict
User = {'Name':'Hamza','Age':32}
User["Name"] = "Ezza"
print(User)














