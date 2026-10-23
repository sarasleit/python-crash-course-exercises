mother_list = ['sara', 'noor', 'roaa', 'abeer', 'hala']
son_list = mother_list[0:3]
print(mother_list)
print(son_list)
print(f"three items in the middle list is")
for i in mother_list[:3] :
    print(f"{i}")
print("the last three item in the list is")
for i in mother_list[-3:] :
    print(f"{i}")
