user_input_list = []
num_elements = int(input("Enter Numer of Element: "))
for i in range(num_elements):
    user_input_list.append(input("Enter Element: "))

print("User Input List: ")
for elements in user_input_list:
    print(elements)