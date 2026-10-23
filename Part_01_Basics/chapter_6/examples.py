'''
define dictionary 
'''

student = {
        "name" : "sara",
        "age" : 22,
        "major" : "communication engineering"
        }

print(f"student name is : {student['name'] }")

student["name"] = "noor"

'''
vary data
'''

print(f"student name is : {student['name'] }")

student["country"] = "jordan"

'''
add new data 
'''

print(f"student country is : {student['country'] }")

print("try print with loop :")

for key , value in student.items():
    print(key,value)

