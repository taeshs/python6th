s = "       Hello World          "

print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.isupper())
print(s.islower())
print(s.istitle())
print(s.isdigit())
print(s.isalpha())

print(s.lstrip())
print(s.rstrip())
print(s.strip())

print(s.replace("world".title(), "there"))
print(s.split(","))
split_str = s.split(",")
print(split_str)
print(" ".join(split_str))

print(s.startswith("Hello"))
print(s.endswith("Hello"))