import os
import time
import msvcrt

# Write function
def writeEmployee():
    with open("employee.txt", 'a') as file:
        c = 'y'
        while c == 'y':
            id = input("\n\tEnter the employee id: ")
            name = input("\tEnter the employee name: ")
            age = input("\tEnter the employee age: ")
            gender = input("\tEnter the employee gender: ")
            salary = input("\tEnter the employee salary: ")
            file.write(id + '\t' + name + '\t' + age + '\t' + gender + '\t' + salary + '\n')
            c = input("\tDo you want to add another employee (y / n) ? : ")
        print("\tOperation done successfully")

# Read function
def readEmployee():
    
    with open("employee.txt", 'r') as file:
        print("\n\tID\tName\tAge\tGender\tSalary")
        print('\t' + '-' * 38)
        for line in file:
            print('\t' + line, end = '')
        print('\n')

# Search function
def searchEmployee():
    id = input("\n\tEnter ID of employee to search for: ")
    with open("employee.txt", 'r') as file:
        flag = False
        for line in file:
            fields = line.split('\t')
            if fields[0] == id:
                flag = True
                print("\tID\tName\tAge\tGender\tSalary")
                print('\t' + '-' * 38)
                print(line)
        if not flag:
            print("\temployee not found !")

# delete function
def deleteEmpolyee():
    id = input("\n\tEnter ID of employee to delete: ")
    file = open("employee.txt", 'r')
    temp_file = open("temp_employee.txt", 'w')
    flag = False
    for line in file:
        fields = line.split('\t')
        if fields[0] == id:
            flag = True
        else :
            temp_file.write(line)
    file.close()
    temp_file.close()
    os.remove("employee.txt")
    os.rename("temp_employee.txt", "employee.txt")
    if not flag:
        print("\temployee not found !")
    else :
        print("\tEmployee deleted successfully...")

# update function
def updateEmployee():
    id = input("\n\tEnter ID of employee to update: ")
    file = open("employee.txt", 'r')
    temp_file = open("temp_employee.txt", 'w')
    flag = False
    for line in file:
        st = line.split('\t')
        if st[0] == id:
            flag = True
            age = input("\tEnter the new age for " + st[1] + " : ")
            line = st[0] + '\t' + st[1] + '\t' + age + '\t' + st[3] + '\t' + st[4] + "\n"
        temp_file.write(line)
    file.close()
    temp_file.close()
    os.remove("employee.txt")
    os.rename("temp_employee.txt", "employee.txt")
    if not flag:
        print("\temployee not found !")
    else :
        print("\tEmployee data updated successfully...")

def main():
    os.system('cls')
    print("\033[1;33;36m\n")
    print(' '*15 + '-'*21 + '\n' + ' '*15 + '|' + ' '*5 + "Main Menu" + ' '*5 + '|' + '\n' + ' '*15 + '-'*21 + '\n')
    print("\033[1;33;35m\n")
    print(' '*10 + '1. Print all\n' + ' '*10 + '2. Add employee\n' + ' '*10 + '3. Search employee\n' + ' '*10 + '4. Update employee\n' + ' '*10 + '5. Delete employee')
    print(' '*10 + '0. Exit')
    print("\033[1;33;35m\n")
    c = input(' '*10 + "Enter: ")
    if c == '0':
        return
    elif c == '1':
        readEmployee()
        print(' '*10 + "Press any key to continue...", end='')
        temp = msvcrt.getch()
        # time.sleep(5)
        main()
    elif c == '2':
        writeEmployee()
        print(' '*10 + "Press any key to continue...", end='')
        temp = msvcrt.getch()
        main()
    elif c == '3':
        searchEmployee()
        print(' '*10 + "Press any key to continue...", end='')
        temp = msvcrt.getch()
        main()
    elif c == '4':
        updateEmployee()
        print(' '*10 + "Press any key to continue...", end='')
        temp = msvcrt.getch()
        main()
    elif c == '5':
        deleteEmpolyee()
        print(' '*10 + "Press any key to continue...", end='')
        temp = msvcrt.getch()
        main()
    else :
        print(' '*10 + "Invalid option!\n")
        #temp = input(' '*10 + "Press any key to continue...")
        print(' '*10 + "Press any key to continue...", end='')
        temp = msvcrt.getch()
        main()

main()
