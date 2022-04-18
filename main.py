from linked_list import LinkedList


list = LinkedList()
# Adding the elements into the list
list.add(0)
list.add(1)
list.add(2)
list.add(3)
list.add(4)
# Displaying before removing the first element
list.display()
print("None")
print("Size: ",list.size())
# Removing the first element in the list
list.remove_first()
print("After removing the first element")
list.display()
print("None")
print("Size: ",list.size())