#For this one, we need to get a string, display the input to the user,
# then count the number of characters. Start with input

countString = input("What is the input string?: ")

# After this, you need to display the number of characters. But how 
# count them? Don't go crazy, there's a method :)

length = len(countString)

#  this is the len() method. len() returns the number of items in
#  an object. Yea, that string is an object. Almost everything in 
#  Python is an object, it's an object oriented programming language.

print (countString + " has " + str(length) + " characters.")

# This line prints out our message with the number of 
# characters in the given string. The str() method takes a non-string
# type and converts to a string. You have to convert it to 
#  concatenate that data with the rest of the statement. 
