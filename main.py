
with open('example.txt', 'r') as file_object:
    content = file_object.read()
    print(content)

with open('example.txt', 'w') as file_object:
    content = """This is a multiline string.
Python is a versatile language.
It is easy to learn and use."""
    print(content)
    file_object.write(content)