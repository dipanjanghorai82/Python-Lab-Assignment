def remove_last(list):
    if list:
        list.pop()
    else:
        print("the list is already empty")

my_list = input("enter list element : ").split()

print("entered list element : " , my_list)
remove_last(my_list)
print("updated list after remove last element :" , my_list)


    