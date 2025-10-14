vowels=['a','e','i','o','u']
count=0
str=input("Enter the text:")
str2=str.lower()
for char in str2:
    if char in vowels:
        count+=1


print(count)    