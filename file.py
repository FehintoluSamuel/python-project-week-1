with open('name.txt', mode='w') as file:
    file.write("Fehintolu Samuel Abdulraheem")
    
with open('name.txt', mode='r') as file:
    read_name=file.read()
read_name=read_name.split()
print(f"The Surname is {read_name[2]}, while the First and Middle name are {read_name[0]} {read_name[1]}")


