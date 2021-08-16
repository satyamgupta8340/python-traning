### Ques 2.  Write a Python program to count and display the vowels of a given text.

j=0
s = input("Enter any text ")
l=s.lower()
for i in l:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        j=j+1
        print(i)
print("Total Number of Vowels in this Text " ,j)
