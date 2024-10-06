# list
Student_names=["shivani","sami","kami","rami","uppu","hydrokentsd"]
print(Student_names)
Student_names[2]="saloni"
print(Student_names[2])
print(Student_names[3])
print(Student_names[1])
print(Student_names[5])



# tuples
rangerlist=("mukul","saloni")
print(rangerlist)



# rangerlist[0]=20



# set 
rangers={10,20,30,40,50,60,70,80,90,100}
print(type(rangers))
print(rangers)




# Duplicates: Sets cannot contain duplicate elements, while lists and tuples can. 
# Order: Sets do not maintain element order, while lists and tuples preserve the order of elements. 
# Mutability: Lists are mutable (can be changed), tuples are immutable (cannot be changed), and sets are generally considered mutable in most languages. 
# Use Cases: 


# Set: 
# Checking if an element exists within a collection without worrying about its position. 
# Removing duplicate elements from a list. 
# Implementing operations like "union" or "intersection" on sets of data. 
# Example: Storing a list of unique user IDs. 



# List: 
# Storing a sequence of elements where order is important. 
# Iterating through elements in a specific order. 
# Modifying a collection of data dynamically. 
# Example: Storing a shopping list with items in a specific order. 


# Tuple: 
# Representing fixed data that should not be changed. 
# Passing data as a group where the order is important, but immutability is desired. 
# Using as keys in dictionaries (since dictionaries require keys to be immutable) 
# Example: Storing coordinates as a pair (x, y). 


# mapping typR
rangers_id={10:"mukul",20:"saloni",13:"Smith"}
print(rangers_id)