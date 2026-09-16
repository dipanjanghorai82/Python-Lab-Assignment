## create a list of 5 fruits by user input

fruits = []
print("please enter 5 fruits : ")

for i in range(1 , 6):
    user_fruit = input(f"enter fruits {i} : ")
    fruits.append(user_fruit)

print("\n2nd item : " , fruits[1])   ## print 2nd item by accessing index 1  
print("4rd item : " , fruits[3])   ## print 4th item by accessing index 3

fruits[-1] = "mango" ## replacing the last item with "mango"  

## now print the updated list
print("\nUpdated list is : " , fruits)


  