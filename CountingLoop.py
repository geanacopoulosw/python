#to count from a set number to a set number
 
num1 = input("please select a number to start counting at: ")
num2 = input("please select a number to end counting at: ") 
intervalnum = input("please select a number interval to count by: ")

print("Couting: ")
for i in range(num1, num2, intervalnum):
    print i,
    

