Name_list = []
Salary_list = []

Name_list_size = int(input("Enter total elements for the name list : "))
Salary_list_size = int(input("Enter total elements for the salary list : "))

for i in range(Name_list_size):
    Name_list.append(input("Enter value for the name list : "))

for i in range(Salary_list_size):
    Salary_list.append(input("Enter value for the salary list : "))

print("Your first list : ", Name_list)
print("Your second list : ", Salary_list)

combined_dict = dict(zip(Name_list, Salary_list))

print("Final dictionary : ", combined_dict)
