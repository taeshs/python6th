# file_object = open('example.txt', 'r')
#
# content = file_object.read()
# print(content)
#
# file_object.close()

file_object = open('new_example.txt', 'w')

content = "This is a new file. \n Pyhton is fun!"

file_object.write(content)

file_object.close()