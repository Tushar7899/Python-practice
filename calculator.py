num_1 = 20
num_2 = 30
sum = num_1 + num_2
print (sum)



# num_1 = float(input("enter a number:"))
# num_2 = float(input("enter another number:"))
# sum = num_1 + num_2 
# print ("The sum is ", sum)
# diff = num_1 - num_2
# print ("The diff is", diff)
# multi = num_1 * num_2
# print("The multi is ",multi)
# div = num_1 / num_2
# print ("The div is ", div)




num_1 = float(input("enter a number:"))
num_2 = float(input("enter another number:"))
choice = input("Enter the opration + - * /")
if choice == "+":    
    sum = num_1 + num_2 
    print ("The sum is ", sum)
if choice == "-":
    diff = num_1 - num_2
    print ("The diff is", diff)
if choice == "*":
    multi = num_1 * num_2
    print("The multi is ",multi)
if choice == "/":
    div = num_1 / num_2
    print ("The div is ", div)
else:
    print("Invalid choice")