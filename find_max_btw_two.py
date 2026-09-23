def find_maximum(nums1 , nums2):
    if nums1 > nums2:
        return nums1
    else:
        return nums2
try:
    first_number = float(input("Enter first number : "))
    second_number = float(input("Enter second number : "))


    result = find_maximum(first_number , second_number)
    print(f"The maximum number is : {result}")

except ValueError:
    print("please enter valid numerical value")    

