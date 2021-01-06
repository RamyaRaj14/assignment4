# program to accept a string and print only capital letters
test_str=input("Enter the string:")
res = [char for char in test_str if char.isupper()]
print("The uppercase characters in string are : " + str(res))