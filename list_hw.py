#our lists to add to the main list
primary = ['red', 'blue', 'yellow']
mixed = ['purple', 'green', 'orange']
pattern = ['dots', 'stripes', 'splats']

#declare and print list1
list1 = [primary, mixed]

print list1
print''

#adding pattern to list1
list1.append(pattern)

print list1
print''

#declaring list2
list2 = []

#modifications and adding to list2
primary.sort()
list2.append(primary)
mixed.reverse()
list2.append(mixed)
pattern.insert(2, 'checkered')
list2.append(pattern)

print list2
print''

#boolean function
def eval_function(x):
    print (bool(x == primary))
    
    
#runinng boolean for list2        
for x in list2:
    eval_function(x)

print ''

#filter of list1(original list)
def siftFunc(x):
    if x == pattern:
        return True
    else:
        return False

#declare new list3    
list3 = filter(siftFunc, list1)

#run filter function for list3
for x in list3:
    list4 = x
    print (list4)
    
print ''

#allow user to select element to delete
y = input ('Choose an element 0-3 to remove in the list: ')
del list4 [y]

print ''
#print list4 with the deletion from list3
print list4
