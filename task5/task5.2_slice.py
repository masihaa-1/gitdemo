#Create a list of numbers from 1 to 10
numbers = list(range(1, 11))  
first_five = numbers[:5]       # slicing from index 0 to 4
reversed_list = first_five[::-1]   # slicing with step -1 reverses the list
#Print the results
print("Original list:", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_list)